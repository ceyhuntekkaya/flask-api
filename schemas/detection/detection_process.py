from marshmallow import Schema, fields


class PlainDetectionProcessSchema(Schema):
    id =  fields.Int()
    detection_id =  fields.Int()
    user_id =  fields.Int()
    process_at =  fields.Int()
    process =  fields.Str()
    create_at = fields.Int()


class DetectionProcessSchema(PlainDetectionProcessSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    active = fields.Bool()
    update_by = fields.Int()
    delete_by = fields.Int()


class DetectionProcessUpdateSchema(Schema):
    id =  fields.Int()
    detection_id =  fields.Int()
    user_id =  fields.Int()
    process_at =  fields.Int()
    process =  fields.Str()
    update_by = fields.Int()


class DetectionProcessDeleteSchema(PlainDetectionProcessSchema):
    id =  fields.Int()
    delete_by = fields.Int()


class DetectionProcessCreateSchema(PlainDetectionProcessSchema):
    id =  fields.Int()
    detection_id =  fields.Int()
    user_id =  fields.Int()
    process_at =  fields.Int()
    process =  fields.Str()