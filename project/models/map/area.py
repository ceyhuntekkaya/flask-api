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


class AreaModel(db.Model):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    description = Column(TEXT)
    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id")
    )



    area_type = Column(String)  # dost düşman
    area_parent = Column(String)  # motorize kara deniz
    area_sub = Column(String)  # piyade
    symbol_code = Column(String)  # app code
    critical_area_type = Column(String, unique=False, nullable=True)
    color = Column(String, unique=False, nullable=False)
    status = Column(Integer, default=1)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)

    created_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    updated_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )
    deleted_by = Column(
        Integer, ForeignKey("users.id"), unique=False, nullable=True
    )

