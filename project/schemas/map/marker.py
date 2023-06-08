from marshmallow import Schema, fields


class PlainMarkerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    type = fields.Str()
    color = fields.Str()
    sensor_id = fields.Int()
    sign_id = fields.Int()
    symbol_id = fields.Int()
    unity_id = fields.Int()
    description = fields.Str()
    latitude = fields.Float()
    longitude = fields.Float()
    map_id = fields.Int()
    layer_id = fields.Int()
    hierarchy_id = fields.Int()
    official_user_id = fields.Int()
    create_at = fields.Int()


class MarkerSchema(PlainMarkerSchema):
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Boolean()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class MarkerUpdateSchema(PlainMarkerSchema):
    update_by = fields.Int()
    is_active = fields.Boolean()


class MarkerDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class MarkerCreateSchema(PlainMarkerSchema):
    create_by = fields.Int()
    is_active = fields.Boolean()