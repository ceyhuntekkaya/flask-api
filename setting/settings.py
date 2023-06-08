#!/usr/bin/python
# -*- coding: utf-8 -*-

from project.models.log.log import LogModel
import os
import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_file = os.getenv("CONF", "polls.stage.yaml")
config_path = BASE_DIR / "app" / "config" / config_file


def get_config(path):
    with open(path) as f:
        _config = yaml.load(f, Loader=yaml.FullLoader)
    return _config


config = get_config(config_path)


async def orm_session_add(app, obj):
    # Add to session and insert.
    async with app["session"]() as session:
        async with session.begin():
            if isinstance(obj, list):
                session.add_all(obj)
            else:
                session.add_all([obj])


async def log_db(request, key, value, user_id):
    await orm_session_add(request.app, LogModel(key=key, log=value, user_id=user_id))
