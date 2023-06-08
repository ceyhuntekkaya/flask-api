from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.constant.identification_type import IdentificationTypeModel
from project.schemas.constant.identification_type import IdentificationTypeSchema

blp = Blueprint("IdentificationTypes", "identification_types", description="Operations on identification types")


@blp.route("/identification_type/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, IdentificationTypeSchema)
    def get(self, item_id):
        item = IdentificationTypeModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = IdentificationTypeModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Identification type deleted"}, 200

    @blp.arguments(IdentificationTypeSchema)
    @blp.response(201, IdentificationTypeSchema)
    def put(self, item_data, item_id):
        item = IdentificationTypeModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = IdentificationTypeModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/identification_type")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, IdentificationTypeSchema(many=True))
    def get(self):
        return IdentificationTypeModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(IdentificationTypeSchema)
    @blp.response(201, IdentificationTypeSchema)
    def post(self, item_data):
        item = IdentificationTypeModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A identification type with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the identification type.")

        return item
