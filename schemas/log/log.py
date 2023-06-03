from marshmallow import Schema, fields


class PlainLogSchema(Schema):
    id = fields.Int(dump_only=True)


class LogSchema(PlainLogSchema):
    store_id = fields.Int(required=True, load_only=True)


class LogUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class LogDeleteSchema(PlainLogSchema):
    id = fields.Int(dump_only=True)


class LogCreateSchema(PlainLogSchema):
    id = fields.Int(dump_only=True)