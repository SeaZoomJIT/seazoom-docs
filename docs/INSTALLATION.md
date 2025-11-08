# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (optional)

## Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/seazoom-voyage-optimizer.git
cd seazoom-voyage-optimizer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
pytest tests/ -v
# Expected: 694 passed
```

## Installation Methods

### Method 1: pip

```bash
pip install seazoom-voyage-optimizer
```

### Method 2: From Source

```bash
git clone https://github.com/yourusername/seazoom-voyage-optimizer.git
cd seazoom-voyage-optimizer
pip install -e .
```

### Method 3: Docker

```bash
docker build -t seazoom:latest .
docker run -it seazoom:latest
```

## Dependencies

- numpy - Numerical computing
- pandas - Data manipulation
- scipy - Scientific computing
- scikit-learn - Machine learning
- plotly - Interactive visualizations
- matplotlib - Static plots
- requests - HTTP requests

## Troubleshooting

### Import Error

```bash
python -c "import seazoom; print('✅ SeaZoom installed')"
```

### Test Failures

```bash
pip install -r requirements.txt --upgrade
pytest tests/ -v
```

### Visualization Issues

```bash
pip install plotly matplotlib
```

## Next Steps

1. Read USAGE.md
2. Explore examples/ folder
3. Check notebooks/ folder
4. Review API.md

---

**SeaZoom Voyage Optimizer** - Production-Ready Maritime Optimization System
