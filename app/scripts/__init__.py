#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Scripts for import and export, mostly used to prepare the
app for actual usage

Once again, find the documentation online at
https://mlh-fellowship.github.io/hermes-docs
'''

import csv
import glob
from app.util.logger import logger
from csv import DictReader
from json import dump, load
from sys import version_info

if version_info > (3, 5):
    from typing import TextIO, Union, Tuple


BOOLEANS = {'TRUE': True, 'FALSE': False}
CSV_HEADERS = ('FILE', 'TAG')
TABLE_MULTI_HDR = 'MULTI'
TABLE_DATA_HDR = 'DATA'
PRI_HDR = 'PRIORITY'
T_HDR = 'TABLE'


def join_lookup_tables():
    # type: () -> None
    '''
    Joins lookup tables
    '''
    scan_tables = glob.glob("data/s_tables/*.csv")
    for s_table in scan_tables:
        with open("data/table.csv") as table, open(s_table) as s, \
             open("data/c_tables/{}base.csv".format(s_table[-8:-4]), "wt", newline='') as c:

            csv1 = csv.reader(table)
            csv2 = csv.reader(s)

            w = csv.writer(c)
            w.writerows(csv1)
            for i, row in enumerate(csv2):
                if i == 0:
                    continue
                w.writerow(row)
        with open("data/c_tables/{}base.csv".format(s_table[-8:-4])) as s_pointer:
            dump_table(s_pointer, "data/c_tables/{}base.json".format(s_table[-8:-4]))


def load_lookup_table(fp):
    # type: (Union[str, TextIO]) -> dict
    '''Loads a previously dumped lookup table

    :param fp: Lookup table file
    :type fp: string or file pointer
    '''
    if type(fp) is str:
        fp = open(fp)
    return load(fp)


def dump_table(in_fp, out_fp, headers=CSV_HEADERS):
    # type: (Union[str, TextIO], Union[str, TextIO], Tuple[str]) -> dict
    '''Dumps lookup table to a file

    :param in_fp: Input file
    :type in_fp: string or file pointer

    :param out_fp: Output file
    :type out_fp: string or file pointer

    :returns: Data object that was dumped
    :rtype: dict
    '''
    if type(in_fp) is str:
        in_fp = open(in_fp)
    if type(out_fp) is str:
        out_fp = open(out_fp, 'w')
    in_reader = DictReader(in_fp)
    lookup_table = dict()
    for row in in_reader:
        for key in row:
            if row[key] in BOOLEANS:
                row[key] = BOOLEANS[row[key]]
        row[PRI_HDR] = int(row[PRI_HDR])

        if row[T_HDR]:
            row[T_HDR] = int(row[T_HDR])
        else:
            pass
        frame = lookup_table
        for header in headers:
            assert header in row, 'Input file is not a recognized format!'
            if row[header] not in frame:
                frame[row[header]] = dict()
            frame = frame[row[header]]
        if len(frame) > 0:
            if TABLE_MULTI_HDR in frame:
                frame[TABLE_DATA_HDR].append(row)
            else:
                last_row = frame.copy()
                frame.clear()
                frame[TABLE_MULTI_HDR] = True
                frame[TABLE_DATA_HDR] = [last_row, row]
        else:
            frame.update(row)
    dump(lookup_table, out_fp, indent=4, sort_keys=True)
    return lookup_table


if __name__ == '__main__':
    logger.error('You cannot call this file directly!')

