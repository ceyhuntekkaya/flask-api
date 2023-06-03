from marshmallow import Schema, fields


class PlainSensorSchema(Schema):
    id = fields.Int(dump_only=True)


class SensorSchema(PlainSensorSchema):
    store_id = fields.Int(required=True, load_only=True)


class SensorUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class SensorDeleteSchema(PlainSensorSchema):
    id = fields.Int(dump_only=True)


class SensorCreateSchema(PlainSensorSchema):
    id = fields.Int(dump_only=True)