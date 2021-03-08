from app import a2pats, ceesim, datastore, model
from app.util.logging import logger
from io import IOBase
from typing import Iterator, Union, TextIO
from xml.etree import ElementTree


def traverse_xml_tree(parent: ElementTree.Element, stack_size=0) -> dict:
    logger.debug(f'Traversing down the XML tree, current stack iteration is: {stack_size}')
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


def strip_xml_namespaces(itr: Iterator) -> None:
    '''Strip XML namespaces from an iterator provided by XML parser
    '''
    logger.debug('Stripping all namespaces from imported CEESIM file...')
    for _, element in itr:
        if '}' in element.tag:
            element.tag = element.tag.split('}', 1)[1]
        for attribute in list(element.attrib.keys()):
            if '}' in attribute:
                new_attribute = attribute.split('}', 1)[1]
                element.attrib[new_attribute] = element.attrib[attribute]
                del element.attrib[attribute]


def import_a2pats(fp: TextIO) -> a2pats:
    '''Import an A²PATS file for conversion
    '''
    # TODO
    pass


def import_ceesim(fp: TextIO) -> ceesim:
    '''Import a CEESIM file for conversion
    '''
    itr = ElementTree.iterparse(fp)
    strip_xml_namespaces(itr)
    store = ceesim()
    # TODO: Add more models
    scan_data = model('SCAN', 'type', 'name')
    data = traverse_xml_tree(itr.root)
    # TODO: Replace type
    # TODO: Replace name
    store.models.append(scan_data)
    return store


def import_(fp: Union[str, TextIO], classtype=datastore, downgrade_peaceful=True) -> datastore:
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
            # Assume CEESIM import
            classtype = ceesim
        if type(fp) is str:
            logger.debug(f'Now opening file {fp} for import')
            try:
                fp = open(fp, encoding='utf-8')
            except:
                return datastore()
        elif not isinstance(fp, IOBase):
            return datastore()
    else:
        assert issubclass(
            classtype, datastore), 'Your import_ call must be of datastore or datastore-like type!'
        if type(fp) is str:
            logger.debug(f'Now opening file {fp} for import')
            fp = open(fp, encoding='utf-8')
        assert isinstance(
            fp, IOBase), 'Your import_ call must provide a valid files-like pointer or file path!'
    if classtype is a2pats:
        return import_a2pats(fp)
    elif classtype is ceesim:
        return import_ceesim(fp)
    else:
        raise ValueError('This type of datastore isn\'t supported yet!')
