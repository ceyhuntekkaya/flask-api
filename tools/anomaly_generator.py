#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import uuid
from datetime import datetime, timedelta

from faker import Faker

from project.resources.database import orm_session_add
from project.models.data.anomaly import Anomaly

from setting.socket import sio

fake = Faker("tr_TR")

top_lat = 39.556354
bottom_lat = 39.195153
left_lng = 32.595868
right_lng = 33.174155
static_elevation = 1059.0


async def generate_single_anomaly(app, lat, lng, created_at, unique_id):
    data = {
        "anomaly_type": "Normal",
        "class_name": "Example Class",
        "confidence": random.randint(70, 100),
        "description": fake.text(),
        "editable_description": fake.text(),
        "lat": lat,
        "lon": lng,
        "elevation": static_elevation,
        "sensor_id": random.randint(1, 5),
        "unit_id": random.randint(1, 20),
        "camera_id": str(f"camera-{random.randint(1, 10)}"),
        "nvr_ip": fake.ipv4(),
        "detector_name": fake.bothify(text="Detector ????-####"),
        "created_at": created_at,
        "unique_id": unique_id,
    }

    await orm_session_add(app, Anomaly(**data))

    # Date is string for socket.
    data['created_at'] = str(data['created_at'])
    await sio.emit('anomaly', {'data': data})


async def generate_path_anomaly(app, total_anomaly_count=20, anomaly_subcount=10, dt=None):
    path_count = random.randint(1, anomaly_subcount)

    for i in range(total_anomaly_count):

        lat = random.uniform(bottom_lat, top_lat)
        lng = random.uniform(left_lng, right_lng)

        if dt:
            created_at = datetime.now() - timedelta(seconds=5)
        else:
            created_at = fake.date_between(
                start_date=datetime(year=2023, month=1, day=20), end_date="today"
            )
            created_at = datetime.fromordinal(created_at.toordinal()).replace(
                hour=random.randint(0, 23), minute=random.randint(0, 59)
            )

        unique_id = str(uuid.uuid4())

        for path in range(path_count):
            # Create first anomaly. Loop  for next.
            await generate_single_anomaly(app, lat, lng, created_at, unique_id)

            # Next point of anomaly values.
            lat += random.uniform(0.01, 0.03)
            lng += random.uniform(0.004, 0.008)
            created_at += timedelta(minutes=random.randint(1, 5))
