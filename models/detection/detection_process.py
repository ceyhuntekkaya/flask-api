from db import db


class DetectionProcessModel(db.Model):
    __tablename__ = "detection_process"

    id = db.Column(db.Integer, primary_key=True)
    detection_id = db.Column(db.Integer, db.ForeignKey("detections.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    process_at = db.Column(db.Integer)
    process = db.Column(db.String, nullable=False)

    create_at = db.Column(db.Integer)
    update_at = db.Column(db.Integer)
    delete_at = db.Column(db.Integer)
    active = db.Column(db.Boolean)

    create_by = db.Column(db.Integer)
    update_by = db.Column(db.Integer)
    delete_by = db.Column(db.Integer)