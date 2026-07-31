import secrets
import string
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles

links = {}

foxhole = FastAPI(title="FoxHole", version="1.0")

STATIC_DIR = Path(__file__).parent / "static"


@foxhole.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


def gerar_codigo_unico():
    caracteres = string.ascii_uppercase + string.digits

    while True:
        codigo = ''.join(secrets.choice(caracteres) for _ in range(6))

        if codigo not in links:
            return codigo


@foxhole.get("/encurtar")
def encurtar(link: str):
    codigo = gerar_codigo_unico()

    links[codigo] = link

    return {
        "codigo": codigo,
        "url_original": link,
        "url_encurtada": f"http://127.0.0.1:8000/{codigo}"
    }


@foxhole.get("/{codigo}")
def redirecionar(codigo: str):

    if codigo not in links:
        raise HTTPException(
            status_code=404,
            detail="Link não encontrado"
        )

    return RedirectResponse(url=links[codigo])


foxhole.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")