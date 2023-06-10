from setting.db import db
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
    Float,
)


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")
