from app.errors import DatastoreError
from arrow import utcnow


class model:
    '''Contains a simple model
    '''
    
    def __init__(self, type: str, name: str, creation_date=utcnow(), **kwargs):
        '''Create a model

        :param type: Type of model
        :type type: str

        :param name: Name of model
        :type name: str

        :param creation_date: Timestamp of creation
        :type creation_date: Arrow
        '''
        self.type = type
        self.name = name
        self.creation_date = creation_date

class datastore:
    '''Contains all generated signals in a Pythonic format
    '''

    def __init__(self):
        '''Create a datastore
        '''
        self.models = list()

    def to_datastore(self, downgrade_peaceful=True) -> 'datastore':
        '''Convert a datastore child to a datastore parent.

        :param downgrade_peaceful: Whether or not to downgrade peacefully when function is called
        :type downgrade_peaceful: bool

        :returns: Datastore object
        :rtype: datastore

        note:: Parent function should not be called in normal usage
        '''
        if downgrade_peaceful:
            return self
        else:
            raise DatastoreError(
                'You cannot call to_datastore on a parent datastore object!')


class a2pats(datastore):
    '''Contains all generated signals in an A²PATS format
    '''

    def to_datastore(self) -> datastore:
        '''Initialize A²PATS to datastore
        '''
        # TODO

    def export(self, file: str) -> bool:
        '''Exports A²PATS to file

        :param file: File location to export to
        :type file: str

        :returns: Success of export
        :rtype: bool
        '''
        # TODO
        return True


class ceesim(datastore):
    '''Contains all generated signals in a CEESIM format
    '''

    def to_datastore(self) -> datastore:
        '''Initialize CEESIM to datastore
        '''
        # TODO
        pass

    def export(self, file: str) -> bool:
        '''Exports CEESIM to file

        :param file: File location to export to
        :type file: str

        :returns: Success of export
        :rtype: bool
        '''
        # TODO
        return True
