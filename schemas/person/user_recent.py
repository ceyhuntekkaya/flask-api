from marshmallow import Schema, fields


class PlainUserRecentSchema(Schema):
    id = fields.Int(dump_only=True)


class UserRecentSchema(PlainUserRecentSchema):
    store_id = fields.Int(required=True, load_only=True)


class UserRecentUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class UserRecentDeleteSchema(PlainUserRecentSchema):
    id = fields.Int(dump_only=True)


class UserRecentCreateSchema(PlainUserRecentSchema):
    id = fields.Int(dump_only=True)