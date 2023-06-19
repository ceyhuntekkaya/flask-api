from marshmallow import Schema, fields


class PlainEquipmentSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    unit_id = fields.Int()
    created_at = fields.Str()
    source = fields.Str()
    symbol_code = fields.Str()
    equipment_type = fields.Str()


class EquipmentSchema(PlainEquipmentSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class EquipmentUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    unit_id = fields.Int()
    symbol_code = fields.Str()
    updated_by = fields.Int()


class EquipmentDeleteSchema(PlainEquipmentSchema):
    id = fields.Int()
    deleted_by = fields.Int()


class EquipmentCreateSchema(PlainEquipmentSchema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    symbol_code = fields.Str()
    unit_id = fields.Int()
    created_by = fields.Int()