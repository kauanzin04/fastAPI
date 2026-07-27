from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="Minha API",
    description="Esta é uma API de exemplo usando FastAPI.",
    version="1.0.0",
)

class usuario(BaseModel):
    nome: str
    idade: int
    email: str

usuarios = []

#GET
@app.get("/")
def inicio():
    return {"message": "API funcionando!"}

#GET buscando dados
@app.get("/usuarios")
def listar_usuarios():
    return usuarios

#POST criando dados
@app.post("/usuarios")
def criar_usuario(usuario: usuario):
    usuarios.append(usuario)
    return {"message": "Usuário criado com sucesso!", "usuario": usuario}

#PUT atualizando dados
@app.put("/usuarios/{id}")
def atualizar_usuario(id: int, usuario: usuario):
    usuarios[id] = usuario
    return {"message": "Usuário atualizado com sucesso!", "usuario": usuario}

#DELETE deletando dados
@app.delete("/usuarios/{id}")
def deletar_usuario(id: int):
    usuario = usuarios.pop(id)
    return {"message": "Usuário deletado com sucesso!", "usuario": usuario}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )