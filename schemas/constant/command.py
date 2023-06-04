from marshmallow import Schema, fields


class PlainCommandSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    active = fields.Bool(required=False, default=True)


class CommandSchema(PlainCommandSchema):
    create_at = fields.Int(required=True)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class CommandUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class CommandDeleteSchema(PlainCommandSchema):
    id = fields.Int(dump_only=True)


class CommandCreateSchema(PlainCommandSchema):
    id = fields.Int(dump_only=True)