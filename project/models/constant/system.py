from setting.db import db


class SystemModel(db.Model):
    __tablename__ = "aselsan_system"

    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, default=1)

    system_status = db.Column(db.Enum("training", "live", "standby", name="SystemStatusEnum"), default="standby")

    create_at = db.Column(db.Integer, nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer, nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)