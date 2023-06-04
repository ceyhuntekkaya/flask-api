from marshmallow import Schema, fields


class PlainDetectionProcessSchema(Schema):
    id = fields.Int(dump_only=True)


class DetectionProcessSchema(PlainDetectionProcessSchema):
    store_id = fields.Int(required=True, load_only=True)


class DetectionProcessUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class DetectionProcessDeleteSchema(PlainDetectionProcessSchema):
    id = fields.Int(dump_only=True)


class DetectionProcessCreateSchema(PlainDetectionProcessSchema):
    id = fields.Int(dump_only=True)