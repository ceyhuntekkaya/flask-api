from marshmallow import Schema, fields


class PlainAnomalyProcessSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    process_at = fields.Int()
    process = fields.Str()
    created_at = fields.Int()


class AnomalyProcessSchema(PlainAnomalyProcessSchema):
    updated_at = fields.Int()
    deleted_at = fields.Int()
    status = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AnomalyProcessUpdateSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    process_at = fields.Int()
    process = fields.Str()
    updated_by = fields.Int()


class AnomalyProcessDeleteSchema(PlainAnomalyProcessSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class AnomalyProcessCreateSchema(PlainAnomalyProcessSchema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    process_at = fields.Int()
    process = fields.Str()
