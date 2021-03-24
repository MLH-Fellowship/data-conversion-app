#!/usr/bin/python
# -*- coding: utf-8 -*-

from app import a2pats, ceesim, datastore, model, MODEL_FILES
from app.scripts import PRI_HDR, TABLE_MULTI_HDR as MULTI_HDR
from app.util.errors import DatastoreError
from app.util.logger import logger
from sys import version_info
from csv import reader

if version_info > (3, 5):
    from typing import Tuple, Union, List


AUTO_MODELS = ('SCAN', 'ANTENNA', 'FREQUENCY')
DEFAULT_HDR = 'DEFAULT'
FILE_HDR = 'FILE'
FUNC_HDR = 'FUNCTION'
INTRAPULSE_NAME = 'INP'
NAME_HDR = 'ModeName'
PULSE_NAME = 'PUL'
STRING_HDR = 'STRING'
TABLE_DATA = 'DATA'
TAG_HDR = 'TAG'


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

        if word == "Circular":
            return word.upper()

        elif word == "Steady":
            return "LORO"

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
    def get_dwell(cps):
        # type: (str) -> str
        '''Convert ComplexPriState to Dwell in MSEC

        :param cps: ComplexPriState
        :type kind: str

        :returns: Dwell in MSEC
        :rtype: str
        '''

        if cps == "false":
            return "N/A"

    @staticmethod
    def get_repeat(cps):
        # type: (str) -> str
        '''Convert ComplexPriState to pulse repeat

        :param cps: ComplexPriState
        :type kind: str

        :returns: pulse repeat
        :rtype: str
        '''

        if cps == "false":
            return "1"

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
def flatten_table(ceesim_data, stack_size=1):
    # type: (dict, int) -> dict
    '''Flattens a table
    '''
    logger.debug(
        'Flattening input table with call stack size at {}'.format(stack_size))
    data_ = dict()
    for key in ceesim_data:
        # logger.debug('Now checking for {} in data'.format(key))
        if key not in data_:
            if type(ceesim_data[key]) not in {dict, list}:
                logger.debug(
                    '{} was not in data, and was added to the flat table'.format(key))
                data_[key] = ceesim_data[key]
            else:
                logger.debug(
                    'Now processing lookup table for subkeys of {}'.format(key))
                frame = ceesim_data[key]
                if type(frame) is list:
                    if len(frame) < 1 or frame[0] is not dict:
                        continue
                    else:
                        frame = frame[0]
                subdict = flatten_table(frame, stack_size + 1)
                subdict.update(data_)
                data_ = subdict
    logger.debug('Now returning flat table with size of {}'.format(len(data_)))
    return data_


def convert_one_key(lookup_data, value):
    # type: (dict, str) -> str
    '''Converts one key given the table lookup parameters
    '''
    # TODO: Table Handler
    if FUNC_HDR in lookup_data and hasattr(functions, lookup_data[FUNC_HDR]):
        funcp_data = getattr(functions, lookup_data[FUNC_HDR])(value)
    else:
        funcp_data = lookup_data["DEFAULT"]

    if lookup_data[STRING_HDR]:
        funcp_data = '"{}"'.format(funcp_data)

    if len(lookup_data["LABEL"]) >= 19:
        return '{} : {}'.format(lookup_data["LABEL"], funcp_data)
    else:
        return '{:<20}{}'.format(lookup_data["LABEL"] + ":", funcp_data)


def obtain_relevant_tags(ceesim_data, ceesim_flattened, tag, fast=True):
    # type: (dict, dict, str, bool) -> Tuple[list, None]
    '''Checks the imported data for relevant data
    '''
    if fast:
        if tag in ceesim_flattened:
            return ceesim_flattened[tag]
    else:
        # TODO: Iterate through entire data
        pass
    return None


