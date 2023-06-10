from marshmallow import Schema, fields


class PlainSensorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class SensorSchema(PlainSensorSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class SensorUpdateSchema(PlainSensorSchema):
    updated_by = fields.Int()
    status = fields.Int()


class SensorDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class SensorCreateSchema(PlainSensorSchema):
    created_by = fields.Int()
    status = fields.Int()
