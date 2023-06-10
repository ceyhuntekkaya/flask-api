from flask.views import MethodView
from flask_smorest import Blueprint
from marshmallow import Schema, fields

import os

blp = Blueprint("BaseRoute", "base_routes", description="Operations on data base routes")

APP_PATH = os.getenv("APP_PATH")
version = os.getenv("VERSION")


class PlainSchema(Schema):
    name = fields.Str()
    description = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    anomaly_at = fields.Int()
    anomaly_level = fields.Int()
    anomaly_color = fields.Str()
    map_id = fields.Int()
    layer_id = fields.Int()
    sensor_id = fields.Int()
    unity_id = fields.Int()
    official_user_id = fields.Int()
    status = fields.Str()
    created_at = fields.Str()


@blp.route("/")
class Base(MethodView):
    @blp.response(200, PlainSchema)
    def get(self, item_id):
        return ""


@blp.route(f"/{APP_PATH}/{version}")
class Plain(MethodView):
    @blp.response(200, PlainSchema)
    def get(self):
        return ""


@blp.route(f"/{APP_PATH}/{version}/ping")
class Ping(MethodView):
    @blp.response(200, PlainSchema)
    def get(self):
        return ""


@blp.route(f"/{APP_PATH}/{version}/manual")
class Manuel(MethodView):
    @blp.response(200, PlainSchema)
    def get(self):
        return ""
