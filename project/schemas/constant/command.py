from marshmallow import Schema, fields


class PlainCommandSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()


class CommandSchema(PlainCommandSchema):
    created_at = fields.Int()
    updated_at = fields.Int()
    deleted_at = fields.Int()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class CommandUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()
    status = fields.Int()
    updated_by = fields.Int()


class CommandDeleteSchema(PlainCommandSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class CommandCreateSchema(PlainCommandSchema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()
