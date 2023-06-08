from marshmallow import Schema, fields


class PlainAnomalyNoteSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    note_at = fields.Int()
    content = fields.Str()
    create_at = fields.Int()


class AnomalyNoteSchema(PlainAnomalyNoteSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Bool()
    update_by = fields.Int()
    delete_by = fields.Int()


class AnomalyNoteUpdateSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    note_at = fields.Int()
    content = fields.Str()
    update_by = fields.Int()


class AnomalyNoteDeleteSchema(PlainAnomalyNoteSchema):
    id = fields.Int()
    delete_by = fields.Int()


class AnomalyNoteCreateSchema(PlainAnomalyNoteSchema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    note_at = fields.Int()
    content = fields.Str()
