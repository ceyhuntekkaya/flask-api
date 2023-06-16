from marshmallow import Schema, fields


class PlainSensorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    source = fields.Str()
    description = fields.Str()
    hierarchy_id = fields.Int()
    sensor_weight = fields.Float()
    unit_id = fields.Int()
    sensor_type = fields.Str()
    evaluation_number = fields.Int()
    rpm = fields.Int()
    detection_range = fields.Int()
    is_fusible = fields.Bool()
    cake_slice = fields.Bool()
    line_of_sight_angle = fields.Float()
    line_of_sight_distance = fields.Float()
    near_circle = fields.Bool()
    circle_radius = fields.Int()
    circle_time_interval = fields.Int()
    is_meteorology_includes = fields.Boolean()
    latitude = fields.Int()
    longitude = fields.Int()
    aselsan_unit_id = fields.Int()
    desired_columns = fields.List(fields.Str())
    models = fields.List(fields.Str())
    filters = fields.List(fields.Str())
    training_config = fields.Dict()
    image = fields.Str()
    is_approved = fields.Bool()
    nvr = fields.Str()
    status = fields.Int()


class SensorSchema(PlainSensorSchema):
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()

    updated_by = fields.Int()
    deleted_by = fields.Int()
    created_by = fields.Int()


class SensorUpdateSchema(PlainSensorSchema):
    updated_by = fields.Int()


class SensorDeleteSchema(Schema):
    id = fields.Int()
    deleted_by = fields.Int()


class SensorCreateSchema(PlainSensorSchema):
    created_by = fields.Int()


class TrainingConfigSchema(PlainSensorSchema):
    created_by = fields.Int()
    clustering_algorithm = fields.Int()
    dbscan_eps = fields.Float()
    dbscan_min_samples = fields.Float()
    dbscan_metric = fields.Str()
    meanshift_bandwith = fields.Float()
    meanshift_n_jobs = fields.Str()
    image = fields.Str()
    nvr = fields.Str()
