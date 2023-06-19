from marshmallow import Schema, fields


class PlainEquipmentSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    description = fields.Str()
    unit_id = fields.Int()
    equipment_type = fields.Str()
    lat = fields.Float()
    lon = fields.Float()
    standardIdentityFirstDigit = fields.Str()
    standardIdentitySecondDigit = fields.Str()
    symbolSet = fields.Str()
    entity = fields.Str()
    entityType = fields.Str()
    sectorIModifier = fields.Str()
    sectorIIModifier = fields.Str()
    hqTaskforceDummy = fields.Str()
    amplifier = fields.Str()
    symbolCode = fields.Str()
    src = fields.Str()


class EquipmentSchema(PlainEquipmentSchema):
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()
    created_at = fields.Str()


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
    created_by = fields.Int()
