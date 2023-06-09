from setting.db import db
from datetime import datetime

class SingModel(db.Model):
    __tablename__ = "sings"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    source = db.Column(db.String, unique=False, nullable=False)
    description = db.Column(db.String)

    hierarchy_id = db.Column(
        db.Integer, db.ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    official_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
