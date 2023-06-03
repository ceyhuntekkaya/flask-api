from marshmallow import Schema, fields


class PlainScreenshotSchema(Schema):
    id = fields.Int(dump_only=True)


class ScreenshotSchema(PlainScreenshotSchema):
    store_id = fields.Int(required=True, load_only=True)


class ScreenshotUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class ScreenshotDeleteSchema(PlainScreenshotSchema):
    id = fields.Int(dump_only=True)


class ScreenshotCreateSchema(PlainScreenshotSchema):
    id = fields.Int(dump_only=True)