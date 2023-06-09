from marshmallow import Schema, fields


class PlainConfigSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    config_json = fields.Str(required=False, default=True)
    created_at = fields.Int(required=True)
    created_by = fields.Int(required=False)


class ConfigSchema(PlainConfigSchema):
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class ConfigUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    config_json = fields.Str(required=False, default=True)
    updated_by = fields.Int()


class ConfigDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class ConfigCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    config_json = fields.Str(required=False, default=True)
    created_at = fields.Int(required=True)
    created_by = fields.Int(required=False)
