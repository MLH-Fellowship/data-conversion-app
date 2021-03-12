#!/usr/bin/python
# -*- coding: utf-8 -*-

from json import load


class config:
    def __init__(self, fp):
        # type: (str) -> config
        self.data = load(open(fp))
        for key in self.data:
            if type(self.data[key]) is list:
                self.data[key] = '\n'.join(self.data[key])
            setattr(self, key, self.data[key])
