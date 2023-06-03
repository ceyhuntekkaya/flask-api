from db import db


class HierarchyModel(db.Model):
    __tablename__ = "hierarchies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    hierarchical_order = db.Column(db.Integer, unique=True, nullable=False)