from setting.db import db
from datetime import datetime
from sqlalchemy import (
    JSON,
    REAL,
    TEXT,
    TIMESTAMP,
    Boolean,
    Column,
    Enum,
    Integer,
    String,
    ForeignKey,
)
class LayerModel(db.Model):
    __tablename__ = "layers"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    description = Column(String)
    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    official_user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    color = Column(String, unique=False, nullable=False)
    layer_type = Column(String, unique=False, nullable=False)
    critical_area_type = Column(String, unique=False, nullable=True)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)
