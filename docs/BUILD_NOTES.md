# Build & Dependency Notes

This project uses `pyproject.toml` as the single source of truth for dependencies.

## Dependency Policy

- Base runtime dependencies are minimal and used by production code paths only.
- Dev/test tools are provided via the `dev` extra and are NOT installed in production images.
- Heavy/optional features are isolated behind extras:
  - `viz`: visualization (bokeh, matplotlib)
  - `opt`: scientific optimization (scipy)
  - `ml`: machine learning runtime (tensorflow)
  - `chem`: cheminformatics (rdkit-pypi)

Install examples:

```bash
# Runtime only
pip install -e .

# Development + docs
pip install -e .[dev,docs]

# Optional features
pip install -e .[viz,opt]
```

## Makefile Targets

- `make install` – install runtime package
- `make install-dev` – install package with dev/docs tooling
- `make install-all` – install optional extras (viz,opt,ml,chem)
- `make verify` – run flake8, black --check, mypy, pytest, diagnostics
- `make docker-build` – build production image (runtime only)
- `make docker-test` – build dev/test image and run tests
- `make audit` – optional security audit (skips if tools unavailable)

## Docker Images

- `docker/Dockerfile` – production runtime image (no dev/test tools)
- `docker/Dockerfile.dev` – CI/dev image (installs [dev,docs,viz,opt])

Secrets and `.env` files are intentionally not copied into Docker images.

## Plugin Architecture

Optional plugins live under `src/seazoom/plugins/` and are loaded via the `PluginManager`.

- Activation: set `SEAZOOM_PLUGINS="eann,waps,quantum,cleanblend,blockchain"` or call `PluginManager.load({...})`.
- Each plugin provides:
  - `is_available()` – checks optional deps
  - `has_fallback = True` – deterministic fallback even if deps missing
  - `run(inputs: dict) -> dict` – returns deterministic outputs with `elapsed_sec`
- Optional extras:
  - `ai` (PyTorch), `quantum` (Qiskit), `blockchain` (Web3)

Testing: unit tests under `tests/plugins/` validate minimal behavior and fallbacks.

## Plugin Registration & Testing

### Auto-Registration

All plugins can be registered automatically using the `register_all()` helper:

```python
from seazoom.plugins.plugin_manager import PluginManager
from seazoom.plugins.register_all import register_all

pm = PluginManager()
register_all(pm)  # Registers all 6 plugins safely
pm.load_from_env()  # Load based on SEAZOOM_PLUGINS env var
```

The `register_all()` function:
- Safely imports all plugin classes with try/except guards
- Handles missing optional dependencies gracefully
- Registers only successfully imported plugins
- Works even when torch, qiskit, or web3 are not installed

### Testing All Plugins

Run the unified test harness to validate all plugins:

```bash
# Test all plugins with deterministic inputs
pytest tests/plugins/test_all_plugins.py -v

# Test specific plugin
pytest tests/plugins/test_eann_fuel_predictor.py -v

# Test all plugins
pytest tests/plugins/ -v
```

The unified test harness (`test_all_plugins.py`) validates:
- All plugins register successfully
- All plugins load from environment
- All plugins run deterministically with mock inputs
- Runtime is bounded (< 2 seconds per plugin)
- Results are consistent across multiple runs

### Environment Variable Usage

Control which plugins are active via the `SEAZOOM_PLUGINS` environment variable:

```bash
# Load all plugins (default if not set)
unset SEAZOOM_PLUGINS

# Load specific plugins only
export SEAZOOM_PLUGINS="eann,waps,cleanblend"

# Load no plugins
export SEAZOOM_PLUGINS=""
```

### Plugin Diagnostics

Check plugin availability using the diagnostics script:

```bash
python3 scripts/diagnostics.py
```

This will report:
- Number of registered plugins
- Number of active plugins
- Mode for each plugin (native/fallback/unavailable)
- Optional dependency status
