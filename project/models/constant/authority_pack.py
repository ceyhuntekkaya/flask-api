from setting.db import db
from datetime import datetime


class AuthorityPackModel(db.Model):
    __tablename__ = "authority_packs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    authority_id = db.Column(
        db.Integer, db.ForeignKey("authorities.id"), unique=False, nullable=False
    )
    role_id = db.Column(
        db.Integer, db.ForeignKey("roles.id"), unique=False, nullable=False
    )

    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=True)
    deleted_at = db.Column(db.TIMESTAMP, nullable=True)
    status = db.Column(db.Integer, default=1)

    created_by = db.Column(db.Integer,nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    deleted_by = db.Column(db.Integer, nullable=True)
