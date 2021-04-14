#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This file handles the conversion between the two file formats.

Once again, find the documentation online at
https://mlh-fellowship.github.io/hermes-docs
'''

from app import a2pats, ceesim, datastore, model, MODEL_FILES
from app.scripts import PRI_HDR, TABLE_MULTI_HDR as MULTI_HDR
from app.util.errors import DatastoreError
from app.util.logger import logger
from app.util.tables import build_table_str
from sys import version_info
from csv import reader

if version_info > (3, 5):
    from typing import Tuple, Union, List


AUTO_MODELS = ('SCAN', 'ANTENNA', "SIGNAL", "PULSE", "PULSE SEQUENCE")
scan_file_name = {"CIRCULAR": "circ", "RASTER": "rast", "SECTOR": "sect", "LORO": "loro", "DWELL": "elec", "HELICAL": "circ"}
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
    '''
    A collection of functions for importing
    '''

    @staticmethod
    def extract_metadata(name):
        # type: (str) -> Tuple[str, str, str]
        '''
        Extracts A2PATS meta from CEESIM name

        Parameters:
         * `name`: (string) ModelName of CEESIM file

        **Returns**: (tuple of 3 strings) Name, version, and node
        '''
        if '_' in name:
            values = name.split('_')
            half = len(values[1]) // 2
            return values[0], values[1][:half], values[1][half:]
        else:
            return name, name, name

    @staticmethod
    def extract_name(name):
        # type: (str) -> str
        '''
        Extracts A2PATS name from CEESIM name

        Parameters:
         * `name`: (string) ModelName of CEESIM file
        
        **Returns**: (string) A2PATS name
        '''
        this_name, version, mode = functions.extract_metadata(name)
        return this_name

    @staticmethod
    def extract_version(name):
        # type: (str) -> str
        '''
        Extracts A2PATS version from CEESIM version

        Parameters:
         * `name`: (string) ModelName of CEESIM file

        **Returns**: (string) CEESIM version
        '''
        this_name, version, mode = functions.extract_metadata(name)
        return version

    @staticmethod
    def extract_mode(name):
        # type: (str) -> str
        '''
        Extracts A2PATS mode from CEESIM name

        Parameters:
         * `name`: (string) ModelName of CEESIM file
        
        **Returns**: (string) CEESIM model
        '''
        this_name, version, mode = functions.extract_metadata(name)
        return mode

    @staticmethod
    def to_mhz(frequency):
        # type: (Union[int, float, str]) -> str
        '''
        Convert Hz to MHz

        Parameters:
         * `frequency`: (number or number as string) Frequency in Hz

        **Returns**: (string) Frequency as MHz
        '''
        def to_str(f): return '{:.10f}'.format(f)
        try:
            return to_str(float(frequency) / 1000000)
        except:
            return to_str(0)

    @staticmethod
    def to_mhz_deviation(frequency):
        return functions.to_mhz(frequency) + ' MHZ'

    @staticmethod
    def to_usec(time):
        # type: (Union[int, float, str]) -> str
        '''
        Convert s to us

        Parameters:
         * `time`: (number or number as string) Seconds
        
        **Returns**: (string) Microseconds
        '''
        def to_str(f): return '{:.5f}'.format(f)
        try:
            return to_str(float(time) * 1000000)
        except:
            return to_str(0)

    @staticmethod
    def intra_status(modstatus):
        # type: (str) -> str
        '''
        Convert modstatus to intrapulse model

        Parameters:
         * `modstatus`: (string) XML ModeStatus tag

        **Returns**: (string) Intrapulse model
        '''

        return "OFF" if modstatus == "false" else "REFERENCE"

    @staticmethod
    def to_caps(word):
        # type: (str) -> str
        '''
        Convert string to all caps

        Parameters:
         * `word`: (string) XML tag text

        **Returns**: (string) XML tag text in all caps
        '''
        if word == "Circular":
            return word.upper()

        elif word == "Steady":
            return "LORO"

        else:
            return "RASTER"

    @staticmethod
    def format_degree(num):
        # type: (Union[int, float]) -> str
        '''
        Convert degree single/double digit to triple decimal point

        Parameters:
         * `num`: (number) Degrees

        **Returns**: (string) Degrees (formatted)
        '''
        def to_str(f): return '{:.3f} DEG'.format(f)
        try:
            return to_str(float(num))
        except:
            return to_str(0)

    @staticmethod
    def format_second(num):
        # type: (Union[int, float]) -> str
        '''
        Convert degree single/double digit to five decimal points

        Parameters:
         * `num`: (number) Seconds
        
        **Returns**: (string) Seconds (formatted)
        '''
        def to_str(f): return '{:.5f} SEC'.format(f)
        try:
            return to_str(float(num))
        except:
            return to_str(0)

    @staticmethod
    def dir_abrev(azdirection):
        # type: (str) -> str
        '''
        Convert full direction to abbreviation

        Parameters:
         * `azdirection`: Direction name
        
        **Returns**: (string) Direction shorthand
        '''

        if azdirection == "Clockwise":
            return "CW"
        else:
            return "CCW"

    @staticmethod
    def motion_overlay(motion):
        # type: (str) -> str
        '''
        Convert elevation scan motion to a2pats scan overlay model

        Parameters:
         * `motion`: (string) Direction of motion

        **Returns**: (string) Scan overlay model
        '''

        if motion == "Unidirectional":
            return "NODDING"

        else:
            return "OFF"

    @staticmethod
    def dir_typ(eldirection):
        # type: (str) -> str
        '''
        Convert up/down direction to a2pats scan type

        Parameters:
         * `eldirection`: (string) Direction string

        **Returns**: (string) A2PATS scan type
        '''

        if eldirection == "Up" or eldirection == "Down":
            return "TRIANGULAR"
        else:
            return "SAWTOOTH"

    @staticmethod
    def dir_dir(eldirection):
        # type: (str) -> str
        '''
        Convert up/down direction to vertical/horizontal

        Parameters:
         * `eldirection`: (string) CEESIM direction

        **Returns**: (string) A2PATS direction
        '''

        if eldirection == "Up":
            return "VERTICAL"
        elif eldirection == "Down":  # it is possible that both up and down should correspond to VERTICAL
            return "HORIZONTAL"

    @staticmethod
    def period_to_hz(num):
        # type: (Union[int, float]) -> str
        '''
        Convert period single/double in seconds to hertz with five decimal points

        Parameters:
         * `num`: (number) Period

        **Returns**: (string) Frequency
        '''
        def to_str(f): return '{:.5f} HZ'.format(f)
        try:
            return to_str(1/float(num))
        except:
            return to_str(1)

    @staticmethod
    def offset_origin(eloffset):
        # type: (int) -> str
        '''
        Convert offset to origin

        Parameters:
         * `eloffset`: (number) Numerical track offset

        **Returns**: (string) Top or bottom origin
        '''
        if eloffset == "0" or eloffset == "BOTTOM":
            return "BOTTOM"
        else:
            return "TOP"

    @staticmethod
    def model_kind(kind):
        # type: (str) -> str
        '''
        Convert kind to model

        Parameters:
         * `kind`: (string) Model kind (shape)

        **Returns**: (string) Model kind
        '''

        assert kind == "Elliptical" or kind == "RECTANGULAR", "Unexpected AntennaModelKind - {}".format(
            kind)
        return "RECTANGULAR"

    @staticmethod
    def format_func(func):
        # type: (str) -> str
        '''Convert func to formatted_func

        Parameters:
         * `func`: (string) Distribution function name

        **Returns**: (string) Distrubtio function (formatted)
        '''

        function = func.split()[0].upper()
        trig = function[:3]
        arg = function[3:]

        return " ".join([trig, arg]).replace("(X)", "X")

    @staticmethod
    def get_dwell(cps):
        # type: (str) -> str
        '''
        Convert ComplexPriState to Dwell in MSEC

        Parameters:
         * `cps`: (string) ComplexPriState
        
        **Returns**: (string) Dwell time
        '''

        # TODO: Fix this function and the one below to reflect real ComplexPriState behavior. On hold due to lack of examples in our sample data

        if cps == "false":
            return "N/A"
        else:
            return "N/A"

    @staticmethod
    def get_repeat(cps):
        # type: (str) -> str
        '''
        Convert ComplexPriState to pulse repeat

        Parameters:
         * `cps`: (string) ComplexPriState

        **Returns**: (string) Pulse repeat
        '''

        if cps == "false":
            return "1"
        else:
            return "1"

    @staticmethod
    def sweep_timer(rate, width):
        # type: (float, float) -> str
        '''
        Finds sweep time using the rate and bar width

        Parameters:
         * `rate`: (string) BarScanRate
         * `width`: (string) BarWidth
        **Returns**: (string) SWEEP TIME '''

        time = float(rate) * float(width)
        return '{:.3f}'.format(time)

    @staticmethod
    def inp_rate(dev, dur):
        # type: (float, float) -> str
        '''
        Finds rate using the deviation and duration

        Parameters:
         * `dev`: (float) LinearFreqDeviation
         * `dur`: (float) LinearFreqDuration

        **Returns**: (string) RATE '''

        rate = float(functions.to_mhz(dev)) / float(functions.to_usec(dur))
        return '{:.6f} MHZ/USEC'.format(rate)

    @staticmethod
    def halve_it(num):
        return str(num / 2)

    @staticmethod
    def timing_mode(cps):
        # type: (str) -> (str)
        '''
        Convert ComplexPriState to timing mode

        Parameters:
         * `cps`: (string) ComplexPriState
        
        **Returns**: (string) Timing mode
        '''
        if cps == "false":
            return "TIME"
        else:
            return cps

    @staticmethod
    def int_name(ModStatus):
        '''
        Determine intrapulse name from MS

        Parameters:
         * `ModStatus`: (string) ModStatus
        
        **Returns**: (string) Intrapulse name
        '''
        # TODO: Determine and associate names for intrapulses, insert ModeName if ModStatus is false

        if ModStatus == "false":
            return "N/A"
        else:
            return '"ModeName"'

    @staticmethod
    def get_four_decimal(number):
        # type: (int) -> float
        '''
        Format to 4 decimal places and absolute value

        Parameters:
         * `number`: (number) Number
        
        **Returns**: (string) Number
        '''
        return '{:.4f}'.format(abs(float(number)))

    @staticmethod
    def get_three_decimal(number):
        # type: (int) -> float
        '''
        Format to 3 decimal places

        Parameters:
         * `number`: (number) Number
        
        **Returns**: (string) Number
        '''
        return '{:.3f}'.format(float(number))

    @staticmethod
    def get_six_decimal(number):
        # type: (int) -> float
        '''
        Format to 6 decimal places

        Parameters:
         * `number`: (number) Number
        
        **Returns**: (string) Number
        '''
        return '{:.6f}'.format(float(number))

    @staticmethod
    def bool_yn(boolean):
        # type: (bool) -> str

        return "YES" if boolean else "NO"
    
    @staticmethod
    def ae_to_vh(az_el):
        # type (str) -> str

        if az_el == "Azimuth":
            return "HORIZONTAL"
        else:
            return "VERTICAL"


def flatten_table(ceesim_data, stack_size=1):
    # type: (dict, int) -> dict
    '''
    Flattens a table

    Parameters:
     * `ceesim_data`: (dictionary) Import ceesim_data from JSON
     * `stack_size`: (int) Number of function calls in recursive mode
    
    **Returns**: (dictionary) Flattened 1 level table
    '''
    logger.debug(
        'Flattening input table with call stack size at {}'.format(stack_size))
    data_ = dict()
    for key in ceesim_data:
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


def convert_one_key(lookup_data, values, keep_tag=True):
    # type: (dict, List[str], bool) -> str
    '''
    Converts one key given the table lookup parameters

    Parameters:
     * `lookup_data`: (dictionary) Lookup data inputted in JSON
     * `values`: (any) Value to convert
     * `keep_tag`: Whether or not to keep the left hand tag side
    
    **Returns**: Converted string
    '''
    if FUNC_HDR in lookup_data and hasattr(functions, lookup_data[FUNC_HDR]):
        funcp_data = getattr(functions, lookup_data[FUNC_HDR])(*values)
    elif values:
        if len(values) > 1:
            logger.warn('Cannot find conversion function ({}) for tag with two inputs.'.format(lookup_data[FUNC_HDR]))
        funcp_data = values[0]
    else:
        funcp_data = lookup_data["DEFAULT"]

    if lookup_data[STRING_HDR]:
        funcp_data = '"{}"'.format(funcp_data)
    
    if not keep_tag:
        return funcp_data

    if len(lookup_data["LABEL"]) >= 19:
        return '{} : {}'.format(lookup_data["LABEL"], funcp_data)
    else:
        return '{:<20}{}'.format(lookup_data["LABEL"] + ":", funcp_data)


def obtain_relevant_tags(ceesim_data, ceesim_flattened, tag, fast=True):
    # type: (dict, dict, str, bool) -> list
    '''
    Checks the imported data for relevant data

    Parameters:
     * `ceesim_data`: (dictionary) JSON ceesim data
     * `ceesim_flattened`: (dictionary, optional) Flattened JSON ceesim data
     * `tag`: (string) Name of tag
     * `fast`: (boolean) Fast mode, requires ceesim_flattened
    
    **Returns**: (list) List of relevant tags
    '''
    if ceesim_flattened is not None and fast and tag in ceesim_flattened:
        return [ceesim_flattened[tag]]
    else:
        acc = list()
        for k, v in ceesim_data.items():
            if type(v) is dict:
                assert k != tag, '{} had subelements when elements were looking in array!'.format(
                    k)
                acc += obtain_relevant_tags(v, None, tag, fast=False)
            elif type(v) is list:
                if k == tag:
                    logger.warn(
                        '{} had subelements that were not checked due to multidict encountered! Adding size {} to list').format(
                            k, len(v))
                    acc += v
                else:
                    for i in v:
                        acc += obtain_relevant_tags(i, None, tag, fast=False)
            elif k == tag:
                acc.append(v)
        return acc


def generate_other_models(ceesim_data, ceesim_flattened, lookup_table):
    # type: (dict, dict, dict) -> list
    '''
    Generate all non INP/PUL models

    Parameters:
     * `ceesim_data`: (dictionary) Imported CEESIM JSON data
     * `ceesim_flattened`: (dictionary, optional) Flattened CEESIM JSON data
     * `lookup_table`: (dictionary) Lookup table JSON imported
    
    **Returns**: (list) List of models
    '''
    logger.debug('Now generating all non-signal models')

    def fill_table(model, pos, value):
        # type: (model, int, str) -> None
        '''
        Fills out table from model with values

        Parameters:
         * `model`: (model class object) Model object
         * `pos`: (int) Position index
         * `value`: (str) Value to fill
        
        **Returns**: None, table is filled in-place
        '''
        if len(model.converted_data) <= pos:
            model.converted_data += [''] * \
                (pos - len(model.converted_data) + 1)
        model.converted_data[pos] = value

    def create_converted(model, opt):
        # type: (model, list) -> None
        '''
        Converts in-place model

        Parameters:
         * `model`: (model class object) Model object
         * `opt`: (list) Options from lookup table
        
        **Returns**: None, table is filled in place
        '''

        if type(opt["TABLE"]) is int:
            table_string = build_table_str(ceesim_data, lookup_table, opt[FILE_HDR], opt["SECTION"], 
                                        opt[PRI_HDR], convert_one_key, obtain_relevant_tags, opt[FILE_HDR] == "ANT")
            fill_table(model, opt[PRI_HDR], table_string)
            return None

        values = []
        for tag in opt[TAG_HDR].split('&'):
            tags = obtain_relevant_tags(ceesim_data, ceesim_flattened, tag) # removed taking the zero-index as it's done below
            if tags:
                value = tags[0]  
                logger.debug("Found tag {} for {} in {} with value: {}".format(opt[TAG_HDR],
                                                                            opt["LABEL"], opt[FILE_HDR], value))
            else:
                if opt[TAG_HDR]:
                    logger.debug('Could not find tag {}, using default value for {} in {}: {}'.format(opt[TAG_HDR],
                                                                                                    opt["LABEL"], opt[FILE_HDR], opt[DEFAULT_HDR]))
                else:
                    logger.debug('Using default value for tagless {} in {}: {}'.format(
                        opt["LABEL"], opt[FILE_HDR], opt[DEFAULT_HDR]))
                value = opt[DEFAULT_HDR]
            values.append(value)

        converted = convert_one_key(opt, values)
        fill_table(model, opt[PRI_HDR], converted)


    def add_headers(mfile, model):
        # type: (str, model) -> None
        '''
        Adds headers to converted model

        Parameters:
         * `mfile`: (string) Name of file
         * `model`: (model) Model class object

        **Returns**: None, data is converted in place
        '''
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
                    htext = "//" + ' '.join(
                        ['*' * lleft, header[1], '*' * right])
                    h_priority = int(header[3])
                    if determine_scan_type(ceesim_data) == "LORO" and mfile == "SIG" and (header[1] == "ANTENNA MODEL" or header[1] == "MULTIPLE SIMULTANEOUS SIGNALS"):
                        h_priority += 3
                    fill_table(model, h_priority, htext)
    models = list()
    name = form_model_name(ceesim_data, ceesim_flattened)
    timestamp = obtain_relevant_tags(ceesim_data, ceesim_flattened, "LastUpdateDate")[0]
    logger.debug('Generic model generator using name: {}'.format(name))
    for mtype in AUTO_MODELS:
        next_model = model(mtype, name, timestamp)
        if mtype not in MODEL_FILES:
            logger.warn(
                'Could not find mtype {} in model files, skipping'.format(mtype))
            continue
        print("!!! mtype: {} name: {}".format(mtype, name))
        table_key = MODEL_FILES[mtype]
        add_headers(table_key, next_model)
        if table_key not in lookup_table:
            logger.warn(
                'Could not find key {} in lookup table, skipping'.format(table_key))
            continue
        logger.debug(
            'Now processing table key {} with mtype {}'.format(table_key, mtype))
        for cdict_key in lookup_table[table_key]:
            key_data = lookup_table[table_key][cdict_key]
            if MULTI_HDR in key_data and TABLE_DATA in key_data:
                data_opts = key_data[TABLE_DATA]
                for opt in data_opts:
                    if opt["SECTION"] == "Main":
                        continue
                    create_converted(next_model, opt)
            else:
                if key_data["SECTION"] == "Main":
                    continue
                create_converted(next_model, key_data)

        models.append(next_model)
    


    inp_deviations = obtain_relevant_tags(ceesim_data, ceesim_flattened, "LinearFreqDeviation")
    inp_durations = obtain_relevant_tags(ceesim_data, ceesim_flattened, "LinearFreqDuration")
    inp_info = zip(inp_deviations, inp_durations)
    print("inp_deviations________: {}".format(len(inp_deviations)))

    #for i, _ in enumerate(inp_deviations):
    #    print(i)
    #    pass
    numModels = len(models)

    count = 1
    for i, info in enumerate(inp_info):
        newName = "{}-{}".format(name, i + 1)
        print('INTRAPULSE {}: {}'.format(count, info[0]))
        next_model = model('INTRAPULSE', newName, timestamp)
        table_key = MODEL_FILES['INTRAPULSE']
        add_headers(table_key, next_model)
        if table_key not in lookup_table:
            logger.warn(
                'Could not find key {} in lookup table, skipping'.format(table_key))
            continue
        logger.debug(
            'Now processing table key {} with mtype {}'.format(table_key, 'INTRAPULSE'))
        print("??? deviation: {} name: {}".format(info[0], newName))
        if 'INTRAPULSE' not in MODEL_FILES:
            logger.warn(
                'Could not find mtype {} in model files, skipping'.format(info[0]))
        count += 1

        for cdict_key in lookup_table[table_key]:
            key_data = lookup_table[table_key][cdict_key]
            if MULTI_HDR in key_data and TABLE_DATA in key_data:
                data_opts = key_data[TABLE_DATA]
                for opt in data_opts:
                    if opt["SECTION"] == "Main":
                        continue
                    create_converted(next_model, opt)
            else:
                if key_data["SECTION"] == "Main":
                    continue
                if not key_data["TAG"]:
                    create_converted(next_model, key_data)
                else:
                    if key_data["TAG"] == "LinearFreqDeviation":
                        fill_table(next_model, key_data[PRI_HDR], convert_one_key(key_data, [info[0]]))
                    if key_data["TAG"] == "LinearFreqDeviation&LinearFreqDuration":
                        fill_table(next_model, key_data[PRI_HDR], convert_one_key(key_data, info))

        models.append(next_model)

    numInpDeviations = len(models) - numModels
    print("numInpDeviations: {}".format(numInpDeviations))

    #for mtype in INTRAPULSE_NAME
    #    next_model = model(mtype, name + i, timestamp)
    #    if mtype not in INTRAPULSE_NAME:
    #        logger.warn(
    #            'Could not find mtype {} in model files, skipping'.format(mInput))
        # table_key = MODEL_FILES[mtype]
        # add_headers(table_key, next_model)
        # if table_key not in lookup_table:
        #     logger.warn(
        #         'Could not find key {} in lookup table, skipping'.format(table_key))
        #     continue
        # logger.debug(
        #     'Now processing table key {} with mtype {}'.format(table_key, mtype))
        # for cdict_key in lookup_table[table_key]:
        #     key_data = lookup_table[table_key][cdict_key]
        #     if MULTI_HDR in key_data and TABLE_DATA in key_data:
        #         data_opts = key_data[TABLE_DATA]
        #         for opt in data_opts:
        #             if opt["SECTION"] == "Main":
        #                 continue
        #             create_converted(next_model, opt)
        #     else:
        #         if key_data["SECTION"] == "Main":
        #             continue
        #         create_converted(next_model, key_data)
    

    #for i, _ in enumerate(inp_deviations):
    #    pass
        # next_model = model("INTRAPULSE", name + i, timestamp)
        # if mtype not in MODEL_FILES:
        #     logger.warn(
        #         'Could not find mtype {} in model files, skipping'.format(mtype))
        #     continue
        # table_key = MODEL_FILES[mtype]
        # add_headers(table_key, next_model)
        # if table_key not in lookup_table:
        #     logger.warn(
        #         'Could not find key {} in lookup table, skipping'.format(table_key))
        #     continue
        # logger.debug(
        #     'Now processing table key {} with mtype {}'.format(table_key, mtype))
        # for cdict_key in lookup_table[table_key]:
        #     key_data = lookup_table[table_key][cdict_key]
        #     if MULTI_HDR in key_data and TABLE_DATA in key_data:
        #         data_opts = key_data[TABLE_DATA]
        #         for opt in data_opts:
        #             if opt["SECTION"] == "Main":
        #                 continue
        #             create_converted(next_model, opt)
        #     else:
        #         if key_data["SECTION"] == "Main":
        #             continue
        #         create_converted(next_model, key_data)
        
        # models.append(next_model)
    
    
    return models


def form_model_name(ceesim_data, ceesim_flattened):
    # type: (dict, dict) -> str
    '''
    Returns the first return type from obtain_relevant_tags

    Parameters:
     * `ceesim_data`: (dictionary, technically optional) CEESIM data imported
     * `ceesim_flattened`: (dictionary) Flattened CEESIM imports
    
    **Returns**: (string) Model name
    '''
    return obtain_relevant_tags(ceesim_data, ceesim_flattened, "ModeName")[0]


def determine_scan_type(ceesim_data):
    # type: (dict) -> str
    '''
    Determines the scan type

    Parameters:
     * `ceesim_data`: (dictionary) CEESIM data imported JSON
    
    **Returns**: (string) Scan type
    '''
    quick_tag = lambda x: obtain_relevant_tags(ceesim_data, None, x)
    az_scan = quick_tag("AzScanKind")
    el_scan = quick_tag("ElScanKind")

    if len(az_scan) > 1 and (az_scan[0] == "Circular" or el_scan[0] == "Circular"):
        return "HELICAL"
    elif not az_scan and not el_scan and quick_tag("RasterFlybackStatus"):
        return "RASTER"
    elif az_scan[0] == "Steady" and el_scan[0] == "Steady":
        return "LORO"
    elif az_scan[0] == "Circular" or el_scan[0] == "Circular":
        return "CIRCULAR"
    else:
        return "SECTOR"


def generate_intrapulse(ceesim_data, lookup_table):
    # type: (dict, dict) -> List[model]
    '''
    Converts intrapulse signals in an imported table using a lookup table

    Parameters:
     * `ceesim_data`: (dictionary) Imported CEESIM data
     * `lookup_table`: (dictionary) Lookup table as JSON
    
    **Returns**: (list of models) List of intrapulse models
    '''
    logger.debug("Now generating the intrapulse models")

    for filetype in lookup_table:
        if filetype is INTRAPULSE_NAME:
            for tag in filetype:

                tag_data = lookup_table[INTRAPULSE_NAME][tag]

                if MULTI_HDR in tag_data:
                    for feature_data in tag_data["DATA"]:
                        convert_one_key(
                            feature_data, [ceesim_data[feature_data["TAG"]]])
                else:
                    # TODO: What if table is flat
                    pass
    # TODO: Return data


def generate_pulse(ceesim_data, lookup_table):
    # type: (dict, dict) -> List[model]
    '''
    Converts pulse signals in an imported table using a lookup table

    Parameters:
     * `ceesim_data`: (dictionary) CEESIM imported JSON data
     * `lookup_table`: (dictionary) Lookup table as JSON
    
    **Returns**: (list of models) List of pulse models
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
                            feature_data, [ceesim_data[feature_data["TAG"]]])
                else:
                    # TODO: What if table is flat
                    pass
    # TODO: Return data


