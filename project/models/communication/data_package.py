from setting.db import db
from datetime import datetime


class DataPackageModel(db.Model):
    __tablename__ = "data_packages"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    data_from = db.Column(db.Integer, db.ForeignKey("users.id"))
    data_to = db.Column(db.Integer, db.ForeignKey("users.id"))

    header = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer)
    send_ip = db.Column(db.String)
    data_type = db.Column(db.String)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
