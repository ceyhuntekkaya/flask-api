from marshmallow import Schema, fields


class PlainNotificationToListSchema(Schema):
    id = fields.Int(dump_only=True)


class NotificationToListSchema(PlainNotificationToListSchema):
    store_id = fields.Int(required=True, load_only=True)


class NotificationToListUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class NotificationToListDeleteSchema(PlainNotificationToListSchema):
    id = fields.Int(dump_only=True)


class NotificationToListCreateSchema(PlainNotificationToListSchema):
    id = fields.Int(dump_only=True)