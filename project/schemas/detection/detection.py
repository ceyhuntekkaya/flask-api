from marshmallow import Schema, fields


class PlainDetectionSchema(Schema):
    id = fields.Int(dump_only=True)
    detection_start_time = fields.Int(required=True)
    detection_lat = fields.Int(required=False, default=True)
    detection_lon = fields.Int(required=True)


class DetectionSchema(PlainDetectionSchema):
    id = fields.Int(dump_only=True)


class DetectionUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    detection_start_time = fields.Int(required=True)
    detection_lat = fields.Int(required=False, default=True)
    detection_lon = fields.Int(required=True)


class DetectionDeleteSchema(Schema):
    id = fields.Int(dump_only=True)
    detection_start_time = fields.Int(required=True)
    detection_lat = fields.Int(required=False, default=True)
    detection_lon = fields.Int(required=True)


class DetectionCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    detection_start_time = fields.Int(required=True)
    detection_lat = fields.Int(required=False, default=True)
    detection_lon = fields.Int(required=True)
