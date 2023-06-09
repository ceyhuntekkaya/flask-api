from marshmallow import Schema, fields


class PlainMediaSourceSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    credential = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    created_at = fields.Int()


class MediaSourceSchema(PlainMediaSourceSchema):
    updated_at = fields.Int()
    deleted_at = fields.Int()
    status = fields.Int()
    status = fields.Str()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class MediaSourceUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    credential = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    updated_by = fields.Int()


class MediaDSourceeleteSchema(PlainMediaSourceSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class MediaSourceCreateSchema(PlainMediaSourceSchema):
    id = fields.Int()
    name = fields.Str()
    credential = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    created_by = fields.Int()
