from db import db


class MessageToListModel(db.Model):
    __tablename__ = "message_to_list"

    id = db.Column(db.Integer, primary_key=True)
    messege_id = db.Column(db.Integer, db.ForeignKey("message.id"))
    read_at = db.Column(db.Integer, nullable=True)
    read_ip = db.Column(db.String)
    

