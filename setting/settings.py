#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlalchemy.dialects.postgresql import asyncpg

from project.models.log.log import LogModel
import os
import pathlib
import yaml
import logging
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from setting import CustomFormatter

from project.resources.sql_init import get_database_sql_file_commands
from project.socket.socket import sio
from .middlewares import setup_middlewares
from .settings import config
from tools.anomaly_generator import generate_path_anomaly
from tools.detections_generator import generate_path_detection

BASE_DIR = pathlib.Path(__file__).parent.parent
config_file = os.getenv("CONF", "polls.stage.yaml")
config_path = BASE_DIR / "app" / "config" / config_file



#APP_PATH = path.dirname(__file__)
#VERSION = config["app"]["version"]
#TEST = config["app"]["test"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.getLogger("sqlalchemy.engine").setLevel(
    logging.INFO if config["app"]["test"] else logging.WARNING
)
logger.propagate = 0
fmt = "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(funcName)s() | -%(message)s"
stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(CustomFormatter(fmt))
logger.addHandler(stdout_handler)




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


async def init_asyncpg(app):
    conf = app["config"]["postgres"]
    app["pool"] = await asyncpg.create_pool(**conf)

    yield

    app["pool"].terminate()
    await app["pool"].close()


async def init_sqlalchemy(app):
    conf = app["config"]["postgres"]
    app["engine"] = create_async_engine(
        f"postgresql+asyncpg://{conf['user']}:{conf['password']}@{conf['host']}:{conf['port']}/{conf['database']}",
        echo=True,
    )
    app["session"] = sessionmaker(
        app["engine"], expire_on_commit=False, class_=AsyncSession
    )

    try:
        await generate_path_anomaly(app)
    except Exception as e:
        logger.error(f"Anomaly generation is not ready yet. Error: {e}")

    try:
        await generate_path_detection(app)
    except Exception as e:
        pass #logger.error(f"Detection generation is not ready yet. Error: {e}")

    try:
        from project.models.base_model import Base
        async with app["engine"].begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        pass #logger.info("Database tables created.")
    except Exception as e:
        pass #logger.error(f"Database tables does not created. Error: {e}")

    try:
        async with app["session"]() as session:
            async with session.begin():
                commands = await get_database_sql_file_commands()
                for command in commands:
                    await session.execute(command)
    except Exception as e:
        pass #logger.error(f"Database commands does not created. Error: {e}")

    yield

    await app["engine"].dispose()
