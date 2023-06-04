from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required 

from db import db
from models.material.sign import SingModel
from schemas.material.sign import SignSchema


blp = Blueprint("Signs", "signs", description="Operations on signs")


@blp.route("/sign/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, SignSchema)
    def get(self, item_id):
        item = SingModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = SingModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Sign deleted"}, 200

     
    @blp.arguments(SignSchema)
    @blp.response(201, SignSchema)
    def put(self, item_data, item_id):
        item = SingModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = SingModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/sign")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, SignSchema(many=True))
    def get(self):
        return SingModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(SignSchema)
    @blp.response(201, SignSchema)
    def post(self, item_data):
        item = SingModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A sign with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the sign.")

        return item
    
