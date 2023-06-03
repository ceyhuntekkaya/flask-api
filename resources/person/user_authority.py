from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.person.user_authority import UserAuthorityModel
from schemas.person.user_authority import UserAuthoritySchema


blp = Blueprint("UserAuthorities", "user_authorities", description="Operations on user authority")


@blp.route("/user_authority/<string:item_id>")
class WithId(MethodView):
    @blp.response(200, UserAuthoritySchema)
    def get(self, item_id):
        item = UserAuthorityModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = UserAuthorityModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "User authority deleted"}, 200

     
    @blp.arguments(UserAuthoritySchema)
    @blp.response(201, UserAuthoritySchema)
    def put(self, item_data, item_id):
        item = UserAuthorityModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = UserAuthorityModel(id=item_id, **item_data)
        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/user_authority")
class Plain(MethodView):
    @blp.response(200, UserAuthoritySchema(many=True))
    def get(self):
        return UserAuthorityModel.query.all()

    @blp.arguments(UserAuthoritySchema)
    @blp.response(201, UserAuthoritySchema)
    def post(self, item_data):
        item = UserAuthorityModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A user authority with that name already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the user authority.")

        return item
    
