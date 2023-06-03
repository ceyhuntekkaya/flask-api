from marshmallow import Schema, fields


class PlainUserPreferenceSchema(Schema):
    id = fields.Int(dump_only=True)


class UserPreferenceSchema(PlainUserPreferenceSchema):
    store_id = fields.Int(required=True, load_only=True)


class UserPreferenceUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class UserPreferenceDeleteSchema(PlainUserPreferenceSchema):
    id = fields.Int(dump_only=True)


class UserPreferenceCreateSchema(PlainUserPreferenceSchema):
    id = fields.Int(dump_only=True)