from marshmallow import Schema, fields


class PlainAuthoritySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    create_by = fields.Int()


class AuthoritySchema(PlainAuthoritySchema):
    create_at = fields.Int()
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()

class AuthorityUpdateSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    update_by = fields.Int()


class AuthorityDeleteSchema(PlainAuthoritySchema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    delete_by = fields.Int()

class AuthorityCreateSchema(PlainAuthoritySchema):
    id = fields.Int(dump_only=True)
    name = fields.Str()