from marshmallow import Schema, fields


class PlainDetectionReportSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
    format = fields.Str()
    created_at = fields.Int(required=False)


class DetectionReportSchema(PlainDetectionReportSchema):
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    status = fields.Int(required=True)
    created_by = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class DetectionReportUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
    format = fields.Str()
    updated_by = fields.Int(required=False)


class DetectionReportDeleteSchema(PlainDetectionReportSchema):
    id = fields.Int()
    deleted_by = fields.Int(required=False)


class DetectionReportCreateSchema(PlainDetectionReportSchema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
    format = fields.Str()
