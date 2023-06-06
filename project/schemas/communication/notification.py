from marshmallow import Schema, fields


class PlainNotificationSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    priority = fields.Int()
    message_type = fields.Str()
    header = fields.Str()
    content = fields.Str()
    notification_from = fields.Int()
    create_by = fields.Int()
    notification_type = fields.Str()


class NotificationSchema(PlainNotificationSchema):
    send_ip = fields.Str()
    create_at = fields.Int()
    delete_at = fields.Int()


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
    delete_at = fields.Int()


class NotificationCreateSchema(PlainNotificationSchema):
    id = fields.Int()
    name = fields.Str()
    priority = fields.Int()
    message_type = fields.Str()
    header = fields.Str()
    content = fields.Str()
    notification_from = fields.Int()
    create_by = fields.Int()
    send_ip = fields.Str()
    notification_type = fields.Str()
