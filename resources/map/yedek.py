from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required 

from db import db
from models.material.sign import MarkerModel
from schemas.material.sign import MarkerSchema


blp = Blueprint("Signs", "markers", description="Operations on marker")


@blp.route("/marker/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, MarkerSchema)
    def get(self, item_id):
        item = MarkerModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = MarkerModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Marker deleted"}, 200

     
    @blp.arguments(MarkerSchema)
    @blp.response(201, MarkerSchema)
    def put(self, item_data, item_id):
        item = MarkerModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = MarkerModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/marker")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, MarkerSchema(many=True))
    def get(self):
        return MarkerModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(MarkerSchema)
    @blp.response(201, MarkerSchema)
    def post(self, item_data):
        item = MarkerModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A marker with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the marker.")

        return item
    
