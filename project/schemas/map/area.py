from marshmallow import Schema, fields


class PlainAreaSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    color = fields.Str()
    area_type = fields.Str()
    critical_area_type = fields.Str()
    created_at = fields.Str()


class AreaSchema(PlainAreaSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class AreaUpdateSchema(PlainAreaSchema):
    updated_by = fields.Int()
    status = fields.Int()


class AreaDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class AreaCreateSchema(PlainAreaSchema):
    created_by = fields.Int()
    status = fields.Int()
