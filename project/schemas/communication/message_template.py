from marshmallow import Schema, fields


class PlainMessageTemplateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()


class MessageTemplateSchema(Schema):
    created_at = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()
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
