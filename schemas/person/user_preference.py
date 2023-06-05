from marshmallow import Schema, fields


class PlainUserPreferenceSchema(Schema):
    id = fields.Int()
    preference_id = fields.Int()
    value = fields.Str()


class UserPreferenceSchema(PlainUserPreferenceSchema):
    create_at = fields.Int(required=False)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    active = fields.Bool(required=True)
    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class UserPreferenceUpdateSchema(Schema):
    id = fields.Int(required=True)
    preference_id = fields.Int()
    value = fields.Str()
    update_by = fields.Int(required=True)


class UserPreferenceDeleteSchema(PlainUserPreferenceSchema):
    id = fields.Int(required=True)
    delete_by = fields.Int(required=True)


class UserPreferenceCreateSchema(PlainUserPreferenceSchema):
    id = fields.Int(required=True)
    preference_id = fields.Int()
    value = fields.Str()
    create_by = fields.Int(required=True)