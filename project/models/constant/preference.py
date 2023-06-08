from setting.db import db


class PreferenceModel(db.Model):
    __tablename__ = "preferences"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    create_at = db.Column(db.Integer, nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer, nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
