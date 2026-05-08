"""Endpoints para captura de muestras."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from app.db import get_db
from app.models.sample import Sample
from app.schemas.sample import SampleCreate, SampleRead

router = APIRouter(prefix="/api/samples", tags=["samples"])


@router.post("", response_model=SampleRead, status_code=201)
def create_sample(payload: SampleCreate, db: Session = Depends(get_db)):
    """Guarda una muestra capturada desde el frontend."""
    sample = Sample(
        label=payload.label,
        phase=payload.phase,
        rep_count=payload.rep_count,
        knee_angle_mean=payload.knee_angle_mean,
        trunk_inclination=payload.trunk_inclination,
        visibility_score=payload.visibility_score,
        features=payload.features,
    )
    try:
        db.add(sample)
        db.commit()
        db.refresh(sample)
    except SQLAlchemyError as exc:
        db.rollback()
        raise HTTPException(status_code=500, detail="No se pudo guardar la muestra.") from exc
    return sample
