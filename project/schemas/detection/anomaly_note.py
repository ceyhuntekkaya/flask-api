from marshmallow import Schema, fields


class PlainAnomalyNoteSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    note_at = fields.Int()
    content = fields.Str()
    created_at = fields.Str()


class AnomalyNoteSchema(PlainAnomalyNoteSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AnomalyNoteUpdateSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    note_at = fields.Int()
    content = fields.Str()
    updated_by = fields.Int()


class AnomalyNoteDeleteSchema(PlainAnomalyNoteSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class AnomalyNoteCreateSchema(PlainAnomalyNoteSchema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    note_at = fields.Int()
    content = fields.Str()
