from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ItemDeleteSchema(PlainItemSchema):
    id = fields.Int(dump_only=True)


class ItemCreateSchema(PlainItemSchema):
    id = fields.Int(dump_only=True)