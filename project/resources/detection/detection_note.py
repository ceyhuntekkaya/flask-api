from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.detection.detection_note import DetectionNoteModel
from project.schemas.detection.detection_note import DetectionNoteSechema

blp = Blueprint("DetectionNotes", "detection_notes", description="Operations on detection note")


@blp.route("/detection_note/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, DetectionNoteSechema)
    def get(self, item_id):
        item = DetectionNoteModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = DetectionNoteModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Detection note deleted"}, 200

    @blp.arguments(DetectionNoteSechema)
    @blp.response(201, DetectionNoteSechema)
    def put(self, item_data, item_id):
        item = DetectionNoteModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = DetectionNoteModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/detection_note")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, DetectionNoteSechema(many=True))
    def get(self):
        return DetectionNoteModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(DetectionNoteSechema)
    @blp.response(201, DetectionNoteSechema)
    def post(self, item_data):
        item = DetectionNoteModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A detection note with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the detection note.")

        return item
