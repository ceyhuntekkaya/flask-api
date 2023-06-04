from marshmallow import Schema, fields


class PlainPreferenceSchema(Schema):
    id = fields.Int(dump_only=True)


class PreferenceSchema(PlainPreferenceSchema):
    store_id = fields.Int(required=True, load_only=True)


class PreferenceUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class PreferenceDeleteSchema(PlainPreferenceSchema):
    id = fields.Int(dump_only=True)


class PreferenceCreateSchema(PlainPreferenceSchema):
    id = fields.Int(dump_only=True)