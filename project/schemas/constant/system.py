from marshmallow import Schema, fields


class PlainSystemSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    system_status = fields.Str()
    created_at = fields.Int(required=True)
    created_by = fields.Int(required=False)


class SystemSchema(PlainSystemSchema):
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class SystemUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    system_status = fields.Str()
    updated_by = fields.Int()


class SystemDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class SystemCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    system_status = fields.Str()
    created_at = fields.Int(required=True)
    created_by = fields.Int(required=False)
