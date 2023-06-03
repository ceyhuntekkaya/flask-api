from marshmallow import Schema, fields


class PlainDataPackageSchema(Schema):
    id = fields.Int(dump_only=True)


class DataPackageSchema(Schema):
    store_id = fields.Int(required=True, load_only=True)


class DataPackagepdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class DataPackageDeleteSchema(Schema):
    id = fields.Int(dump_only=True)


class DataPackageCreateSchema(Schema):
    id = fields.Int(dump_only=True)