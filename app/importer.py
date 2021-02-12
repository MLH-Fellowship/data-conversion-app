from app import datastore
from typing import Union, TextIO


def import_(fp: Union[str, TextIO], classtype=datastore, downgrade_peaceful=True) -> 'datastore':
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
            classtype = datastore
    else:
        assert issubclass(
            classtype, datastore), 'Your import_ call must be of datastore or datastore-like type!'
    # TODO


def import_a2pats():
    '''Import an A²PATS file for conversion
    '''
    pass


def import_ceesim():
    '''Import a CEESIM file for conversion
    '''
    pass
