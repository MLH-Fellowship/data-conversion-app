#!/usr/bin/python
# -*- coding: utf-8 -*-


'''
Main errors class, with nothing else implemented

Once again, find the documentation online at
https://mlh-fellowship.github.io/hermes-docs
'''

from app.util.logger import logger

class DatastoreError(Exception):
    pass

if __name__ == '__main__':
    logger.error('You cannot call this file directly!')
