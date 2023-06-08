from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.detection.anomaly_process import AnomalyProcessModel
from project.schemas.detection.anomaly_process import AnomalyProcessSchema

blp = Blueprint("AnomalyProcess", "anomaly_process", description="Operations on anomaly process")


@blp.route("/anomaly_process/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AnomalyProcessSchema)
    def get(self, item_id):
        item = AnomalyProcessModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = AnomalyProcessModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Anomaly process deleted"}, 200

    @blp.arguments(AnomalyProcessSchema)
    @blp.response(201, AnomalyProcessSchema)
    def put(self, item_data, item_id):
        item = AnomalyProcessModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = AnomalyProcessModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/anomaly_process")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AnomalyProcessSchema(many=True))
    def get(self):
        return AnomalyProcessModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(AnomalyProcessSchema)
    @blp.response(201, AnomalyProcessSchema)
    def post(self, item_data):
        item = AnomalyProcessModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A anomaly process with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the anomaly process.")

        return item
