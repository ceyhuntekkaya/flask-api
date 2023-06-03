from marshmallow import Schema, fields


class PlainCommandCollarMarkSchema(Schema):
    id = fields.Int(dump_only=True)


class CommandCollarMarkSchema(PlainCommandCollarMarkSchema):
    store_id = fields.Int(required=True, load_only=True)


class CommandCollarMarkUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class CommandCollarMarkDeleteSchema(PlainCommandCollarMarkSchema):
    id = fields.Int(dump_only=True)


class CommandCollarMarkCreateSchema(PlainCommandCollarMarkSchema):
    id = fields.Int(dump_only=True)