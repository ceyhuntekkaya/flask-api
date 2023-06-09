from marshmallow import Schema, fields


class PlainUserRecentSchema(Schema):
    id = fields.Int()
    type = fields.Str()
    value = fields.Str()


class UserRecentSchema(PlainUserRecentSchema):
    created_at = fields.Int(required=False)
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    status = fields.Int(required=True)
    created_by = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class UserRecentUpdateSchema(Schema):
    id = fields.Int(required=True)
    type = fields.Str()
    value = fields.Str()
    updated_by = fields.Int(required=True)


class UserRecentDeleteSchema(PlainUserRecentSchema):
    id = fields.Int(required=True)
    deleted_by = fields.Int(required=True)


class UserRecentCreateSchema(PlainUserRecentSchema):
    id = fields.Int(required=True)
    type = fields.Str()
    value = fields.Str()
    created_by = fields.Int(required=True)