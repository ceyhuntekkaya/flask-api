from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Enum,
    Integer,
    ForeignKey,
)


class SystemModel(db.Model):
    __tablename__ = "aselsan_system"

    id = Column(Integer, primary_key=True)
    status = Column(Integer, default=1)

    system_status = Column(Enum("training", "live", "standby", name="SystemStatusEnum"), default="standby")

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
