from flask.views import MethodView
from flask_smorest import Blueprint, abort
from project.service.constant.authority_pack import AuthorityPackService
from flask_jwt_extended import jwt_required
from project.exception.entity_not_found import EntityNotFoundException
from project.exception.unexpected_entity import UnexpectedEntityException
from setting.db import db
from project.schemas.constant.authority_pack import AuthorityPackSchema

blp = Blueprint("AuthorityPacks", "authority_paks", description="Operations on authority packs")

main_route = "authority_pack"


@blp.route(f"/{main_route}/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AuthorityPackSchema)
    def get(self, item_id):
        service = AuthorityPackService(db.session)
        item = service.getById(item_id)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @jwt_required()
    def delete(self, item_id):
        service = AuthorityPackService(db.session)
        item = service.delete(item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item

    @blp.arguments(AuthorityPackSchema)
    @blp.response(201, AuthorityPackSchema)
    def put(self, item_data, item_id):
        service = AuthorityPackService(db.session)
        item = service.update(item_data, item_id, 1)
        if type(item) == EntityNotFoundException:
            abort(409, message="Error: {}".format(item))
        return item


@blp.route(f"/{main_route}")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AuthorityPackSchema(many=True))
    def get(self):
        service = AuthorityPackService(db.session)
        return service.getAll()

    @jwt_required(fresh=True)
    @blp.arguments(AuthorityPackSchema)
    @blp.response(201, AuthorityPackSchema)
    def post(self, item_data):
        service = AuthorityPackService(db.session)
        item = service.add(item_data, 1)
        if type(item) == UnexpectedEntityException:
            abort(409, message="Error: {}".format(item))
        return item
