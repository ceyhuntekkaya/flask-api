from marshmallow import Schema, fields


class PlainAnomalyProcessSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    process_at = fields.Int()
    process = fields.Str()
    create_at = fields.Int()


class AnomalyProcessSchema(PlainAnomalyProcessSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Bool()
    update_by = fields.Int()
    delete_by = fields.Int()


class AnomalyProcessUpdateSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    process_at = fields.Int()
    process = fields.Str()
    update_by = fields.Int()


class AnomalyProcessDeleteSchema(PlainAnomalyProcessSchema):
    id = fields.Int()
    delete_by = fields.Int()


class AnomalyProcessCreateSchema(PlainAnomalyProcessSchema):
    id = fields.Int()
    anomaly_id = fields.Int()
    user_id = fields.Int()
    process_at = fields.Int()
    process = fields.Str()
