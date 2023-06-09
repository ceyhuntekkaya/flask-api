from marshmallow import Schema, fields


class PlainMapSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Int()


class MapSchema(PlainMapSchema):
    updated_at = fields.Int()
    deleted_at = fields.Int()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class MapUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    updated_by = fields.Int()


class MapDeleteSchema(PlainMapSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class MapCreateSchema(PlainMapSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_by = fields.Int()
