//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   A123Z_TEST01
//
// Created: 2021-01-21T17:26:11

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "A123Z"
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "NSIN-EMITTER"
SYSTEM NAME:        "A123Z_TEST01"
VERSION:            "A123Z_TEST01"
MODE:               "A123Z_TEST01"

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO
ENABLE MULTIPATH:   NO

//********************** PULSE MODEL **********************

PULSE MODEL:        SEQUENCE REFERENCE

MODEL NAME:         "PulName"
USE REF FREQUENCY:  YES
USE REF SCAN:       NO

NON-COHERENT:       NO

//******************* INTRAPULSE MODEL ********************

INTRAPULSE NOTES:   ""

INTRAPULSE MODEL:   OFF

//******************** FREQUENCY MODEL ********************

FREQUENCY NOTES:    ""

FREQUENCY MODEL:    STABLE

FREQUENCY:          5000000000 MHZ

SYNC TO SCAN:       NO

//********************** SCAN MODEL ***********************

SCAN MODEL:         REFERENCE

MODEL NAME:         "ScanName"

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL *********************

ANTENNA MODEL:      REFERENCE

MODEL NAME:         "AntName"

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO
