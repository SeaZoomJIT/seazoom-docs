# SeaZoom Voyage Optimizer - Architecture & Design

## Overview

SeaZoom is a comprehensive maritime voyage optimization system that minimizes total voyage cost while respecting operational constraints. It integrates multiple specialized modules for data management, optimization, risk assessment, and visualization.

## Module Architecture

```
seazoom/optim/
├── voyage_optimizer.py          # Core optimization engine
├── data_interface.py            # Unified data access layer
├── port_manager.py              # Port operations & fees
├── emission_zone_model.py       # Emission cost calculation
├── risk_layer.py                # Risk assessment & penalties
├── visualization.py             # Interactive visualizations
├── ai_refiner.py                # ML-based predictions
├── rerouting_ai.py              # Route optimization (A*, Dijkstra)
└── main.py                      # Integration & orchestration
```

## Core Modules

### 1. VoyageOptimizer (`voyage_optimizer.py`)

**Purpose**: Core voyage optimization engine

**Key Features**:
- Great-circle distance calculations (haversine formula)
- Cubic fuel consumption model: `fuel_per_nm = coeff * v^3`
- Piecewise constant speed optimization (per-segment)
- Cubic polynomial speed profile optimization (smooth trajectories)
- Crew fatigue modeling (hard constraints & soft penalties)
- Cost evaluation with fuel, crew, and emission components

**Key Methods**:
- `compute_distances_nm()` - Calculate segment distances
- `fuel_rate_per_nm(speed)` - Cubic fuel model
- `evaluate_plan(speed_profile)` - Total cost calculation
- `optimize_piecewise_speeds(deadline, bounds)` - Per-segment optimization
- `optimize_cubic_profile(num_points, deadline, bounds)` - Polynomial optimization
- `crew_fatigue_penalty(schedule, mode)` - Fatigue modeling
- `report()` - Generate optimization report

**Mathematical Model**:
```
Minimize: total_cost = fuel_cost + crew_cost + emission_cost + port_costs + risk_surcharge

Subject to:
  - speed_min ≤ v_i ≤ speed_max (speed bounds)
  - total_time ≤ time_available (deadline constraint)
  - continuous_hours ≤ max_continuous_hours (crew fatigue)
  - v(s) ∈ [v_min, v_max] for all s ∈ [0,1] (polynomial bounds)
```

### 2. DataInterface (`data_interface.py`)

**Purpose**: Unified data access layer for manual and API sources

**Features**:
- Load CSV files for tariffs, weather, zones, risks
- Cache loaded data for performance
- Future API hooks for live data (OpenWeather, MarineTraffic, etc.)
- Fallback mechanisms for missing data

**Key Methods**:
- `load_csv(filename, data_type)` - Load and cache CSV
- `get_port_data(port_name)` - Retrieve port information
- `get_tariff(lat, lon)` - Get nearest port tariff
- `get_weather(lat, lon, date)` - Weather data (mock/API)
- `get_emission_zones()` - Load ECA definitions
- `get_risk_zones()` - Load risk zone definitions
- `create_sample_csvs()` - Generate sample data files

**Data Files** (CSV format):
- `port_tariffs.csv`: Port fees, congestion, wait times
- `emission_zones.csv`: ECA definitions and fees
- `risk_zones.csv`: Piracy/conflict zones and multipliers

### 3. PortManager (`port_manager.py`)

**Purpose**: Manage port operations, fees, and congestion

**Features**:
- Port entry/exit tariff calculation
- Congestion-based waiting time estimation
- Demurrage penalty computation
- Optimal departure time recommendation
- Total voyage port cost calculation

**Key Methods**:
- `compute_port_cost(port_name, tonnage, dwell_time)` - Port cost breakdown
- `get_optimal_departure_time(port_name, horizon)` - Departure recommendation
- `estimate_port_queue_time(port_name, arrival_time)` - Queue estimation
- `compute_total_voyage_port_costs(waypoints, dwell_times)` - Total port costs

**Cost Components**:
- Tariff: `tariff_per_teu * vessel_teu`
- Demurrage: `dwell_time * demurrage_per_hour`
- Congestion Surcharge: `demurrage * congestion_level * 0.5`

