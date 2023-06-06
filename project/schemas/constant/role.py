from marshmallow import Schema, fields


class PlainRoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    is_active = fields.Bool(required=False, default=True)
    create_at = fields.Int(required=True)
    create_by = fields.Int(required=False)


class RoleSchema(PlainRoleSchema):
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class RoleUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    is_active = fields.Bool(required=False, default=True)
    update_by = fields.Int()


class RoleDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class RoleCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    is_active = fields.Bool(required=False, default=True)
    create_at = fields.Int(required=True)
    create_by = fields.Int(required=False)
