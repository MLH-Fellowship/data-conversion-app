#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Tables handler. Creates tables according to the spec. Because this file
is imported by app.converter, you avoid multiple dependency or circular
imports by passing in the converter function convert_one_key to the
build_table function, which then gets passed to populate_table. This
follows the adage of Don't Repeat Yourself.

Once again, find the documentation online at
https://mlh-fellowship.github.io/hermes-docs
'''

from app.util.logger import logger
# NOTE: OrderedDict is not necessary if Python 2 support is dropped, as in
# later versions of Python, dictionaries now remember insertion order.
from collections import OrderedDict
from sys import version_info
from copy import copy

if version_info > (3, 5):
    from typing import List, Union, Callable as function, Tuple

# Default number of rows the header will take up if the number
# of rows cannot be detected.
DEF_HDRRW_CNT = 2
# Whether or not +/- is to be appended to the table by default
DEF_PLMN_STAT = False
DATA_HDR = 'DATA'
MULTI_HDR = 'MULTI'
SEC_HDR = 'SECTION'
PRI_HDR = 'PRIORITY'
LBL_HDR = 'LABEL'
TBL_HDR = 'TABLE'


def split_header_auto(table, default=DEF_HDRRW_CNT):
    # type: (List[List[str]], int) -> Tuple[List[List[str]], int]
    '''
    Automatically detect header height

    Parameters:
     * `table`: (list of list of strings) 2D matrix used to create the table
     * `default`: (int) default number of header rows
    
    **Returns**: (tuple of list of list of strings and integer) Formatted table and number of header rows
    '''
    # TODO
    logger.debug('Unable to determine header height, using default {}'.format(default))
    if len(table) < 1:
        logger.warn('Table was empty, nothing to do in app.util.tables.split_header_auto')
        return table, 0
    headers = [s.rsplit(' ', 1) for s in table[0]]
    headers_n = [[h[0] for h in headers], [h[1] if len(h) > 1 else str() for h in headers]]
    if len(table) < 2:
        logger.warn('Table data was empty, but headers were rearranged')
        return headers_n, len(headers_n)
    return headers_n + table[1:], len(headers_n)


def determine_max_width(table, column, default=0):
    # type: (List[List[str]], int, int) -> int
    '''
    Determines the minimum width necessary to fill the space. If a default value
    is provided, then the default value is returned when the determined width
    is smaller than the default value, or it cannot be determined.

    Parameters:
     * `table`: (list of list of strings) 2D matrix used to create the table
     * `column`: (integer) Column to determine the width
     * `default`: (integer) Default width length
    
    **Returns**: (integer) width length
    '''
    max_value = max([len(v[column]) for v in table])
    return max_value if max_value >= default else default


def determine_max_widths(table, default=0):
    # type: (List[List[str]], int) -> List[int]
    '''
    Determines all max widths

    Parameters:
     * `table`: (list of list of strings) 2D matrix of table to fill
     * `default`: (integer) Default table width
    
    **Returns**: (list of ints) All max widths by column
    '''
    if not len(table):
        return list()
    return [determine_max_width(table, i, default) + 2 for i in range(len(table[0]))]


def assemble_lookup_data(table_data, section, priority):
    # type: (Union[dict, List[dict]], str, int) -> List[dict]
    '''
    Assembles some data from the lookup table

    Parameters:
     * `table_data`: (dictionaries) List of lookups from lookup table
     * `section`: (string) Section name to check
     * `priority`: (integer) Section priority to check
    
    **Returns**: (list of dictionaries) Lookup table list
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

    Parameters:
     * `ceesim_data`: (dictionary) CEESIM JSON imported data
     * `lookup_table`: (dictionary) Lookup table JSON imported
     * `file`: (string) File type as ANT, SCAN, etc
     * `section`: (string) Section header as in ModeName, etc
     * `priority*: (integer) Priority from the lookup table
     * `obtainer`: (function) Obtainer that obtains values from converter
    
    **Returns**: (tuple of list of list of strings and list of dictionaries),
    the return data is the new table as well as all headers in a list format
    '''
    headers = assemble_lookup_data(lookup_table[file], section, priority)
    cols = []
    for hdr in headers:
        if hdr["TAG"]:
            values = []
            for tag in hdr["TAG"].split('&'):
                tags = obtainer(ceesim_data, None, tag, fast=False)
                values.append(tags)
            cols.append(list(zip(*values))[0])
        else:
            cols.append((hdr["DEFAULT"],))
    len3 = len(max(cols, key=lambda i: len(i) if type(i) is list else 0))
    for i, row in enumerate(cols):
        if type(row) is not list:
            cols[i] = [row] * len3
    data = [list(row) for row in zip(*cols)]

    if file == "SCAN" and headers[0]["LABEL"] == "SWEEP BLANK":
        levels = int(data[0][-1])
        inc_data = data * levels
        inc_data_list = []
        for level in range(levels):
            row = inc_data[level]
            row[-1] = str(level + 1)
            if level % 2 == 0:
                row[-4] = "UP-RIGHT"
            else:
                row[-4] = "DOWN-LEFT"
            inc_data_list.append(copy(inc_data[level]))

        data = inc_data_list

    return data, headers


def create_empty_table(relevant_data, headers):
    # type: (List[List[str]], OrderedDict) -> List[List[str]]
    '''
    Initializes an empty table
    '''
    return [[str()] * len(headers)] * len(relevant_data)


def dedupe_rows(table):
    # type(List[List[str]]) -> List[List[str]]
    '''
    Dedupes rows
    '''
    rows = set()
    for row in range(len(table) - 1, 1, -1):
        if tuple(table[row]) in rows:
            del table[row]
        else:
            rows.add(tuple(table[row]))
    return table


def populate_table(table, relevant_data, headers, converter):
    # type: (List[List[str]], List[List[str]], List[dict], function) -> List[List[str]]
    '''
    Assembles a list of list of strings 
    '''

    if len(table) > 0:
        table[0] = [hdr[LBL_HDR] for hdr in headers]
        table[1:] = [[converter(hdr, relevant_data[row - 1][idx], keep_tag=False)
                      for idx, hdr in enumerate(headers)] for row in range(1, len(table) + 1)]
    return dedupe_rows(table)


def sort_table(table, headers):
    # type: (List[List[str]], List[dict]) -> List[List[str]]
    '''
    Sorts table columns
    '''
    table_t = [list(row) for row in zip(*table)]
    row_idx = [hdr[TBL_HDR] for hdr in headers]
    table_t = [row for _, row in sorted(zip(row_idx, table_t))]
    table = [list(row) for row in zip(*table_t)]
    return table


def build_table(ceesim_data, lookup_table, file, section, priority, converter, obtainer, add_sign=False):
    # type: (dict, dict, str, str, int, function, function, bool) -> List[str]
    '''
    Builds the table and returns all rows

    converter: function -- convert_one_key
    obtainer: function -- obtain_relevant_tags
    '''
    data, headers = assemble_relevant_data(
        ceesim_data, lookup_table, file, section, priority, obtainer)
    table = populate_table(create_empty_table(
        data, headers), data, headers, converter)
    table = sort_table(table, headers)
    widths = determine_max_widths(table)
    table, size = split_header_auto(table)
    if add_sign:
        widths.insert(0, 3)
        for i in range(size):
            table[i].insert(0, str())
        for i in range(size, len(table)):
            table[i].insert(0, '+/-')
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


if __name__ == '__main__':
    logger.error('You cannot call this file directly!')
