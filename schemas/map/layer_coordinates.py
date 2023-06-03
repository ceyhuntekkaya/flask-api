from marshmallow import Schema, fields


class PlainLayerCoordinatesSchema(Schema):
    id = fields.Int(dump_only=True)


class LayerCoordinatesSchema(PlainLayerCoordinatesSchema):
    store_id = fields.Int(required=True, load_only=True)


class LayerCoordinatesUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class LayerCoordinatesDeleteSchema(PlainLayerCoordinatesSchema):
    id = fields.Int(dump_only=True)


class LayerCoordinatesCreateSchema(PlainLayerCoordinatesSchema):
    id = fields.Int(dump_only=True)