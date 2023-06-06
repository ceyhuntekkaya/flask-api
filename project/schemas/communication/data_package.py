from marshmallow import Schema, fields


class PlainDataPackageSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    data_from = fields.Int()
    data_to = fields.Int()
    header = fields.Str()
    content = fields.Str()
    priority = fields.Int()
    data_type = fields.Str()
    create_at = fields.Int()


class DataPackageSchema(Schema):
    send_ip = fields.Str()
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Boolean()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class DataPackageUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    data_from = fields.Int()
    data_to = fields.Int()
    header = fields.Str()
    content = fields.Str()
    priority = fields.Int()
    data_type = fields.Str()
    is_active = fields.Boolean()
    update_by = fields.Int()


class DataPackageDeleteSchema(Schema):
    id = fields.Int()
    delete_by = fields.Int()


class DataPackageCreateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    data_from = fields.Int()
    data_to = fields.Int()
    header = fields.Str()
    content = fields.Str()
    priority = fields.Int()
    data_type = fields.Str()
    send_ip = fields.Str()
