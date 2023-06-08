from marshmallow import Schema, fields


class PlainConfigSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    config_json = fields.Str(required=False, default=True)
    create_at = fields.Int(required=True)
    create_by = fields.Int(required=False)


class ConfigSchema(PlainConfigSchema):
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class ConfigUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    config_json = fields.Str(required=False, default=True)
    update_by = fields.Int()


class ConfigDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class ConfigCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    config_json = fields.Str(required=False, default=True)
    create_at = fields.Int(required=True)
    create_by = fields.Int(required=False)
