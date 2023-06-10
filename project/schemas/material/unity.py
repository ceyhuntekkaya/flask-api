from marshmallow import Schema, fields


class PlainUnitySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class UnitySchema(PlainUnitySchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class UnityUpdateSchema(PlainUnitySchema):
    status = fields.Int()
    updated_by = fields.Int()


class UnityDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class UnityCreateSchema(PlainUnitySchema):
    status = fields.Int()
    created_by = fields.Int()
