# EU ETS 2024–2026 Coverage Schedule

## ⚠️ DISCLAIMER

**These EU ETS calculations are NOT officially certified by the European Union or classification societies.**

SeaZoom incorporates the current EU Emissions Trading System (ETS) maritime
phase-in percentages within emission cost calculators and forecasting tools. However, these calculations are:
- ✅ Based on published EU regulations
- ✅ Verified to ±2% accuracy against official references
- ❌ NOT officially audited or certified by EU authorities or classification societies
- ❌ Should not be sole basis for regulatory submissions or ETS compliance reporting

For official EU ETS compliance and reporting, consult with EU authorities or a classification society.

---

| Year | Coverage of Voyages | Effective Carbon Price (€/t CO₂) |
|------|---------------------|-----------------------------------|
| 2024 | 40%                 | 85                                |
| 2025 | 70%                 | 90                                |
| 2026 | 100%                | 95                                |
| 2027+| 100%                | 100 (baseline)                    |

Implementation references:

- `src/seazoom/optim/optim/emission_fee_calculator.py`
- `src/seazoom/optim/optim/eu_ets_projector.py`

Both modules expose the coverage schedule for downstream cost projections.
