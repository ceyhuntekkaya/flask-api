from marshmallow import Schema, fields


class PlainSystemSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    system_status = fields.Str()
    create_at = fields.Int(required=True)
    create_by = fields.Int(required=False)


class SystemSchema(PlainSystemSchema):
    update_at = fields.Int(required=False)
    delete_at = fields.Int(required=False)
    update_by = fields.Int(required=False)
    delete_by = fields.Int(required=False)


class SystemUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    system_status = fields.Str()
    update_by = fields.Int()


class SystemDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class SystemCreateSchema(Schema):
    id = fields.Int(dump_only=True)
    status = fields.Int(required=True)
    system_status = fields.Str()
    create_at = fields.Int(required=True)
    create_by = fields.Int(required=False)
