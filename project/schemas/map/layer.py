from marshmallow import Schema, fields


class PlainLayerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class LayerSchema(PlainLayerSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class LayerUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    updated_by = fields.Int()


class LayerDeleteSchema(PlainLayerSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class LayerCreateSchema(PlainLayerSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_by = fields.Int()
