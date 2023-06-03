from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.map.layer_coordinates import LayerCoordinateModel
from schemas.map.layer_coordinates import LayerCoordinateSchema


blp = Blueprint("LayerCoordinates", "layer_coordinatess", description="Operations on layer coordinates")


@blp.route("/layer_coordinate/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, LayerCoordinateSchema)
    def get(self, item_id):
        item = LayerCoordinateModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = LayerCoordinateModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Layer coordinates deleted"}, 200

     
    @blp.arguments(LayerCoordinateSchema)
    @blp.response(201, LayerCoordinateSchema)
    def put(self, item_data, item_id):
        item = LayerCoordinateModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = LayerCoordinateModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/layer_coordinate")
class Plain(MethodView):
    @blp.response(200, LayerCoordinateSchema(many=True))
    def get(self):
        return LayerCoordinateModel.query.all()

    @blp.arguments(LayerCoordinateSchema)
    @blp.response(201, LayerCoordinateSchema)
    def post(self, item_data):
        item = LayerCoordinateModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A layer coordinates with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the layer coordinates.")

        return item
    