### 4. EmissionZoneModel (`emission_zone_model.py`)

**Purpose**: Calculate emission costs by geographic region

**Features**:
- Define Emission Control Areas (ECAs): EU, North America, China coastal
- Regional emission fee calculation
- Fuel type surcharges (HFO vs MGO)
- Voyage-wide emission cost breakdown

**Key Methods**:
- `get_emission_fee(lat, lon, emission_tons)` - Regional fee
- `get_zone_name(lat, lon)` - Zone identification
- `compute_segment_emission_cost(lat1, lon1, lat2, lon2, fuel)` - Segment cost
- `compute_voyage_emission_cost(waypoints, segment_fuel)` - Total emissions
- `get_fuel_surcharge(fuel_type, zone)` - Fuel type adjustment

**ECA Zones** (Predefined):
- EU ECA: North Sea, Baltic, Mediterranean
- North America ECA: US/Canada coasts
- China Coastal: Coastal waters

### 5. RiskLayer (`risk_layer.py`)

**Purpose**: Model maritime security risks and apply cost penalties

**Features**:
- Piracy risk zones (Somali Basin, Gulf of Aden, etc.)
- Conflict zone identification
- Insurance surcharge calculation
- Route avoidance recommendations

**Key Methods**:
- `get_risk_multiplier(lat, lon)` - Cost multiplier for location
- `get_risk_zone_name(lat, lon)` - Zone identification
- `compute_segment_risk_cost(lat1, lon1, lat2, lon2, base_cost)` - Segment risk
- `compute_voyage_risk_cost(waypoints, segment_costs)` - Total risk cost
- `get_insurance_surcharge(route_risk, cargo_value)` - Insurance cost
- `recommend_route_avoidance()` - High-risk zone recommendations

**Risk Multipliers**:
- Safe Waters: 1.0x
- Moderate Risk: 1.2x - 1.3x
- High Risk: 1.5x+

### 6. VoyageVisualizer (`visualization.py`)

**Purpose**: Create interactive visualizations for voyage analysis

**Features**:
- Route mapping with zones
- Cost breakdown charts
- Speed profile plots
- Fuel vs speed relationships
- Pareto frontier (cost vs time tradeoff)
- Support for both matplotlib (static) and plotly (interactive)

**Key Methods**:
- `plot_route_with_zones(waypoints, zones)` - Route map
- `plot_cost_breakdown(cost_dict)` - Pie/bar chart
- `plot_speed_profile(distances, speeds)` - Speed over distance
- `plot_fuel_vs_speed(speeds, fuel_rates)` - Cubic relationship
- `plot_cost_vs_time(times, costs)` - Pareto frontier

### 7. AIRefiner (`ai_refiner.py`)

**Purpose**: ML-based voyage prediction and optimization

**Features**:
- Train on historical voyage data
- Predict optimal ETA adjustments
- Cost-saving recommendations
- Speed adjustment suggestions
- Feature importance analysis

**Key Methods**:
- `train_on_historical_data(voyages, target)` - Model training
- `predict_cost(voyage_features)` - Cost prediction
- `predict_eta_adjustment(base_eta, weather, congestion)` - ETA adjustment
- `recommend_speed_adjustment(speed, fuel_price, time_penalty)` - Speed recommendation
- `get_feature_importance()` - Feature analysis
- `create_mock_training_data(n_samples)` - Generate synthetic data

**Models Supported**:
- Random Forest Regressor
- Gradient Boosting Regressor

### 8. ReroutingAI (`rerouting_ai.py`)

**Purpose**: Compute alternate routes using graph search algorithms

**Features**:
- Dijkstra's shortest path algorithm
- A* search with haversine heuristic
- Dynamic cost adjustment based on tariffs and risks
- Multiple alternative route generation

**Key Methods**:
- `compute_segment_cost(lat1, lon1, lat2, lon2, base_cost)` - Segment cost
- `dijkstra_shortest_path(start, end, candidates)` - Shortest path
- `a_star_search(start, end, candidates)` - A* search
- `find_alternative_routes(start, end, candidates, num_alt)` - Multiple routes

