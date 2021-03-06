#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Imports files for handling

Once again, find the documentation online at
https://mlh-fellowship.github.io/hermes-docs
'''

from app import a2pats, ceesim, datastore
from app.util.logger import logger
from io import IOBase
from sys import version_info
from xml.etree import ElementTree

if version_info > (3, 5):
    from typing import Iterator, Union, TextIO


def traverse_xml_tree(parent, stack_size=0):
    # type: (ElementTree.Element, int) -> dict
    '''
    Traverse the XML tree and return it as a dictionary

    Parameters:
     * `parent`: Element tree to traverse
     * `stack_size`: (integer, optional) Stack size
    
    **Returns**: (dictionary) XML tree as dictionary
    '''
    if stack_size == 0:
        logger.debug('Now traversing XML tree beginning at initial stack')
    data = dict()
    for child in parent:
        if child.text:
            text = child.text.strip()
        if not text:
            text = traverse_xml_tree(child, stack_size + 1)
        if child.tag in data:
            if type(data[child.tag]) is not list:
                data[child.tag] = [data[child.tag]]
            data[child.tag].append(text)
        else:
            data[child.tag] = text
    return data


def strip_xml_namespaces(itr):
    # type: (Iterator) -> None
    '''
    Strip XML namespaces from an iterator provided by XML parser

    Parameters:
     * `itr`: Iterator from an ElementTree
    
    **Returns**: None, strip happens in place
    '''
    logger.debug('Stripping all namespaces from imported CEESIM file')
    for _, element in itr:
        if '}' in element.tag:
            element.tag = element.tag.split('}', 1)[1]
        for attribute in list(element.attrib.keys()):
            if '}' in attribute:
                new_attribute = attribute.split('}', 1)[1]
                element.attrib[new_attribute] = element.attrib[attribute]
                del element.attrib[attribute]


def import_a2pats(fp):
    # type: (TextIO) -> a2pats
    '''
    Import an A??PATS file for conversion

    Parameters:
     * `fp`: File pointer
    '''
    # TODO
    pass


def import_ceesim(fp):
    # type: (TextIO) -> ceesim
    '''
    Import a CEESIM file for conversion

    Parameters:
     * `fp`: File pointer

    **Returns**: Imported CEESIM object
    '''
    logger.debug('CEESIM importer called, begining CEESIM import with XML file')
    itr = ElementTree.iterparse(fp)
    strip_xml_namespaces(itr)
    data = traverse_xml_tree(itr.root)
    store = ceesim(data)
    return store


def import_(fp, classtype=datastore, downgrade_peaceful=True):
    # type: (Union[str, TextIO], type, bool) -> datastore
    '''Import data dynamically

    :param fp: File pointer or string to import file
    :type fp: str or file-like pointer

    :param classtype: Class type to import as (must be of instance datastore)
    :type classtype: datastore or datastore-like

    :param downgrade_peaceful: Whether or not to ignore errors
    :type downgrade_peaceful: bool

    :returns: Database object for typing
    :rtype: datastore or datastore-like
    '''
    logger.debug('Generic importer called, automatically detecting import type')
    if downgrade_peaceful:
        if not issubclass(classtype, datastore):
            # Assume CEESIM import
            logger.debug('Unable to determine type, assuming CEESIM')
            classtype = ceesim
        if type(fp) is str:
            logger.debug('Now opening file {} for import'.format(fp))
            try:
                fp = open(fp, encoding='utf-8')
            except:
                logger.debug('Failed to open, returning empty object')
                return datastore()
        elif not isinstance(fp, IOBase):
            logger.debug('Unrecognizable file pointer, returning empty object')
            return datastore()
    else:
        assert issubclass(
            classtype, datastore), 'Your import_ call must be of datastore or datastore-like type!'
        if type(fp) is str:
            logger.debug('Now opening file {} for import'.format(fp))
            fp = open(fp, encoding='utf-8')
        assert isinstance(
            fp, IOBase), 'Your import_ call must provide a valid files-like pointer or file path!'


    if classtype is a2pats:
        logger.debug('A2PATS file provided, importing as A2PATS')
        return import_a2pats(fp)
    elif classtype is ceesim:
        logger.debug('CEESIM file provided, importing as CEESIM')
        return import_ceesim(fp)
    else:
        raise ValueError('This type of datastore isn\'t supported yet!')


if __name__ == '__main__':
    logger.error('You cannot call this file directly!')
