from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.constant.authority import AuthorityService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from db import db
from project.schemas.constant.authority import AuthoritySchema

blp = Blueprint("Authorities", "authorities", description="Operations on authorities")

main_route = "authority"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AuthoritySchema)
    def get(self, item_id):
        service = AuthorityService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = AuthorityService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(AuthoritySchema)
    @blp.response(201, AuthoritySchema)
    def put(self, item_data, item_id):
        service = AuthorityService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AuthoritySchema(many=True))
    def get(self):
        service = AuthorityService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(AuthoritySchema)
    @blp.response(201, AuthoritySchema)
    def post(self, item_data):
        service = AuthorityService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