def generate_other_models(ceesim_data, ceesim_flattened, lookup_table):
    # type: (dict, dict, dict) -> list
    '''Generate all non INP/PUL models
    '''
    logger.debug('Now generating all non-signal models')

    def fill_table(model, pos, value):
        if len(model.converted_data) <= pos:
            model.converted_data += [''] * \
                (pos - len(model.converted_data) + 1)
        model.converted_data[pos] = value

    def create_converted(model, opt):
        tags = obtain_relevant_tags(
            ceesim_data, ceesim_flattened, opt[TAG_HDR])
        if tags:
            value = tags[0]
        else:
            logger.debug('Could not find tag, using default tag for {}: {}: {}'.format(
                opt[FILE_HDR], opt[TAG_HDR], opt[DEFAULT_HDR]))
            value = opt[DEFAULT_HDR]
        converted = convert_one_key(opt, value)
        fill_table(model, opt[PRI_HDR], converted)

    def add_headers(mfile, model):
        with open("data/headers.csv") as head:
            headers = reader(head)
            for header in headers:
                if header[0] == mfile:
                    left = (int(header[2]) - len(header[1]) - 3) / 2
                    lleft = int(left)
                    right = lleft
                    if lleft == left:
                        left = lleft
                        right = lleft + 1
                    htext = ' '.join(
                        ['*' * lleft, header[1], '*' * right])
                    fill_table(model, int(header[3]), htext)
    models = list()
    # TODO: Pull correct name from flatted data with obtain_relevant_tags, currently uses split_emitter_modes
    # Path to ModeName: ceesim_data["Scenario"]["Platforms"]["Platform"][1]["Emitters"]["Emitter"]["Emitter_Modes"]["Emitter_Mode"][0]["EmitterModeHeader"]["ModeName"]
    name = split_emitter_modes(ceesim_data)[0]["EmitterModeHeader"]["ModeName"] # obtain_relevant_tags(ceesim_data, ceesim_flattened, NAME_HDR)
    logger.debug('Generic model generator using name: {}'.format(name))
    for mtype in AUTO_MODELS:
        next_model = model(mtype, name)
        if mtype not in MODEL_FILES:
            logger.warn(
                'Could not find mtype {} in model files, skipping'.format(mtype))
            continue
        table_key = MODEL_FILES[mtype]
        add_headers(table_key, next_model)
        if table_key not in lookup_table:
            logger.warn(
                'Could not find key {} in lookup table, skipping'.format(table_key))
            continue
        logger.debug(
            'Now processing table key {} with mtype {}'.format(table_key, mtype))
        for cdict_key in lookup_table[table_key]:
            if MULTI_HDR in lookup_table[table_key][cdict_key] and TABLE_DATA in lookup_table[table_key][cdict_key]:
                data_opts = lookup_table[table_key][cdict_key][TABLE_DATA]
                for opt in data_opts:
                    create_converted(next_model, opt)
            else:
                create_converted(next_model, opt)
        models.append(next_model)
    return models


def scan_splitter():
    pass


def generate_intrapulse(ceesim_data, lookup_table):
    # type: (dict, dict) -> List[model]
    '''Converts intrapulse signals in an imported table using a lookup table
    '''
    logger.debug("Now generating the intrapulse models")

    for filetype in lookup_table:
        if filetype is INTRAPULSE_NAME:
            for tag in filetype:

                tag_data = lookup_table[INTRAPULSE_NAME][tag]

                if MULTI_HDR in tag_data:
                    for feature_data in tag_data["DATA"]:
                        convert_one_key(
                            feature_data, ceesim_data[feature_data["TAG"]])
                else:
                    # TODO: What if table is flat
                    pass
    # TODO: Return data


def generate_pulse(ceesim_data, lookup_table):
    # type: (dict, dict) -> List[model]
    '''Converts pulse signals in an imported table using a lookup table
    '''
    logger.debug("Now generating the pulse models")

    for filetype in lookup_table:
        if filetype is PULSE_NAME:
            for tag in filetype:

                if tag:
                    tag_data = lookup_table[PULSE_NAME][tag]

                if MULTI_HDR in tag_data:
                    for feature_data in tag_data["DATA"]:
                        convert_one_key(
                            feature_data, ceesim_data[feature_data["TAG"]])
                else:
                    # TODO: What if table is flat
                    pass
    # TODO: Return data


ITERATOR_KEYS = ('Scenario', 'Platforms', 'Platform')
SEARCH_TO_RETURN_KEYS = ('Emitters', 'Emitter', 'EmitterModes', 'EmitterMode')


def split_emitter_modes(ceesim_data):
    # type: (dict) -> List[dict]
    '''Converts CEESIM data to a list of emitter mode dicts
    '''
    def split_emitter_modes_helper(data):
        # type: (dict) -> List[dict]
        frame = data
        for key in SEARCH_TO_RETURN_KEYS:
            if key in frame:
                frame = frame[key]
            else:
                return list()
        if type(frame) is list:
            return frame
        return list()

    frame = ceesim_data
    for key in ITERATOR_KEYS:
        if key in frame:
            frame = frame[key]
        else:
            return list()
    if type(frame) is not list:
        return list()
    modes = list()
    for platform in frame:
        modes += split_emitter_modes_helper(platform)
    return modes


def convert_to_a2pats(ceesim_data, lookup_table):
    # type: (ceesim, dict) -> a2pats
    '''Convert CEESIM data to A²PATS data

    :param data: CEESIM data to import
    :type data: ceesim

    :returns: A²PATS data
    :rtype: a2pats
    '''
    logger.info('Beginning CEESIM to A2PATS conversion')
    flattened_data = flatten_table(ceesim_data.imported_data)
    emitter_modes = split_emitter_modes(ceesim_data.imported_data)
    store = a2pats(imported_type='A2PATS')
    # TODO: Use emitter modes instead
    generic_models = generate_other_models(
        ceesim_data.imported_data, flattened_data, lookup_table)
    logger.debug('Added {} models from generate_other_models'.format(
        len(generic_models)))
    store.models += generic_models
    # TODO: Generate models
    return store


def convert_to_ceesim(a2pats_data):
    # type: (a2pats) -> ceesim
    '''Convert A²PATS data to CEESIM data

    :param data: A²PATS data to import
    :type data: a2pats

    :returns: CEESIM data
    :rtype: ceesim
    '''
    # TODO
    pass


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
