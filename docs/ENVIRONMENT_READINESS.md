# Environment Readiness Checklist

Updated: 2025-11-02

## Python & Package Stack
- Python 3.11.7 (`/opt/anaconda3/bin/python`)
- NumPy 1.26.4 (segfaults on import in current sandbox)
- SciPy 1.11.4 (depends on the same NumPy build)
- Pandas 2.1.4
- Plotly 5.9.0
- Cryptography 42.0.2
- Pytest 7.4.0

> See `reports/dependency_lock.txt` for the full pip snapshot.

## Calibration Workflow
1. Run `scripts/benchmark_simulation_and_reporting.py` with `PYTHONPATH=src`.
2. Execute the field calibration helper:
   ```bash
   python - <<'EOF'
   from importlib.machinery import SourceFileLoader
   import json
   module = SourceFileLoader('field_cal', 'src/seazoom/optim/optim/field_calibration.py').load_module()
   FieldCalibrator = module.FieldCalibrator
   result = FieldCalibrator.calibrate(source='data/benchmarking/live_vessels', mode='fleet')
   with open('/tmp/field_calibration_run.json', 'w') as f:
       json.dump(result, f, indent=2)
   EOF
   ```
3. Copy the `/tmp/field_calibration_run.json` output into `_logs/` for permanent storage.

## Validation Scripts
- `scripts/run_phase9_validation.py` (writes to `/tmp` when `_logs/` is read-only).
- `scripts/benchmark_simulation_and_reporting.py` (requires `PYTHONPATH=src` in CLI usage).
- Optional Phase 11 environment check script (see `scripts/run_phase11_environment_check.py` if present).

## Known Issues
- Creating virtual environments inside the repository fails because symlink creation is disallowed in this sandbox.
- Outbound network access is blocked; pinned wheels for NumPy/SciPy cannot be downloaded.
- `pytest tests --maxfail=3 --disable-warnings -q` currently segfaults (NumPy runtime bug).

## Recommended Actions
1. Re-run the dependency installation steps on an environment with network and symlink capabilities (e.g., containerized CI runner).
2. After installing compatible NumPy/SciPy builds, rerun `pytest` and benchmark scripts to refresh `_logs/phase11_validation_test.log`.
3. Consider containerizing the stack (Phase 12 action item) to avoid host-level binary drift.
