from app import a2pats, ceesim
from app.converter import convert_to_a2pats
from app.importer import import_
from sys import argv


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
        print('File failed to export!')
        return None


if __name__ == '__main__':
    if len(argv) > 0:
        convert(argv[0])
