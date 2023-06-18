from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
)


class UserAuthorityModel(db.Model):
    __tablename__ = "user_authorities"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    authority_id = Column(Integer, ForeignKey("authorities.id"))
    authority_type = Column(String, unique=False, nullable=True)

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

