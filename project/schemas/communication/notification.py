from marshmallow import Schema, fields


class PlainNotificationSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    priority = fields.Int()
    message_type = fields.Str()
    header = fields.Str()
    content = fields.Str()
    notification_from = fields.Int()
    created_by = fields.Int()
    notification_type = fields.Str()


class NotificationSchema(PlainNotificationSchema):
    send_ip = fields.Str()
    created_at = fields.Int()
    deleted_at = fields.Int()


class NotificationUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    priority = fields.Int()
    message_type = fields.Str()
    header = fields.Str()
    content = fields.Str()
    notification_from = fields.Int()
    notification_type = fields.Str()


class NotificationDeleteSchema(PlainNotificationSchema):
    id = fields.Int()
    deleted_at = fields.Int()


class NotificationCreateSchema(PlainNotificationSchema):
    id = fields.Int()
    name = fields.Str()
    priority = fields.Int()
    message_type = fields.Str()
    header = fields.Str()
    content = fields.Str()
    notification_from = fields.Int()
    created_by = fields.Int()
    send_ip = fields.Str()
    notification_type = fields.Str()
