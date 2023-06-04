from marshmallow import Schema, fields


class PlainNotificationSchema(Schema):
    id = fields.Int(dump_only=True)


class NotificationSchema(PlainNotificationSchema):
    store_id = fields.Int(required=True, load_only=True)


class NotificationUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class NotificationDeleteSchema(PlainNotificationSchema):
    id = fields.Int(dump_only=True)


class NotificationCreateSchema(PlainNotificationSchema):
    id = fields.Int(dump_only=True)