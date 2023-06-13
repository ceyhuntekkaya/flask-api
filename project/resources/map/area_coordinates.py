from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.map.area_coordinates import AreaCoordinateService
from project.schemas.map.area_coordinates import AreaCoordinateSchema
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db


blp = Blueprint("AreaCoordinates", "area_coordinates", description="Operations on area coordinates")

main_route = "area_coordinate"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AreaCoordinateSchema)
    def get(self, item_id):
        service = AreaCoordinateService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = AreaCoordinateService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(AreaCoordinateSchema)
    @blp.response(201, AreaCoordinateSchema)
    def put(self, item_data, item_id):
        service = AreaCoordinateService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AreaCoordinateSchema(many=True))
    def get(self):
        service = AreaCoordinateService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(AreaCoordinateSchema)
    @blp.response(201, AreaCoordinateSchema)
    def post(self, item_data):
        service = AreaCoordinateService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
