#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Entrypoint of the program. Run `python app.py -h` for help.
See the web version of this documentation at https://mlh-fellowship.github.io/hermes-docs/

Documentation for the program entrypoint is not available on the website.
'''

from app import a2pats, ceesim
from app.converter import convert_to_a2pats, split_emitter_modes, determine_scan_type, scan_file_name
from app.exporter import dump_a2pats
from app.importer import import_
from app.scripts import join_lookup_tables, dump_table
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
    '''
    Prepares a lookup table

    Parameters:
     * `unparsed`: (string) Unprased CSV table path
     * `parsed`: (string) Parsed JSON output path
    
    **Returns**: JSON lookup table as dictionary
    '''
    if isfile(parsed):
        return join_lookup_tables()
    else:
        if isfile(unparsed):
            return dump_table(unparsed, parsed)
        else:
            return dict()


def print_lookup_table(file):
    # type: (str) -> None
    '''
    Prints stats about the lookup table

    Parameters:
     * `file`: (string) JSON lookup table path

    **Returns**: None
    '''
    data = dump_table(file, DEFAULT_TABLE_PATH)
    logger.info(
        'Table has {} keys and was successfully dumped'.format(len(data)))


def convert(input_file, output_file):
    # type: (str, str) -> a2pats
    '''
    Load CEESIM file and convert to A²PATS. Output files that do not
    exist are created automatically.

    Parameters:
     * `input_file`: (string) Location of file to import
     * `output_file`: (string) Location of file to export (does not have to exist)

    **Returns**: (a2pats class object) A²PATS object (if successful)
    '''
    logger.debug(
        'Main app converter called, using provided input and output files')
    input_data = import_(input_file, ceesim)  # -> CEESIM object
    emitter_modes = split_emitter_modes(input_data.imported_data)
    for i, emitter_mode in enumerate(emitter_modes):
        mode_num = "0" + str(i+1) if len(str(i+1)) == 1 else str(i+1)
        logger.debug("!!Working on Emitter Mode {}".format(mode_num))
        scan_type = determine_scan_type(emitter_mode)
        logger.info("Scan Type: {}".format(scan_type))
        path_to_tables = "data/c_tables/"
        lookup_table = prepare_lookup_table(path_to_tables + scan_file_name[scan_type] + "base.csv", \
                                                path_to_tables + scan_file_name[scan_type] + "base.json")
        output_data = convert_to_a2pats(emitter_mode, lookup_table)
        if scan_type == "HELICAL":
            mode_num += " (Needs Edit)"
        success = dump_a2pats(output_data, output_file + "/{}".format(mode_num))
    if success:
        return output_data
    else:
        logger.error('File failed to export!')
        return None


def parse_arguments(epilog):
    # type: (str) -> None
    '''
    Parse arguments passed from shell

    Parameters:
     * `epilog`: (string) Epilog to show on help screen
    
    **Returns**: None
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
