from project.models.base_model import BaseModelClass
from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
)

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UserPreferenceModel(Base, db.Model, BaseModelClass):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True)
    value = Column(String, unique=False, nullable=True)
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

    preference_id = Column(Integer, ForeignKey("preferences.id"))

