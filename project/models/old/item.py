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


class ItemModel(db.Model):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    description = Column(String)
    price = Column(Float(precision=2), unique=False, nullable=False)

    store_id = db.Column(
        Integer, ForeignKey("stores.id"), unique=False, nullable=False
    )
    store = db.relationship("StoreModel", back_populates="items")

    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")
