from marshmallow import Schema, fields


class PlainSignSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class SignSchema(PlainSignSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class SignUpdateSchema(Schema):
    updated_by = fields.Int()
    status = fields.Int()


class SignDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class SignCreateSchema(PlainSignSchema):
    created_by = fields.Int()
    status = fields.Int()
