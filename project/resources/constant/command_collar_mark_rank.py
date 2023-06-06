from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.constant.command_collar_mark_rank import CommandCollarMarkRankModel
from project.schemas.constant.command_collar_mark_rank import CommandCollarMarkRankSchema

blp = Blueprint("CommandCollarMarkRanks", "command_collar_mark_ranks",
                description="Operations on command collar mark rank")


@blp.route("/command_collar_mark_rank/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @jwt_required()
    @blp.response(200, CommandCollarMarkRankSchema)
    def get(self, item_id):
        item = CommandCollarMarkRankModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = CommandCollarMarkRankModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "command collar mark rank deleted"}, 200

    @blp.arguments(CommandCollarMarkRankSchema)
    @blp.response(201, CommandCollarMarkRankSchema)
    def put(self, item_data, item_id):
        item = CommandCollarMarkRankModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = CommandCollarMarkRankModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/command_collar_mark_rank")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, CommandCollarMarkRankSchema(many=True))
    def get(self):
        return CommandCollarMarkRankModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(CommandCollarMarkRankSchema)
    @blp.response(201, CommandCollarMarkRankSchema)
    def post(self, item_data):
        item = CommandCollarMarkRankModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A command collar mark rank with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the command collar mark rank.")

        return item
