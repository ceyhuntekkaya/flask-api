from marshmallow import Schema, fields


class PlainLayerCoordinateSchema(Schema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    layer_id = fields.Int()
    created_at = fields.Str()


class LayerCoordinateSchema(PlainLayerCoordinateSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class LayerCoordinateUpdateSchema(Schema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    layer_id = fields.Int()
    updated_by = fields.Int()


class LayerCoordinateDeleteSchema(PlainLayerCoordinateSchema):
    id = fields.Int()
    deleted_at = fields.Str()


class LayerCoordinateCreateSchema(PlainLayerCoordinateSchema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    layer_id = fields.Int()
    created_by = fields.Int()
