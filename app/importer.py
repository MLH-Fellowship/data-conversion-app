from app import a2pats, ceesim, datastore
from io import IOBase
from typing import Union, TextIO


def import_a2pats(fp: TextIO) -> a2pats:
    '''Import an A²PATS file for conversion
    '''
    pass


def import_ceesim(fp: TextIO) -> ceesim:
    '''Import a CEESIM file for conversion
    '''
    pass


def import_(fp: Union[str, TextIO], classtype=datastore, downgrade_peaceful=True) -> datastore:
    '''Import data dynamically

    :param fp: File pointer or string to import file
    :type fp: str or TextIO

    :param classtype: Class type to import as (must be of instance datastore)
    :type classtype: datastore or datastore-like

    :param downgrade_peaceful: Whether or not to ignore errors
    :type downgrade_peaceful: bool

    :returns: Database object for typing
    :rtype: datastore or datastore-like
    '''
    if downgrade_peaceful:
        if not issubclass(classtype, datastore):
            # Assume ceesim import
            classtype = ceesim
        if type(fp) is str:
            try:
                fp = open(fp)
            except:
                return datastore()
        elif not isinstance(fp, IOBase):
            return datastore()
    else:
        assert issubclass(
            classtype, datastore), 'Your import_ call must be of datastore or datastore-like type!'
        if type(fp) is str:
            fp = open(fp)
        assert isinstance(
            fp, IOBase), 'Your import_ call must provide a valid files-like pointer or file path!'
    if classtype is a2pats:
        return import_a2pats(fp)
    elif classtype is ceesim:
        return import_ceesim(fp)
    else:
        raise ValueError('This type of datastore isn\'t supported yet!')


def xml_to_dictionary(filepath: str) -> dict:
    pass
