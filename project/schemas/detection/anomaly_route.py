from marshmallow import Schema, fields


class PlainAnomalyRouteSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    latitude = fields.Int()
    longitude = fields.Int()
    description = fields.Str()
    anomaly_at = fields.Int()
    anomaly_level = fields.Int()


class AnomalyRouteSchema(PlainAnomalyRouteSchema):
    create_at = fields.Int()
    delete_at = fields.Int()
    delete_by = fields.Int()


class AnomalyRouteUpdateSchema(Schema):
    id = fields.Int()
    anomaly_id = fields.Int()
    latitude = fields.Int()
    longitude = fields.Int()
    description = fields.Str()
    anomaly_at = fields.Int()
    anomaly_level = fields.Int()


class AnomalyRouteDeleteSchema(PlainAnomalyRouteSchema):
    id = fields.Int()
    delete_by = fields.Int()


class AnomalyRouteCreateSchema(PlainAnomalyRouteSchema):
    id = fields.Int()
    anomaly_id = fields.Int()
    latitude = fields.Int()
    longitude = fields.Int()
    description = fields.Str()
    anomaly_at = fields.Int()
    anomaly_level = fields.Int()
