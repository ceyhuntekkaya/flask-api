from db import db


class MessageTemplateModel(db.Model):
    __tablename__ = "message_templates"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)