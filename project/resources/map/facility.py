from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.map.facility import FacilityService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.map.facility import FacilitySchema

blp = Blueprint("Facilities", "facilities", description="Operations on facility")

main_route = "facility"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, FacilitySchema)
    def get(self, item_id):
        service = FacilityService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = FacilityService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(FacilitySchema)
    @blp.response(201, FacilitySchema)
    def put(self, item_data, item_id):
        service = FacilityService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, FacilitySchema(many=True))
    def get(self):
        service = FacilityService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(FacilitySchema)
    @blp.response(201, FacilitySchema)
    def post(self, item_data):
        service = FacilityService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
