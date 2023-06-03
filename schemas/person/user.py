from marshmallow import Schema, fields


class PlainUserSchema(Schema):
    id = fields.Int(dump_only=True)


class UserSchema(PlainUserSchema):
    #id = fields.Int(required=True, load_only=True)
    name = fields.Str(required=True)
    surname = fields.Str(required=True)
    registration_number = fields.Str(required=False)
    phone = fields.Str(required=False)
    mail = fields.Str(required=False)
    code = fields.Str(required=False)
    phone_extension_line = fields.Str(required=False)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    create_at = fields.Int(required=True)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    active = fields.Bool(required=True)

    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)
    last_login = fields.Int(required=False)
    last_login_ip = fields.Int(required=False)

    role_id = fields.Int(required=True)
    hierarchy_id = fields.Int(required=True)
    command_id = fields.Int(required=True)
    command_collar_mark_id = fields.Int(required=True)
    command_collar_mark_rank_id = fields.Int(required=True)



class UserUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class UserDeleteSchema(PlainUserSchema):
    id = fields.Int(dump_only=True)


class UserCreateSchema(PlainUserSchema):
    id = fields.Int(dump_only=True)