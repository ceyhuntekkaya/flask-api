#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from datetime import datetime, timedelta, date

import bcrypt
import jwt
import psycopg2
import requests
from psycopg2.extras import RealDictCursor

from setting import log_setting
from .settings import config
from project.socket.socket import sio

conf = config["auth"]


async def generate_token(user_id, role="user", refresh_token=False):

    if refresh_token:
        secret = conf["REFRESH_JWT_SECRET"]
        algorithm = conf["REFRESH_JWT_ALGORITHM"]
        delta = timedelta(seconds=conf["REFRESH_JWT_EXP_DELTA_SECONDS"])
    else:
        secret = conf["JWT_SECRET"]
        algorithm = conf["JWT_ALGORITHM"]
        delta = timedelta(seconds=conf["JWT_EXP_DELTA_SECONDS"])

    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.utcnow() + delta,
    }

    return jwt.encode(payload, secret, algorithm)


async def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password.encode(), bcrypt.gensalt()).decode()


async def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    try:
        return bcrypt.checkpw(plain_text_password.encode(), hashed_password.encode())
    except ValueError:
        return False


def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


async def send_event_to_ai(event_type, data):
    data = {
        "event_type": event_type,
        "data": data
    }
    data = json.loads(json.dumps(data, default=json_serial))

    try:
        r = await requests.post(f"{config['ai']['ip_address']}/ai/v1/events", json=data)
        logger.info(f"AI request completed. Status code: {r.status_code}, Response: {r.json()}")
    except Exception as e:
        logger.error(e)


async def send_test_to_ai(data):
    data = json.loads(json.dumps(data, default=json_serial))

    try:
        r = await requests.post(f"{config['ai']['ip_address']}/ai/v1/events/test", json=data)
        # logger.info(f"AI request completed. Status code: {r.status_code}, Response: {r.json()}")

        # AI'den gelen yanıtı döndür
        response_data = r.json()
        if response_data is not None:
            return str(response_data)
        else:
            return "err"
    except Exception as e:
        logger.error(e)
        return "Ai ile iletişim kurulamadı."


async def send_database_status():
    try:
        response = await requests.post(f"{config['ai']['ip_address']}/ai/v1/events/database-status", json="")
        r = response.json()

        print("AI request completed.")
        return "OK"
    except Exception as e:
        print("error")
        return "AI ile iletişim kurulamadı."


async def send_database_data(request):
    try:
        data = await request.json()
        table_statuses = data
        print("tables")
        print(table_statuses)
        await sio.emit('database_status', table_statuses)

        return "OK"
    except Exception as e:
        return "Err"


async def initialize_sensor_config_numbers():
    mirsad_conn = psycopg2.connect(
        host=config["mirsad_postgres"]["host"],
        port=config["mirsad_postgres"]["port"],
        user=config["mirsad_postgres"]["user"],
        password=config["mirsad_postgres"]["password"],
        database=config["mirsad_postgres"]["database"]
    )
    conn = psycopg2.connect(
        host=config["postgres"]["host"],
        port=config["postgres"]["port"],
        user=config["postgres"]["user"],
        password=config["postgres"]["password"],
        database=config["postgres"]["database"]
    )

    mirsad_conn.autocommit = True
    conn.autocommit = True
    mirsad_cur = mirsad_conn.cursor(cursor_factory=RealDictCursor)
    cur = mirsad_conn.cursor(cursor_factory=RealDictCursor)

    query = """ SELECT ? FROM ?; """
    mirsad_cur.execute(query)
    result = mirsad_cur.fetchall()

    query = """ INSERT INTO ? (?) VALUES (?); """
    cur.execute(query)

    mirsad_cur.close()
    mirsad_conn.close()

