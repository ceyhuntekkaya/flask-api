from marshmallow import Schema, fields


class PlainMediaSchema(Schema):
    id = fields.Int(dump_only=True)


class MediaSchema(PlainMediaSchema):
    store_id = fields.Int(required=True, load_only=True)


class MediaUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class MediaDeleteSchema(PlainMediaSchema):
    id = fields.Int(dump_only=True)


class MediaCreateSchema(PlainMediaSchema):
    id = fields.Int(dump_only=True)