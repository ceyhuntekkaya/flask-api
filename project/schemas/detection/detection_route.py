from marshmallow import Schema, fields


class PlainDetectionRouteSchema(Schema):
    id = fields.Int()
    detection_id = fields.Int()
    latitude = fields.Int()
    longitude = fields.Int()
    description = fields.Str()
    detection_at = fields.Int()
    anomaly_level = fields.Int()


class DetectionRouteSchema(PlainDetectionRouteSchema):
    create_at = fields.Int()
    delete_at = fields.Int()
    delete_by = fields.Int()


class DetectionRouteUpdateSchema(Schema):
    id = fields.Int()
    detection_id = fields.Int()
    latitude = fields.Int()
    longitude = fields.Int()
    description = fields.Str()
    detection_at = fields.Int()
    anomaly_level = fields.Int()


class DetectionRouteDeleteSchema(PlainDetectionRouteSchema):
    id = fields.Int()
    delete_by = fields.Int()


class DetectionRouteCreateSchema(PlainDetectionRouteSchema):
    id = fields.Int()
    detection_id = fields.Int()
    latitude = fields.Int()
    longitude = fields.Int()
    description = fields.Str()
    detection_at = fields.Int()
    anomaly_level = fields.Int()
