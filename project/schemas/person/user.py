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
    password = fields.Str(required=True)


class UserSchema(PlainUserSchema):
    registration_number = fields.Str(required=False)
    phone = fields.Str(required=False)
    mail = fields.Str(required=False)
    code = fields.Str(required=False)
    phone_extension_line = fields.Str(required=False)

    create_at = fields.Int(required=False)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    is_active = fields.Bool(required=True)

    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)
    last_login = fields.Int(required=False)
    last_login_ip = fields.Int(required=False)


class UserLoginSchema(Schema):
    id = fields.Int(dump_only=False)
    name = fields.Str(required=False)
    surname = fields.Str(required=False)
    role_id = fields.Int(required=False)
    hierarchy_id = fields.Int(required=False)
    command_id = fields.Int(required=False)
    command_collar_mark_id = fields.Int(required=False)
    command_collar_mark_rank_id = fields.Int(required=False)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    egistration_number = fields.Str(required=False)
    phone = fields.Str(required=False)
    mail = fields.Str(required=False)
    code = fields.Str(required=False)
    phone_extension_line = fields.Str(required=False)

    create_at = fields.Int(required=False)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    is_active = fields.Bool(required=False)

    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)
    last_login = fields.Int(required=False)
    last_login_ip = fields.Int(required=False)


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
