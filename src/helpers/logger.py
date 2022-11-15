#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.client import HTTPConnection
import logging
from logging import Logger

def create_logger(verbose: bool) -> Logger:
    logger = logging.getLogger('azdev-cli')
    logger.setLevel(logging.INFO)
    formatter = None
    level = logging.DEBUG if verbose else logging.INFO
    logging.getLogger('azdev-cli').setLevel(level)
    if level == logging.DEBUG:
        HTTPConnection.debuglevel = 1
        formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s :  %(message)s')
    else:
        formatter = logging.Formatter('%(name)s : %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger