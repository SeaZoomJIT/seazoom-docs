# MEPC.308(73) – Carbon Intensity Indicator (CII)

## ⚠️ DISCLAIMER

**These CII calculations are NOT officially certified by the IMO or classification societies.**

SeaZoom calculates CII using the official formulation. However, these calculations are:
- ✅ Based on published IMO standards (MEPC.308(73))
- ✅ Verified to ±2% accuracy against official references
- ❌ NOT officially audited or certified by IMO or classification societies
- ❌ Should not be sole basis for regulatory submissions

For official CII certification and compliance reporting, engage a classification society (DNV, ABS, Lloyd's Register).

---

\[
\mathrm{CII} = \frac{\mathrm{Fuel~Consumed} \times \mathrm{CF}}{\mathrm{Capacity} \times \mathrm{Distance}} \times 10^6
\]

Where CF is the fuel-specific carbon factor. The platform ships the following
values (tonnes CO₂ per tonne fuel) in `UnitValidator.CO2_EMISSION_FACTORS`:

- Heavy Fuel Oil (HFO): 3.200
- Marine Gas Oil (MGO): 3.150
- Very Low Sulfur Fuel Oil (VLSFO): 3.114
- Liquefied Natural Gas (LNG): 2.750

Reference implementation: `src/seazoom/core/models/cii_calculator.py` and
`src/seazoom/core/models/cii_compliance_tracker.py`. Both modules accept fuel
type inputs and default to HFO for tanker scenarios. Summary reports utilise
`calculate_cii_report` for compliance tracking.

Regression coverage: `tests/regression/test_regulatory_compliance.py::test_cii_calculation_within_two_percent`.
