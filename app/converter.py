#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import a2pats, ceesim, datastore, model, ALLOWED_MODELS, MODEL_FILES
from app.util.errors import DatastoreError
from app.util.logger import logger
from sys import version_info

if version_info > (3, 5):
    from typing import Tuple, Union


AUTO_MODELS = ('SCAN', 'ANTENNA', 'FREQUENCY')
FUNC_HDR = 'FUNCTION'
INTRAPULSE_NAME = 'INP'
STRING_HDR = 'STRING'
TABLE_DATA = 'DATA'
TABLE_LIST = 'MULTI'


class functions:
    '''A collection of functions for importing
    '''

    @staticmethod
    def extract_metadata(name):
        # type: (str) -> Tuple[str, str, str]
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
    def extract_name(name):
        # type: (str) -> str
        '''Extracts A2PATS name from CEESIM name

        :param name: ModelName of CEESIM
        :type name: str

        :returns: Name
        :rtype: str
        '''
        this_name, version, mode = functions.extract_metadata(name)
        return this_name

    @staticmethod
    def extract_version(name):
        # type: (str) -> str
        '''Extracts A2PATS version from CEESIM version

        :param name: ModelName of CEESIM
        :type name: str

        :returns: Version
        :rtype: str
        '''
        this_name, version, mode = functions.extract_metadata(name)
        return version

    @staticmethod
    def extract_mode(name):
        # type: (str) -> str
        '''Extracts A2PATS mode from CEESIM name

        :param name: ModelName of CEESIM
        :type name: str

        :returns: Mode
        :rtype: str
        '''

    @staticmethod
    def to_mhz(frequency):
        # type: (Union[int, float, str]) -> str
        '''Convert Hz to MHz

        :param frequency: Hz frequency
        :type frequency: int, float, or str

        :returns: MHz Frequency
        :rtype: str
        '''
        def to_str(f): return '{:.10f}'.format(f)
        try:
            return to_str(float(frequency) / 1000000)
        except:
            return to_str(0)

    @staticmethod
    def to_usec(time):
        # type: (Union[int, float, str]) -> str
        '''Convert s to us

        :param time: s
        :type time: int, float, or str

        :returns: us
        :rtype: str
        '''
        def to_str(f): return '{:.5f}'.format(f)
        try:
            return to_str(float(time) * 1000000)
        except:
            return to_str(0)

    @staticmethod
    def intra_status(modstatus):
        # type: (str) -> str
        '''Convert modstatus to intrapulse model

        :param modstatus: XML ModeStatus tag
        :type modstatus: str

        :returns: intrapulse model
        :rtype: str
        '''

        return "OFF" if modstatus == "false" else "REFERENCE"

    @staticmethod
    def to_caps(word):
        # type: (str) -> str
        '''Convert string to all caps

        :param word: XML tag text
        :type word: str

        :returns: capslock word
        :rtype: str
        '''

        return word.upper()

    @staticmethod
    def format_degree(num):
        # type: (Union[int, float]) -> str
        '''Convert degree single/double digit to triple decimal point

        :param num: number of degrees
        :type num: int or float

        :returns: formatted degrees
        :rtype: str
        '''
        def to_str(f): return '{:.3f} DEG'.format(f)
        try:
            return to_str(float(num))
        except:
            return to_str(0)

    @staticmethod
    def format_second(num):
        # type: (Union[int, float]) -> str
        '''Convert degree single/double digit to five decimal points

        :param num: number of seconds
        :type num: int or float

        :returns: formatted seconds
        :rtype: str
        '''
        def to_str(f): return '{:.5f} SEC'.format(f)
        try:
            return to_str(float(num))
        except:
            return to_str(0)

    @staticmethod
    def dir_abrev(azdirection):
        # type: (str) -> str
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
    def motion_overlay(motion):
        # type: (str) -> str
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
    def dir_typ(eldirection):
        # type: (str) -> str
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
    def dir_dir(eldirection):
        # type: (str) -> str
        '''Convert up/down direction to vertical/horizontal

        :param num: direction up/down
        :type num: str

        :returns: a2pats direction
        :rtype: str
        '''

        if eldirection == "Up":
            return "VERTICAL"
        elif eldirection == "Down":  # it is possible that both up and down should correspond to VERTICAL
            return "HORIZONTAL"

    @staticmethod
    def period_to_hz(num):
        # type: (Union[int, float]) -> str
        '''Convert period single/double in seconds to hertz with five decimal points

        :param num: period in seconds
        :type num: int or float

        :returns: formatted hertz
        :rtype: str
        '''
        def to_str(f): return '{:.5f} HZ'.format(f)
        try:
            return to_str(float(1/num))
        except:
            return to_str(0)

    @staticmethod
    def offset_origin(eloffset):
        # type: (int) -> str
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

    @staticmethod
    def model_kind(kind):
        # type: (str) -> str
        '''Convert kind to model

        :param kind: kind of model (usually a shape)
        :type kind: str

        :returns: antenna model
        :rtype: str
        '''

        assert kind == "Elliptical", "Unexpected AntennaModelKind - {}".format(
            kind)
        return "RECTANGULAR"

    @staticmethod
    def format_func(func):
        # type: (str) -> str
        '''Convert func to formatted_func

        :param func: distribution function
        :type kind: str

        :returns: formatted distribution function
        :rtype: str
        '''

        function = func.split()[0].upper()
        trig = function[:3]
        arg = function[3:]

        return " ".join([trig, arg]).replace("(X)", "X")

    @staticmethod
    # TODO: if possible, we should really accept a second parameter here to
    def ant_model(emitterid): return "_".join([emitterid, "ANT"])

    @staticmethod
    # consolidate these four very similar functions
    def freq_model(emitterid): return "_".join([emitterid, "Freq"])

    @staticmethod
    def seq_model(emitterid): return "_".join([emitterid, "Seq"])

    @staticmethod
    def scan_model(emitterid): return "_".join([emitterid, "Scan"])


