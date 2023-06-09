from marshmallow import Schema, fields


class PlainCommandCollarMarkSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    command_id = fields.Int(dump_only=True)


class CommandCollarMarkSchema(PlainCommandCollarMarkSchema):
    created_at = fields.Int(required=True)
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    created_by = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class CommandCollarMarkUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    command_id = fields.Int()
    updated_by = fields.Int(required=False)


class CommandCollarMarkDeleteSchema(PlainCommandCollarMarkSchema):
    id = fields.Int(dump_only=True)
    deleted_by = fields.Int(required=False)


class CommandCollarMarkCreateSchema(PlainCommandCollarMarkSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    command_id = fields.Int()
    created_by = fields.Int(required=False)
