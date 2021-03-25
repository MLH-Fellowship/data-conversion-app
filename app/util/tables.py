#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Tables handler. Creates tables according to the spec. Because this file
is imported by app.converter, you avoid multiple dependency or circular
imports by passing in the converter function convert_one_key to the
build_table function, which then gets passed to populate_table. This
follows the adage of Don't Repeat Yourself.

Author: Gideon Tong
'''

from app.util.logger import logger
# NOTE: OrderedDict is not necessary if Python 2 support is dropped, as in
# later versions of Python, dictionaries now remember insertion order. 
from collections import OrderedDict
from sys import version_info

if version_info > (3, 5):
    from typing import List

# Default number of rows the header will take up if the number
# of rows cannot be detected.
DEF_HDRRW_CNT = 3
# Whether or not +/- is to be appended to the table by default
DEF_PLMN_STAT = False


def detect_header_height(headers, default=DEF_HDRRW_CNT):
    # type: (List[str], int) -> int
    '''
    Automatically detect header height
    '''
    # TODO
    logger.debug('Unable to determine header height for colsize {}, using default {}'.format(
        len(headers), default))
    return default


def assemble_relevant_data(ceesim_data, lookup_table, section, priority):
    # type: (dict, dict, str, int) -> OrderedDict
    '''
    Finds the relevant data, creating multiple rows if necessary
    '''
    data = OrderedDict()
    return data


def populate_table(relevant_data, converter):
    # type: (OrderedDict, function) -> List[List[str]]
    '''
    Assembles a list of list of strings 
    '''
    pass


def build_table(ceesim_data, lookup_table, section, priority, converter):
    # type: (dict, dict, str, int, function) -> List
    '''
    Builds the table and returns all rows
    '''
    # TODO
    return list()


def build_table_str(**kwargs):
    # type: (dict) -> str
    '''
    Builds the table and returns as a string
    '''
    return '\n'.join(build_table(**kwargs))
