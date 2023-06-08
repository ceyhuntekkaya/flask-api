from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.detection.anomaly import AnomalyService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from db import db
from project.schemas.detection.anomaly import AnomalySchema

blp = Blueprint("Anomalies", "anomalies", description="Operations on detection")

main_route = "anomaly"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AnomalySchema)
    def get(self, item_id):
        service = AnomalyService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = AnomalyService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(AnomalySchema)
    @blp.response(201, AnomalySchema)
    def put(self, item_data, item_id):
        service = AnomalyService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AnomalySchema(many=True))
    def get(self):
        service = AnomalyService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(AnomalySchema)
    @blp.response(201, AnomalySchema)
    def post(self, item_data):
        service = AnomalyService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