# I'm not sure if this is the right method
def flatten_table(data, stack_size=1):
    # type: (dict, int) -> dict
    '''Flattens a table
    '''
    logger.debug('Flattening input table with call stack size at')
    data_ = dict()
    for key in data:
        if key not in data_:
            if type(data[key]) not in {dict, list}:
                data_[key] = data[key]
            else:
                frame = data[key]
                if frame is list:
                    if len(frame) < 1 or frame[0] is not dict:
                        continue
                    else:
                        frame = frame[0]
                subdict = flatten_table(frame, stack_size + 1)
                subdict.update(data_)
                data_ = subdict
    return data_


def convert(data):
    # type: (Union[a2pats, ceesim]) -> Union[a2pats, ceesim]
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
        logger.warn('Provided type to convert was correct, but unrecognized')
        return data.to_datastore()
    else:
        raise DatastoreError(
            'Provided type to convert was neither of class a2pats or ceesim.')


def convert_one_key(lookup_data, value):
    # type: (dict, str) -> str
    '''Converts one key given the table lookup parameters
    '''
    # TODO: Table Handler
    if FUNC_HDR in lookup_data:
        funcp_data = getattr(functions, lookup_data[FUNC_HDR])(value)
        if lookup_data[STRING_HDR]:
            return '"{:<15}:   {}"'.format(lookup_data["LABEL"], funcp_data)
        else:
            return 'funcp_data'.format()
    else:
        return value


def obtain_relevant_tags(data, flattened_data, tag):
    # type: (dict, dict, str) -> Tuple[list, None]
    '''Checks the imported data for relevant data
    '''
    # TODO
    return None


def generate_other_models(data, flattened_data, table):
    # type: (dict, dict, dict) -> list
    '''Generate all non INP/PUL models
    '''
    def create_converted(model, cdict_key, opt):
        tags = obtain_relevant_tags(data, flattened_data, cdict_key)
        if not tags:
            # TODO: Use default value
        converted = convert_one_key(opt, tags[0])
        # TODO: Place value in correct position

    models = list()
    name = ''  # TODO: Generate name
    for mtype in AUTO_MODELS:
        next_model = model(mtype, name)
        table_key = MODEL_FILES[mtype]
        for cdict_key in data[table_key]:
            if not cdict_key:
                # TODO: Fill all default values
                continue
            if data[table_key][cdict_key][TABLE_LIST] and TABLE_DATA in data[table_key][cdict_key]:
                data_opts = data[table_key][cdict_key][TABLE_DATA]
                for opt in data_opts:
                    create_converted(model, cdict_key, opt)
            else:
                create_converted(model, cdict_key, opt)
        models.append(next_model)
    return models


def generate_intrapulse(data, table):
    # type: (dict, dict) -> dict
    '''Converts intrapulse signals in an imported table using a lookup table
    '''
    # TODO: Logic to find signals -> list of signals
    for tag in table:
        if INTRAPULSE_NAME in table[tag]:
            if TABLE_LIST in table[tag][INTRAPULSE_NAME] and table[tag][INTRAPULSE_NAME][TABLE_LIST]:
                # TODO: What if table is list
                pass
            else:
                # TODO: What if table is flat
                pass
    # TODO: Return data


def generate_pulse(data, table):
    # type: (dict, dict) -> dict
    '''Converts pulse signals in an imported table using a lookup table
    '''
    # TODO
    pass


def convert_to_a2pats(data, table):
    # type: (ceesim, dict) -> a2pats
    '''Convert CEESIM data to A²PATS data

    :param data: CEESIM data to import
    :type data: ceesim

    :returns: A²PATS data
    :rtype: a2pats
    '''
    logger.info('Beginning CEESIM to A2PATS conversion')
    flattened_data = flatten_table(data)
    store = a2pats(imported_type='A2PATS')
    for type_ in ALLOWED_MODELS:
        # TODO
        next_model = model(type_, 'insert_name')
        store.models.append(next_model)
    return store


def convert_to_ceesim(data):
    # type: (a2pats) -> ceesim
    '''Convert A²PATS data to CEESIM data

    :param data: A²PATS data to import
    :type data: a2pats

    :returns: CEESIM data
    :rtype: ceesim
    '''
    # TODO
    pass
