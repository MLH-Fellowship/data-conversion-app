from app.errors import DatastoreError
from arrow import utcnow

ALLOWED_MODELS = {
    'SIGNAL',
    'PULSE',
    'PULSE SEQUENCE',
    'SCAN',
    'ANTENNA',
    'FREQUENCY'
}


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
        assert type in ALLOWED_MODELS, 'Model type was not an allowed type!'
        self.type = type
        self.name = name
        self.creation_date = creation_date
        self.data = list()


class SIGNAL(model):

    def __init__(self, name, database, nato, system, version, mode, creation_date=utcnow()):
        self.database = database
        self.classifcation = "UNCLASSIFIED"
        self.nato = nato
        self.system = system
        self.version = version
        self.mode = mode
        self.enable_doppler = "NO"
        self.enable_multipath = "NO"
        self.enable_mss = "NO"

        super().__init__("SIGNAL", name, creation_date)


class PULSE(model):

    def __init__(self, name, use_ref_frequency, use_ref_scan, non_coherent,
                 time_stagger, pri_timing_mode, pw_timing_mode,
                 use_local_freq, pri_fill, pw_fill, pulse_repeat_fill, dwell_time_fill,
                 attenuation_fill, frequency_fill, creation_date=utcnow()):
        self.sig_model = "SEQUENCE REFERENCE"
        self.urf = use_ref_frequency
        self.urs = use_ref_scan
        self.non_coherent = non_coherent

        self.pul_model = time_stagger
        self.pri_tm = pri_timing_mode
        self.pw_tm = pw_timing_mode
        self.ulf = use_local_freq
        self.pri_fill = pri_fill
        self.pw_fill = pw_fill
        self.pr_fill = pulse_repeat_fill
        self.dt_fill = dwell_time_fill
        self.a_fill = attenuation_fill
        self.f_fill = frequency_fill

        super().__init__("PULSE", name, creation_date)


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
