from marshmallow import Schema, fields


class PlainCommandCollarMarkRankSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    is_active = fields.Bool(required=False, default=True)
    command_collar_mark_id = fields.Int(dump_only=True)


class CommandCollarMarkRankSchema(PlainCommandCollarMarkRankSchema):
    create_at = fields.Int(required=True)
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    create_by = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class CommandCollarMarkRankUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    is_active = fields.Bool(required=False, default=True)
    command_collar_mark_id = fields.Int()
    update_by = fields.Int(required=False)


class CommandCollarMarkRankDeleteSchema(PlainCommandCollarMarkRankSchema):
    id = fields.Int(dump_only=True)
    delete_by = fields.Int(required=False)


class CommandCollarMarkRankCreateSchema(PlainCommandCollarMarkRankSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    is_active = fields.Bool(required=False, default=True)
    command_collar_mark_id = fields.Int()
    create_by = fields.Int(required=False)