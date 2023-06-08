from db import db


class IdentificationTypeModel(db.Model):
    __tablename__ = "identification_type"

    id = db.Column(db.Integer, primary_key=True)

    identification_id = db.Column(db.Integer)
    identification = db.Column(db.String)

    create_at = db.Column(db.Integer, nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer, nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
