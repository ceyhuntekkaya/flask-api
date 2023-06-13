from marshmallow import Schema, fields


class PlainAreaCoordinateSchema(Schema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    area_id = fields.Int()
    created_at = fields.Str()


class AreaCoordinateSchema(PlainAreaCoordinateSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AreaCoordinateUpdateSchema(Schema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    area_id = fields.Int()
    updated_by = fields.Int()


class AreaCoordinateDeleteSchema(PlainAreaCoordinateSchema):
    id = fields.Int()
    deleted_at = fields.Str()


class AreaCoordinateCreateSchema(PlainAreaCoordinateSchema):
    id = fields.Int()
    row_number = fields.Int()
    latitude = fields.Float()
    longitude = fields.Float()
    area_id = fields.Int()
    created_by = fields.Int()
