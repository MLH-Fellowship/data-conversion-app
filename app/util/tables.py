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
    from typing import List, Union

# Default number of rows the header will take up if the number
# of rows cannot be detected.
DEF_HDRRW_CNT = 3
# Whether or not +/- is to be appended to the table by default
DEF_PLMN_STAT = False
DATA_HDR = 'DATA'
MULTI_HDR = 'MULTI'
SEC_HDR = 'SECTION'
PRI_HDR = 'PRIORITY'


def detect_header_height(headers, default=DEF_HDRRW_CNT):
    # type: (List[str], int) -> int
    '''
    Automatically detect header height
    '''
    # TODO
    logger.debug('Unable to determine header height for colsize {}, using default {}'.format(
        len(headers), default))
    return default


def determine_max_width(table, column, default=0):
    # type: (List[List[str]], int, int) -> int
    '''
    Determines the minimum width necessary to fill the space. If a default value
    is provided, then the default value is returned when the determined width
    is smaller than the default value, or it cannot be determined.
    '''
    max_value = max([len(v[column]) for v in table])
    return max_value if max_value >= default else default


def determine_max_widths(table, default=0):
    # type: (List[List[str]], int) -> List[int]
    '''
    Determines all max widths
    '''
    if not len(table):
        return list()
    return [determine_max_width(table, i, default) + 2 for i in range(len(table[0]))]


def assemble_lookup_data(table_data, section, priority):
    # type: (Union[dict, List[dict]], str, int) -> List[dict]
    '''
    Assembles some data from the lookup table
    '''
    data = list()
    for azkey in table_data:
        if MULTI_HDR in table_data[azkey]:
            data += assemble_lookup_data(table_data[azkey][DATA_HDR])
        else:
            if table_data[azkey][SEC_HDR] == section and table_data[azkey][PRI_HDR] == priority:
                data.append(table_data[azkey])
    return data


def assemble_relevant_data(ceesim_data, lookup_table, file, section, priority):
    # type: (dict, dict, str, str, int) -> Tuple(OrderedDict, OrderedDict)
    '''
    Finds the relevant data, creating multiple rows if necessary
    '''
    data = OrderedDict()
    headers = OrderedDict()
    # TODO
    for azkey in lookup_table[file]:
        if MULTI_HDR in lookup_table[file][azkey]:
            pass
    return data, headers


def create_empty_table(relevant_data, headers):
    # type: (OrderedDict, OrderedDict) -> List[List[str]]
    '''
    Initializes an empty table
    '''
    return [[str()] * len(headers)] * len(relevant_data)


def populate_table(table, relevant_data, converter):
    # type: (List[List[str]], OrderedDict, function) -> List[List[str]]
    '''
    Assembles a list of list of strings 
    '''
    # TODO
    pass


def build_table(ceesim_data, lookup_table, file, section, priority, converter):
    # type: (dict, dict, str, str, int, function) -> List[str]
    '''
    Builds the table and returns all rows
    '''
    data, headers = assemble_relevant_data(
        ceesim_data, lookup_table, section, priority)
    table = populate_table(create_empty_table(data, headers), data, converter)
    widths = determine_max_widths(table)
    # TODO: Insert +/- if necessary
    # NOTE: The following list is built with list comprehension. For the sake
    # of code readability it is advised to expand this eventually and it makes
    # the most sense to expand this when the above TODO is added.
    output_table = [''.join([item.center(widths[idx])
                             for idx, item in enumerate(row)]) for row in table]
    return output_table


def build_table_str(**kwargs):
    # type: (dict) -> str
    '''
    Builds the table and returns as a string
    '''
    return '\n'.join(build_table(**kwargs))
