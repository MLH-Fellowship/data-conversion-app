from app import datastore
from typing import Tuple, Union, TextIO


class functions:
    '''A collection of functions for importing
    '''

    @staticmethod
    def extract_metadata(name: str) -> Tuple[str, str, str]:
        '''Extracts A2PATS meta from CEESIM name

        :param name: ModeName of CEESIM
        :type name: str

        :returns: name, version, mode
        :rtype: tuple
        '''
        if '_' in name:
            values = name.split('_')
            half = len(values[1]) / 2
            return values[0], values[1][:half], values[1][half:]
        else:
            return name, name, name

    @staticmethod
    def extract_name(name: str) -> str:
        '''Extracts A2PATS name from CEESIM name

        :param name: ModelName of CEESIM
        :type name: str

        :returns: Name
        :rtype: str
        '''
        this_name, version, mode = functions.extract_metadata(name)
        return this_name

    @staticmethod
    def extract_version(name: str) -> str:
        '''Extracts A2PATS version from CEESIM version

        :param name: ModelName of CEESIM
        :type name: str

        :returns: Version
        :rtype: str
        '''
        this_name, version, mode = functions.extract_metadata(name)
        return version

    @staticmethod
    def extract_mode(name: str) -> str:
        '''Extracts A2PATS mode from CEESIM name

        :param name: ModelName of CEESIM
        :type name: str

        :returns: Mode
        :rtype: str
        '''

    @staticmethod
    def to_mhz(frequency: Union[int, float, str]) -> str:
        '''Convert Hz to MHz

        :param frequency: Hz frequency
        :type frequency: int, float, or str

        :returns: MHz Frequency
        :rtype: str
        '''
        def to_str(f): return f'{f:.10f}'
        try:
            return to_str(float(frequency) / 1000000)
        except:
            return to_str(0)

    @staticmethod
    def to_usec(time: Union[int, float, str]) -> str:
        '''Convert s to us

        :param time: s
        :type time: int, float, or str

        :returns: us
        :rtype: str
        '''
        def to_str(f): return f'{f:.5f}'
        try:
            return to_str(float(time) * 1000000)
        except:
            return to_str(0)


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
