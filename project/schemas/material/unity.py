from marshmallow import Schema, fields


class PlainUnitySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_at = fields.Int()


class UnitySchema(PlainUnitySchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Bool()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class UnityUpdateSchema(PlainUnitySchema):
    is_active = fields.Bool()
    update_by = fields.Int()


class UnityDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class UnityCreateSchema(PlainUnitySchema):
    is_active = fields.Bool()
    create_by = fields.Int()
