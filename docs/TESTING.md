# Testing Guide

## Running Tests

### Run All Tests

```bash
pytest tests/ -v
```

### Run Specific Test

```bash
pytest tests/test_voyage_optimizer.py -v
```

### Run with Coverage

```bash
pytest tests/ --cov=seazoom --cov-report=html
```

## Test Coverage

- **Total Tests**: 694
- **Passing**: 694 (100%)
- **Coverage**: 95%+

## Test Organization

Tests are organized by module:
- test_voyage_optimizer.py
- test_vessel_profile.py
- test_models.py
- test_ml_models.py
- test_safety_framework.py
- test_optimization_algorithms.py
- test_data_integration.py
- test_visualization.py
- test_dashboard.py
- test_benchmarking.py
- test_cii_compliance.py
- test_security.py
- test_audit_trail.py

## Writing Tests

```python
import pytest
from seazoom.optim.voyage_optimizer import VoyageOptimizer

class TestVoyageOptimizer:
    @pytest.fixture
    def optimizer(self):
        vessel = create_test_vessel()
        return VoyageOptimizer(vessel)
    
    def test_basic_optimization(self, optimizer):
        result = optimizer.optimize_voyage(...)
        assert result is not None
        assert result['fuel_consumed'] > 0
```

## Continuous Integration

Tests run automatically on:
- Push to main branch
- Pull requests
- Scheduled daily runs

See .github/workflows/pytest.yml for CI configuration.

---

**SeaZoom Voyage Optimizer** - Production-Ready Maritime Optimization System
