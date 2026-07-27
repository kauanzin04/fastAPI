# ⚡ FastAPI

Uma API REST simples desenvolvida com **FastAPI**, um framework moderno e de alto desempenho para Python. O projeto demonstra a criação de endpoints, o processamento de requisições HTTP e o retorno de respostas em formato JSON, servindo como base para aplicações web e serviços backend.

## ✨ Funcionalidades

* Criação de endpoints REST.
* Suporte aos métodos HTTP (`GET`, `POST`, `PUT` e `DELETE`).
* Respostas em formato JSON.
* Validação automática de dados com **Pydantic**.
* Documentação interativa gerada automaticamente.

## 🛠️ Tecnologias Utilizadas

* Python 3
* FastAPI
* Uvicorn
* Pydantic

## 🚀 Executando o Projeto

Instale as dependências:

```bash
pip install fastapi uvicorn
```

Inicie o servidor:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

* **Servidor:** `http://127.0.0.1:8000`
* **Documentação Swagger:** `http://127.0.0.1:8000/docs`
* **Documentação ReDoc:** `http://127.0.0.1:8000/redoc`

## 📚 Objetivo

Este projeto foi desenvolvido para praticar conceitos fundamentais de desenvolvimento de APIs utilizando FastAPI, incluindo roteamento, tratamento de requisições, validação de dados e criação de serviços web escaláveis.
