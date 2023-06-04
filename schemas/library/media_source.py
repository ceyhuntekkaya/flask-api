from marshmallow import Schema, fields


class PlainMediaSourceSchema(Schema):
    id = fields.Int(dump_only=True)


class MediaSourceSchema(PlainMediaSourceSchema):
    store_id = fields.Int(required=True, load_only=True)


class MediaSourceUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class MediaDSourceeleteSchema(PlainMediaSourceSchema):
    id = fields.Int(dump_only=True)


class MediaSourceCreateSchema(PlainMediaSourceSchema):
    id = fields.Int(dump_only=True)