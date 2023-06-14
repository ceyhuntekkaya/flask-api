from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    ForeignKey,
)


class AreaLayerModel(db.Model):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True)
    area_id = Column(
        Integer, ForeignKey("areas.id"), unique=False, nullable=True
    )
    layer_id = Column(
        Integer, ForeignKey("layers.id"), unique=False, nullable=True
    )

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    created_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
