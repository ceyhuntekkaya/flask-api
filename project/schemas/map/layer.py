from marshmallow import Schema, fields

from project.schemas.map.sensor import PlainSensorSchema
from project.schemas.map.unit import PlainUnitSchema


class PlainLayerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    created_at = fields.DateTime()
    status = fields.Int()
    unit_id = fields.Int()
    sensors = fields.List(fields.Nested(PlainSensorSchema()))
    units = fields.List(fields.Nested(PlainUnitSchema()))


class LayerSchema(PlainLayerSchema):
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class LayerUpdateSchema(PlainLayerSchema):
    updated_by = fields.Int()


class LayerDeleteSchema(PlainLayerSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class LayerCreateSchema(PlainLayerSchema):
    created_by = fields.Int()


class LayerForAreaSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    status = fields.Int()
