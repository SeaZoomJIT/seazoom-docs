# Usage Guide

## Quick Start

### Basic Voyage Optimization

```python
from seazoom.optim.voyage_optimizer import VoyageOptimizer
from seazoom.models.vessel_profile import VesselProfile

# Create vessel
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

# Optimize voyage
optimizer = VoyageOptimizer(vessel)
result = optimizer.optimize_voyage(
    origin_lat=35.0,
    origin_lon=139.0,
    destination_lat=51.5,
    destination_lon=0.0,
    cargo_weight=50000.0,
    fuel_price_usd_per_tonne=450.0
)

print(f"Fuel Savings: {result['fuel_savings_percent']:.1f}%")
```

## Common Use Cases

### Multi-Route Comparison

```python
routes = [
    {"name": "Direct", "waypoints": [(35.0, 139.0), (51.5, 0.0)]},
    {"name": "Northern", "waypoints": [(35.0, 139.0), (55.0, 10.0), (51.5, 0.0)]}
]

for route in routes:
    result = optimizer.optimize_route(route["waypoints"])
    print(f"{route['name']}: {result['fuel_consumed']} tonnes")
```

### Real-Time Monitoring

```python
from seazoom.dashboard.realtime_monitor import RealtimeMonitor

monitor = RealtimeMonitor()
monitor.add_vessel_data(vessel_imo, speed, fuel, position, eta)
alerts = monitor.get_alerts()
```

### Industry Benchmarking

```python
from seazoom.analytics.industry_benchmarking import IndustryBenchmarking

benchmarking = IndustryBenchmarking()
comparison = benchmarking.get_peer_comparison(vessel_imo, efficiency, vessel_type)
```

### CII Compliance

```python
from seazoom.models.cii_compliance_tracker import CIIComplianceTracker

tracker = CIIComplianceTracker()
result = tracker.calculate_cii(fuel_consumed, distance_nm, dwt)
print(f"CII Rating: {result['rating']}")
```

## Examples

See examples/ folder for complete examples:
- basic_voyage_optimization.py
- advanced_multi_route_optimization.py
- real_time_monitoring.py
- benchmarking_analysis.py

## Notebooks

See notebooks/ folder for interactive tutorials.

## API Reference

See API.md for detailed API documentation.

---

**SeaZoom Voyage Optimizer** - Production-Ready Maritime Optimization System
