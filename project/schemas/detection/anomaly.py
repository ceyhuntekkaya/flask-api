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
    create_at = fields.Int()


class AnomalySchema(PlainAnomalySchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Bool()
    update_by = fields.Int()
    delete_by = fields.Int()


class AnomalyUpdateSchema(PlainAnomalySchema):
    update_by = fields.Int()


class AnomalyDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class AnomalyCreateSchema(PlainAnomalySchema):
    create_at = fields.Int()
