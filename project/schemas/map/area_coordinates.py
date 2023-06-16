from marshmallow import Schema, fields


class PlainAreaCoordinateSchema(Schema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()


class AreaCoordinateSchema(PlainAreaCoordinateSchema):
    area_id = fields.Int()
    created_at = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AreaCoordinateUpdateSchema(PlainAreaCoordinateSchema):
    updated_by = fields.Int()


class AreaCoordinateDeleteSchema(Schema):
    id = fields.Int()
    deleted_at = fields.Str()


class AreaCoordinateCreateSchema(Schema):
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
