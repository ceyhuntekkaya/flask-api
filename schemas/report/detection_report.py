from marshmallow import Schema, fields


class PlainDetectionReportSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
    format = fields.Str()
    create_at = fields.Int(required=False)

class DetectionReportSchema(PlainDetectionReportSchema):
    
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    is_active = fields.Bool(required=True)
    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)

class DetectionReportUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
    format = fields.Str()
    update_by = fields.Int(required=False)

class DetectionReportDeleteSchema(PlainDetectionReportSchema):
    id = fields.Int()
    delete_by = fields.Int(required=False)

class DetectionReportCreateSchema(PlainDetectionReportSchema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
    format = fields.Str()