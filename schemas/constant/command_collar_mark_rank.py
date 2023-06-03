from marshmallow import Schema, fields


class PlainCommandCollarMarkRankSchema(Schema):
    id = fields.Int(dump_only=True)


class CommandCollarMarkRankSchema(PlainCommandCollarMarkRankSchema):
    store_id = fields.Int(required=True, load_only=True)


class CommandCollarMarkRankUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class CommandCollarMarkRankDeleteSchema(PlainCommandCollarMarkRankSchema):
    id = fields.Int(dump_only=True)


class CommandCollarMarkRankCreateSchema(PlainCommandCollarMarkRankSchema):
    id = fields.Int(dump_only=True)