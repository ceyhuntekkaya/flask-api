from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.map.layer import LayerModel
from schemas.map.layer import LayerSchema


blp = Blueprint("Layers", "layers", description="Operations on layer")


@blp.route("/layer/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, LayerSchema)
    def get(self, item_id):
        item = LayerModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = LayerModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Layer deleted"}, 200

     
    @blp.arguments(LayerSchema)
    @blp.response(201, LayerSchema)
    def put(self, item_data, item_id):
        item = LayerModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = LayerModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/layer")
class Plain(MethodView):
    @blp.response(200, LayerSchema(many=True))
    def get(self):
        return LayerModel.query.all()

    @blp.arguments(LayerSchema)
    @blp.response(201, LayerSchema)
    def post(self, item_data):
        item = LayerModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A layer with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the layer.")

        return item
    
