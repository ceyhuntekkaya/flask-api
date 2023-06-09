from marshmallow import Schema, fields


class PlainCommandCollarMarkRankSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    command_collar_mark_id = fields.Int(dump_only=True)


class CommandCollarMarkRankSchema(PlainCommandCollarMarkRankSchema):
    created_at = fields.Int(required=True)
    updated_at = fields.Int(required=False)
    deleted_at = fields.Int(required=False)
    created_by = fields.Int(required=False)
    updated_by = fields.Int(required=False)
    deleted_by = fields.Int(required=False)


class CommandCollarMarkRankUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    command_collar_mark_id = fields.Int()
    updated_by = fields.Int(required=False)


class CommandCollarMarkRankDeleteSchema(PlainCommandCollarMarkRankSchema):
    id = fields.Int(dump_only=True)
    deleted_by = fields.Int(required=False)


class CommandCollarMarkRankCreateSchema(PlainCommandCollarMarkRankSchema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    hierarchical_order = fields.Str(required=True)
    status = fields.Int(required=False, default=True)
    command_collar_mark_id = fields.Int()
    created_by = fields.Int(required=False)