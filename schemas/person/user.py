from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)


class UserSchema(PlainUserSchema):
    store_id = fields.Int(required=True, load_only=True)


class UserUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class UserDeleteSchema(PlainUserSchema):
    id = fields.Int(dump_only=True)


class UserCreateSchema(PlainUserSchema):
    id = fields.Int(dump_only=True)