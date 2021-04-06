//****************** SIGNAL DEFINITION FILE *******************
//
// Model:   A123Z_TEST05
//
// Created: Mon Jan 25, 2021  04:24 PM

//****************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "SIG EXPORT"
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "EMITTER"
SYSTEM NAME:        "A123Z"
VERSION:            "TES"
MODE:               "T05"

//******************** SPECIAL FEATURES ********************

ENABLE DOPPLER:     NO
ENABLE MULTIPATH:   NO

//********************** PULSE MODEL ***********************

PULSE MODEL:        SEQUENCE REFERENCE

MODEL NAME:         "A123Z_TEST05"
USE REF FREQUENCY:  YES
USE REF SCAN:       NO

NON-COHERENT:       NO

//******************* INTRAPULSE MODEL *******************

INTRAPULSE NOTES:   ""

INTRAPULSE MODEL:   OFF

//******************** FREQUENCY MODEL *********************

FREQUENCY NOTES:    ""

FREQUENCY MODEL:    STABLE

FREQUENCY:          1000.00 MHZ

SYNC TO SCAN:       NO

//********************** SCAN MODEL **********************

SCAN NOTES:         ""

SCAN MODEL:         LORO

AZIMUTH OFFSET:     "0.000 DEG"
ELEVATION OFFSET:   0.000 DEG

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL **********************

ANTENNA MODEL:      REFERENCE

MODEL NAME:         "A123Z_TEST05"

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO