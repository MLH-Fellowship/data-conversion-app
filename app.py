from app import a2pats, ceesim
from app.converter import convert_to_a2pats
from app.exporter import dump_a2pats
from app.importer import import_
from app.util import config as config_
from app.util.logging import logger, set_up_logger
from argparse import ArgumentParser
from logging import DEBUG, INFO, ERROR, CRITICAL


def convert(input_file: str, output_file: str) -> a2pats:
    '''Load CEESIM file and convert to A²PATS

    :param input_file: Location of file to import
    :type input_file: str

    :param output_file: Location of file to export (does not have to exist)
    :type output_file: str

    :returns: A²PATS object (if successful)
    :rtype: a2pats
    '''
    logger.debug('Main app converter called, using provided input and output files')
    input_data = import_(input_file, ceesim)
    output_data = convert_to_a2pats(input_data)
    success = dump_a2pats(output_data, output_file)
    if success:
        return output_data
    else:
        logger.error('File failed to export!')
        return None


def parse_arguments():
    '''Parse arguments
    '''
    parser = ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', help='Enable verbose mode, overrides -s')
    parser.add_argument('-s', '--suppress', action='count', help='Supress logging, -ss to completely silence')
    parser.add_argument('input', default=None, help='Input file to convert')
    parser.add_argument('output', default=None, help='Output file after conversion')
    args = parser.parse_args()
    if args.verbose:
        set_up_logger(DEBUG)
    elif args.suppress > 1:
        set_up_logger(CRITICAL)
    elif args.suppress:
        set_up_logger(ERROR)
    else:
        set_up_logger(INFO)
    print(args.input, args.output)


if __name__ == '__main__':
    config = config_('data/config.json')
    print(config.header)
    print(config.credits)
    parse_arguments()
