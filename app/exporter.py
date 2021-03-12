from app import a2pats, ceesim, datastore, model
from app.util.logging import logger
from datetime import datetime
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

sample_data = {
    'ModeName': 'A123Z_TEST01',
    'CreationDate': '2021-01-21T17:26:11',
    'EmitterId': 'A123Z',
    'EmitterName': 'NSIN-EMITTER',
    'ComplexPriState': 'false',
    'DwellStatus': 'false',
    'Pri': 0.0001,
    'PulseWidth': 5e-06,
    'ModStatus': 'false',
    'Frequency': 5000000000,
    'AzScanKind': 'Circular',
    'AzInitialBeamOffset': 0,
    'ElInitialBeamOffset': 0,
    'AzScanPeriod': 1,
    'AzDirection': 'Clockwise',
    'ElScanMotion': 'Unidirectional',
    'ElDirection': 'Up',
    'ElTrackOffset': 0,
    'ElSectorWidth': 90,
    'ElScanPeriod': 1.048576,
    'AntennaModelKind': 'Elliptical',
    'AzScanShape': 'Sin(x)/x R1',
    'AzBeamwidth': 2.9443359375,
    'AzSidelobeRatio': -24,
    'ElBeamWidth': 2.5937594433,
    'ElSidelobeRatio': -24,
    'ElScanShape': 'Sin(x)/x R1'
}

# Certain units for numerical values need adjustment. Furthermore, the data needs to change format
# Boolean strings need switching to Python boolean


def to_timestamp(time, downgrade_peaceful=True):
    # type: (datetime, bool) -> str
    '''Convert a time to an A²PATS-compatible timestamp (ISO 8601)

    :param time: Time or timestamp-like object
    :type time: datetime

    :param downgrade_peaceful: Whether or not to downgrade peacefully when function is called
    :type downgrade_peaceful: bool

    :returns: ISO 8601 timestamp
    :rtype: str
    '''
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
    '''Create a header or model description for a model

    :param data: Data to serialize
    :type data: model

    :param sect: Section type
    :type sect: str

    :returns: Serialized object
    :rtype: str
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


def dump_a2pats(obj, folder):
    # type: (a2pats, PathLike) -> bool
    '''Dump A2PATS object

    :param obj: A2PATS object
    :type obj: A2PATS-like object

    :param folder: Folder location
    :type folder: str

    :returns: True on success
    :rtype: boolean
    '''
    # TODO
    return False


def dump_ceesim(obj, folder):
    # type: (ceesim, PathLike) -> bool
    '''Dump CEESIM object

    :param obj: CEESIM object
    :type obj: CEESIM-like object

    :param folder: Folder location
    :type folder: str

    :returns: True on success:
    :rtype: boolean
    '''
    # TODO
    return False


def dump(obj, folder, export_type=a2pats):
    # type: (datastore, PathLike, type) -> bool
    '''Dump data dynmically

    :param obj: Datastore object
    :type obj: datastore-like object

    :param folder: Folder location
    :type folder: str

    :returns: True on success
    :rtype: boolean
    '''
    logger.debug('Generic dump function called, auto-detcting type...')
    assert issubclass(
        type(obj), datastore), 'Your data must be a datastore-like object!'
    if type(obj) is a2pats:
        logger.debug('Detected A2PATS, exporting as A2PATS')
        return dump_a2pats(obj)
    elif type(obj) is ceesim:
        logger.debug('Detected CEESIM, exporting as CEESIM')
        return dump_ceesim(obj)
    assert type(
        obj) is not export_type, 'You cannot auto-dump a datastore object!'


if __name__ == '__main__':
    logger.error('You cannot call this file directly!')
