from datetime import datetime

from setting.db import db
from project.models.base_model import BaseModelClass

from sqlalchemy import (
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class UserModel(Base, db.Model, BaseModelClass):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    surname = Column(String, unique=False, nullable=False)
    registration_number = Column(String, unique=True, nullable=True)
    phone = Column(String, unique=False, nullable=True)
    mail = Column(String, unique=True, nullable=True)
    code = Column(String, unique=False, nullable=True)
    phone_extension_line = Column(String, unique=False, nullable=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String(255), nullable=False)

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
    last_login = Column(Integer, nullable=True)
    last_login_ip = Column(String, unique=False, nullable=True)

    role_id = Column(
        Integer, ForeignKey("roles.id"), unique=False, nullable=True
    )
    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    command_id = Column(
        Integer, ForeignKey("commands.id"), unique=False, nullable=False
    )
    command_collar_mark_id = Column(
        Integer, ForeignKey("command_collar_marks.id"), unique=False, nullable=False
    )
    command_collar_mark_rank_id = Column(
        Integer, ForeignKey("command_collar_mark_ranks.id"), unique=False, nullable=False
    )

