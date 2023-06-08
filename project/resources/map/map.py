from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.map.map import MapService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.map import MapSchema

blp = Blueprint("Maps", "maps", description="Operations on map")

main_route = "map"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, MapSchema)
    def get(self, item_id):
        service = MapService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = MapService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(MapSchema)
    @blp.response(201, MapSchema)
    def put(self, item_data, item_id):
        service = MapService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, MapSchema(many=True))
    def get(self):
        service = MapService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(MapSchema)
    @blp.response(201, MapSchema)
    def post(self, item_data):
        service = MapService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
