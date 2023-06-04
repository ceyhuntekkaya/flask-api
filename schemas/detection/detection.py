from marshmallow import Schema, fields


class PlainDetectionSchema(Schema):
    id = fields.Int(dump_only=True)


class DetectionSchema(PlainDetectionSchema):
    store_id = fields.Int(required=True, load_only=True)


class DetectionUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class DetectionDeleteSchema(PlainDetectionSchema):
    id = fields.Int(dump_only=True)


class DetectionCreateSchema(PlainDetectionSchema):
    id = fields.Int(dump_only=True)