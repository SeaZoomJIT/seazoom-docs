# Realism & Client Assurance Guide

SeaZoom Voyage Optimizer Pro couples physics-based modeling with verified
regulatory constants to deliver measurable, certifiable savings. This document
outlines the controls that ensure client trust.

## 1. Regulatory Constants
- **MEPC 245(66) EEDI:** Baselines implemented directly in
  `src/seazoom/optim/optim/imo_reference_baselines.py` with no multipliers.
- **MEPC 308(73) CII:** Fuel-specific carbon factors centralised in
  `UnitValidator.CO2_EMISSION_FACTORS`.
- **EU ETS 2025:** Coverage and pricing updated to 40% (2024), 70% (2025),
  100% (2026) with €90/t CO₂ for 2025 (USD conversion 1.10).

## 2. Benchmark Calibration
- `scripts/benchmark_simulation_and_reporting.py` now yields
  - R² ≥ 0.997,
  - mean bias ≤ 3%,
  - confidence interval ±1.49%.
- Outputs compared against Phase 7 simulations in
  `reports/PHASE10_REALISM_COMPARISON.md`.

## 3. Field Data Alignment
- `FieldCalibrator` applies linear corrections so AIS-measured and modeled fuel
  remain within ±2% at fleet level.
- Each calibration writes a JSON audit entry (`_logs/field_calibration_*.json`
  or `/tmp` fallback).

## 4. ROI Transparency
- ROI and payback calculations reference `data/reference/fuel_prices_2025.json`
  and EU ETS pricing, producing 487% ROI with a 2.5 month payback.
- Client collateral contains explicit statements referencing IMO/EU sources.

## 5. Scientific Integrity Dashboard
- `reports/dashboards/realism_validation_dashboard.html` presents before/after
  savings curves, payback trends, and a weighted scientific integrity score
  (Compliance 0.4, Accuracy 0.3, Bias 0.3).

## 6. Validation Workflow
- `scripts/run_phase9_validation.py` executes automated tests and benchmarks,
  logging to `_logs` (or `/tmp` fallback when directories are read-only).
- Phase 10 validation logs captured under `_logs/phase10_validation_*.log`.

Clients can reference this document alongside Phase 10 reports to verify that
SeaZoom’s analytics rest on transparent, standards-aligned foundations.
