from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.detection.anomaly_note import AnomalyNoteModel
from project.schemas.detection.anomaly_note import AnomalyNoteSchema

blp = Blueprint("AnomalyNotes", "anomaly_notes", description="Operations on anomaly note")


@blp.route("/anomaly_note/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AnomalyNoteSchema)
    def get(self, item_id):
        item = AnomalyNoteModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = AnomalyNoteModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Anomaly note deleted"}, 200

    @blp.arguments(AnomalyNoteSchema)
    @blp.response(201, AnomalyNoteSchema)
    def put(self, item_data, item_id):
        item = AnomalyNoteModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = AnomalyNoteModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/anomaly_note")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AnomalyNoteSchema(many=True))
    def get(self):
        return AnomalyNoteModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(AnomalyNoteSchema)
    @blp.response(201, AnomalyNoteSchema)
    def post(self, item_data):
        item = AnomalyNoteModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A anomaly note with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the anomaly note.")

        return item
