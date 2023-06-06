#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pathlib

import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_file = os.getenv("CONF", "polls.stage.yaml")
config_path = BASE_DIR / "app" / "config" / config_file


def get_config(path):
    """

    :param path: Configuration file path.
    :return: Returns configuration file.

    """
    with open(path) as f:
        _config = yaml.load(f, Loader=yaml.FullLoader)
    return _config


config = get_config(config_path)
