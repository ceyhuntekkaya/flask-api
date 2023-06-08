from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.detection.detection import DetectionService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.detection.detection import DetectionSchema

blp = Blueprint("Detections", "detections", description="Operations on detection")

main_route = "detection"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, DetectionSchema)
    def get(self, item_id):
        service = DetectionService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = DetectionService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(DetectionSchema)
    @blp.response(201, DetectionSchema)
    def put(self, item_data, item_id):
        service = DetectionService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, DetectionSchema(many=True))
    def get(self):
        service = DetectionService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(DetectionSchema)
    @blp.response(201, DetectionSchema)
    def post(self, item_data):
        service = DetectionService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
