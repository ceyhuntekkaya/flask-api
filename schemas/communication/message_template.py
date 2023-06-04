from marshmallow import Schema, fields


class PlainMessageTemplateSchema(Schema):
    id = fields.Int(dump_only=True)


class MessageTemplateSchema(Schema):
    store_id = fields.Int(required=True, load_only=True)


class MessageTemplateUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class MessageTemplateeleteSchema(Schema):
    id = fields.Int(dump_only=True)


class MessageTemplateCreateSchema(Schema):
    id = fields.Int(dump_only=True)