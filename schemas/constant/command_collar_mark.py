from marshmallow import Schema, fields


class PlainCommandCollarMarkSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    active = fields.Bool(required=False, default=True)
    command_id = fields.Int(dump_only=True)

class CommandCollarMarkSchema(PlainCommandCollarMarkSchema):
    create_at = fields.Int(required=True)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)

class CommandCollarMarkUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    active = fields.Bool(required=False, default=True)
    command_id = fields.Int()
    update_by = fields.Int(required=False)

class CommandCollarMarkDeleteSchema(PlainCommandCollarMarkSchema):
    id = fields.Int(dump_only=True)
    delete_by = fields.Int(required=False)

class CommandCollarMarkCreateSchema(PlainCommandCollarMarkSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    active = fields.Bool(required=False, default=True)
    command_id = fields.Int()
    create_by = fields.Int(required=False)