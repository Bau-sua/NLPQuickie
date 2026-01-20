![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
# NLPQuickie 🧠

API FastAPI + spaCy (español) para NLP: conteo palabras, palabra más usada, NER entidades. Tests 100% cov.

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128-orange)](https://fastapi.tiangolo.com)
[![spaCy](https://img.shields.io/badge/spaCy-3.8-green)](https://spacy.io)

## 🚀 Inicio rápido
```bash
git clone <repo>
cd NLPQuickie
venv\\Scripts\\activate  # Windows
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m spacy download es_core_news_sm
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
[localhost:8000/docs](http://localhost:8000/docs)

## 📋 Endpoints
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Bienvenida |
| GET | `/live` | Health check |
| GET | `/process` | Info uso |
| POST | `/process` | `{\"text\": \"...\"}` → NLP JSON |

**Ejemplo POST:**
```bash
curl -X POST http://localhost:8000/process \\
  -H \"Content-Type: application/json\" \\
  -d '{\"text\": \"Elon Musk fundó Tesla en California.\"}'
```
**Respuesta:**
```json
{
  \"word_count\": 6,
  \"most_common_word\": {\"word\": \"en\", \"count\": 1},
  \"entities\": [
    {\"text\": \"Elon Musk\", \"label\": \"PERSON\"},
    {\"text\": \"Tesla\", \"label\": \"ORG\"},
    {\"text\": \"California\", \"label\": \"LOC\"}
  ],
  \"cleaned_sample\": \"elon musk fundó tesla en california\"
}
```

## 🧠 Features NLP (`process.py`)
- **Pre-proceso:** Regex `[^\w\s]` quita puntuación.
- **Conteo/top palabra:** `collections.Counter` (case-insens).
- **NER:** spaCy `es_core_news_sm` lazy load (PERSON, ORG, LOC...).
- Lazy: Primera llamada carga modelo.

## 🧪 Tests (100% cov)
```bash
pytest --cov
pytest tests/test_process.py::test_word_count  # Single
```
- 14 tests: unit (process_text), integration (endpoints).
- Mock spaCy para NER.

## 🔧 Desarrollo
Ver [AGENTS.md](AGENTS.md):
- Lint: `ruff check --fix .`
- Format: `black . ; isort .`
- Types: `mypy . --strict`
- Tests: `pytest --cov`

## 📊 Coverage
`pytest --cov-report=html` → `htmlcov/index.html`

## 🤝 Contribuir
1. Fork/PR.
2. Tests pass + lint.
3. `pre-commit run`.

## 📄 License
MIT.

Desarrollado con ❤️ por opencode.