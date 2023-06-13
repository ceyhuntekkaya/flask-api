from marshmallow import Schema, fields


class PlainUnitSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class UnitSchema(PlainUnitSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class UnitUpdateSchema(PlainUnitSchema):
    status = fields.Int()
    updated_by = fields.Int()


class UnitDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class UnitCreateSchema(PlainUnitSchema):
    status = fields.Int()
    created_by = fields.Int()
