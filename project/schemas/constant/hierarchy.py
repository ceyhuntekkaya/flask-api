from marshmallow import Schema, fields


class PlainHierarchySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()


class HierarchySchema(PlainHierarchySchema):
    created_at = fields.Str()
    updated_at = fields.Str()
    deleted_at = fields.Str()
    status = fields.Int()
    created_by = fields.Int()
    updated_by = fields.Int()
    deleted_by = fields.Int()


class HierarchyUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()
    status = fields.Int()
    updated_by = fields.Int()


class HierarchyDeleteSchema(PlainHierarchySchema):
    id = fields.Int()
    deleted_by = fields.Int()


class HierarchyCreateSchema(PlainHierarchySchema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()
