from marshmallow import Schema, fields


class PlainRoleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    created_at = fields.Int(required=True)
    created_by = fields.Int(required=False)


class RoleSchema(PlainRoleSchema):
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class RoleUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    updated_by = fields.Int()


class RoleDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class RoleCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    created_at = fields.Int(required=True)
    created_by = fields.Int(required=False)
