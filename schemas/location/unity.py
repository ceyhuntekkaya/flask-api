from marshmallow import Schema, fields


class PlainUnitySchema(Schema):
    id = fields.Int(dump_only=True)


class UnitySchema(PlainUnitySchema):
    store_id = fields.Int(required=True, load_only=True)


class UnityUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class UnityDeleteSchema(PlainUnitySchema):
    id = fields.Int(dump_only=True)


class UnityCreateSchema(PlainUnitySchema):
    id = fields.Int(dump_only=True)