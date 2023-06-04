from marshmallow import Schema, fields


class PlainDetectionNoteSchema(Schema):
    id = fields.Int(dump_only=True)


class DetectionNoteSechema(PlainDetectionNoteSchema):
    store_id = fields.Int(required=True, load_only=True)


class DetectionNoteUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class DetectionNoteDeleteSchema(PlainDetectionNoteSchema):
    id = fields.Int(dump_only=True)


class DetectionNoteCreateSchema(PlainDetectionNoteSchema):
    id = fields.Int(dump_only=True)