ITERATOR_KEYS = ('Scenario', 'Platforms', 'Platform')
SEARCH_TO_RETURN_KEYS = ('Emitters', 'Emitter', 'EmitterModes', 'EmitterMode')


def split_emitter_modes(ceesim_data):
    # type: (dict) -> List[dict]
    '''
    Converts CEESIM data to a list of emitter mode dicts

    Parameters:
     * `ceesim_data`: (dictionary) CEESIM imported data JSON
    
    **Returns**: (list of dictionaries) Emitter modes list
    '''
    def split_emitter_modes_helper(data):
        # type: (dict) -> List[dict]
        '''
        Helper function that returns inside frame

        Parameters:
         * `data`: (dictionary) Sub-dict
        
        **Returns**: (list of dictionaries) Emitter modes inside the frame
        '''
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
    '''
    Convert CEESIM data to A²PATS data

    Parameters:
     * `ceesim_data`: (ceesim class object) CEESIM emitter mode data to import
     * `lookup_table`: (dictionary) Looktable table JSON
    
    **Returns**: (a2pats class object) A2PATS data
    '''
    logger.info('Beginning CEESIM to A2PATS conversion')
    flattened_data = flatten_table(ceesim_data)
    store = a2pats(imported_type='A2PATS')
    generic_models = generate_other_models(
        ceesim_data, flattened_data, lookup_table)
    logger.debug('Added {} models from generate_other_models'.format(
        len(generic_models)))
    store.models += generic_models
    return store


def convert(data):
    # type: (Union[a2pats, ceesim]) -> Union[a2pats, ceesim]
    '''
    Dynamically convert data to its corresponding format

    Parameters:
     * `data`: (a2pats or ceesim class object) A²PATS or CEESIM data to import

    **Returns**: (a2pats or ceesim class object) A²PATS or CEESIM data
    '''
    if type(data) is a2pats:
        return None
    elif type(data) is ceesim:
        return convert_to_a2pats(data)
    elif isinstance(data, datastore):
        logger.warn('Provided type to convert was correct, but unrecognized')
        return data.to_datastore()
    else:
        raise DatastoreError(
            'Provided type to convert was neither of class a2pats or ceesim.')


if __name__ == '__main__':
    logger.error('You cannot call this file directly!')