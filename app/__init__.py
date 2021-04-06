#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
The entrypoint of the "app" Hermes package. Worth renaming
if you have the time. A nicely-generated documentation is available for this package
at https://mlh-fellowship.github.io/hermes-docs, or you can install the development
dependencies (no dependencies are required to actually run the package, they
are only for development) yourself to compile the HTML documentation yourself.

To compile such documentation (remember to hide source code):

```sh
pdoc --html --config show_source_code=False --output-dir docs app
```

The HTML documentation can be viewed locally without the need for a web server.
Should you want to update the online documentation, please see the GitHub
repository `mlh-fellowship/hermes-docs`.

### Python 2.x

This package is written for Python 2.x compatability. It has been tested on
Python 2.7, 3.7, 3.8, and 3.9. It is current cross-compatabile with those tested
versions of Python, but specifically requires Python 2.x compatability after
Python's 2.x end-of-life support due to the fact that the military likely
has computers that still only have Python 2.x on them.

### Purpose

This file contains dataclasses used for storing and import and
export of data. While implementing the full dataclass may make sense,
that has not been done at this time.

### Todo

A2PATS imports have not been handled, nor are they on the roadmap.
'''

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
    '''
    A simple, cross-compatabile model with both A2PATS and CEESIM
    '''

    def __init__(self, type, name, creation_date=datetime.utcnow(), **kwargs):
        # type: (str, str, datetime, dict) -> model
        '''
        Creates a simple-cross-compatabile model

        Parameters
         * `type`: (string) Type of model
         * `name`: (string) Name of model
         * `creation_date`: (Arrow, datetime, or other datetime-like-object) Timestamp of model creation

        Notes:
         * `creation_date` is unlikely to ever recieve an Arrow object, but it
           was used in development of the project. This is due to the fact that
           the military does not install dependencies

        **Returns**: (model class object) Model object created
        '''
        assert type in ALLOWED_MODELS, 'Model type was not an allowed type!'
        self.type = type
        self.name = name
        self.creation_date = creation_date
        self.data = kwargs
        self.converted_data = list()


class datastore:
    '''
    Contains all generated signals in a Pythonic format
    '''

    def __init__(self, imported_data=dict(), imported_type='CEESIM'):
        # type: (dict, str) -> datastore
        '''
        Create a datastore

        Parameters:
         * `imported_data`: (dictionary) Imported data
         * `imported_type`: (string) CEESIM or A2PATS

        **Returns**: (datastore class object) Datastore object
        '''
        self.imported_data = imported_data
        self.imported_type = imported_type
        self.models = list()

    def dump_imported_data(self, fp):
        # type: (Union[str, TextIO]) -> bool
        '''
        Dumps imported data to a file

        Parameters:
         * `fp`: (string or file pointer with .open() handler) File to import
        
        **Returns**: (boolean) Whether or not import was a success
        '''
        logger.info('Dumping imported data as JSON object...')
        if type(fp) is str:
            fp = open(fp, 'w')
        dump(self.imported_data, fp, indent=4, sort_keys=True)
        # As you can tell, we assume it's always successful
        return True


class a2pats(datastore):
    '''
    Contains all generated signals in an A²PATS format
    '''


class ceesim(datastore):
    '''
    Contains all generated signals in a CEESIM format
    '''
