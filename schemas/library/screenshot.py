from marshmallow import Schema, fields


class PlainScreenShotSchema(Schema):
    id = fields.Int(dump_only=True)


class ScreenShotSchema(PlainScreenShotSchema):
    store_id = fields.Int(required=True, load_only=True)


class ScreenShotUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ScreenShotDeleteSchema(PlainScreenShotSchema):
    id = fields.Int(dump_only=True)


class ScreenShotCreateSchema(PlainScreenShotSchema):
    id = fields.Int(dump_only=True)