from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    ForeignKey,
)


class UnitLayerModel(db.Model):
    __tablename__ = "units"

    id = Column(Integer, primary_key=True)
    unit_id = Column(
        Integer, ForeignKey("units.id"), unique=False, nullable=False
    )
    layer_id = Column(
        Integer, ForeignKey("layers.id"), unique=False, nullable=False
    )

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
