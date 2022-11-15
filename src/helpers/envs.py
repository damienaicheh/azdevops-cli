#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

def get_env(name: str) -> str:
    """get Azure DevOps environment variable from the current shell session"""
    key = name.upper().replace('.', '_')
    val = os.getenv(key)
    # logger.debug(f'get_env : {name} ( {key} ) = {val}')
    return val