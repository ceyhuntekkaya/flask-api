from setting.db import db
from datetime import datetime

class SensorModel(db.Model):
    __tablename__ = "sensors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    source = db.Column(db.String, unique=False, nullable=False)
    description = db.Column(db.String)

    hierarchy_id = db.Column(
        db.Integer, db.ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    official_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)

    sensor_weight = db.Column(db.REAL)
    unity_id = db.Column(db.Integer, db.ForeignKey("unities.id"), nullable=True)
    sensor_type = db.Column(db.String)
    evaluation_number = db.Column(db.Integer)
    rpm = db.Column(db.Integer)
    detection_range = db.Column(db.Integer)
    is_fusible = db.Column(db.Boolean)
    cake_slice = db.Column(db.Boolean)
    line_of_sight_angle = db.Column(db.REAL, default=3.0)
    line_of_sight_distance = db.Column(db.REAL, default=1000.0)
    near_circle = db.Column(db.Boolean, default=False)
    circle_radius = db.Column(db.Integer, default=250)
    circle_time_interval = db.Column(db.Integer, default=30)
    is_meteorology_includes = db.Column(db.Boolean)

    desired_columns = db.Column(db.ARRAY(db.String))
    # Allows "range", "azimuth", "directionangle", "velocity", "tacticaldataid", "snr", "temperature",
    # "humidity", "precipitationtype", "visibility", "roadconditon"

    models = db.Column(
        db.ARRAY(db.String)
    )  # "ecod", "copod", "if" (Minimum 1 item selected) (If no choice default is "if")
    filters = db.Column(
        db.ARRAY(db.String)
    )  # "tespit tekrarı", "hız", "tespit süresi" (Minimum 0 item selected)

    # Config
    training_config = db.Column(db.JSON)
    image = db.Column(db.TEXT)
    is_approved = db.Column(db.Boolean)

    nvr = db.Column(db.String)
