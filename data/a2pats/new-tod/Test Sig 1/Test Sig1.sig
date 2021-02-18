//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test Sig1
//
// Created: Wed Feb 17, 2021  12:27 PM

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      ""
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "NSIN1"
SYSTEM NAME:        "68EWS"
VERSION:            "1"
MODE:               "1"

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO
ENABLE MULTIPATH:   NO

//********************** PULSE MODEL **********************

PULSE MODEL:        SEQUENCE REFERENCE

MODEL NAME:         "Test_Sig1"
USE REF FREQUENCY:  YES
USE REF SCAN:       NO

NON-COHERENT:       NO

//******************* INTRAPULSE MODEL ********************

INTRAPULSE NOTES:   ""

INTRAPULSE MODEL:   OFF

//******************** FREQUENCY MODEL ********************

FREQUENCY NOTES:    ""

FREQUENCY MODEL:    STABLE

FREQUENCY:          5000.0000000000 MHZ

SYNC TO SCAN:       NO

//********************** SCAN MODEL ***********************

SCAN MODEL:         REFERENCE

MODEL NAME:         "Test Sig 1 Scan"

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL *********************

ANTENNA MODEL:      REFERENCE

MODEL NAME:         "Test Sig 1 Ant"

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO
