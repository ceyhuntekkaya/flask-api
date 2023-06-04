from marshmallow import Schema, fields


class PlainMessageToListSchema(Schema):
    id = fields.Int(dump_only=True)


class MessageToListSchema(PlainMessageToListSchema):
    store_id = fields.Int(required=True, load_only=True)


class MessageToListUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class MessageToListDeleteSchema(PlainMessageToListSchema):
    id = fields.Int(dump_only=True)


class MessageToListCreateSchema(PlainMessageToListSchema):
    id = fields.Int(dump_only=True)