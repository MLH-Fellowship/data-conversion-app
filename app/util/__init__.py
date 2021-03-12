#!/usr/bin/python
# -*- coding: utf-8 -*-

from json import load


class config:
    def __init__(self, fp):
        # type: (str) -> config
        self.data = load(open(fp))
        self.header = self.data['header']
        self.credits = self.data['credits']
