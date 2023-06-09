from marshmallow import Schema, fields


class PlainMessageSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    priority = fields.Int()
    message_type = fields.Str()
    header = fields.Str()
    content = fields.Str()
    message_from = fields.Int()
    original_message_id = fields.Int()
    created_by = fields.Int()


class MessageSchema(PlainMessageSchema):
    send_ip = fields.Str()
    created_at = fields.Int()
    deleted_at = fields.Int()
    

class MessageUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    priority = fields.Int()
    message_type = fields.Str()
    header = fields.Str()
    content = fields.Str()
    message_from = fields.Int()
    original_message_id = fields.Int()


class MessageDeleteSchema(PlainMessageSchema):
    id = fields.Int()
    deleted_at = fields.Int()


class MessageCreateSchema(PlainMessageSchema):
    id = fields.Int()
    name = fields.Str()
    priority = fields.Int()
    message_type = fields.Str()
    header = fields.Str()
    content = fields.Str()
    message_from = fields.Int()
    original_message_id = fields.Int()
    created_by = fields.Int()
    send_ip = fields.Str()