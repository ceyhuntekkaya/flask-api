from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.detection.anomaly_route import AnomalyRouteService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from db import db
from project.schemas.detection.anomaly_route import AnomalyRouteSchema

blp = Blueprint("AnomalyRoutes", "anomaly_routes", description="Operations on anomaly route")

main_route = "anomaly_route"

@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AnomalyRouteSchema)
    def get(self, item_id):
        service = AnomalyRouteService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = AnomalyRouteService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(AnomalyRouteSchema)
    @blp.response(201, AnomalyRouteSchema)
    def put(self, item_data, item_id):
        service = AnomalyRouteService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AnomalyRouteSchema(many=True))
    def get(self):
        service = AnomalyRouteService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(AnomalyRouteSchema)
    @blp.response(201, AnomalyRouteSchema)
    def post(self, item_data):
        service = AnomalyRouteService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
