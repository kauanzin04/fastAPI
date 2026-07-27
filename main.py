import os
from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Minha API",
    description="Esta é uma API de exemplo usando FastAPI.",
    version="1.0.0",
)

mensagem = os.environ.get("apareceu", "olá, mundo!")  # Valor padrão caso a variável de ambiente não esteja definida

@app.get("/")
def read_root():
    return {"message": mensagem}

@app.get("/status")
def read_status():
    return {"status": "API está funcionando corretamente."}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )