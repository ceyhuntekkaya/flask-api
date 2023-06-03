from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.material.symbol import SymbolModel
from schemas.material.symbol import SymbolSchema


blp = Blueprint("Symbols", "symbols", description="Operations on symbol")


@blp.route("/symbol/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, SymbolSchema)
    def get(self, item_id):
        item = SymbolModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = SymbolModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Symbol deleted"}, 200

     
    @blp.arguments(SymbolSchema)
    @blp.response(201, SymbolSchema)
    def put(self, item_data, item_id):
        item = SymbolModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = SymbolModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/symbol")
class Plain(MethodView):
    @blp.response(200, SymbolSchema(many=True))
    def get(self):
        return SymbolModel.query.all()

    @blp.arguments(SymbolSchema)
    @blp.response(201, SymbolSchema)
    def post(self, item_data):
        item = SymbolModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A symbol with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the symbol.")

        return item
    
