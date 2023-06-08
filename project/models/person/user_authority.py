from setting.db import db


class UserAuthorityModel(db.Model):
    __tablename__ = "user_authorities"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    authority_type = db.Column(db.String, unique=False, nullable=True)
    create_at = db.Column(db.Integer,nullable=True)
    update_at = db.Column(db.Integer, nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)

    create_by = db.Column(db.Integer,nullable=True)
    update_by = db.Column(db.Integer, nullable=True)
    delete_by = db.Column(db.Integer, nullable=True)

    authority_id = db.Column(db.Integer, db.ForeignKey("authorities.id"))
