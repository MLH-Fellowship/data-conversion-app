#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import a2pats, ceesim
from app.converter import convert_to_a2pats
from app.exporter import dump_a2pats
from app.importer import import_
from app.scripts import load_lookup_table, dump_lookup_table
from app.util import config as config_
from app.util.logger import logger, set_up_logger
from argparse import ArgumentParser
from logging import DEBUG, INFO, ERROR, CRITICAL
from os.path import isfile
from sys import argv


DEFAULT_UNPARSED_TABLE_PATH = 'data/table.csv'
DEFAULT_TABLE_PATH = 'data/table.json'


def prepare_lookup_table(unparsed=DEFAULT_UNPARSED_TABLE_PATH, parsed=DEFAULT_TABLE_PATH):
    # type: (str, str) -> dict
    '''Prepares a lookup table
    '''
    if isfile(parsed):
        return load_lookup_table(parsed)
    else:
        if isfile(unparsed):
            return dump_lookup_table(unparsed, parsed)
        else:
            return dict()


def print_lookup_table(file):
    # type: (str) -> None
    '''Prints stats about the lookup table
    '''
    data = dump_lookup_table(file, DEFAULT_TABLE_PATH)
    logger.info(
        'Table has {} keys and was successfully dumped'.format(len(data)))


def convert(input_file, output_file):
    # type: (str, str) -> a2pats
    '''Load CEESIM file and convert to A²PATS

    :param input_file: Location of file to import
    :type input_file: str

    :param output_file: Location of file to export (does not have to exist)
    :type output_file: str

    :returns: A²PATS object (if successful)
    :rtype: a2pats
    '''
    logger.debug(
        'Main app converter called, using provided input and output files')
    lookup_table = prepare_lookup_table()
    input_data = import_(input_file, ceesim)  # -> CEESIM object
    output_data = convert_to_a2pats(input_data, lookup_table)
    success = dump_a2pats(output_data, output_file)
    if success:
        return output_data
    else:
        logger.error('File failed to export!')
        return None


def parse_arguments(epilog):
    # type: (str) -> None
    '''Parse arguments
    '''
    parser = ArgumentParser(add_help=False)
    parser.add_argument('-i', '--input', help='Input file to convert')
    parser.add_argument('-o', '--output', help='Output file after conversion')
    parser.add_argument('-t', '--table', help='Dump a lookup table and exit')
    parser.add_argument('-w', '--server', action='store_true',
                        help='Start the app in server mode')
    parser.add_argument('-v', '--verbose', action='count',
                        help='Enable verbose mode, overrides -s')
    parser.add_argument('-s', '--suppress', action='count',
                        help='Supress logging, -ss to completely silence')
    parser.add_argument('-h', '--help', action='store_true',
                        help='Show this help message and exit')
    if len(argv) == 1:
        parser.print_help()
        exit(2)
    args = parser.parse_args()
    if args.help:
        parser.print_help()
        print(epilog)
        exit()
    if args.verbose:
        set_up_logger(DEBUG)
    elif args.suppress:
        if args.suppress > 1:
            set_up_logger(CRITICAL)
        else:
            set_up_logger(ERROR)
    else:
        set_up_logger(INFO)
    if args.table:
        print_lookup_table(args.table)
    if args.server:
        from app.server import server
        server.run()
    if args.input and args.output:
        convert(args.input, args.output)


if __name__ == '__main__':
    config = config_('data/config.json')
    print(config.header)
    print(config.credits)
    parse_arguments(config.help)
