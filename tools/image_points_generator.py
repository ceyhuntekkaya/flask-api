#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import json

from faker import Faker


fake = Faker("tr_TR")

TOTAL_DETECTION_COUNT = 20000

top_lat = 39.556354
bottom_lat = 39.195153
left_lng = 32.595868
right_lng = 33.174155

result = []
for point in range(2000):
    result.append({
        "lab": random.randint(1, 15),
        "lat": random.uniform(bottom_lat, top_lat),
        "lon": random.uniform(left_lng, right_lng)
    })

print(json.dumps(result))
