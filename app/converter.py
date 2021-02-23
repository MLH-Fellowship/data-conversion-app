from app.errors import DatastoreError
from app import a2pats, ceesim, datastore
from typing import Union a


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
