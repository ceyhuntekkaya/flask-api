from marshmallow import Schema, fields


class PlainHierarchySchema(Schema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()


class HierarchySchema(PlainHierarchySchema):
    create_at = fields.Int()
    update_at = fields.Int()
    delete_at = fields.Int()
    is_active = fields.Bool()
    create_by = fields.Int()
    update_by = fields.Int()
    delete_by = fields.Int()


class HierarchyUpdateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()
    is_active = fields.Bool()
    update_by = fields.Int()


class HierarchyDeleteSchema(PlainHierarchySchema):
    id = fields.Int()
    delete_by = fields.Int()


class HierarchyCreateSchema(PlainHierarchySchema):
    id = fields.Int()
    name = fields.Str()
    hierarchical_order = fields.Int()
