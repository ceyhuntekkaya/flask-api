from setting.db import db
from datetime import datetime

from sqlalchemy import (
    JSON,
    TIMESTAMP,
    Column,
    Integer,
    ForeignKey,
    TEXT
)


class ConfigModel(db.Model):
    __tablename__ = "aselsan_config"

    id = Column(Integer, primary_key=True)
    description = Column(TEXT)
    config_json = Column(JSON)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
