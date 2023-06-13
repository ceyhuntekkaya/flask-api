from marshmallow import Schema, fields


class PlainFacilitySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    created_at = fields.Str()


class FacilitySchema(PlainFacilitySchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class FacilityUpdateSchema(Schema):
    updated_by = fields.Int()
    status = fields.Int()


class FacilityDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class FacilityCreateSchema(PlainFacilitySchema):
    created_by = fields.Int()
    status = fields.Int()
