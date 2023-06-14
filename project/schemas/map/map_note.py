from marshmallow import Schema, fields


class PlainMapNoteSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class MapNoteSchema(PlainMapNoteSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class MapNoteUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    updated_by = fields.Int()


class MapNoteDeleteSchema(PlainMapNoteSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class MapNoteCreateSchema(PlainMapNoteSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_by = fields.Int()
