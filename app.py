from app import a2pats, ceesim
from app.converter import convert_to_a2pats
from app.importer import import_
from app.util import config as config_
from app.util.logging import logger, set_up_logger
from logging import DEBUG
from sys import argv


set_up_logger(DEBUG)


def convert(input_file: str, output_file: str) -> a2pats:
    '''Load CEESIM file and convert to A²PATS

    :param input_file: Location of file to import
    :type input_file: str

    :param output_file: Location of file to export (does not have to exist)
    :type output_file: str

    :returns: A²PATS object (if successful)
    :rtype: a2pats
    '''
    input_data = import_(input_file, ceesim)
    output_data = convert_to_a2pats(input_data)
    success = output_data.export(output_file)
    if success:
        return output_data
    else:
        logger.error('File failed to export!')
        return None


if __name__ == '__main__':
    config = config_('data/config.json')
    print(config.header)
    print(config.credits)
    if len(argv) > 2:
        convert(argv[1], argv[2])
