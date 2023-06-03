from marshmallow import Schema, fields


class PlainCommandSchema(Schema):
    id = fields.Int(dump_only=True)


class CommandSchema(PlainCommandSchema):
    store_id = fields.Int(required=True, load_only=True)


class CommandUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class CommandDeleteSchema(PlainCommandSchema):
    id = fields.Int(dump_only=True)


class CommandCreateSchema(PlainCommandSchema):
    id = fields.Int(dump_only=True)