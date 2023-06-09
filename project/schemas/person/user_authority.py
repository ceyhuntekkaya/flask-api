from marshmallow import Schema, fields


class PlainUserAuthoritySchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    authority_type = fields.Str()
    authority_id = fields.Int()


class UserAuthoritySchema(PlainUserAuthoritySchema):
    created_at = fields.Int(required=False)
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    status = fields.Int(required=True)
    created_by = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class UserAuthorityUpdateSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int()
    authority_type = fields.Str()
    authority_id = fields.Int()
    updated_by = fields.Int(required=True)


class UserAuthorityDeleteSchema(PlainUserAuthoritySchema):
    id = fields.Int(required=True)
    deleted_by = fields.Int(required=True)


class UserAuthorityCreateSchema(PlainUserAuthoritySchema):
    id = fields.Int(required=True)
    user_id = fields.Int()
    authority_type = fields.Str()
    authority_id = fields.Int()
    created_by = fields.Int(required=True)
