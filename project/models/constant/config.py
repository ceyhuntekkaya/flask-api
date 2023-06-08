from setting.db import db


class ConfigModel(db.Model):
    __tablename__ = "aselsan_config"

    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.Integer, default=1)
    config_json = db.Column(db.JSON)

    create_at = db.Column(db.Integer, nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer, nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
