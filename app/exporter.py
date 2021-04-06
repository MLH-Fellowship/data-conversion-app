#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Exports to a file or a folder, does all the handling,
file writing, etc.

Once again, find the documentation online at
https://mlh-fellowship.github.io/hermes-docs
'''

from app import a2pats, ceesim, datastore, model, MODEL_FILES
from app.util.logger import logger
from datetime import datetime
from os import mkdir
from os.path import join, isdir, isfile
from sys import version_info

if version_info > (3, 5):
    from os import PathLike

CONSTANTS = {
    'header': {
        'length': 60,
        'title': 'DEFINITION FILE'
    },

    'model_desc': {
        'length': 58,
        'title': 'MODEL'
    },

    'mss': {
        'length': 73,
        'title': 'MULTIPLE SIMULTANEOUS SIGNALS'
    }
}


def to_timestamp(time, downgrade_peaceful=True):
    # type: (datetime, bool) -> str
    '''
    Convert a time to an A²PATS-compatible timestamp (ISO 8601)

    Parameters:
     * `time`: (Arrow, datetime, or datetime-like) Time or timestamp-like object
     * `downgrade_peaceful`: (boolean) Whether or not to ignore errors

    **Returns**: (string) ISO 8601 timestamp
    '''
    if type(time) is str:
        time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S")
    def to_str(obj): return time.strftime('%a %b %d, %Y  %I:%M %p')
    if downgrade_peaceful:
        try:
            return to_str(time)
        except:
            return to_str(None)
    assert type(time) is datetime, 'Timestamp must be either date object or string!'
    return to_str(time)


def to_str_section(data, sect='header'):
    # type: (model, str) -> str
    '''
    Create a header or model description for a model

    Parameters:
     * `data`: (model class object) Data to serialize
     * `sect`: (string) Section type

    **Returns**: (string) Serialized object
    '''
    assert type(data) is model, 'You can only convert sections of entire models!'
    left = (CONSTANTS[sect]['length'] -
            len(data.type) - len(CONSTANTS[sect]['title']) - 3) / 2
    lleft = int(left)
    right = lleft
    if lleft == left:
        left = lleft
        right = lleft + 1
    title = ' '.join(
        ['*' * lleft, data.type, CONSTANTS[sect]['title'], '*' * right])

    if sect == "header":
        lines = [title, '', ' {:<9}{}'.format('Model:', data.name), '',
                 ' {:<9}{}'.format('Created:', to_timestamp(data.creation_date))]
        return '\n'.join(['//' + line for line in lines])

    elif sect == "model_desc":
        top = ['//' + title, '{} NOTES:   ""'.format(data.type)] if data.type in \
            ["FREQUENCY", "INTRAPULSE"] else ['//' + title]
        lines = top + ['{} MODEL:'.format(data.type)]


def dump_a2pats_file(model_, folder):
    # type: (model, PathLike) -> bool
    '''
    Dump single A2PATS object

    Parameters:
     * `model_`: (model class object) Model object in A2PATS
     * `folder`: (string or path like string) Location to dump files
    
    **Returns**: (boolean) True on success
    '''
    logger.debug('Now exporting A2PATS model {}'.format(model_.name))
    filename = '{}.{}'.format(model_.name, MODEL_FILES[model_.type].lower())
    # NOTE: The following path joiner works best in Python 3.5+
    # due to the implemenation of os.path.join(path, *paths). If
    # you are the maintainer of this project please be assured
    # that os.path.join(path, *paths) does not accept all types
    # of PathLike objects and you can replace this with a call
    # to os.path.normpath or os.path.realpath should there
    # be issues on legacy versions of Python.
    filepath = join(folder, filename)
    header = to_str_section(model_)
    sections = [header, ''] + model_.converted_data
    try:
        with open(filepath, 'w') as fp:
            fp.write('\n'.join(sections))
        return True
    except:
        return False


def dump_a2pats(obj, folder):
    # type: (a2pats, PathLike) -> bool
    '''
    Dump A2PATS object

    Parameters:
     * `obj`: (a2pats class object) A2PATS object
     * `folder`: (str or Path like object) Folder location to export
    
    **Returns**: (boolean) True on success
    '''
    if isfile(folder):
        logger.error('{} is a filepath, a folder cannot be placed here. Aborting'.format(folder))
        return False
    if not isdir(folder):
        logger.debug('{} does not exist, creating folder'.format(folder))
        mkdir(folder)
    logger.info('Now exporting A2PATS to folder {}'.format(folder))
    for model_ in obj.models:
        dump_a2pats_file(model_, folder)
    return True


def dump(obj, folder, export_type=a2pats):
    # type: (datastore, PathLike, type) -> bool
    '''Dump data dynmically

    Parameters:
     * `obj`: (datastore class object) Datastore object
     * `folder`: (str or path like object) Folder location of export
     * `export_type`: (class) Export type
    
    **Returns**: (boolean) True on success
    '''
    logger.debug('Generic dump function called, auto-detcting type...')
    assert issubclass(
        type(obj), datastore), 'Your data must be a datastore-like object!'
    if type(obj) is a2pats:
        logger.debug('Detected A2PATS, exporting as A2PATS')
        return dump_a2pats(obj, folder)
    elif type(obj) is ceesim:
        logger.debug('Detected CEESIM, exporting as CEESIM')
        return None
    assert type(
        obj) is not export_type, 'You cannot auto-dump a datastore object!'


if __name__ == '__main__':
    logger.error('You cannot call this file directly!')
