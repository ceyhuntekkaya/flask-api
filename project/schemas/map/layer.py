from marshmallow import Schema, fields


class PlainLayerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    color = fields.Str()
    layer_type = fields.Str()
    critical_area_type = fields.Str()
    created_at = fields.Str()


class LayerSchema(PlainLayerSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class LayerUpdateSchema(PlainLayerSchema):
    updated_by = fields.Int()
    status = fields.Int()


class LayerDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class LayerCreateSchema(PlainLayerSchema):
    created_by = fields.Int()
    status = fields.Int()
