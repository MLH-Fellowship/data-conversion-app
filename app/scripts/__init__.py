#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv import DictReader
from json import dump, load
from sys import version_info

if version_info > (3, 5):
    from typing import TextIO, Union


CSV_HEADERS = ('TAG', 'FILE')


def load_lookup_table(fp):
    # type: (Union[str, TextIO]) -> dict
    '''Loads a previously dumped lookup table

    :param fp: Lookup table file
    :type fp: string or file pointer
    '''
    if type(fp) is str:
        fp = open(fp)
    return load(fp)


def dump_lookup_table(in_fp, out_fp):
    # type: (Union[str, TextIO], Union[str, TextIO]) -> dict
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
        frame = lookup_table
        for header in CSV_HEADERS:
            assert header in row, 'Input file is not a recognized format!'
            if row[header] not in frame:
                frame[row[header]] = dict()
                frame = frame[row[header]]
    dump(lookup_table, out_fp)
    return lookup_table


if __name__ == '__main__':
    pass
