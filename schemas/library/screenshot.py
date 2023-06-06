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
    map_id = fields.Int()
    layer_id = fields.Int()
    sensor_id = fields.Int()
    unity_id = fields.Int()
    official_user_id = fields.Int()


class ScreenshotSchema(PlainScreenshotSchema):
    create_at = fields.Int()
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Boolean()
    status = fields.Str()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


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
    map_id = fields.Int()
    layer_id = fields.Int()
    sensor_id = fields.Int()
    unity_id = fields.Int()
    official_user_id = fields.Int()
    status = fields.Str()
    update_by = fields.Int()


class ScreenshotDeleteSchema(PlainScreenshotSchema):
    id = fields.Int()
    delete_by = fields.Int()



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
    map_id = fields.Int()
    layer_id = fields.Int()
    sensor_id = fields.Int()
    unity_id = fields.Int()
    official_user_id = fields.Int()
    status = fields.Str()