from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
)


class DataPackageModel(db.Model):
    __tablename__ = "data_packages"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    data_from = Column(Integer, ForeignKey("users.id"))
    data_to = Column(Integer, ForeignKey("users.id"))

    header = Column(String, nullable=False)
    content = Column(TEXT, nullable=False)
    priority = Column(Integer)
    send_ip = Column(String)
    data_type = Column(String)

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
