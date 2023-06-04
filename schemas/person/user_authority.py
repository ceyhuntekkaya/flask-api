from marshmallow import Schema, fields


class PlainUserAuthoritySchema(Schema):
    id = fields.Int(dump_only=True)


class UserAuthoritySchema(PlainUserAuthoritySchema):
    store_id = fields.Int(required=True, load_only=True)


class UserAuthorityUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class UserAuthorityDeleteSchema(PlainUserAuthoritySchema):
    id = fields.Int(dump_only=True)


class UserAuthorityCreateSchema(PlainUserAuthoritySchema):
    id = fields.Int(dump_only=True)