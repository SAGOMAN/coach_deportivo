"""Esquemas para entrada/salida de muestras."""

from datetime import datetime

from pydantic import BaseModel, Field


class SampleCreate(BaseModel):
    """Carga util para guardar una muestra."""

    label: str = Field(pattern="^(correcto|incorrecto)$")
    phase: str = "neutral"
    rep_count: int = 0
    knee_angle_mean: float | None = None
    trunk_inclination: float | None = None
    visibility_score: float | None = None
    features: dict = Field(default_factory=dict)


class SampleRead(BaseModel):
    """Respuesta de muestra persistida."""

    id: int
    label: str
    phase: str
    rep_count: int
    knee_angle_mean: float | None
    trunk_inclination: float | None
    visibility_score: float | None
    features: dict
    captured_at: datetime

    model_config = {"from_attributes": True}
