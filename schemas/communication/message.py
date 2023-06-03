from marshmallow import Schema, fields


class PlainMessageSchema(Schema):
    id = fields.Int(dump_only=True)


class MessageSchema(PlainMessageSchema):
    store_id = fields.Int(required=True, load_only=True)


class MessageUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class MessageDeleteSchema(PlainMessageSchema):
    id = fields.Int(dump_only=True)


class MessageCreateSchema(PlainMessageSchema):
    id = fields.Int(dump_only=True)