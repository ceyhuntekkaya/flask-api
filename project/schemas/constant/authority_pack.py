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
    update_at = fields.Int()


class AuthorityPackDeleteSchema(PlainAuthorityPackSchema):
    id = fields.Int()
    delete_at = fields.Int()


class AuthorityPackCreateSchema(PlainAuthorityPackSchema):
    id = fields.Int()
    name = fields.Str()
    authority_id = fields.Int()
    role_id = fields.Int()