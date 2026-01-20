from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any

from process import process_text

# Crear instancia de FastAPI con metadatos
app = FastAPI(
    title="NLPQuickie",
    description="API simple para tareas de Procesamiento de Lenguaje Natural (NLP) usando spaCy",
    version="0.1.0",
)


# Modelo Pydantic para validar el body del POST /process
# Asegura que el JSON tenga campo 'text' de tipo string
class TextInput(BaseModel):
    """
    Modelo de entrada para el endpoint POST /process.
    Campos requeridos:
    - text: str (el texto a procesar con NLP)
    """

    text: str


@app.get("/")
def read_root() -> Dict[str, Any]:
    """
    Endpoint raíz: Mensaje de bienvenida y estado de la app.
    """
    return {
        "message": "Bienvenido a NLPQuickie",
        "endpoints": ["/live", "/process (POST)"],
    }


@app.get("/live")
def read_alive() -> Dict[str, Any]:
    """
    Health check: Confirma que el servidor está vivo y respondiendo.
    Retorna 200 OK para monitoreo (uptime).
    """
    return {"status": "200 OK", "alive": True, "service": "NLP API"}


@app.get("/process")
def read_process_get() -> Dict[str, Any]:
    """
    Info sobre el endpoint de procesamiento (GET temporal).
    Para procesar texto, usa POST /process con JSON {'text': 'tu texto'}
    """
    return {
        "message": "Endpoint NLP listo. Usa POST /process",
        "example": {"text": "Apple es una empresa en California"},
    }


@app.post("/process")  # Renombrado para evitar conflicto con import
def api_process_text(input_data: TextInput) -> Dict[str, Any]:
    """
    Endpoint principal POST /process:
    - Recibe JSON con 'text'
    - Valida con Pydantic
    - Llama a process_text() en process.py
    - Retorna entidades NER, tokens, etc.
    Ejemplo request: curl -X POST http://localhost:8000/process -H "Content-Type: application/json" -d '{"text": "Hola mundo"}'
    """
    # Procesar el texto recibido
    result = process_text(input_data.text)
    return result
