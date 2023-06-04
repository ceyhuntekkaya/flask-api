from db import db


class SymbolModel(db.Model):
    __tablename__ = "symbols"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)

    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
