from marshmallow import Schema, fields


class PlainIdentificationTypeSchema(Schema):
    id = fields.Int(dump_only=True)
    identification_id = fields.Int(required=True)
    identification = fields.Str(required=False, default=True)
    create_at = fields.Int(required=True)
    create_by = fields.Int(required=False)


class IdentificationTypeSchema(PlainIdentificationTypeSchema):
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class IdentificationTypeUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    identification_id = fields.Int(required=True)
    identification = fields.Str(required=False, default=True)
    update_by = fields.Int()


class IdentificationTypeDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class IdentificationTypeCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    identification_id = fields.Int(required=True)
    identification = fields.Str(required=False, default=True)
    create_at = fields.Int(required=True)
    create_by = fields.Int(required=False)
