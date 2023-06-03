from marshmallow import Schema, fields


class PlainDetectionReportSchema(Schema):
    id = fields.Int(dump_only=True)


class DetectionReportSchema(PlainDetectionReportSchema):
    store_id = fields.Int(required=True, load_only=True)


class DetectionReportUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class DetectionReportDeleteSchema(PlainDetectionReportSchema):
    id = fields.Int(dump_only=True)


class DetectionReportCreateSchema(PlainDetectionReportSchema):
    id = fields.Int(dump_only=True)