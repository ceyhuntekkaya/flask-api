from marshmallow import Schema, fields


class PlainSensorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_at = fields.Int()

class SensorSchema(PlainSensorSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    active = fields.Bool()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()

class SensorUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    update_by = fields.Int()

class SensorDeleteSchema(PlainSensorSchema):
    id = fields.Int()
    delete_by = fields.Int()

class SensorCreateSchema(PlainSensorSchema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_by = fields.Int()