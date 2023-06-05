from marshmallow import Schema, fields


class PlainLayerCoordinateSchema(Schema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    layer_id = fields.Int()
    create_at = fields.Int()

class LayerCoordinateSchema(PlainLayerCoordinateSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    active = fields.Boolean()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()

class LayerCoordinateUpdateSchema(Schema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    layer_id = fields.Int()
    update_by = fields.Int()

class LayerCoordinateDeleteSchema(PlainLayerCoordinateSchema):
    id = fields.Int()
    delete_at = fields.Int()

class LayerCoordinateCreateSchema(PlainLayerCoordinateSchema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    layer_id = fields.Int()
    create_by = fields.Int()