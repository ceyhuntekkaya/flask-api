from setting.db import db


class NotificationToListModel(db.Model):
    __tablename__ = "notification_to_list"

    id = db.Column(db.Integer, primary_key=True)
    notification_id = db.Column(db.Integer, db.ForeignKey("notifications.id"))
    read_at = db.Column(db.Integer, nullable=True)
    read_ip = db.Column(db.String)
    