from marshmallow import Schema, fields


class PlainRoleSchema(Schema):
    id = fields.Int(dump_only=True)


class RoleSchema(PlainRoleSchema):
    store_id = fields.Int(required=True, load_only=True)


class RoleUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class RoleDeleteSchema(PlainRoleSchema):
    id = fields.Int(dump_only=True)


class RoleCreateSchema(PlainRoleSchema):
    id = fields.Int(dump_only=True)