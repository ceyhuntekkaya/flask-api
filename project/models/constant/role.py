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

class RoleModel(db.Model):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)

