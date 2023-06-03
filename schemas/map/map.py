from marshmallow import Schema, fields


class PlainMapSchema(Schema):
    id = fields.Int(dump_only=True)


class MapSchema(PlainMapSchema):
    store_id = fields.Int(required=True, load_only=True)


class MapUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class MapDeleteSchema(PlainMapSchema):
    id = fields.Int(dump_only=True)


class MapCreateSchema(PlainMapSchema):
    id = fields.Int(dump_only=True)