# AGENTS.md

## Project Overview
FastAPI web app for NLP tasks using spaCy. Run with Uvicorn. Dev deps: ruff, black, mypy, pytest.

## Setup Commands
```bash
# Activate venv (Windows)
venv\\Scripts\\activate

# Install runtime deps
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Install dev deps (add requirements-dev.txt)
pip install ruff black mypy pytest pytest-cov isort
```

## Run Commands
```bash
# Dev server (reload)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Prod
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Lint & Format
```bash
# Lint (Ruff)
ruff check .

# Fix lint
ruff check --fix .

# Format (Black)
black .

# Sort imports
isort .

# Check all
pre-commit run --all-files
```

## Typecheck
```bash
mypy . --strict
```

## Test
```bash
pytest

# Single file
pytest tests/test_process.py

# Single test
pytest tests/test_process.py::test_nlp_pipe

# Coverage
pytest --cov
```

## Code Style

### Naming
- snake_case (funcs, vars)
- PascalCase (classes)
- UPPER_CASE (consts)

### Imports
Stdlib > 3rd > local. isort.

### Formatting
Black (88 chars), ruff.

### Typing
Full hints, mypy strict, Pydantic.

### FastAPI
HTTPException, deps, tags.

### spaCy
Lazy load, disable unused.

### Logging
logging.getLogger(__name__)

### Testing
pytest fixtures for app/nlp.

### Agent Rules
Run lint/type/test after changes. No comments unless asked. Mimic main.py style.

No Cursor/Copilot rules.