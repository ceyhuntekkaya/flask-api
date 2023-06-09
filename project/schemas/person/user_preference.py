from marshmallow import Schema, fields


class PlainUserPreferenceSchema(Schema):
    id = fields.Int()
    preference_id = fields.Int()
    value = fields.Str()


class UserPreferenceSchema(PlainUserPreferenceSchema):
    created_at = fields.Int(required=False)
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    status = fields.Int(required=True)
    created_by = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class UserPreferenceUpdateSchema(Schema):
    id = fields.Int(required=True)
    preference_id = fields.Int()
    value = fields.Str()
    updated_by = fields.Int(required=True)


class UserPreferenceDeleteSchema(PlainUserPreferenceSchema):
    id = fields.Int(required=True)
    deleted_by = fields.Int(required=True)


class UserPreferenceCreateSchema(PlainUserPreferenceSchema):
    id = fields.Int(required=True)
    preference_id = fields.Int()
    value = fields.Str()
    created_by = fields.Int(required=True)