from marshmallow import Schema, fields


class PlainDetectionRouteSchema(Schema):
    id = fields.Int(dump_only=True)


class DetectionRouteSchema(PlainDetectionRouteSchema):
    store_id = fields.Int(required=True, load_only=True)


class DetectionRouteUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class DetectionRouteDeleteSchema(PlainDetectionRouteSchema):
    id = fields.Int(dump_only=True)


class DetectionRouteCreateSchema(PlainDetectionRouteSchema):
    id = fields.Int(dump_only=True)