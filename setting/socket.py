#!/usr/bin/python
# -*- coding: utf-8 -*-

import socketio

from setting import logger

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', async_handlers=True, monitor_clients=True)


@sio.on('connect')
async def connect(sid, environ):
    logger.debug(f"User sid ({sid}) connected.")


@sio.on('disconnect')
async def disconnect(sid):
    logger.debug(f"User sid ({sid}) disconnected.")
