from marshmallow import Schema, fields


class PlainMessageTemplateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()


class MessageTemplateSchema(Schema):
    created_at = fields.Int()
    updated_at = fields.Int()
    deleted_at = fields.Int()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class MessageTemplateUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
    status = fields.Int()
    updated_by = fields.Int()


class MessageTemplateDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class MessageTemplateCreateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
