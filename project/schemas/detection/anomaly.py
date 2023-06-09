from marshmallow import Schema, fields


class PlainAnomalySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    anomaly_at = fields.Int()
    anomaly_level = fields.Int()
    anomaly_color = fields.Str()
    map_id = fields.Int()
    layer_id = fields.Int()
    sensor_id = fields.Int()
    unity_id = fields.Int()
    official_user_id = fields.Int()
    status = fields.Str()
    created_at = fields.Int()


class AnomalySchema(PlainAnomalySchema):
    updated_at = fields.Int()
    deleted_at = fields.Int()
    status = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AnomalyUpdateSchema(PlainAnomalySchema):
    updated_by = fields.Int()


class AnomalyDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class AnomalyCreateSchema(PlainAnomalySchema):
    created_at = fields.Int()
