from marshmallow import Schema, fields


class PlainMessageTemplateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()


class MessageTemplateSchema(Schema):
    create_at = fields.Int()
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Boolean()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class MessageTemplateUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
    is_active = fields.Boolean()
    update_by = fields.Int()


class MessageTemplateDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class MessageTemplateCreateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    header = fields.Str()
    content = fields.Str()
