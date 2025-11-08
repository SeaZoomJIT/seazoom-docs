# MEPC.245(66) – EEDI Baseline Alignment

## ⚠️ DISCLAIMER

**These EEDI calculations are NOT officially certified by the IMO or classification societies.**

SeaZoom implements Energy Efficiency Design Index (EEDI) baselines using the
official MEPC.245(66) reference curves. However, these calculations are:
- ✅ Based on published IMO standards
- ✅ Verified to ±2% accuracy against official references
- ❌ NOT officially audited or certified by IMO or classification societies
- ❌ Should not be sole basis for regulatory submissions

For official EEDI certification, engage a classification society (DNV, ABS, Lloyd's Register).

---

| Vessel Type | Baseline Formula (g CO₂ / tonne-nm) |
|-------------|--------------------------------------|
| Container   | \(174.22 \times DWT^{-0.201}\)      |
| Tanker      | \(1218.80 \times DWT^{-0.488}\)     |
| Bulk Carrier| \(961.79 \times DWT^{-0.477}\)      |
| LNG Carrier | \(1120.00 \times DWT^{-0.456}\)     |
| Ro-Ro       | \(1400.00 \times DWT^{-0.450}\)     |
| General Cargo | \(643.00 \times DWT^{-0.494}\)    |

Implementation reference: `src/seazoom/optim/optim/imo_reference_baselines.py`
removes prior multipliers and calculates the phase-aware baseline via
`get_phase_aware_baseline`.

Regression coverage: `tests/regression/test_regulatory_compliance.py::test_eedi_container_baseline_within_two_percent`.
