from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required 

from db import db
from models.log.log import LogModel
from schemas.log.log import LogSchema


blp = Blueprint("Logs", "logs", description="Operations on log")


@blp.route("/log/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, LogSchema)
    def get(self, item_id):
        item = LogModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = LogModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Log deleted"}, 200

     
    @blp.arguments(LogSchema)
    @blp.response(201, LogSchema)
    def put(self, item_data, item_id):
        item = LogModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = LogModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/log")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, LogSchema(many=True))
    def get(self):
        return LogModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(LogSchema)
    @blp.response(201, LogSchema)
    def post(self, item_data):
        item = LogModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A log with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the log.")

        return item
    
