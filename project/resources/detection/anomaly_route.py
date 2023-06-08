from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.detection.anomaly_route import AnomalyRouteModel
from project.schemas.detection.anomaly_route import AnomalyRouteSchema

blp = Blueprint("AnomalyRoutes", "anomaly_routes", description="Operations on anomaly route")


@blp.route("/anomaly_route/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AnomalyRouteSchema)
    def get(self, item_id):
        item = AnomalyRouteModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = AnomalyRouteModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Anomaly route deleted"}, 200

    @blp.arguments(AnomalyRouteSchema)
    @blp.response(201, AnomalyRouteSchema)
    def put(self, item_data, item_id):
        item = AnomalyRouteModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = AnomalyRouteModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/anomaly_route")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AnomalyRouteSchema(many=True))
    def get(self):
        return AnomalyRouteModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(AnomalyRouteSchema)
    @blp.response(201, AnomalyRouteSchema)
    def post(self, item_data):
        item = AnomalyRouteModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A anomaly route with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the anomaly route.")

        return item
