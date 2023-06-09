from marshmallow import Schema, fields


class PlainMediaSchema(Schema):
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


class MediaSchema(PlainMediaSchema):
    created_at = fields.Int()
    updated_at = fields.Int()
    deleted_at = fields.Int()
    status = fields.Int()
    status = fields.Str()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class MediaUpdateSchema(Schema):
    updated_by = fields.Int()


class MediaDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class MediaCreateSchema(PlainMediaSchema):
    created_by = fields.Int()
    status = fields.Int()
