from db import db


class DetectionNoteModel(db.Model):
    __tablename__ = "detection_notes"

    id = db.Column(db.Integer, primary_key=True)
    detection_id = db.Column(db.Integer, db.ForeignKey("detections.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    note_at = db.Column(db.Integer)
    content = db.Column(db.String, nullable=False)