from marshmallow import Schema, fields


class PlainMediaSourceSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    credential = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    create_at = fields.Int()
   
class MediaSourceSchema(PlainMediaSourceSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Boolean()
    status = fields.Str()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()

class MediaSourceUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    credential = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    update_by = fields.Int()

class MediaDSourceeleteSchema(PlainMediaSourceSchema):
    id = fields.Int()
    delete_by = fields.Int()

class MediaSourceCreateSchema(PlainMediaSourceSchema):
    id = fields.Int()
    name = fields.Str()
    credential = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    create_by = fields.Int()
    