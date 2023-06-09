from setting.db import db
from datetime import datetime


class IdentificationTypeModel(db.Model):
    __tablename__ = "identification_type"

    id = db.Column(db.Integer, primary_key=True)

    identification_id = db.Column(db.Integer)
    identification = db.Column(db.String)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
