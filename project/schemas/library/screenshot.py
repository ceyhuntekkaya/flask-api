from marshmallow import Schema, fields


class PlainScreenshotSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    begin_at = fields.Int()
    end_at = fields.Int()
    media_type = fields.Str()
    credential = fields.Str()
    storage_address = fields.Str()
    media_source_id = fields.Int()
    layer_id = fields.Int()
    area_id = fields.Int()
    sensor_id = fields.Int()
    unit_id = fields.Int()


class ScreenshotSchema(PlainScreenshotSchema):
    created_at = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    status = fields.Str()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class ScreenshotUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    begin_at = fields.Int()
    end_at = fields.Int()
    media_type = fields.Str()
    credential = fields.Str()
    storage_address = fields.Str()
    media_source_id = fields.Int()
    layer_id = fields.Int()
    area_id = fields.Int()
    sensor_id = fields.Int()
    unit_id = fields.Int()
    status = fields.Str()
    updated_by = fields.Int()


class ScreenshotDeleteSchema(PlainScreenshotSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class ScreenshotCreateSchema(PlainScreenshotSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    begin_at = fields.Int()
    end_at = fields.Int()
    media_type = fields.Str()
    credential = fields.Str()
    storage_address = fields.Str()
    media_source_id = fields.Int()
    layer_id = fields.Int()
    area_id = fields.Int()
    sensor_id = fields.Int()
    unit_id = fields.Int()
    status = fields.Str()
