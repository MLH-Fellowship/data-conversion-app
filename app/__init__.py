from app.exporter import dump as dump_datastore
from arrow import utcnow
from json import dump
from typing import TextIO, Union

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
        self.data = kwargs


# 2021.03.09 Gideon Tong:
# I don't really think these SIGNAL or PULSE classes are necessary

class SIGNAL(model):

    def __init__(self, name, database, nato, system, version, mode, creation_date=utcnow()):
        self.database = database
        self.classifcation = 'UNCLASSIFIED'
        self.nato = nato
        self.system = system
        self.version = version
        self.mode = mode
        self.enable_doppler = 'NO'
        self.enable_multipath = 'NO'
        self.enable_mss = 'NO'

        super().__init__('SIGNAL', name, creation_date)


class PULSE(model):

    def __init__(self, name, use_ref_frequency, use_ref_scan, non_coherent,
                 time_stagger, pri_timing_mode, pw_timing_mode,
                 use_local_freq, pri_fill, pw_fill, pulse_repeat_fill, dwell_time_fill,
                 attenuation_fill, frequency_fill, creation_date=utcnow()):
        self.sig_model = 'SEQUENCE REFERENCE'
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

        super().__init__('PULSE', name, creation_date)


class datastore:
    '''Contains all generated signals in a Pythonic format
    '''

    def __init__(self, imported_data=dict(), imported_type='CEESIM'):
        '''Create a datastore
        '''
        self.imported_data = imported_data
        # TODO: Change logic if A2PATS importer written
        self.imported_type = imported_type
        self.models = list()

    def dump_imported_data(self, fp: Union[str, TextIO]) -> bool:
        '''Dumps imported data to a file

        :param fp: File pointer
        :type fp: str or file-like pointer

        :returns: True on success
        :rtype: boolean
        '''
        if type(fp) is str:
            fp = open(fp, 'w')
        dump(self.imported_data, fp, indent=4, sort_keys=True)

    def export(self, folder: str) -> bool:
        '''Exports dynamically

        :param folder: Folder location to export to
        :type folder: str

        :returns: Success of export
        :rtype: bool
        '''
        return dump_datastore(self, folder)


class a2pats(datastore):
    '''Contains all generated signals in an A²PATS format
    '''
    pass


class ceesim(datastore):
    '''Contains all generated signals in a CEESIM format
    '''
    pass
