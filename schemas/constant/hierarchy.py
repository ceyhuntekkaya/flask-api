from marshmallow import Schema, fields


class PlainHierarchySchema(Schema):
    id = fields.Int(dump_only=True)


class HierarchySchema(PlainHierarchySchema):
    store_id = fields.Int(required=True, load_only=True)


class HierarchyUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class HierarchyDeleteSchema(PlainHierarchySchema):
    id = fields.Int(dump_only=True)


class HierarchyCreateSchema(PlainHierarchySchema):
    id = fields.Int(dump_only=True)