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
LBL_HDR = 'LABEL'


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
        if type(azkey) == dict:
            if azkey[SEC_HDR] == section and azkey[PRI_HDR] == priority:
                data.append(azkey)
        elif MULTI_HDR in table_data[azkey]:
            data += assemble_lookup_data(table_data[azkey][DATA_HDR], section, priority)
        else:
            if table_data[azkey][SEC_HDR] == section and table_data[azkey][PRI_HDR] == priority:
                data.append(table_data[azkey])
    return data


def assemble_relevant_data(ceesim_data, lookup_table, file, section, priority, obtainer):
    # type: (dict, dict, str, str, int, function) -> Tuple(List[List[str]], List[dict])
    '''
    Finds the relevant data, creating multiple rows if necessary
    '''
    # TODO: Order the headers properly. This is caused by the fact that we
    # do not actually keep track of header order anywhere in code or in
    # the lookup table, so we currently do not have this information. Thus,
    # the data is assembled in the order it is recived from the function,
    # of which the behavior is undefined.
    headers = assemble_lookup_data(lookup_table[file], section, priority)
    cols = [obtainer(ceesim_data, None, hdr["TAG"], fast=False)
            if hdr["TAG"] else hdr["DEFAULT"]
            for hdr in headers]
    mx_lst_lngth = 0
    for element in cols:
        if type(element) is list and len(element) > mx_lst_lngth:
            mx_lst_lngth = len(element)
    # cols = [[col] for col in cols if type(col) != list]
    # for i, element in enumerate(cols):
    #     while type(element) is list and len(element) < mx_lst_lngth:
    #           cols[i].append(cols[i][0])

    data = [list(row) for row in zip(*cols)]
    # logger.debug(cols)
    # logger.debug(data)
    return data, headers


def create_empty_table(relevant_data, headers):
    # type: (List[List[str]], OrderedDict) -> List[List[str]]
    '''
    Initializes an empty table
    '''
    return [[str()] * len(headers)] * len(relevant_data)


def populate_table(table, relevant_data, headers, converter):
    # type: (List[List[str]], List[List[str]], List[dict], function) -> List[List[str]]
    '''
    Assembles a list of list of strings 
    '''
    # TODO: Split headers into multiple rows if necessary
    table[0] = [hdr[LBL_HDR] for hdr in headers]
    table[1:] = [[converter(hdr, relevant_data[row - 1][idx])
                  for idx, hdr in enumerate(headers)] for row in range(1, len(table))]
    return table


def build_table(ceesim_data, lookup_table, file, section, priority, converter, obtainer):
    # type: (dict, dict, str, str, int, function, function) -> List[str]
    '''
    Builds the table and returns all rows

    converter: function -- convert_one_key
    obtainer: function -- obtain_relevant_tags
    '''
    data, headers = assemble_relevant_data(
        ceesim_data, lookup_table, file, section, priority, obtainer)
    table = populate_table(create_empty_table(
        data, headers), data, headers, converter)
    widths = determine_max_widths(table)
    # TODO: Insert +/- if necessary
    # NOTE: The following list is built with list comprehension. For the sake
    # of code readability it is advised to expand this eventually and it makes
    # the most sense to expand this when the above TODO is added.
    output_table = [''.join([item.center(widths[idx])
                             for idx, item in enumerate(row)]) for row in table]
    return output_table


def build_table_str(*args):
    # type: (dict) -> str
    '''
    Builds the table and returns as a string
    '''
    return '\n'.join(build_table(*args))
