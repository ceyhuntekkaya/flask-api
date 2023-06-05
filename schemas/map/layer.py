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
    active = fields.Boolean()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()

class LayerUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    color = fields.Str()
    layer_type = fields.Str()
    critical_area_type = fields.Str()
    update_by = fields.Int()

class LayerDeleteSchema(PlainLayerSchema):
    id = fields.Int()
    delete_by = fields.Int()

class LayerCreateSchema(PlainLayerSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    color = fields.Str()
    layer_type = fields.Str()
    critical_area_type = fields.Str()
    create_by = fields.Int()