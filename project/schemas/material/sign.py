from marshmallow import Schema, fields


class PlainSignSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_at = fields.Int()


class SignSchema(PlainSignSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Bool()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class SignUpdateSchema(Schema):
    update_by = fields.Int()
    is_active = fields.Bool()


class SignDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class SignCreateSchema(PlainSignSchema):
    create_by = fields.Int()
    is_active = fields.Bool()
