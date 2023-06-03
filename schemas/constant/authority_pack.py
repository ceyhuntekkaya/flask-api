from marshmallow import Schema, fields


class PlainAuthorityPackSchema(Schema):
    id = fields.Int(dump_only=True)


class AuthorityPackSchema(PlainAuthorityPackSchema):
    store_id = fields.Int(required=True, load_only=True)


class AuthorityPackUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class AuthorityPackDeleteSchema(PlainAuthorityPackSchema):
    id = fields.Int(dump_only=True)


class AuthorityPackCreateSchema(PlainAuthorityPackSchema):
    id = fields.Int(dump_only=True)