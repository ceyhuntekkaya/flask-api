from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.constant.command import CommandModel
from project.schemas.constant.command import CommandSchema

blp = Blueprint("Command", "commands", description="Operations on command")


@blp.route("/command/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, CommandSchema)
    def get(self, item_id):
        item = CommandModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = CommandModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "command deleted"}, 200

    @blp.arguments(CommandSchema)
    @blp.response(201, CommandSchema)
    def put(self, item_data, item_id):
        item = CommandModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = CommandModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/command")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, CommandSchema(many=True))
    def get(self):
        return CommandModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(CommandSchema)
    @blp.response(201, CommandSchema)
    def post(self, item_data):
        item = CommandModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A command with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the command.")

        return item
