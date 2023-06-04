from db import db


class UnityModel(db.Model):
    __tablename__ = "unities"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    source = db.Column(db.String, unique=False, nullable=False)
    description = db.Column(db.String)

    hierarchy_id = db.Column(
        db.Integer, db.ForeignKey("hierarchies.id"), unique=False, nullable=False
    )
    official_user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
