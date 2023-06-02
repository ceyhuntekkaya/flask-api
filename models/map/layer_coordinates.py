from db import db


class LayerCoordinateModel(db.Model):
    __tablename__ = "layer_coordinates"

    id = db.Column(db.Integer, primary_key=True)
    row_number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)

    layer_id = db.Column(
        db.Integer, db.ForeignKey("layers.id"), unique=False, nullable=False
    )
   
