from db import db


class NotificationModel(db.Model):
    __tablename__ = "notifications"

    id = db.Column(db.Integer, primary_key=True)
    
    header = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    priority = db.Column(db.Integer)
    send_ip = db.Column(db.String)
    notification_type = db.Column(db.String)

    notification_from = db.Column(db.Integer, db.ForeignKey("users.id"))

    create_at = db.Column(db.Integer,nullable=True)
    delete_at = db.Column(db.Integer, nullable=True)
    create_by = db.Column(db.Integer,nullable=True)
