from marshmallow import Schema, fields


class PlainCommandSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()


class CommandSchema(PlainCommandSchema):
    create_at = fields.Int()
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Bool()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class CommandUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()
    is_active = fields.Bool()
    update_by = fields.Int()


class CommandDeleteSchema(PlainCommandSchema):
    id = fields.Int()
    delete_by = fields.Int()


class CommandCreateSchema(PlainCommandSchema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()