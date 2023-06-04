from marshmallow import Schema, fields


class PlainSignSchema(Schema):
    id = fields.Int(dump_only=True)


class SignSchema(PlainSignSchema):
    store_id = fields.Int(required=True, load_only=True)


class SignUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class SignDeleteSchema(PlainSignSchema):
    id = fields.Int(dump_only=True)


class SignCreateSchema(PlainSignSchema):
    id = fields.Int(dump_only=True)