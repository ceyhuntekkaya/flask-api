from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.detection.anomaly import AnomalyModel
from project.schemas.detection.anomaly import AnomalySchema

blp = Blueprint("Anomalies", "anomalies", description="Operations on detection")


@blp.route("/anomaly/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AnomalySchema)
    def get(self, item_id):
        item = AnomalyModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = AnomalyModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Detection deleted"}, 200

    @blp.arguments(AnomalySchema)
    @blp.response(201, AnomalySchema)
    def put(self, item_data, item_id):
        item = AnomalyModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = AnomalyModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/anomaly")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AnomalySchema(many=True))
    def get(self):
        return AnomalyModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(AnomalySchema)
    @blp.response(201, AnomalySchema)
    def post(self, item_data):
        item = AnomalyModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A anomaly with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the detection.")

        return item
