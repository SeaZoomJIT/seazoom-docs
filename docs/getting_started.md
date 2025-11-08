# Getting Started with SeaZoom

Welcome to SeaZoom AI Suite! This guide will help you install, configure, and run your first voyage optimization.

## Installation

### Prerequisites

- Python 3.9+
- pip or conda
- Git

### Quick Install

```bash
# Clone the repository
git clone https://github.com/SeaZoomJIT/seazoom-voyage-optimizer.git
cd seazoom-voyage-optimizer

# Install dependencies
pip install -r requirements.txt

# Or use conda
conda env create -f environment.yml
conda activate seazoom_v2.1.1e
```

### Verify Installation

```bash
# Run tests to verify everything works
pytest -q --disable-warnings

# Expected output: 1019 passed ✅
```

## Quick Start

### 1. Basic Voyage Optimization

```python
from seazoom.optim.optim.voyage_optimizer import VoyageOptimizer

# Initialize optimizer
optimizer = VoyageOptimizer()

# Define vessel parameters
vessel_params = {
    'vessel_type': 'Container',
    'dwt': 14000,
    'speed_service': 20.5,
    'fuel_type': 'VLSFO'
}

# Define voyage
voyage = {
    'origin': 'Singapore',
    'destination': 'Rotterdam',
    'distance_nm': 11000,
    'departure_time': '2025-01-15 08:00:00'
}

# Run optimization
result = optimizer.optimize_voyage(vessel_params, voyage)

print(f"Fuel Savings: {result['fuel_savings_percent']:.2f}%")
print(f"Cost Savings: ${result['cost_savings']:,.2f}")
print(f"CO₂ Reduction: {result['co2_reduction_tonnes']:.2f} tonnes")
```

### 2. Multi-Vessel Fleet Optimization

```python
from seazoom.optim.optim.voyage_optimizer import VoyageOptimizer

optimizer = VoyageOptimizer()

# Define fleet
fleet = [
    {'vessel_type': 'Container', 'dwt': 14000, 'speed_service': 20.5},
    {'vessel_type': 'Tanker', 'dwt': 50000, 'speed_service': 15.0},
    {'vessel_type': 'Bulk', 'dwt': 65000, 'speed_service': 14.5},
]

# Optimize all vessels
results = []
for vessel in fleet:
    result = optimizer.optimize_voyage(vessel, voyage)
    results.append(result)

# Aggregate results
total_fuel_savings = sum(r['fuel_savings_tonnes'] for r in results)
total_cost_savings = sum(r['cost_savings'] for r in results)

print(f"Fleet Fuel Savings: {total_fuel_savings:,.0f} tonnes")
print(f"Fleet Cost Savings: ${total_cost_savings:,.2f}")
```

### 3. Enable Plugins

```python
from seazoom.plugins.plugin_manager import PluginManager

# Initialize plugin manager
pm = PluginManager()

# Enable all plugins
pm.enable_all_plugins()

# Or enable specific plugins
pm.enable_plugin('EANN')
pm.enable_plugin('BiLSTM')
pm.enable_plugin('CleanBlend')

# Run optimization with plugins
result = optimizer.optimize_voyage(vessel_params, voyage)
```

## Configuration

### Environment Variables

```bash
# Disable optional dependencies (for lightweight deployments)
export SEAZOOM_DISABLE_SCIPY=1

# Set encryption key for secure operations
export SEAZOOM_KEY=$(python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")

# Enable debug logging
export SEAZOOM_DEBUG=1
```

### Configuration Files

Configuration files are located in `configs/`:

- `configs/base.yaml` - Base configuration
- `configs/dev.yaml` - Development settings
- `configs/production.yaml` - Production settings

## Common Tasks

### Run Benchmarks

```bash
# Run comprehensive benchmarks
python scripts/benchmark_v2_1_1.py

# Run specific benchmark
python scripts/run_comprehensive_benchmark.py
```

### Generate Reports

```bash
# Generate optimization report
python scripts/generate_insight_dashboard.py

# Generate static dashboard
python scripts/generate_static_dashboard.py
```

### Validate System

```bash
# Run diagnostics
python scripts/diagnostics.py

# Validate plugins
python scripts/validate_plugins.py

# Validate imports
python scripts/validate_imports.py
```

## Troubleshooting

### Import Errors

If you encounter import errors, ensure the package is installed in editable mode:

```bash
pip install -e .
```

### Missing Dependencies

Some plugins require optional dependencies. Install them as needed:

```bash
# For PyTorch-based plugins
pip install torch

# For Qiskit quantum plugin
pip install qiskit

# For blockchain features
pip install web3
```

### Test Failures

If tests fail, check your environment:

```bash
# Verify Python version
python --version  # Should be 3.9+

# Verify dependencies
pip list | grep -E "torch|qiskit|web3"

# Run specific test
pytest tests/unit/test_voyage_optimizer.py -v
```

## Next Steps

- 📊 Explore [Benchmarks & Results](benchmarks.md)
- 🔌 Learn about [Plugin System](plugins_overview.md)
- 📚 Read [API Reference](api_reference.md)
- ⚔️ Understand [Competitive Edge](competitive_edge.md)

## Support

For questions or issues:

- 📧 Email: [jit@seazoom.co.uk](mailto:jit@seazoom.co.uk)
- 🌐 Website: [https://seazoom.co.uk](https://seazoom.co.uk)
- 🐙 GitHub Issues: [SeaZoomJIT/seazoom-voyage-optimizer/issues](https://github.com/SeaZoomJIT/seazoom-voyage-optimizer/issues)

