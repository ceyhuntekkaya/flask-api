from marshmallow import Schema, fields


class PlainLogSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    event_type = fields.Str()
    event_at = fields.Str()
    user_ip = fields.Str()
    unity_id = fields.Int()


class LogSchema(PlainLogSchema):
    description = fields.Str()


class LogUpdateSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    event_type = fields.Str()
    event_at = fields.Str()
    user_ip = fields.Str()
    unity_id = fields.Int()
    description = fields.Str()


class LogDeleteSchema(PlainLogSchema):
    id = fields.Int()


class LogCreateSchema(PlainLogSchema):
    id = fields.Int()
    user_id = fields.Int()
    event_type = fields.Str()
    event_at = fields.Str()
    user_ip = fields.Str()
    unity_id = fields.Int()
    description = fields.Str()
