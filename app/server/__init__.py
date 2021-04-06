#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Unimplemented web server

Once again, find the documentation online at
https://mlh-fellowship.github.io/hermes-docs
'''

from app.util.logger import logger
from flask import Flask

server = Flask(__name__)


if __name__ == '__main__':
    logger.error('You cannot call this file directly!')
