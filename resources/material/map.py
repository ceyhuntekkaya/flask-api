from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required 

from db import db
from models.map_item.map import MapModel
from schemas.map_item.map import MapSchema


blp = Blueprint("Maps", "maps", description="Operations on map")


@blp.route("/map/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, MapSchema)
    def get(self, item_id):
        item = MapModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = MapModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Map deleted"}, 200

     
    @blp.arguments(MapSchema)
    @blp.response(201, MapSchema)
    def put(self, item_data, item_id):
        item = MapModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = MapModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/map")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, MapSchema(many=True))
    def get(self):
        return MapModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(MapSchema)
    @blp.response(201, MapSchema)
    def post(self, item_data):
        item = MapModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A map with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the map.")

        return item
    
