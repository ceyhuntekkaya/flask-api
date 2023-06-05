from marshmallow import Schema, fields


class PlainDetectionNoteSchema(Schema):
    id =  fields.Int()
    detection_id =  fields.Int()
    user_id =  fields.Int()
    note_at =  fields.Int()
    content =  fields.Str()
    create_at = fields.Int()


class DetectionNoteSechema(PlainDetectionNoteSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    active = fields.Bool()
    update_by = fields.Int()
    delete_by = fields.Int()


class DetectionNoteUpdateSchema(Schema):
    id =  fields.Int()
    detection_id =  fields.Int()
    user_id =  fields.Int()
    note_at =  fields.Int()
    content =  fields.Str()
    update_by = fields.Int()

class DetectionNoteDeleteSchema(PlainDetectionNoteSchema):
    id =  fields.Int()
    delete_by = fields.Int()


class DetectionNoteCreateSchema(PlainDetectionNoteSchema):
    id =  fields.Int()
    detection_id =  fields.Int()
    user_id =  fields.Int()
    note_at =  fields.Int()
    content =  fields.Str()