**Cost Factors**:
- Distance (haversine)
- Risk multipliers
- Port tariffs
- Emission fees

### 9. Main Integration (`main.py`)

**Purpose**: Unify all modules into a cohesive system

**Features**:
- Initialize all components
- Load sample CSV data
- Run complete voyage optimization
- Generate comprehensive reports
- Create visualizations

**Key Class**: `SeaZoomOptimizer`
- `optimize_voyage(waypoints, vessel, params, deadline)` - Full optimization
- `generate_report(result)` - Formatted report
- `run_example_voyage()` - Example: Shanghai → Rotterdam

## Data Flow

```
Input Data (CSV/API)
    ↓
DataInterface (load & cache)
    ↓
VoyageOptimizer (core optimization)
    ├→ PortManager (port costs)
    ├→ EmissionZoneModel (emission costs)
    ├→ RiskLayer (risk costs)
    └→ AIRefiner (predictions)
    ↓
ReroutingAI (alternative routes)
    ↓
VoyageVisualizer (plots)
    ↓
Report & Recommendations
```

## Integration Points

### Dependency Injection Pattern

All modules accept dependencies in constructors:

```python
port_manager = PortManager(data_interface)
emission_model = EmissionZoneModel(data_interface)
risk_layer = RiskLayer(data_interface)
rerouting_ai = ReroutingAI(port_manager, risk_layer)
```

### Future API Hooks

Marked with `TODO` comments for easy integration:

- **Weather API**: `DataInterface.get_weather()` → OpenWeather, NOAA
- **Port Data API**: `DataInterface.get_port_data()` → MarineTraffic, IHS
- **Risk Data API**: `RiskLayer` → IMO piracy reports, conflict datasets
- **Tariff API**: `PortManager` → Live port tariff feeds

## Configuration & Customization

### Vessel Parameters

```python
vessel = {
    'coeff': 0.0001,              # Cubic fuel coefficient
    'crew_cost_per_day': 1200,    # $/day
    'max_continuous_hours': 14,   # Crew fatigue limit
    'fuel_tanks_tonnes': 5000,    # Fuel capacity
}
```

### Economic Parameters

```python
params = {
    'bunker_price': 600,          # $/tonne
    'co2_factor': 3.15,           # tonnes CO2/tonne fuel
    'co2_price_per_ton': 50,      # $/tonne CO2
    'demurrage_per_hour': 200,    # $/hour
}
```

### Optimization Options

```python
result = optimizer.optimize_piecewise_speeds(
    arrival_deadline=datetime.now() + timedelta(days=30),
    speed_bounds=(10.0, 18.0),
    crew_fatigue_mode='soft',      # or 'hard'
    fatigue_penalty_weight=1000.0,
)
```

## Performance Considerations

- **Vectorization**: NumPy arrays for fast computation
- **Caching**: DataInterface caches loaded CSVs
- **Numerical Integration**: Gauss-Legendre quadrature for polynomial profiles
- **Optimization**: SciPy SLSQP with bounds and constraints

## Testing

Comprehensive test suite in `tests/test_voyage_optimizer.py`:
- Distance calculations
- Fuel model verification
- Cost evaluation
- Optimization convergence
- Crew fatigue modeling
- Edge cases and error handling

Run tests:
```bash
pytest tests/test_voyage_optimizer.py -v
```

## Future Enhancements

1. **Live API Integration**: Connect to real-time data sources
2. **Stochastic Optimization**: Handle weather/demand uncertainty
3. **Multi-Objective Optimization**: Pareto frontier exploration
4. **Bunkering Decisions**: Optimize fuel stops
5. **AIS Integration**: Real-time vessel tracking
6. **Advanced ML**: Deep learning for complex patterns
7. **Distributed Computing**: Parallel optimization for large fleets

## References

- Haversine Formula: https://en.wikipedia.org/wiki/Haversine_formula
- IMO 2030/2050 Regulations: https://www.imo.org/
- Emission Control Areas: https://www.imo.org/en/OurWork/Environment/Pages/Sulphur-oxides-(SOx)-%E2%80%93-Regulation-14.aspx

