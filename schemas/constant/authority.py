from marshmallow import Schema, fields


class PlainAuthoritySchema(Schema):
    id = fields.Int(dump_only=True)


class AuthoritySchema(PlainAuthoritySchema):
    store_id = fields.Int(required=True, load_only=True)


class AuthorityUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class AuthorityDeleteSchema(PlainAuthoritySchema):
    id = fields.Int(dump_only=True)


class AuthorityCreateSchema(PlainAuthoritySchema):
    id = fields.Int(dump_only=True)