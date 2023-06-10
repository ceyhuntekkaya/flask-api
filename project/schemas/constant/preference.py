from marshmallow import Schema, fields


class PlainPreferenceSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class PreferenceSchema(PlainPreferenceSchema):
    created_at = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()

    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class PreferenceUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    updated_by = fields.Int()


class PreferenceDeleteSchema(PlainPreferenceSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class PreferenceCreateSchema(PlainPreferenceSchema):
    id = fields.Int()
    name = fields.Str()