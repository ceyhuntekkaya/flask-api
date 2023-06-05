from marshmallow import Schema, fields


class PlainPreferenceSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class PreferenceSchema(PlainPreferenceSchema):
    create_at = fields.Int()
    update_at = fields.Int()
    delete_at = fields.Int()
    active = fields.Int()

    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class PreferenceUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    update_by = fields.Int()


class PreferenceDeleteSchema(PlainPreferenceSchema):
    id = fields.Int()
    delete_by = fields.Int()


class PreferenceCreateSchema(PlainPreferenceSchema):
    id = fields.Int()
    name = fields.Str()