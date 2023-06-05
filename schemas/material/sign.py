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
    active = fields.Bool()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class SignUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    update_by = fields.Int()


class SignDeleteSchema(PlainSignSchema):
    id = fields.Int()
    delete_by = fields.Int()


class SignCreateSchema(PlainSignSchema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_by = fields.Int()