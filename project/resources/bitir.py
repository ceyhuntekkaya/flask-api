version = config["app"]["software_version"]

# Index


# Auth
app.router.add_post(f"/api/{version}/auth/register", views_auth.register)
app.router.add_post(f"/api/{version}/auth/login", views_auth.login)

# Anomaly
app.router.add_get(f"/api/{version}/anomaly/{{anomaly_id:\d+}}", views_anomaly.get_anomaly)
app.router.add_get(f"/api/{version}/anomaly", views_anomaly.get_anomalies)
app.router.add_post(f"/api/{version}/anomaly", views_anomaly.set_anomaly)
app.router.add_put(f"/api/{version}/anomaly/{{anomaly_id:\d+}}", views_anomaly.put_anomaly)
app.router.add_get(f"/api/{version}/anomaly/counts", views_anomaly.get_anomaly_counts_daily)
app.router.add_post(f"/api/{version}/anomaly/generator", views_anomaly.anomaly_generator)

# Detection
app.router.add_get(f"/api/{version}/detections", views_detection.get_detections)
app.router.add_get(f"/api/{version}/detections/counts", views_detection.get_detections_counts_daily)
app.router.add_get(f"/api/{version}/identification-types", views_detection.get_identification_types)

# Sensors
app.router.add_get(f"/api/{version}/sensors/{{sensor_id:\d+}}", views_sensor.get_sensor)
app.router.add_put(f"/api/{version}/sensors/config/{{sensor_config_id:\d+}}", views_sensor.put_sensor_config)
app.router.add_get(f"/api/{version}/sensors", views_sensor.get_sensors)
app.router.add_post(f"/api/{version}/sensors", views_sensor.set_sensor)
app.router.add_delete(f"/api/{version}/sensors/config/{{sensor_config_id:\d+}}", views_sensor.delete_sensor_config)
app.router.add_get(f"/api/{version}/sensors/config/{{sensor_config_id:\d+}}/image/points",
                   views_sensor.get_sensor_image_points)
app.router.add_put(f"/api/{version}/sensors/config/{{sensor_config_id:\d+}}/approve",
                   views_sensor.approve_sensor_config_image)
app.router.add_put(f"/api/{version}/sensors/config/{{sensor_config_id:\d+}}/image",
                   views_sensor.put_sensor_config_image_and_image_points)
app.router.add_get(f"/api/{version}/sensors/config/images/{{image_id:\d+}}", views_sensor.sensor_images)
app.router.add_post(f"/api/{version}/sensors/config/{{sensor_config_id:\d+}}/images", views_sensor.set_sensor_images)

# Config
app.router.add_get(f"/api/{version}/config", views_config.get_config)
app.router.add_post(f"/api/{version}/config", views_config.set_config)

# System
app.router.add_get(f"/api/{version}/system/status", views_system.get_system_status)
app.router.add_put(f"/api/{version}/system/status", views_system.put_system_status)

# Anomaly Test
app.router.add_post(f"/api/{version}/anomali-test", views_anomalyTest.anomalyTest)

# Messages
app.router.add_post(f"/api/{version}/msg", views_anomaly.send_mesagge)

# DatabaseConnection
app.router.add_post(f"/api/{version}/database-status", views_system.databaseStatus)
app.router.add_post(f"/api/{version}/database-data", views_system.databaseStatusReceive)