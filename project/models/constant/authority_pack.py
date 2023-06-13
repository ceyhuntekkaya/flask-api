from setting.db import db
from datetime import datetime

from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
    TEXT
)


class AuthorityPackModel(db.Model):
    __tablename__ = "authority_packs"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    authority_id = Column(
        Integer, ForeignKey("authorities.id"), unique=False, nullable=False
    )
    role_id = Column(
        Integer, ForeignKey("roles.id"), unique=False, nullable=True
    )
    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    description = Column(TEXT)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
