from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from flask_jwt_extended import jwt_required

from db import db
from project.models.constant.command_collar_mark import CommandCollarMarkModel
from project.schemas.constant.command_collar_mark import CommandCollarMarkSchema

blp = Blueprint("CommandCollarMark", "command_collar_marks", description="Operations on command collar mark")


@blp.route("/command_collar_mark/<string:item_id>")
class WithId(MethodView):
    @jwt_required()
    @blp.response(200, CommandCollarMarkSchema)
    def get(self, item_id):
        item = CommandCollarMarkModel.query.get_or_404(item_id)
        return item

    @jwt_required()
    def delete(self, item_id):
        item = CommandCollarMarkModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "command collar mark deleted"}, 200

    @blp.arguments(CommandCollarMarkSchema)
    @blp.response(201, CommandCollarMarkSchema)
    def put(self, item_data, item_id):
        item = CommandCollarMarkModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = CommandCollarMarkModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item


@blp.route("/command_collar_mark")
class Plain(MethodView):
    @jwt_required()
    @blp.response(200, CommandCollarMarkSchema(many=True))
    def get(self):
        return CommandCollarMarkModel.query.all()

    @jwt_required(fresh=True)
    @blp.arguments(CommandCollarMarkSchema)
    @blp.response(201, CommandCollarMarkSchema)
    def post(self, item_data):
        item = CommandCollarMarkModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A command collar mark with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the command collar mark.")

        return item
