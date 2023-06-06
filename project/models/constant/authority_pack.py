from db import db


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

    create_at = db.Column(db.Integer, nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)
