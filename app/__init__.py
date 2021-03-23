#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.util.logger import logger
from datetime import datetime
from json import dump
from sys import version_info

if version_info > (3, 5):
    from typing import TextIO, Union

ALLOWED_MODELS = {
    'SIGNAL',
    'PULSE',
    'PULSE SEQUENCE',
    'SCAN',
    'ANTENNA',
    'FREQUENCY',
    'INTRAPULSE'
}

MODEL_FILES = {
    'SIGNAL': 'SIG',
    'PULSE': 'PUL',
    'PULSE SEQUENCE': 'PULSEQ',
    'SCAN': 'SCAN',
    'ANTENNA': 'ANT',
    'INTRAPULSE': 'INP'
}


class model:
    '''Contains a simple model
    '''

    def __init__(self, type, name, creation_date=datetime.utcnow(), **kwargs):
        # type: (str, str, datetime, dict) -> model
        '''Create a model

        :param type: Type of model
        :type type: str

        :param name: Name of model
        :type name: str

        :param creation_date: Timestamp of creation
        :type creation_date: Arrow
        '''
        assert type in ALLOWED_MODELS, 'Model type was not an allowed type!'
        self.type = type
        self.name = name
        self.creation_date = creation_date
        self.data = kwargs
        self.converted_data = list()


class datastore:
    '''Contains all generated signals in a Pythonic format
    '''

    def __init__(self, imported_data=dict(), imported_type='CEESIM'):
        # type: (dict, str) -> datastore
        '''Create a datastore
        '''
        self.imported_data = imported_data
        # TODO: Change logic if A2PATS importer written
        self.imported_type = imported_type
        self.models = list()

    def dump_imported_data(self, fp):
        # type: (Union[str, TextIO]) -> bool
        '''Dumps imported data to a file

        :param fp: File pointer
        :type fp: str or file-like pointer

        :returns: True on success
        :rtype: boolean
        '''
        logger.info('Dumping imported data as JSON object...')
        if type(fp) is str:
            fp = open(fp, 'w')
        dump(self.imported_data, fp, indent=4, sort_keys=True)


class a2pats(datastore):
    '''Contains all generated signals in an A²PATS format
    '''


class ceesim(datastore):
    '''Contains all generated signals in a CEESIM format
    '''
