#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from os import path

from setting import CustomFormatter
from setting.settings import config

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
