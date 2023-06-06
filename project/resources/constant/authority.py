from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.constant.authority import AuthorityModel
from project.schemas.constant.authority import AuthoritySchema

blp = Blueprint("Authorities", "authorities", description="Operations on authorities")


@blp.route("/authority/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, AuthoritySchema)
    def get(self, item_id):
        item = AuthorityModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = AuthorityModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "authority deleted"}, 200

    @blp.arguments(AuthoritySchema)
    @blp.response(201, AuthoritySchema)
    def put(self, item_data, item_id):
        item = AuthorityModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = AuthorityModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/authority")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, AuthoritySchema(many=True))
    def get(self):
        return AuthorityModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(AuthoritySchema)
    @blp.response(201, AuthoritySchema)
    def post(self, item_data):
        item = AuthorityModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A authority with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the authority.")

        return item
