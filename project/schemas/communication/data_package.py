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
    created_at = fields.Str()


class DataPackageSchema(Schema):
    send_ip = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class DataPackageUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    data_from = fields.Int()
    data_to = fields.Int()
    header = fields.Str()
    content = fields.Str()
    priority = fields.Int()
    data_type = fields.Str()
    status = fields.Int()
    updated_by = fields.Int()


class DataPackageDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


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
