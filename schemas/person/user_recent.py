from marshmallow import Schema, fields


class PlainUserRecentSchema(Schema):
    id = fields.Int()
    type = fields.Str()
    value = fields.Str()


class UserRecentSchema(PlainUserRecentSchema):
    create_at = fields.Int(required=False)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    active = fields.Bool(required=True)
    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class UserRecentUpdateSchema(Schema):
    id = fields.Int(required=True)
    type = fields.Str()
    value = fields.Str()
    update_by = fields.Int(required=True)


class UserRecentDeleteSchema(PlainUserRecentSchema):
    id = fields.Int(required=True)
    delete_by = fields.Int(required=True)


class UserRecentCreateSchema(PlainUserRecentSchema):
    id = fields.Int(required=True)
    type = fields.Str()
    value = fields.Str()
    create_by = fields.Int(required=True)