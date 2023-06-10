from setting.db import db
from datetime import datetime
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
    ARRAY
)
class SensorModel(db.Model):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=False, nullable=False)
    source = Column(String, unique=False, nullable=False)
    description = Column(String)

    hierarchy_id = Column(
        Integer, ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    official_user_id = Column(Integer, db.ForeignKey("users.id"), nullable=True)

    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, nullable=True)
    deleted_at = Column(TIMESTAMP, nullable=True)
    status = Column(Integer, default=1)

    created_by = Column(Integer, nullable=True)
    updated_by = Column(Integer, nullable=True)
    deleted_by = Column(Integer, nullable=True)

    sensor_weight = Column(REAL)
    unity_id = Column(Integer, db.ForeignKey("unities.id"), nullable=True)
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
