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
    is_active = fields.Bool()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class SensorUpdateSchema(PlainSensorSchema):
    update_by = fields.Int()
    is_active = fields.Bool()


class SensorDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class SensorCreateSchema(PlainSensorSchema):
    create_by = fields.Int()
    is_active = fields.Bool()
