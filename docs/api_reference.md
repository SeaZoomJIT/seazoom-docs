# API Reference

## Core Classes

### VoyageOptimizer

Main optimization engine for voyage planning and fuel efficiency.

```python
from seazoom.optim.optim.voyage_optimizer import VoyageOptimizer

optimizer = VoyageOptimizer()
```

#### Methods

**`optimize_voyage(vessel_params, voyage_params)`**

Optimize a single voyage for fuel efficiency and emissions reduction.

**Parameters**:
- `vessel_params` (dict): Vessel specifications
  - `vessel_type` (str): 'Container', 'Tanker', 'Bulk', 'LNG', 'Ro-Ro', 'General'
  - `dwt` (float): Deadweight tonnage
  - `speed_service` (float): Service speed (knots)
  - `fuel_type` (str): 'HFO', 'MGO', 'VLSFO', 'LNG'

- `voyage_params` (dict): Voyage specifications
  - `origin` (str): Port of origin
  - `destination` (str): Port of destination
  - `distance_nm` (float): Distance in nautical miles
  - `departure_time` (str): ISO format datetime

**Returns**: dict with optimization results
```python
{
    'fuel_savings_percent': 5.9,
    'fuel_savings_tonnes': 189.0,
    'co2_reduction_tonnes': 584.0,
    'cost_savings': 137705.14,
    'optimized_route': [...],
    'recommended_speed': 18.5,
    'fuel_blend': {'VLSFO': 0.7, 'MGO': 0.3},
    'compliance_status': 'COMPLIANT'
}
```

**Example**:
```python
result = optimizer.optimize_voyage(
    vessel_params={
        'vessel_type': 'Container',
        'dwt': 14000,
        'speed_service': 20.5,
        'fuel_type': 'VLSFO'
    },
    voyage_params={
        'origin': 'Singapore',
        'destination': 'Rotterdam',
        'distance_nm': 11000,
        'departure_time': '2025-01-15 08:00:00'
    }
)
```

---

### PluginManager

Manage and configure optimization plugins.

```python
from seazoom.plugins.plugin_manager import PluginManager

pm = PluginManager()
```

#### Methods

**`enable_all_plugins()`**

Enable all available plugins.

```python
pm.enable_all_plugins()
```

**`enable_plugin(plugin_name)`**

Enable a specific plugin.

**Parameters**:
- `plugin_name` (str): Plugin name ('EANN', 'BiLSTM', 'Quantum', 'WAPS', 'CleanBlend', 'Blockchain')

```python
pm.enable_plugin('EANN')
pm.enable_plugin('BiLSTM')
```

**`disable_plugin(plugin_name)`**

Disable a specific plugin.

```python
pm.disable_plugin('Blockchain')
```

**`get_plugin_status()`**

Get status of all plugins.

**Returns**: dict with plugin status
```python
{
    'EANN': {'enabled': True, 'version': '1.0', 'status': 'active'},
    'BiLSTM': {'enabled': True, 'version': '1.0', 'status': 'active'},
    ...
}
```

**`configure_plugins(config)`**

Configure plugin parameters.

**Parameters**:
- `config` (dict): Plugin configuration

```python
pm.configure_plugins({
    'EANN': {'ensemble_size': 10, 'learning_rate': 0.001},
    'BiLSTM': {'hidden_size': 128, 'num_layers': 2},
})
```

---

## Utility Functions

### Compliance Checking

```python
from seazoom.core.models.cii_calculator import CIICalculator

calculator = CIICalculator()

# Calculate CII rating
cii_rating = calculator.calculate_cii(
    vessel_type='Container',
    dwt=14000,
    annual_co2=10240,
    annual_distance=100000
)
```

### Fuel Chemistry

```python
from seazoom.core.models.fuel_chemistry import FuelChemistry

chemistry = FuelChemistry()

# Get fuel properties
properties = chemistry.get_fuel_properties(fuel_type='VLSFO')
# Returns: {'density': 0.87, 'viscosity': 11.5, 'sulfur_content': 0.5, 'co2_factor': 3.114}

# Optimize fuel blend
blend = chemistry.optimize_blend(
    vessel_type='Container',
    available_fuels=['HFO', 'MGO', 'VLSFO'],
    cost_weights={'HFO': 1.0, 'MGO': 1.5, 'VLSFO': 1.2}
)
```

### Weather Integration

```python
from seazoom.plugins.waps_simulator import WAPSSimulator

simulator = WAPSSimulator()

# Get weather forecast
forecast = simulator.get_forecast(
    origin='Singapore',
    destination='Rotterdam',
    departure_time='2025-01-15 08:00:00'
)

# Predict weather impact
impact = simulator.predict_weather_impact(
    route=waypoints,
    forecast_data=forecast
)
```

