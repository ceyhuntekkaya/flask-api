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

class CommandCollarMarkModel(db.Model):
    __tablename__ = "command_collar_marks"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    hierarchical_order = Column(Integer, unique=True, nullable=False)
    command_id = Column(
        Integer, ForeignKey("commands.id"), unique=False, nullable=False
    )

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)
