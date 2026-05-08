"""Modelo ORM para muestras etiquetadas."""

from datetime import datetime

from sqlalchemy import DateTime, Float, Integer, JSON, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class Sample(Base):
    """Registro de una muestra capturada desde webcam."""

    __tablename__ = "samples"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    label: Mapped[str] = mapped_column(String(20), nullable=False, index=True)
    phase: Mapped[str] = mapped_column(String(20), nullable=False, default="neutral")
    rep_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    knee_angle_mean: Mapped[float | None] = mapped_column(Float, nullable=True)
    trunk_inclination: Mapped[float | None] = mapped_column(Float, nullable=True)
    visibility_score: Mapped[float | None] = mapped_column(Float, nullable=True)
    features: Mapped[dict] = mapped_column(JSON, nullable=False)
    captured_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
