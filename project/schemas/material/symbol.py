from marshmallow import Schema, fields


class PlainSymbolSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_at = fields.Int()


class SymbolSchema(PlainSymbolSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Bool()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class SymbolUpdateSchema(Schema):
    update_by = fields.Int()
    is_active = fields.Bool()


class SymbolDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class SymbolCreateSchema(PlainSymbolSchema):
    create_by = fields.Int()
    is_active = fields.Bool()
