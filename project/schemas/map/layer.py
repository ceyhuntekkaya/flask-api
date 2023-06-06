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
    create_at = fields.Int()


class LayerSchema(PlainLayerSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Boolean()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class LayerUpdateSchema(PlainLayerSchema):
    update_by = fields.Int()
    is_active = fields.Boolean()


class LayerDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class LayerCreateSchema(PlainLayerSchema):
    create_by = fields.Int()
    is_active = fields.Boolean()
