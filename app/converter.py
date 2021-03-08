from app.errors import DatastoreError
from app import a2pats, ceesim, datastore
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


    @staticmethod
    def intra_status(modstatus: str) -> str:
        '''Convert modstatus to intrapulse model

        :param modstatus: XML ModeStatus tag
        :type modstatus: str

        :returns: intrapulse model
        :rtype: str
        '''

        return "OFF" if modstatus == "false" else "REFERENCE"

    
    @staticmethod
    def to_caps(word: str) -> str:
        '''Convert string to all caps

        :param word: XML tag text
        :type word: str

        :returns: capslock word
        :rtype: str
        '''

        return word.upper()


    @staticmethod
    def format_degree(num: Union[int, float]) -> str:
        '''Convert degree single/double digit to triple decimal point

        :param num: number of degrees
        :type num: int or float

        :returns: formatted degrees
        :rtype: str
        '''
        def to_str(f): return f'{f:.3f} DEG'
        try:
            return to_str(float(num))
        except:
            return to_str(0)


    @staticmethod
    def format_second(num: Union[int, float]) -> str:
        '''Convert degree single/double digit to five decimal points

        :param num: number of seconds
        :type num: int or float

        :returns: formatted seconds
        :rtype: str
        '''
        def to_str(f): return f'{f:.5f} SEC'
        try:
            return to_str(float(num))
        except:
            return to_str(0)

    
    @staticmethod
    def dir_abrev(azdirection: str) -> str:
        '''Convert full direction to abbreviation

        :param num: direction as a word
        :type num: str

        :returns: direction as an abbreviation
        :rtype: str
        '''

        if azdirection == "Clockwise":
            return "CW"
        else:
            return "CCW"

    
    @staticmethod
    def motion_overlay(motion: str) -> str:
        '''Convert elevation scan motion to a2pats scan overlay model

        :param motion: direction of motion
        :type motion: str

        :returns: scan overlay model
        :rtype: str
        '''

        if motion == "Unidirectional":
            return "NODDING"
        else:
            return "OFF"

    
    @staticmethod
    def dir_typ(eldirection: str) -> str:
        '''Convert up/down direction to a2pats scan type

        :param num: direction up/down
        :type num: str

        :returns: a2pats scan type
        :rtype: str
        '''

        if eldirection == "Up" or eldirection == "Down":
            return "TRIANGULAR"
        else:
            return "SAWTOOTH"

    
    @staticmethod
    def dir_dir(eldirection: str) -> str:
        '''Convert up/down direction to vertical/horizontal

        :param num: direction up/down
        :type num: str

        :returns: a2pats direction
        :rtype: str
        '''

        if eldirection == "Up":
            return "VERTICAL"
        elif eldirection == "Down": # it is possible that both up and down should correspond to VERTICAL
            return "HORIZONTAL"


    @staticmethod
    def period_to_hz(num: Union[int, float]) -> str:
        '''Convert period single/double in seconds to hertz with five decimal points

        :param num: period in seconds
        :type num: int or float

        :returns: formatted hertz
        :rtype: str
        '''
        def to_str(f): return f'{f:.5f} HZ'
        try:
            return to_str(float(1/num))
        except:
            return to_str(0)

    
    @staticmethod
    def offset_origin(eloffset: int) -> str:
        '''Convert offset to origin

        :param eloffset: numerical track offset
        :type eloffset: int

        :returns: top/bottom origin
        :rtype: str
        '''

        if eloffset == 0:
            return "BOTTOM"
        else:
            return "TOP"


def convert(data: Union[a2pats, ceesim]) -> Union[a2pats, ceesim]:
    '''Dynamically convert data to its corresponding format

    :param data: A²PATS or CEESIM data to import
    :type data: a2pats or ceesim

    :returns: A²PATS or CEESIM data
    :rtype: a2pats or ceesim
    '''
    if type(data) is a2pats:
        return convert_to_ceesim(data)
    elif type(data) is ceesim:
        return convert_to_a2pats(data)
    elif isinstance(data, datastore):
        # TODO: Replace print with logger.warning
        print('Provided type to convert was correct, but unrecognized')
        return data.to_datastore()
    else:
        raise DatastoreError('Provided type to convert was neither of class a2pats or ceesim.')


def convert_to_a2pats(data: ceesim) -> a2pats:
    '''Convert CEESIM data to A²PATS data

    :param data: CEESIM data to import
    :type data: ceesim

    :returns: A²PATS data
    :rtype: a2pats
    '''
    # TODO
    pass


def convert_to_ceesim(data: a2pats) -> ceesim:
    '''Convert A²PATS data to CEESIM data

    :param data: A²PATS data to import
    :type data: a2pats

    :returns: CEESIM data
    :rtype: ceesim
    '''
    # TODO
    pass

