from marshmallow import Schema, fields

from project.schemas.map.sensor import PlainSensorSchema


class PlainUnitSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    base_unit_id = fields.Int(required=False)
    unit_type = fields.Str()
    unit_command = fields.Str()
    hierarchy_id = fields.Int()
    unit_parent = fields.Str()
    unit_sub = fields.Str()
    symbol_code = fields.Str()
    critical_unit_type = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    sensors = fields.List(fields.Nested(PlainSensorSchema()))


class UnitSchema(PlainUnitSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class UnitUpdateSchema(PlainUnitSchema):
    status = fields.Int()
    updated_by = fields.Int()


class UnitDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class UnitCreateSchema(PlainUnitSchema):
    status = fields.Int()
    created_by = fields.Int()





