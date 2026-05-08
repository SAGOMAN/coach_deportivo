"""FastAPI: sirve la SPA y archivos estáticos (MediaPipe corre en el navegador)."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.db import Base, engine
from app import models  # noqa: F401
from app.routers.samples import router as samples_router

ROOT = Path(__file__).resolve().parent.parent
STATIC = ROOT / "static"

app = FastAPI(title="Contador de ejercicios")
app.mount("/static", StaticFiles(directory=str(STATIC)), name="static")
app.include_router(samples_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
async def index():
    return FileResponse(str(STATIC / "index.html"))
