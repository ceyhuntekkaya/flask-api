from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    role_id = fields.Int(required=True)
    hierarchy_id = fields.Int(required=True)
    command_id = fields.Int(required=True)
    command_collar_mark_id = fields.Int(required=True)
    command_collar_mark_rank_id = fields.Int(required=True)
    username = fields.Str(required=True)


class RegisterSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    role_id = fields.Int(required=True)
    hierarchy_id = fields.Int(required=True)
    command_id = fields.Int(required=True)
    command_collar_mark_id = fields.Int(required=True)
    command_collar_mark_rank_id = fields.Int(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserSchema(PlainUserSchema):
    registration_number = fields.Str(required=False)
    phone = fields.Str(required=False)
    mail = fields.Str(required=False)
    code = fields.Str(required=False)
    phone_extension_line = fields.Str(required=False)

    created_at = fields.Int(required=False)
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    status = fields.Int(required=True)

    created_by = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)
    last_login = fields.Int(required=False)
    last_login_ip = fields.Int(required=False)


class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserUpdateSchema(PlainUserSchema):
    name = fields.Str()
    price = fields.Float()


class UserDeleteSchema(Schema):
    registration_number = fields.Str(required=False)
    phone = fields.Str(required=False)
    mail = fields.Str(required=False)
    code = fields.Str(required=False)
    phone_extension_line = fields.Str(required=False)


class UserCreateSchema(PlainUserSchema):
    id = fields.Int(dump_only=True)
