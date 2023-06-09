#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import jwt
from aiohttp import web
from aiohttp.web_middlewares import middleware
from jwt import ExpiredSignatureError

from setting import log_setting
from project.socket.database import async_fetch
from project.socket.response import Response
from settings import config
from setting.settings import log_db

resp = Response()
conf = config["auth"]


async def handle_404(request):
    host = request.remote
    logging.warning(host)
    return resp.not_found(message="The requested URL is not found.")


async def handle_500(request):
    host = request.remote
    logging.warning(host)
    return resp.error(message="Internal server error.")


def create_error_middleware(overrides):
    @web.middleware
    async def error_middleware(request, handler):
        try:
            response = await handler(request)
            override = overrides.get(response.status)
            if override:
                return await override(request)
            return response
        except web.HTTPException as ex:
            override = overrides.get(ex.status)
            if override:
                return await override(request)
            raise

    return error_middleware


def login_required(func):
    def wrapper(request):
        if not request.user:
            message = "Auth required. Proper authorization is not provided."
            return resp.unauthorized(message=message)
        return func(request)

    return wrapper


@middleware
async def auth_middleware(request, handler):
    request.user = None
    access_token = request.headers.get("Authorization", None)
    if access_token is not None:
        try:
            access_token = access_token.replace("Bearer ", "")
            payload = jwt.decode(
                access_token, conf["JWT_SECRET"], algorithms=conf["JWT_ALGORITHM"]
            )
            # {'user_id': 1, 'role': 'user', 'exp': 1654084729}

            sql = "SELECT * FROM aselsan_users WHERE id = $1;"
            user = await async_fetch(
                request.app, sql, payload["user_id"], fetch_one=True, return_type=None
            )
            request.user = user

        except jwt.DecodeError:
            return resp.unauthorized(message="JWT Token is invalid.")

        except (
                jwt.ExpiredSignatureError,
                jwt.exceptions.ExpiredSignatureError,
                ExpiredSignatureError,
        ):
            return resp.unauthorized(message="JWT Token is expired.")

        except jwt.InvalidTokenError:
            return resp.unauthorized(message="JWT Token is invalid.")

        logging.debug(
            f"User ID: {request.user} | IP Address: {request.remote} | URL: {request.url}"
        )

    return await handler(request)


@middleware
async def add_log_db(request, handler):
    if request.method == "POST" or request.method == "PUT" or request == "DELETE":
        try:
            _in = await request.json()
            await log_db(request, request.rel_url, _in, request.user['id'])
        except Exception as e:
            logger.error(f"Log error: {e}")
    elif request.method == "GET":
        try:
            _in = dict(request.rel_url.query)
            await log_db(request, request.rel_url, _in, request.user['id'])
        except Exception as e:
            logger.error(f"Log error: {e}")

    return await handler(request)


def setup_middlewares(app):
    # error_middleware = create_error_middleware({404: handle_404, 500: handle_500})
    app.middlewares.append(auth_middleware)
    app.middlewares.append(add_log_db)
    # app.middlewares.append(error_middleware)
