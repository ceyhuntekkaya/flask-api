#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from datetime import datetime

from faker import Faker

from resources.database import orm_session_add
from resources.database.models import Detection

fake = Faker("tr_TR")

TOTAL_DETECTION_COUNT = 20

top_lat = 39.556354
bottom_lat = 39.195153
left_lng = 32.595868
right_lng = 33.174155
static_elevation = 1059.0


async def generate_single_detection(app, lat, lng, unique_id):
    data = {
        "detectionstarttime": unique_id,
        "detectionlat": lat,
        "detectionlon": lng,
    }

    await orm_session_add(app, Detection(**data))


async def generate_path_detection(app):
    path_count = random.randint(1, 10)

    for i in range(TOTAL_DETECTION_COUNT):

        lat = random.uniform(bottom_lat, top_lat)
        lng = random.uniform(left_lng, right_lng)
        starts_at = fake.date_between(
            start_date=datetime(year=2022, month=11, day=1), end_date="today"
        )
        starts_at = datetime.fromordinal(starts_at.toordinal()).replace(
            hour=random.randint(0, 23), minute=random.randint(0, 59)
        )
        unique_id = starts_at

        for path in range(path_count):
            # Create first detection. Loop  for next.
            await generate_single_detection(app, lat, lng, unique_id)

            # Next point of detection values.
            lat += random.uniform(0.01, 0.03)
            lng += random.uniform(0.004, 0.008)
