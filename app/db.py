"""Configuracion de base de datos para PostgreSQL."""

from collections.abc import Generator
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://<user>:<password>@<host>:5432/<database>",
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """Base declarativa de SQLAlchemy."""


def get_db() -> Generator[Session, None, None]:
    """Entrega una sesion por request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
