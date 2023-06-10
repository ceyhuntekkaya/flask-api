from marshmallow import Schema, fields


class PlainAuthorityPackSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    authority_id = fields.Int()
    role_id = fields.Int()


class AuthorityPackSchema(PlainAuthorityPackSchema):
    store_id = fields.Int(required=True, load_only=True)


class AuthorityPackUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    authority_id = fields.Int()
    role_id = fields.Int()
    updated_at = fields.Str()


class AuthorityPackDeleteSchema(PlainAuthorityPackSchema):
    id = fields.Int()
    deleted_at = fields.Str()


class AuthorityPackCreateSchema(PlainAuthorityPackSchema):
    id = fields.Int()
    name = fields.Str()
    authority_id = fields.Int()
    role_id = fields.Int()