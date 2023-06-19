from setting.db import db
from datetime import datetime
from sqlalchemy import (
    TEXT,
    TIMESTAMP,
    Column,
    Integer,
    String,
    ForeignKey,
    Float
)


class EquipmentModel(db.Model):
    __tablename__ = "equipments"

    id = Column(Integer, primary_key=True)
    src = Column(String, unique=False)
    description = Column(TEXT)
    unit_id = Column(Integer, ForeignKey("units.id"), unique=False, nullable=False)
    name = Column(String, unique=True, nullable=False)
    equipment_type = Column(String)
    lat = Column(Float(precision=5), nullable=False)
    lon = Column(Float(precision=5), nullable=False)

    standardIdentityFirstDigit = Column(String)
    standardIdentitySecondDigit = Column(String)
    symbolSet = Column(String)
    entity = Column(String)
    entityType = Column(String)
    sectorIModifier = Column(String)
    sectorIIModifier = Column(String)
    hqTaskforceDummy = Column(String)
    amplifier = Column(String)
    symbolCode = Column(String)






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