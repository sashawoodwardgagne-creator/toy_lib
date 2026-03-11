# toy-lib

A tiny, fully functional example Python library that you can install directly
from a Git repository. It demonstrates best practices:

- `pyproject.toml` (modern packaging with Hatchling)
- `src/` layout
- CLI entry point (`toy-hello`)
- Including data files
- Basic unit tests with `pytest`

## Install from a local path
```bash
python -m pip install .
```

## Install from GitHub (replace ORG/REPO and tag)
```bash
python -m pip install "git+https://github.com/ORG/REPO.git@v0.1.0"
```

## Use in Python
```python
from toy_lib import add, greet
print(add(2, 3))      # 5
print(greet("Sasha")) # Hello, Sasha!
```

## CLI
```bash
toy-hello Sasha
# -> Hello, Sasha!
```

## Run tests
```bash
python -m pip install -e .[dev]
pytest -q
```
