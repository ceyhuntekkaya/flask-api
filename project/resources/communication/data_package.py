from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.communication.data_package import DataPackageModel
from project.schemas.communication.data_package import DataPackageSchema

blp = Blueprint("DataPackages", "data_packages", description="Operations on data packages")


@blp.route("/data_package/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, DataPackageSchema)
    def get(self, item_id):
        item = DataPackageModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = DataPackageModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Data Package deleted"}, 200

    @blp.arguments(DataPackageSchema)
    @blp.response(201, DataPackageSchema)
    def put(self, item_data, item_id):
        item = DataPackageModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = DataPackageModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/data_package")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, DataPackageSchema(many=True))
    def get(self):
        return DataPackageModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(DataPackageSchema)
    @blp.response(201, DataPackageSchema)
    def post(self, item_data):
        item = DataPackageModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A Data Package with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the data package.")

        return item
