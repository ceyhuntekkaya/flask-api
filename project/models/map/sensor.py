from setting.db import db
from datetime import datetime
from sqlalchemy import (
    JSON,
    REAL,
    TEXT,
    TIMESTAMP,
    Boolean,
    Column,
    Integer,
    String,
    ForeignKey,
    ARRAY,
    Float
)


class SensorModel(db.Model):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True)
    source = Column(String, unique=False, nullable=False)
    description = Column(TEXT)
    hierarchy_id = Column(Integer, ForeignKey("hierarchies.id"), unique=False, nullable=False)
    name = Column(String, unique=True, nullable=False)
    sensor_weight = Column(REAL)
    aselsan_unit_id = Column(Integer)
    unit_id = Column(Integer, ForeignKey("units.id"), nullable=True)
    sensor_type = Column(String)
    evaluation_number = Column(Integer)
    rpm = Column(Integer)
    detection_range = Column(Integer)
    is_fusible = Column(Boolean)
    cake_slice = Column(Boolean)
    line_of_sight_angle = Column(REAL, default=3.0)
    line_of_sight_distance = Column(REAL, default=1000.0)
    near_circle = Column(Boolean, default=False)
    circle_radius = Column(Integer, default=250)
    circle_time_interval = Column(Integer, default=30)
    is_meteorology_includes = Column(Boolean)
    latitude = Column(Float(precision=5), nullable=False)
    longitude = Column(Float(precision=5), nullable=False)
    desired_columns = Column(ARRAY(String))
    # Allows "range", "azimuth", "directionangle", "velocity", "tacticaldataid", "snr", "temperature",
    # "humidity", "precipitationtype", "visibility", "roadconditon"

    models = Column(
        ARRAY(String)
    )  # "ecod", "copod", "if" (Minimum 1 item selected) (If no choice default is "if")
    filters = Column(
        ARRAY(String)
    )  # "tespit tekrarı", "hız", "tespit süresi" (Minimum 0 item selected)

    # Config
    training_config = Column(JSON)
    image = Column(TEXT)
    is_approved = Column(Boolean)

    nvr = Column(String)

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