---

## Data Models

### Vessel Parameters

```python
vessel_params = {
    'vessel_type': str,           # 'Container', 'Tanker', 'Bulk', 'LNG', 'Ro-Ro', 'General'
    'dwt': float,                 # Deadweight tonnage
    'speed_service': float,       # Service speed (knots)
    'fuel_type': str,             # 'HFO', 'MGO', 'VLSFO', 'LNG'
    'length_overall': float,      # Optional: Length (meters)
    'beam': float,                # Optional: Beam (meters)
    'draft': float,               # Optional: Draft (meters)
}
```

### Voyage Parameters

```python
voyage_params = {
    'origin': str,                # Port of origin
    'destination': str,           # Port of destination
    'distance_nm': float,         # Distance (nautical miles)
    'departure_time': str,        # ISO format datetime
    'arrival_deadline': str,      # Optional: ISO format datetime
    'weather_routing': bool,      # Optional: Enable weather routing
    'compliance_level': str,      # Optional: 'STRICT', 'STANDARD', 'RELAXED'
}
```

### Optimization Result

```python
result = {
    'fuel_savings_percent': float,        # Fuel efficiency improvement (%)
    'fuel_savings_tonnes': float,         # Fuel saved (tonnes)
    'co2_reduction_tonnes': float,        # CO₂ reduction (tonnes)
    'cost_savings': float,                # Cost savings (USD)
    'optimized_route': list,              # Waypoints (lat, lon)
    'recommended_speed': float,           # Optimal speed (knots)
    'fuel_blend': dict,                   # Recommended fuel blend
    'compliance_status': str,             # 'COMPLIANT', 'WARNING', 'NON_COMPLIANT'
    'confidence_interval': float,         # Confidence (0-1)
    'execution_time_ms': float,           # Execution time (milliseconds)
}
```

---

## Error Handling

```python
from seazoom.core.exceptions import (
    VoyageOptimizationError,
    PluginError,
    ComplianceError,
    FuelChemistryError
)

try:
    result = optimizer.optimize_voyage(vessel_params, voyage_params)
except VoyageOptimizationError as e:
    print(f"Optimization failed: {e}")
except ComplianceError as e:
    print(f"Compliance check failed: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Configuration

### Environment Variables

```bash
# Disable optional dependencies
export SEAZOOM_DISABLE_SCIPY=1

# Set encryption key
export SEAZOOM_KEY=<fernet_key>

# Enable debug logging
export SEAZOOM_DEBUG=1
```

### Configuration Files

```yaml
# configs/production.yaml
optimization:
  max_iterations: 1000
  convergence_threshold: 0.001
  
plugins:
  enabled: ['EANN', 'BiLSTM', 'Quantum', 'WAPS', 'CleanBlend', 'Blockchain']
  
compliance:
  level: 'STRICT'
  standards: ['IMO_MEPC_245', 'IMO_MEPC_308', 'EU_ETS', 'FuelEU']
```

---

## Examples

### Basic Optimization

```python
from seazoom.optim.optim.voyage_optimizer import VoyageOptimizer

optimizer = VoyageOptimizer()

result = optimizer.optimize_voyage(
    vessel_params={'vessel_type': 'Container', 'dwt': 14000, 'speed_service': 20.5, 'fuel_type': 'VLSFO'},
    voyage_params={'origin': 'Singapore', 'destination': 'Rotterdam', 'distance_nm': 11000, 'departure_time': '2025-01-15 08:00:00'}
)

print(f"Fuel Savings: {result['fuel_savings_percent']:.2f}%")
print(f"Cost Savings: ${result['cost_savings']:,.2f}")
```

### Fleet Optimization

```python
fleet = [
    {'vessel_type': 'Container', 'dwt': 14000, 'speed_service': 20.5, 'fuel_type': 'VLSFO'},
    {'vessel_type': 'Tanker', 'dwt': 50000, 'speed_service': 15.0, 'fuel_type': 'HFO'},
]

total_savings = 0
for vessel in fleet:
    result = optimizer.optimize_voyage(vessel, voyage_params)
    total_savings += result['cost_savings']

print(f"Total Fleet Savings: ${total_savings:,.2f}")
```

---

## Support

For API questions or issues:

📧 [jit@seazoom.co.uk](mailto:jit@seazoom.co.uk)  
🌐 [https://seazoom.co.uk](https://seazoom.co.uk)

