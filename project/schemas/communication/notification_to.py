from marshmallow import Schema, fields


class PlainNotificationToListSchema(Schema):
    id = fields.Int()
    message_id = fields.Int()
    read_at = fields.Int()


class NotificationToListSchema(PlainNotificationToListSchema):
    read_ip = fields.Str()


class NotificationToListUpdateSchema(Schema):
    id = fields.Int()
    message_id = fields.Int()
    read_at = fields.Int()
    read_ip = fields.Str()


class NotificationToListDeleteSchema(PlainNotificationToListSchema):
    id = fields.Int()


class NotificationToListCreateSchema(PlainNotificationToListSchema):
    id = fields.Int()
    message_id = fields.Int()
    read_at = fields.Int()
    read_ip = fields.Str()
