from marshmallow import Schema, fields


class PlainIdentificationTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    identification_id = fields.Int(required=True)
    identification = fields.Str(required=False, default=True)
    created_at = fields.Int(required=True)
    created_by = fields.Int(required=False)


class IdentificationTypeSchema(PlainIdentificationTypeSchema):
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class IdentificationTypeUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    identification_id = fields.Int(required=True)
    identification = fields.Str(required=False, default=True)
    updated_by = fields.Int()


class IdentificationTypeDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class IdentificationTypeCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    identification_id = fields.Int(required=True)
    identification = fields.Str(required=False, default=True)
    created_at = fields.Int(required=True)
    created_by = fields.Int(required=False)
