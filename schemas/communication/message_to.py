from marshmallow import Schema, fields


class PlainMessageToListSchema(Schema):
    id = fields.Int()
    messege_id = fields.Int()
    read_at = fields.Int()


class MessageToListSchema(PlainMessageToListSchema):
    read_ip = fields.Str()


class MessageToListUpdateSchema(Schema):
    id = fields.Int()
    messege_id = fields.Int()
    read_at = fields.Int()
    read_ip = fields.Str()

class MessageToListDeleteSchema(PlainMessageToListSchema):
    id = fields.Int()


class MessageToListCreateSchema(PlainMessageToListSchema):
    id = fields.Int()
    messege_id = fields.Int()
    read_at = fields.Int()
    read_ip = fields.Str()
