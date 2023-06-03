from marshmallow import Schema, fields


class PlainLayerCoordinateSchema(Schema):
    id = fields.Int(dump_only=True)


class LayerCoordinateSchema(PlainLayerCoordinateSchema):
    store_id = fields.Int(required=True, load_only=True)


class LayerCoordinateUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class LayerCoordinateDeleteSchema(PlainLayerCoordinateSchema):
    id = fields.Int(dump_only=True)


class LayerCoordinateCreateSchema(PlainLayerCoordinateSchema):
    id = fields.Int(dump_only=True)