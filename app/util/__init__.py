#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Utility class, this file just contains a config dataclass
with nothing else implemented.

Once again, find the documentation online at
https://mlh-fellowship.github.io/hermes-docs
'''

from app.util.logger import logger
from json import load


class config:
    def __init__(self, fp):
        # type: (str) -> config
        '''
        Creates a config dataclass
        '''
        self.data = load(open(fp))
        for key in self.data:
            if type(self.data[key]) is list:
                self.data[key] = '\n'.join(self.data[key])
            setattr(self, key, self.data[key])


if __name__ == '__main__':
    logger.error('You cannot call this file directly!')
