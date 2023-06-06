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
)
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base, relationship
from models.base_model import BaseModelClass

Base = declarative_base()


class Detection(Base, BaseModelClass):
    __tablename__ = "detectiontable"

    id = Column(Integer, primary_key=True)
    detectionstarttime = Column(TIMESTAMP)
    detectionlat = Column(REAL)
    detectionlon = Column(REAL)
