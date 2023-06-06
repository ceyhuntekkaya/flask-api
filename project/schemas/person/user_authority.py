from marshmallow import Schema, fields


class PlainUserAuthoritySchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    authority_type = fields.Str()
    authority_id = fields.Int()


class UserAuthoritySchema(PlainUserAuthoritySchema):
    create_at = fields.Int(required=False)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    is_active = fields.Bool(required=True)
    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class UserAuthorityUpdateSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int()
    authority_type = fields.Str()
    authority_id = fields.Int()
    update_by = fields.Int(required=True)


class UserAuthorityDeleteSchema(PlainUserAuthoritySchema):
    id = fields.Int(required=True)
    delete_by = fields.Int(required=True)


class UserAuthorityCreateSchema(PlainUserAuthoritySchema):
    id = fields.Int(required=True)
    user_id = fields.Int()
    authority_type = fields.Str()
    authority_id = fields.Int()
    create_by = fields.Int(required=True)
