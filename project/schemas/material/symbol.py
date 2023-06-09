from marshmallow import Schema, fields


class PlainSymbolSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Int()


class SymbolSchema(PlainSymbolSchema):
    updated_at = fields.Int()
    deleted_at = fields.Int()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class SymbolUpdateSchema(Schema):
    updated_by = fields.Int()
    status = fields.Int()


class SymbolDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class SymbolCreateSchema(PlainSymbolSchema):
    created_by = fields.Int()
    status = fields.Int()
