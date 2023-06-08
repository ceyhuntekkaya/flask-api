#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

from aiohttp import web


class Response:

    @staticmethod
    def custom(message="OK", status_code=200, data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=status_code, dumps=json.dumps)

    @staticmethod
    def plain_text(message="Hello Ulive!"):
        return web.Response(text=message, status=200, content_type="text/plain")

    @staticmethod
    def success(message="OK", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=200, dumps=json.dumps)

    @staticmethod
    def success_space():
        return web.json_response(status=200)

    @staticmethod
    def created(message="Created", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=201)

    @staticmethod
    def no_content(message="No Content", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=204)

    @staticmethod
    def not_modified(message="Not Modified", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=304)

    @staticmethod
    def bad_request(message="Bad Request", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=400)

    @staticmethod
    def invalid_input(message="Invalid Input", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=422)

    @staticmethod
    def not_acceptable(message="Not Acceptable", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=406)

    @staticmethod
    def already_exists(message="Already Exists", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=409)

    @staticmethod
    def too_many_requests(message="Too Many Requests", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=429)

    @staticmethod
    def unauthorized(message="Unauthorized", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=401)

    @staticmethod
    def forbidden(message="Forbidden", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=403)

    @staticmethod
    def payment_required(message="Payment Required", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=402)

    @staticmethod
    def not_found(message="Not Found", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=404)

    @staticmethod
    def error(message="Server Error", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=500)

    @staticmethod
    def not_implemented(message="Not Implemented", data=None):
        response = {
            "message": message,
            "data": data,
        }
        return web.json_response(data=response, status=501)

    @staticmethod
    def html(data):
        return web.json_response(text=data, content_type="text/html")

    @staticmethod
    def file(data, content_type='application/pdf'):
        return web.Response(body=data, content_type=content_type)
