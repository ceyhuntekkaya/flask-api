from marshmallow import Schema, fields
from project.schemas.map.area_coordinates import AreaCoordinateSchema, AreaCoordinateCreateSchema, PlainAreaCoordinateSchema
from project.schemas.map.area_layer import AreaLayerSchema, AreaLayerCreateSchema
from project.schemas.map.layer import LayerForAreaSchema


class PlainAreaSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    area_type = fields.Str()
    area_parent = fields.Str()
    area_sub = fields.Str()
    symbol_code = fields.Str()
    critical_area_type = fields.Str()
    color = fields.Str()
    status = fields.Int()
    created_at = fields.Str(dump_only=True)
    coordinates = fields.List(fields.Nested(PlainAreaCoordinateSchema()))
    layers = fields.List(fields.Nested(LayerForAreaSchema()))


class AreaSchema(PlainAreaSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AreaBaseCreateSchema(PlainAreaSchema):
    created_by = fields.Int()
    status = fields.Int()


class AreaBaseUpdateSchema(PlainAreaSchema):
    id = fields.Int()
    updated_by = fields.Int()
    status = fields.Int()


class AreaUpdateSchema(PlainAreaSchema):
    area = fields.Nested(AreaBaseUpdateSchema())
    coordinates = fields.List(fields.Nested(AreaCoordinateCreateSchema()))
    layers = fields.List(fields.Nested(AreaLayerCreateSchema()))


class AreaDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class AreaCreateSchema(PlainAreaSchema):
    area = fields.Nested(AreaBaseCreateSchema())
    coordinates = fields.List(fields.Nested(AreaCoordinateCreateSchema()))
    layers = fields.List(fields.Nested(AreaLayerCreateSchema()))


class AreaDetailSchema(PlainAreaSchema):
    created_by = fields.Int()
    status = fields.Int()
    coordinates = fields.List(fields.Nested(AreaCoordinateSchema()), dump_only=True)
    layers = fields.List(fields.Nested(AreaLayerSchema()), dump_only=True)
    # abc = fields.Nested(AreaLayerSchema(), dump_only=True)


class AreaForTreeSchema(Schema):
    area = fields.Nested(AreaBaseCreateSchema())
    coordinates = fields.List(fields.Nested(AreaCoordinateCreateSchema()))
