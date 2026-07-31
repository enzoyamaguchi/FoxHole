# 🦊 Foxhole API — Fast & Minimalist Link Shortener

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg)](https://fastapi.tiangolo.com/)

> **Foxhole** é uma API RESTful leve e funcional desenvolvida em Python para encurtamento rápido de URLs e redirecionamento dinâmico.

---

## 📐 Como a Aplicação Funciona

O fluxo do Foxhole foi projetado para ser direto e simples:

1. **Encurtamento (`GET /encurtar`):** A aplicação recebe uma URL, gera um código aleatório e único de 6 caracteres utilizando a biblioteca `secrets` e armazena o mapeamento na memória.
2. **Redirecionamento (`GET /{codigo}`):** O usuário acessa o link encurtado, o backend busca o código correspondente e redireciona automaticamente para a URL de destino (`HTTP 307`). Caso o código não exista, a API retorna `HTTP 404`.
3. **Interface Visual (`GET /`):** A API serve diretamente os arquivos estáticos da interface web construída para interação do usuário.

---

## 🛠️ Tecnologias Utilizadas

### Backend
* **Linguagem:** Python 3.10+
* **Framework Web:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Geração de Hashes:** Módulo nativo `secrets` e `string`

### Frontend
* **Interface Visual:** HTML/CSS/JS estático gerado com auxílio de **Inteligência Artificial**, permitindo foco total na construção da lógica de backend em Python.

---

## DEMONSTRAÇÂO 
![Demonstração do projeto](./img/demo.gif)
## 📂 Estrutura do Projeto

```text
foxhole/
├── static/
│   ├── index.html       # Interface gráfica (Gerada Totalmente com IA)
├── main.py              # Aplicação principal FastAPI e rotas
