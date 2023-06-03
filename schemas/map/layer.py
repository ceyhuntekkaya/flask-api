from marshmallow import Schema, fields


class PlainLayerSchema(Schema):
    id = fields.Int(dump_only=True)


class LayerSchema(PlainLayerSchema):
    store_id = fields.Int(required=True, load_only=True)


class LayerUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class LayerDeleteSchema(PlainLayerSchema):
    id = fields.Int(dump_only=True)


class LayerCreateSchema(PlainLayerSchema):
    id = fields.Int(dump_only=True)