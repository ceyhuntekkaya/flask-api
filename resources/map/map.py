from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.map.map import MapModel
from schemas.map.map import MapSchema


blp = Blueprint("Maps", "maps", description="Operations on map")


@blp.route("/map/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, MapSchema)
    def get(self, item_id):
        item = MapModel.query.get_or_404(item_id)
        return item

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
    @blp.response(200, MapSchema(many=True))
    def get(self):
        return MapModel.query.all()

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
    
