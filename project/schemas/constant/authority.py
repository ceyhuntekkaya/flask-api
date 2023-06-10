from marshmallow import Schema, fields


class PlainAuthoritySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    created_by = fields.Int()


class AuthoritySchema(PlainAuthoritySchema):
    created_at = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AuthorityUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    updated_by = fields.Int()


class AuthorityDeleteSchema(PlainAuthoritySchema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    deleted_by = fields.Int()


class AuthorityCreateSchema(PlainAuthoritySchema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
