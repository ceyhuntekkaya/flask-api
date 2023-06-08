#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

import dateutil.parser
from cerberus import Validator

to_date = lambda s: datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
to_date_milisecond = lambda s: datetime.strptime(s, "%Y-%m-%d %H:%M:%S.%f")
to_iso_date = lambda s: dateutil.parser.isoparse(s)
to_int = lambda s: int(s)


async def validate_auth_register(_in):
    schema = {
        "username": {
            "type": "string",
            "required": True,
            "nullable": False,
            "minlength": 1,
        },
        "password": {
            "type": "string",
            "required": True,
            "nullable": False,
            "minlength": 1,
        },
        "firstname": {"type": "string", "required": False, "nullable": False},
        "lastname": {"type": "string", "required": False, "nullable": False},
        "rank": {"type": "string", "required": False, "nullable": False},
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_auth_login(_in):
    schema = {
        "username": {
            "type": "string",
            "required": True,
            "nullable": False,
            "minlength": 1,
        },
        "password": {
            "type": "string",
            "required": True,
            "nullable": False,
            "minlength": 1,
        },
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_set_anomaly(_in):
    schema = {
        "anomaly_type": {"type": "string", "required": True, "nullable": False},
        "class_name": {"type": "string", "required": True, "nullable": False},
        "confidence": {"type": "float", "required": True, "nullable": False},
        "description": {"type": "string", "required": True, "nullable": False},
        "editable_description": {"type": "string", "required": True, "nullable": False},
        "lat": {"type": "float", "required": True, "nullable": False},
        "lon": {"type": "float", "required": True, "nullable": False},
        "elevation": {"type": "float", "required": True, "nullable": False},
        "sensor_id": {"type": "integer", "required": True, "nullable": False},
        "unit_id": {"type": "integer", "required": True, "nullable": False},
        "unique_id": {"type": "string", "required": True, "nullable": False},
        "camera_id": {"type": "string", "required": True, "nullable": False},
        "nvr_ip": {"type": "string", "required": True, "nullable": False},
        "detector_name": {"type": "string", "required": True, "nullable": False},
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_get_anomalies(_in):
    schema = {
        "starts_at": {
            "type": "datetime",
            "coerce": to_iso_date,
            "required": False,
            "nullable": False,
        },
        "ends_at": {
            "type": "datetime",
            "coerce": to_iso_date,
            "required": False,
            "nullable": False,
        },
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_get_detections(_in):
    schema = {
        "starts_at": {
            "type": "datetime",
            "coerce": to_iso_date,
            "required": False,
            "nullable": False,
        },
        "ends_at": {
            "type": "datetime",
            "coerce": to_iso_date,
            "required": False,
            "nullable": False,
        },
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_get_training_configs(_in):
    schema = {
        "is_approved": {
            "type": "integer",
            "required": False,
            "nullable": False,
            "coerce": to_int,
        }
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_set_training_config_image(_in):
    schema = {
        "image": {"type": "string", "required": True, "nullable": False}
    }

    v = Validator(schema, allow_unknown=True)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_put_anomaly(_in):
    schema = {
        "editable_description": {"type": "string", "required": False, "nullable": False},
        "is_approved": {"type": "integer", "required": False, "nullable": False},
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_set_system_status(_in):
    schema = {
        "system_status": {
            "type": "string", "required": False, "nullable": False, "allowed": ["training", "live", "standby"]
        }
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_set_sensor_images(_in):
    schema = {
        "image": {"type": "string", "required": False, "nullable": False},
        "sensor_id": {"type": "integer", "required": False, "nullable": False},
        "image_order": {"type": "integer", "required": False, "nullable": False},
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_set_sensor(_in):
    schema = {
        "sensor_id": {"type": "integer", "required": True, "nullable": False},
        "unit_id": {"type": "integer", "required": True, "nullable": False},
        "sensor_name": {"type": "string", "required": True, "nullable": False},
        "sensor_weight": {"type": "float", "required": True, "nullable": False},
        "sensor_type": {"type": "string", "required": True, "nullable": False},
        "evaluation_number": {"type": "integer", "required": True, "nullable": False},
        "rpm": {"type": "integer", "required": True, "nullable": False},
        "detection_range": {"type": "integer", "required": True, "nullable": False},
        "is_fusible": {"type": "boolean", "required": True, "nullable": False},
        "cake_slice": {"type": "boolean", "required": True, "nullable": False},
        "line_of_sight_angle": {"type": "float", "required": True, "nullable": False},
        "line_of_sight_distance": {
            "type": "float",
            "required": True,
            "nullable": False,
        },
        "near_circle": {"type": "boolean", "required": True, "nullable": False},
        "circle_radius": {"type": "integer", "required": True, "nullable": False},
        "circle_time_interval": {
            "type": "integer",
            "required": True,
            "nullable": False,
        },
        "is_meteorology_includes": {
            "type": "boolean",
            "required": True,
            "nullable": False,
        },
        "desired_columns": {
            "type": "list",
            "required": True,
            "nullable": False,
            "schema": {
                "type": "string",
                "allowed": [
                    "range",
                    "azimuth",
                    "directionangle",
                    "velocity",
                    "tacticaldataid",
                    "snr",
                ],
            },
        },
        "models": {
            "type": "list",
            "required": True,
            "nullable": False,
            "schema": {"type": "string", "allowed": ["ecod", "copod", "if"]},
        },
        "filters": {
            "type": "list",
            "required": True,
            "nullable": False,
            "schema": {
                "type": "string",
                "allowed": ["tespit tekrarı", "hız", "tespit süresi"],
            },
        },
        "training_config": {
            "type": "dict",
            "required": True,
            "nullable": False,
            "schema": {
                "clustering_algorithm": {
                    "type": "string",
                    "required": True,
                    "nullable": False,
                    "allowed": ["dbscan", "meanshift"],
                },
                "dbscan_eps": {"type": "float", "required": True, "nullable": False},
                "dbscan_min_samples": {
                    "type": "float",
                    "required": True,
                    "nullable": False,
                },
                "dbscan_metric": {
                    "type": "string",
                    "required": True,
                    "nullable": False,
                },
                "meanshift_bandwith": {
                    "type": "float",
                    "required": True,
                    "nullable": False,
                },
                "meanshift_n_jobs": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
            },
        },
        "image": {"type": "string", "required": False, "nullable": False},
        "nvr": {"type": "string", "required": False, "nullable": True},

    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_put_sensor(_in):
    schema = {
        "sensor_name": {"type": "string", "required": True, "nullable": False},
        "sensor_weight": {"type": "float", "required": True, "nullable": False},
        "sensor_type": {"type": "string", "required": True, "nullable": False},
        "evaluation_number": {"type": "integer", "required": True, "nullable": False},
        "rpm": {"type": "integer", "required": True, "nullable": False},
        "detection_range": {"type": "integer", "required": True, "nullable": False},
        "is_fusible": {"type": "boolean", "required": True, "nullable": False},
        "cake_slice": {"type": "boolean", "required": True, "nullable": False},
        "line_of_sight_angle": {"type": "float", "required": True, "nullable": False},
        "line_of_sight_distance": {
            "type": "float",
            "required": True,
            "nullable": False,
        },
        "near_circle": {"type": "boolean", "required": True, "nullable": False},
        "circle_radius": {"type": "integer", "required": True, "nullable": False},
        "circle_time_interval": {
            "type": "integer",
            "required": True,
            "nullable": False,
        },
        "is_meteorology_includes": {
            "type": "boolean",
            "required": True,
            "nullable": False,
        },
        "desired_columns": {
            "type": "list",
            "required": True,
            "nullable": False,
            "schema": {
                "type": "string",
                "allowed": [
                    "range",
                    "azimuth",
                    "directionangle",
                    "velocity",
                    "tacticaldataid",
                    "snr"
                ],
            },
        },
        "models": {
            "type": "list",
            "required": True,
            "nullable": False,
            "schema": {"type": "string", "allowed": ["ecod", "copod", "if"]},
        },
        "filters": {
            "type": "list",
            "required": True,
            "nullable": False,
            "schema": {
                "type": "string",
                "allowed": ["tespit tekrarı", "hız", "tespit süresi"],
            },
        },
        "training_config": {
            "type": "dict",
            "required": True,
            "nullable": False,
            "schema": {
                "clustering_algorithm": {
                    "type": "string",
                    "required": True,
                    "nullable": False,
                    "allowed": ["dbscan", "meanshift"],
                },
                "dbscan_eps": {"type": "float", "required": True, "nullable": False},
                "dbscan_min_samples": {
                    "type": "float",
                    "required": True,
                    "nullable": False,
                },
                "dbscan_metric": {
                    "type": "string",
                    "required": True,
                    "nullable": False,
                },
                "meanshift_bandwith": {
                    "type": "float",
                    "required": True,
                    "nullable": False,
                },
                "meanshift_n_jobs": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
            },
        },
        "image": {"type": "string", "required": False, "nullable": False},
        "nvr": {"type": "string", "required": False, "nullable": True},
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_get_anomaly_counts_daily(_in):
    schema = {
        "starts_at": {
            "type": "datetime",
            "coerce": to_iso_date,
            "required": False,
            "nullable": False,
        },
        "ends_at": {
            "type": "datetime",
            "coerce": to_iso_date,
            "required": False,
            "nullable": False,
        },
        "date_type": {
            "type": "string",
            "required": True,
            "nullable": False,
            "allowed": ["hour", "day", "month"],
        },
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors


async def validate_config_file_json(_in):
    schema = {
        "system": {
            "type": "dict",
            "required": True,
            "nullable": False,
            "schema": {
                "exclude_dates": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "activated": {
                            "type": "boolean",
                            "required": True,
                            "nullable": False,
                        },
                        "dates": {
                            "type": "list",
                            "required": True,
                            "nullable": False,
                            "schema": {
                                "type": "list",
                                "schema": {
                                    "type": "datetime",
                                    "coerce": to_iso_date,
                                    "required": True,
                                    "nullable": False,
                                },
                            },
                        },
                    },
                },
                "anomaly_gate": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "ratio": {"type": "float", "required": True, "nullable": False},
                        "anomaly_density_time_threshold": {"type": "float", "required": True, "nullable": False},
                        "anomaly_density_control_timer": {"type": "float", "required": True, "nullable": False}
                    },
                },
                "general_condition_evaluation": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "activated": {
                            "type": "boolean",
                            "required": True,
                            "nullable": False,
                        },
                        "time_range": {
                            "type": "integer",
                            "required": True,
                            "nullable": False,
                        },
                        "last_n_day": {
                            "type": "integer",
                            "required": True,
                            "nullable": False,
                        },
                        "columns": {
                            "type": "list",
                            "required": True,
                            "nullable": False,
                            "schema": {
                                "type": "string",
                                "required": True,
                                "nullable": False,
                            },
                        },
                    },
                },
                "helper_conf": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "pin_distance": {
                            "type": "integer",
                            "required": True,
                            "nullable": False,
                        }
                    },
                },
                "debugging": {"type": "boolean", "required": True, "nullable": False},
                "center": {
                    "type": "list",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "type": "float",
                        "required": True,
                        "nullable": False,
                        "minlength": 4,
                        "maxlength": 4,
                    },
                },
                "export_group_csv": {
                    "type": "boolean",
                    "required": True,
                    "nullable": False,
                },
                "moving_object": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "activated": {
                            "type": "boolean",
                            "required": True,
                            "nullable": False,
                        },
                        "distance_threshold": {
                            "type": "integer",
                            "required": True,
                            "nullable": False,
                        },
                    },
                },
                "drawing": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "map_figure_path": {
                            "type": "string",
                            "required": True,
                            "nullable": False,
                        },
                        "map_borders": {
                            "type": "list",
                            "required": True,
                            "nullable": False,
                            "schema": {
                                "type": "float",
                                "required": True,
                                "nullable": False,
                                "minlength": 4,
                                "maxlength": 4,
                            },
                        },
                    },
                },
                "common_columns": {
                    "type": "list",
                    "required": True,
                    "nullable": False,
                    "schema": {"type": "string", "required": True, "nullable": False},
                },
                "dump": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "dump_interval": {
                            "type": "integer",
                            "required": True,
                            "nullable": False,
                        },
                        "source": {
                            "type": "string",
                            "required": True,
                            "nullable": False,
                        },
                        "cluster_source": {
                            "type": "string",
                            "required": True,
                            "nullable": False,
                        },
                        "condition_data": {
                            "type": "string",
                            "required": True,
                            "nullable": False,
                        },
                    },
                },

                "interface": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "mirsad": {
                            "type": "dict",
                            "required": True,
                            "nullable": False,
                            "schema": {
                                "host": {
                                    "type": "string",
                                    "required": True,
                                    "nullable": False,
                                },
                                "port": {
                                    "type": "string",
                                    "required": True,
                                    "nullable": False,
                                },
                                "database": {
                                    "type": "string",
                                    "required": True,
                                    "nullable": False,
                                },
                                "user": {
                                    "type": "string",
                                    "required": True,
                                    "nullable": False,
                                },
                                "password": {
                                    "type": "string",
                                    "required": True,
                                    "nullable": False,
                                },
                                "is_only_polygon_areas_selected": {
                                    "type": "boolean",
                                    "required": True,
                                    "nullable": False,
                                },
                            },
                        },
                        "takdim": {
                            "type": "dict",
                            "required": True,
                            "nullable": False,
                            "schema": {
                                "host": {
                                    "type": "string",
                                    "required": True,
                                    "nullable": False,
                                },
                                "is_only_polygon_areas_selected": {
                                    "type": "boolean",
                                    "required": True,
                                    "nullable": False,
                                },
                            },
                        },
                    },
                },
            },
        },
        "preprocessing": {
            "type": "dict",
            "required": True,
            "nullable": False,
            "schema": {
                "minimum_record_number": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
                "velocity_lower_threshold": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
                "velocity_upper_threshold": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
                "midas": {
                    "type": "dict",
                    "required": True,
                    "nullable": False,
                    "schema": {
                        "detectionelapsedtime_lower_interval": {
                            "type": "integer",
                            "required": True,
                            "nullable": False,
                        },
                        "detectionelapsedtime_upper_interval": {
                            "type": "integer",
                            "required": True,
                            "nullable": False,
                        },
                    },
                },
            },
        },
        "cascade_model": {
            "type": "dict",
            "required": True,
            "nullable": False,
            "schema": {
                "master_detection_type": {
                    "type": "list",
                    "required": True,
                    "nullable": False,
                    "schema": {"type": "integer", "required": True, "nullable": False},
                }
            },
        },
        "yaztat_rest_api": {
            "type": "dict",
            "required": True,
            "nullable": False,
            "schema": {
                "algorithm_crashed": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
                "data_processed_time_control": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
                "data_transportation_control_time": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
                "heartbeat_repeat_time": {
                    "type": "integer",
                    "required": True,
                    "nullable": False,
                },
                "rest_api_ip": {"type": "string", "required": True, "nullable": False},
                "port": {"type": "string", "required": True, "nullable": False},
                "version": {"type": "string", "required": True, "nullable": False},
                "sensorUuid": {"type": "string", "required": True, "nullable": False},
                "sensor_id": {"type": "integer", "required": True, "nullable": False},
                "unit_id": {"type": "integer", "required": True, "nullable": False},
                "sensor_lat": {"type": "float", "required": True, "nullable": False},
                "sensor_long": {"type": "float", "required": True, "nullable": False},
                "sensor_type": {"type": "string", "required": True, "nullable": False},
                "height": {"type": "integer", "required": True, "nullable": False},
                "range": {"type": "integer", "required": True, "nullable": False},
                "description": {"type": "string", "required": True, "nullable": False},
                "gps": {"type": "boolean", "required": True, "nullable": False},
                "sensitivityAdjustable": {
                    "type": "boolean",
                    "required": True,
                    "nullable": False,
                },
                "icon_name": {"type": "string", "required": True, "nullable": False},
                "layer_name": {"type": "string", "required": True, "nullable": False},
                "detection_parameters_type": {
                    "type": "string",
                    "required": True,
                    "nullable": False,
                },
            },
        },
    }

    v = Validator(schema)
    valid = v.validate(_in)
    return valid, v.errors
