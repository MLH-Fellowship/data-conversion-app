//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test Sig2
//
// Created: Wed Feb 17, 2021  1:14 PM

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "TOUR OF DUTY EXAMPLE SIGNAL 2"
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "NSIN1"
SYSTEM NAME:        "68 EWS"
VERSION:            "2"
MODE:               "2"

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO
ENABLE MULTIPATH:   NO

//********************** PULSE MODEL **********************

PULSE MODEL:        SEQUENCE REFERENCE

MODEL NAME:         "Test2_Seq"
USE REF FREQUENCY:  NO
USE REF SCAN:       NO

NON-COHERENT:       NO

//******************* INTRAPULSE MODEL ********************

INTRAPULSE MODEL:   REFERENCE

MODEL NAME:         "Test2_Intra_Pulse"

//******************** FREQUENCY MODEL ********************

FREQUENCY MODEL:    REFERENCE

MODEL NAME:         "Test2_Freq"

SYNC TO SCAN:       NO

//********************** SCAN MODEL ***********************

SCAN MODEL:         REFERENCE

MODEL NAME:         "Test2_Raster Scan"

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL *********************

ANTENNA MODEL:      REFERENCE

MODEL NAME:         "Test2_Ant"

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO
