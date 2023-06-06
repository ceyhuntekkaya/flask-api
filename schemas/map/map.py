from marshmallow import Schema, fields


class PlainMapSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_at = fields.Int()

class MapSchema(PlainMapSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Boolean()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()

class MapUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    update_by = fields.Int()

class MapDeleteSchema(PlainMapSchema):
    id = fields.Int()
    delete_by = fields.Int()

class MapCreateSchema(PlainMapSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_by = fields.Int()