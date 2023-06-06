from db import db


class MarkerModel(db.Model):
    __tablename__ = "markers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)

    type = db.Column(db.String, unique=False, nullable=False)
    color = db.Column(db.String, unique=False, nullable=False)

    sensor_id = db.Column(db.Integer, db.ForeignKey("maps.id"), nullable=True)
    sign_id = db.Column(db.Integer, db.ForeignKey("maps.id"), nullable=True)
    symbol_id = db.Column(db.Integer, db.ForeignKey("maps.id"), nullable=True)
    unity_id = db.Column(db.Integer, db.ForeignKey("maps.id"), nullable=True)

    description = db.Column(db.String)
    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)

    map_id = db.Column(db.Integer, db.ForeignKey("maps.id"), nullable=True)
    layer_id = db.Column(db.Integer, db.ForeignKey("layers.id"), nullable=True)
    hierarchy_id = db.Column(
        db.Integer, db.ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    official_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)