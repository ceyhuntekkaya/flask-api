from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
import os

from db import db
from blocklist import BLOCKLIST

#from resources._user import blp as UserBlueprint
# from resources._item import blp as ItemBlueprint
# from resources._store import blp as StoreBlueprint
# from resources._tag import blp as TagBlueprint


from resources.communication.data_package import blp as DataPackageBlueprint
from resources.communication.message import blp as MessageBlueprint
from resources.communication.message_template import blp as MessageTemplateBlueprint
from resources.communication.notification import blp as NotificationBlueprint
from resources.communication.message_to import blp as MessageToListBlueprint
from resources.communication.notification_to import blp as NotificationToListBlueprint

from resources.constant.authority import blp as AuthorityBlueprint
from resources.constant.authority_pack import blp as AuthorityPackBlueprint
from resources.constant.command import blp as CommandBlueprint
from resources.constant.command_collar_mark import blp as CommandCollarMarkBlueprint
from resources.constant.command_collar_mark_rank import blp as CommandCollarMarkRankBlueprint
from resources.constant.hierarchy import blp as HierarchyBlueprint
from resources.constant.preference import blp as PreferenceBlueprint
from resources.constant.role import blp as RoleBlueprint


from resources.detection.detection import blp as DetectionPrint
from resources.detection.detection_note import blp as DetectionNotePrint
from resources.detection.detection_process import blp as DetectionProcessPrint
from resources.detection.detection_route import blp as DetectionRoutePrint

from resources.library.media import blp as MediaBlueprint
from resources.library.media_source import blp as MediaSourceBlueprint
from resources.library.screenshot import blp as ScreenshotBlueprint

from resources.material.unity import blp as UnityBlueprint

from resources.log.log import blp as LogBlueprint


from resources.material.sign import blp as SingBlueprint
from resources.material.sensor import blp as SensorBlueprint
from resources.material.symbol import blp as SymbolBlueprint
from resources.map.map import blp as MapBlueprint
from resources.map.layer import blp as LayerBlueprint
from resources.map.layer_coordinates import blp as LayerCoordinatesBlueprint
from resources.map.marker import blp as MarkerBlueprint

from resources.person.user import blp as UserBlueprint
from resources.person.user_authority import blp as UserAuthorityBlueprint
from resources.person.user_preference import blp as UserPreferenceBlueprint
from resources.person.user_recent import blp as UserRecentBlueprint

from resources.report.detection_report import blp as DetectionReportBlueprint




from initialize import FirstRecords


def create_app(db_url=None):
    app = Flask(__name__)
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL") # or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "jose"
    jwt = JWTManager(app)

    # @jwt.additional_claims_loader
    # def add_claims_to_jwt(identity):
    #     # TODO: Read from a config file instead of hard-coding
    #     if identity == 1:
    #         return {"is_admin": True}
    #     return {"is_admin": False}

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )
    with app.app_context():
        db.create_all()
        FirstRecords.check()

    #api.register_blueprint(UserBlueprint)
    # api.register_blueprint(ItemBlueprint)
    # api.register_blueprint(StoreBlueprint)
    # api.register_blueprint(TagBlueprint)

    api.register_blueprint(DataPackageBlueprint)
    api.register_blueprint(MessageBlueprint)
    api.register_blueprint(MessageTemplateBlueprint)
    api.register_blueprint(NotificationBlueprint)
    api.register_blueprint(MessageToListBlueprint)
    api.register_blueprint(NotificationToListBlueprint)

    api.register_blueprint(AuthorityBlueprint)
    api.register_blueprint(AuthorityPackBlueprint)
    api.register_blueprint(CommandBlueprint)
    api.register_blueprint(CommandCollarMarkBlueprint)
    api.register_blueprint(CommandCollarMarkRankBlueprint)
    api.register_blueprint(HierarchyBlueprint)
    api.register_blueprint(PreferenceBlueprint)
    api.register_blueprint(RoleBlueprint)


    api.register_blueprint(DetectionPrint)
    api.register_blueprint(DetectionRoutePrint)
    api.register_blueprint(DetectionNotePrint)
    api.register_blueprint(DetectionProcessPrint)

    api.register_blueprint(MediaBlueprint)
    api.register_blueprint(MediaSourceBlueprint)
    api.register_blueprint(ScreenshotBlueprint)

    api.register_blueprint(UnityBlueprint)

    api.register_blueprint(LogBlueprint)

    api.register_blueprint(MapBlueprint)
    api.register_blueprint(MarkerBlueprint)
    api.register_blueprint(LayerBlueprint)
    api.register_blueprint(LayerCoordinatesBlueprint)

    api.register_blueprint(SingBlueprint)
    api.register_blueprint(SensorBlueprint)
    api.register_blueprint(SymbolBlueprint)

    api.register_blueprint(UserBlueprint)
    api.register_blueprint(UserAuthorityBlueprint)
    api.register_blueprint(UserPreferenceBlueprint)
    api.register_blueprint(UserRecentBlueprint)

    api.register_blueprint(DetectionReportBlueprint)




    return app
