from marshmallow import Schema, fields


class PlainMarkerSchema(Schema):
    id = fields.Int(dump_only=True)


class MarkerSchema(PlainMarkerSchema):
    store_id = fields.Int(required=True, load_only=True)


class MarkerUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class MarkerDeleteSchema(PlainMarkerSchema):
    id = fields.Int(dump_only=True)


class MarkerCreateSchema(PlainMarkerSchema):
    id = fields.Int(dump_only=True)