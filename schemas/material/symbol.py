from marshmallow import Schema, fields


class PlainSymbolSchema(Schema):
    id = fields.Int(dump_only=True)


class SymbolSchema(PlainSymbolSchema):
    store_id = fields.Int(required=True, load_only=True)


class SymbolUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class SymbolDeleteSchema(PlainSymbolSchema):
    id = fields.Int(dump_only=True)


class SymbolCreateSchema(PlainSymbolSchema):
    id = fields.Int(dump_only=True)