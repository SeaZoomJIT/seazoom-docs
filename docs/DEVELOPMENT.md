# Development Guide

## Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/seazoom-voyage-optimizer.git
cd seazoom-voyage-optimizer
```

### 2. Create Development Environment

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install black flake8 mypy pytest pytest-cov
```

### 3. Verify Setup

```bash
pytest tests/ -q
# Expected: 694 passed
```

## Development Workflow

### 1. Create Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

```bash
# Edit files
# Add tests
pytest tests/ -v
```

### 3. Code Quality

```bash
black seazoom/ tests/
flake8 seazoom/ tests/
mypy seazoom/
```

### 4. Commit Changes

```bash
git add .
git commit -m "Add your feature description"
```

### 5. Push and Create PR

```bash
git push origin feature/your-feature-name
# Create pull request on GitHub
```

## Code Style

Follow PEP 8:
- Classes: PascalCase
- Functions: snake_case
- Constants: UPPER_SNAKE_CASE
- Private: _leading_underscore

## Module Structure

```
seazoom/my_module/
├── __init__.py
├── core.py
├── models.py
├── utils.py
└── validators.py
```

## Testing

```python
import pytest

class TestMyClass:
    @pytest.fixture
    def instance(self):
        return MyClass(param="test")
    
    def test_method(self, instance):
        result = instance.method()
        assert result is not None
```

## Git Workflow

Commit messages:
- feat: Add new feature
- fix: Fix bug
- docs: Update documentation
- style: Format code
- refactor: Refactor code
- test: Add tests
- chore: Update dependencies

## Performance Optimization

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()
# Your code here
profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)
```

## Contributing

1. Fork repository
2. Create feature branch
3. Make changes
4. Write tests
5. Run tests
6. Format code
7. Create pull request

## Pull Request Checklist

- [ ] Tests pass (694/694)
- [ ] Code formatted (black)
- [ ] Code linted (flake8)
- [ ] Type checked (mypy)
- [ ] Documentation updated
- [ ] Commit messages clear
- [ ] No breaking changes

---

**SeaZoom Voyage Optimizer** - Production-Ready Maritime Optimization System
