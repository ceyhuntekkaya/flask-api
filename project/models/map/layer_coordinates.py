from setting.db import db


class LayerCoordinateModel(db.Model):
    __tablename__ = "layer_coordinates"

    id = db.Column(db.Integer, primary_key=True)
    row_number = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)

    layer_id = db.Column(
        db.Integer, db.ForeignKey("layers.id"), unique=False, nullable=False
    )

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)

