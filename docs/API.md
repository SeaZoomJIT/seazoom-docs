# API Reference

## Core Classes

### VoyageOptimizer

Main optimization engine.

```python
from seazoom.optim.voyage_optimizer import VoyageOptimizer

optimizer = VoyageOptimizer(vessel)
result = optimizer.optimize_voyage(origin_lat, origin_lon, destination_lat, destination_lon, cargo_weight, fuel_price)
```

**Methods:**
- `optimize_voyage(...)` → Dict
- `optimize_route(waypoints)` → Dict
- `compare_routes(routes)` → List[Dict]
- `set_parameters(...)` → None

### VesselProfile

Vessel characteristics.

```python
from seazoom.models.vessel_profile import VesselProfile

vessel = VesselProfile(
    imo="1234567",
    name="Example Vessel",
    vessel_type="Bulk Carrier",
    loa=190.0,
    beam=32.0,
    draft_design=10.5,
    dwt=65000.0,
    power_main=6000.0,
    speed_design=14.5
)
```

## Physics Models

### HoltropMennenModel

Hydrodynamic resistance calculation.

```python
from seazoom.models.holtrop_mennen import HoltropMennenModel

model = HoltropMennenModel(vessel)
resistance = model.calculate_resistance(speed=12.0, draft=10.5)
power = model.calculate_power_required(speed=12.0, draft=10.5)
fuel = model.calculate_fuel_consumption(speed=12.0, draft=10.5, sfc=0.18)
```

### WeatherPenaltyModel

Weather impact on fuel consumption.

```python
from seazoom.models.weather_penalty import WeatherPenaltyModel

model = WeatherPenaltyModel()
penalty = model.calculate_penalty(headwind_knots=15.0, sea_state=3, wave_height_m=2.5)
weather = model.get_weather_data(latitude=35.0, longitude=139.0)
```

## Data Integration

### OpenDataIntegrator

AIS and market data integration.

```python
from seazoom.data.open_data_integration import OpenDataIntegrator

integrator = OpenDataIntegrator()
position = integrator.get_vessel_position(mmsi="123456789")
price = integrator.get_fuel_price(location="Singapore", fuel_type="VLSFO")
rate = integrator.get_freight_rate(route="Asia-Europe")
vessels = integrator.get_nearby_vessels(latitude=35.0, longitude=139.0, radius_nm=100)
```

### WeatherDataFetcher

Weather data integration.

```python
from seazoom.data.weather_data_fetcher import WeatherDataFetcher

fetcher = WeatherDataFetcher()
weather = fetcher.get_weather(latitude=35.0, longitude=139.0)
forecast = fetcher.get_forecast(latitude=35.0, longitude=139.0, hours=24)
```

## Monitoring & Analytics

### RealtimeMonitor

Real-time performance monitoring.

```python
from seazoom.dashboard.realtime_monitor import RealtimeMonitor

monitor = RealtimeMonitor()
monitor.add_vessel_data(vessel_imo, speed, fuel_consumption, position, eta)
alerts = monitor.get_alerts()
metrics = monitor.get_performance_metrics(vessel_imo)
summary = monitor.get_fleet_summary()
```

### IndustryBenchmarking

Industry benchmarking.

```python
from seazoom.analytics.industry_benchmarking import IndustryBenchmarking

benchmarking = IndustryBenchmarking()
comparison = benchmarking.get_peer_comparison(vessel_imo, efficiency, vessel_type)
percentile = benchmarking.get_percentile_ranking(efficiency, vessel_type)
avg = benchmarking.get_industry_average(vessel_type)
```

## Compliance & Security

### CIIComplianceTracker

CII compliance tracking.

```python
from seazoom.models.cii_compliance_tracker import CIIComplianceTracker

tracker = CIIComplianceTracker()
result = tracker.calculate_cii(fuel_consumed, distance_nm, dwt)
status = tracker.get_compliance_status(vessel_imo)
penalty = tracker.estimate_penalty(cii_rating, fuel_consumed)
```

### DataEncryptionManager

Data encryption and security.

```python
import os
from seazoom.security.data_encryption import DataEncryptionManager

os.environ.setdefault("SEAZOOM_KEY", DataEncryptionManager.generate_key())

encryption = DataEncryptionManager()
encrypted = encryption.encrypt_vessel_data(vessel_imo, data)
decrypted = encryption.decrypt_vessel_data(vessel_imo, encrypted)
hashed = encryption.hash_sensitive_data(data, salt)
```

### AuditTrailManager

Audit trail and compliance logging.

```python
from seazoom.audit.audit_trail import AuditTrailManager

audit = AuditTrailManager()
audit.log_calculation(entity_id, calculation_type, inputs, result, user_id, reason)
audit.log_decision(entity_id, decision_type, decision, rationale, user_id, confidence)
history = audit.get_entity_history(entity_id, entity_type)
report = audit.generate_compliance_report(entity_id)
```

## Visualization

### VoyagePlotter

Voyage route visualization.

```python
from seazoom.visualization.voyage_plotter import VoyagePlotter

plotter = VoyagePlotter(use_plotly=True)
html = plotter.plot_voyage_route(waypoints, title, show_fuel, show_speed)
html = plotter.plot_fuel_consumption_profile(distances, fuel_consumed, title)
html = plotter.plot_multi_route_comparison(routes, title)
```

### PerformanceDashboard

Performance monitoring dashboard.

```python
from seazoom.visualization.performance_dashboard import PerformanceDashboard

dashboard = PerformanceDashboard()
html = dashboard.create_kpi_dashboard(vessel_name, fuel, speed, efficiency, cii, compliance)
html = dashboard.create_alert_dashboard(alerts, title)
html = dashboard.create_fleet_summary(vessels, title)
```

### BenchmarkingCharts

Industry benchmarking visualization.

```python
from seazoom.visualization.benchmarking_charts import BenchmarkingCharts

charts = BenchmarkingCharts()
html = charts.create_peer_comparison(vessel_name, efficiency, peer_data)
html = charts.create_percentile_analysis(efficiency, percentiles)
html = charts.create_performance_ranking(vessels, metric)
```

## Error Handling

```python
from seazoom.core.exceptions import (
    InvalidVesselError,
    OptimizationError,
    DataIntegrationError,
    ValidationError
)

try:
    result = optimizer.optimize_voyage(...)
except InvalidVesselError as e:
    print(f"Invalid vessel: {e}")
except OptimizationError as e:
    print(f"Optimization failed: {e}")
```

---

**SeaZoom Voyage Optimizer** - Production-Ready Maritime Optimization System
