from app.errors import DatastoreError


class datastore:
    '''Contains all generated signals in a Pythonic format
    '''

    def __init__(self):
        '''Create a datastore
        '''
        # TODO
        self.signals = None
        self.shifts = None
        self.keys = None

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
        pass


class ceesim(datastore):
    '''Contains all generated signals in a CEESIM format
    '''

    def to_datastore(self) -> datastore:
        '''Initialize CEESIM to datastore
        '''
        # TODO
        pass
