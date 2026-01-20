![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
# NLPQuickie 🧠

FastAPI + spaCy (Spanish) API for NLP: word count, most common word, NER entities. 100% test coverage.

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.128-orange)](https://fastapi.tiangolo.com)
[![spaCy](https://img.shields.io/badge/spaCy-3.8-green)](https://spacy.io)

## 🚀 Quick Start
```bash
git clone <repo>
cd NLPQuickie
.\venv\Scripts\activate  # Windows
pip install -r requirements.txt
pip install -r requirements-dev.txt
python -m spacy download es_core_news_sm
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
[localhost:8000/docs](http://localhost:8000/docs)

## 📋 Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome |
| GET | `/live` | Health check |
| GET | `/process` | Usage info |
| POST | `/process` | `{\"text\": \"...\"}` → NLP JSON |

**POST Example:**
```bash
curl -X POST http://localhost:8000/process \\
  -H \"Content-Type: application/json\" \\
  -d '{\"text\": \"Elon Musk founded Tesla in California.\"}'
```
**Response:**
```json
{
  \"word_count\": 6,
  \"most_common_word\": {\"word\": \"in\", \"count\": 1},
  \"entities\": [
    {\"text\": \"Elon Musk\", \"label\": \"PERSON\"},
    {\"text\": \"Tesla\", \"label\": \"ORG\"},
    {\"text\": \"California\", \"label\": \"LOC\"}
  ],
  \"cleaned_sample\": \"elon musk founded tesla in california\"
}
```

## 🧠 NLP Features (`process.py`)
- **Pre-process:** Regex `[^\w\s]` removes punctuation.
- **Word count/top word:** `collections.Counter` (case-insensitive).
- **NER:** spaCy `es_core_news_sm` lazy load (PERSON, ORG, LOC...).
- Lazy: Model loads on first call.

## 🧪 Tests (100% cov)
```bash
pytest --cov
pytest tests/test_process.py::test_word_count  # Single
```
- 14 tests: unit (process_text), integration (endpoints).
- Mock spaCy for NER.

## 🔧 Development
See [AGENTS.md](AGENTS.md):
- Lint: `ruff check --fix .`
- Format: `black . ; isort .`
- Types: `mypy . --strict`
- Tests: `pytest --cov`

## 📊 Coverage
`pytest --cov-report=html` → `htmlcov/index.html`

## 🤝 Contributing
1. Fork/PR.
2. Tests pass + lint.
3. `pre-commit run`.

## 📄 License
MIT.

Built with ❤️ by opencode.