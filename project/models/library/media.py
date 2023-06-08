from setting.db import db


class MediaModel(db.Model):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String, unique=True, nullable=False)

    latitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    longitude = db.Column(db.Float(precision=5), unique=False, nullable=False)
    begin_at = db.Column(db.Integer, nullable=False)
    end_at = db.Column(db.Integer, nullable=False)

    media_type = db.Column(db.String, unique=True, nullable=False)
    credential = db.Column(db.String)
    storage_address = db.Column(db.String)
    
    media_source_id = db.Column(db.Integer, db.ForeignKey("media_sources.id"), nullable=True)
    map_id = db.Column(db.Integer, db.ForeignKey("maps.id"), nullable=True)
    layer_id = db.Column(db.Integer, db.ForeignKey("layers.id"), nullable=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey("sensors.id"), nullable=True)
    unity_id = db.Column(db.Integer, db.ForeignKey("unities.id"), nullable=True)
    official_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    status = db.Column(db.String, unique=True, nullable=False)

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
