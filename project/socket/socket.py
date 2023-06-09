from project.socket.response import Response

import socketio
from sqlalchemy import func, select, or_
from setting.settings import logger
import json
from project.socket.database import async_fetch, orm_fetch, orm_session_add
from project.models.detection.anomaly import AnomalyModel as Anomaly
from datetime import datetime, timedelta, date


resp = Response()

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', async_handlers=True, monitor_clients=True)


@sio.on('connect')
async def connect(sid, environ):
    logger.debug(f"User sid ({sid}) connected.")


@sio.on('disconnect')
async def disconnect(sid):
    logger.debug(f"User sid ({sid}) disconnected.")


async def send_message(request):
    msg = await request.text()  # JSON metnini string olarak alın
    data = json.loads(msg)  # JSON metnini Python nesnesine dönüştürün
    message = data.get('data')  # "data" alanındaki mesajı alın

    # WebSocket üzerinden istek gönderme
    await sio.emit('msg', {'data': message})

    return resp.success()

@validator(validate_set_anomaly)
async def set_anomaly(request):
    _input = await request.json()

    unique_id = _input["unique_id"]
    query = select(Anomaly).where(Anomaly.unique_id == unique_id, or_(Anomaly.is_approved == 0, Anomaly.is_approved == 1))
    anomaly = await orm_fetch(request.app, query, return_type="record", fetch_one=True)

    if anomaly:
        _input["is_approved"] = anomaly.is_approved
    else:
        _input["is_approved"] = -1

    _input["created_at"] = datetime.now()
    await orm_session_add(request.app, Anomaly(**_input))
    logger.info(f"Anomaly created. Data: {_input}")

    _input["created_at"] = datetime.now().__format__('YYYY-MM-DD"T"HH24:MI:SS"Z"')
    await sio.emit('anomaly', {'data': _input})

    return resp.success()



