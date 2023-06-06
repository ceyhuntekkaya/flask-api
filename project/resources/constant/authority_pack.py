from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.constant.authority_pack import AuthorityPackModel
from project.schemas.constant.authority_pack import AuthorityPackSchema

blp = Blueprint("AuthorityPacks", "authority_paks", description="Operations on authority packs")


@blp.route("/authority_pack/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AuthorityPackSchema)
    def get(self, item_id):
        item = AuthorityPackModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = AuthorityPackModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "authority pack deleted"}, 200

    @blp.arguments(AuthorityPackSchema)
    @blp.response(201, AuthorityPackSchema)
    def put(self, item_data, item_id):
        item = AuthorityPackModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = AuthorityPackModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/authority_pack")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AuthorityPackSchema(many=True))
    def get(self):
        return AuthorityPackModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(AuthorityPackSchema)
    @blp.response(201, AuthorityPackSchema)
    def post(self, item_data):
        item = AuthorityPackModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A authority pack with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the authority pack.")

        return item
