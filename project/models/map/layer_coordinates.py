from setting.db import db
from datetime import datetime

class LayerCoordinateModel(db.Model):
    __tablename__ = "layer_coordinates"

    id = db.Column(db.Integer, primary_key=True)
    row_number = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)

    layer_id = db.Column(
        db.Integer, db.ForeignKey("layers.id"), unique=False, nullable=False
    )

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)

