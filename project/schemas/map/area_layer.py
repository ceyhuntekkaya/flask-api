from marshmallow import Schema, fields


class PlainAreaLayerSchema(Schema):
    id = fields.Int()
    area_id = fields.Str()
    layer_id = fields.Int()


class AreaLayerSchema(PlainAreaLayerSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AreaLayerUpdateSchema(PlainAreaLayerSchema):
    updated_at = fields.Str()
    updated_by = fields.Int()


class AreaLayerDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class AreaLayerCreateSchema(Schema):
    layer_id = fields.Int()

