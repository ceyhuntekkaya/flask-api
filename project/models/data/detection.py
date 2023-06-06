from sqlalchemy import (
    REAL,
    TIMESTAMP,
    Column,
    Integer,
)
from sqlalchemy.orm import declarative_base
from project.models.base_model import BaseModelClass

Base = declarative_base()


class Detection(Base, BaseModelClass):
    __tablename__ = "detectiontable"

    id = Column(Integer, primary_key=True)
    detectionstarttime = Column(TIMESTAMP)
    detectionlat = Column(REAL)
    detectionlon = Column(REAL)
