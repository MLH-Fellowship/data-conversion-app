//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test Sig4
//
// Created: Wed Feb 17, 2021  2:57 PM

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "TOUR OF DUTY EXAMPLE SIGNAL 4"
CLASSIFICATION:     "SECRET"
NATO NAME:          "NSIN4"
SYSTEM NAME:        "68 EWS"
VERSION:            "4"
MODE:               "4"

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO
ENABLE MULTIPATH:   NO

//********************** PULSE MODEL **********************

PULSE MODEL:        SEQUENCE REFERENCE

MODEL NAME:         "Test4_Seq"
USE REF FREQUENCY:  NO
USE REF SCAN:       NO

NON-COHERENT:       NO

//******************* INTRAPULSE MODEL ********************

INTRAPULSE NOTES:   ""

INTRAPULSE MODEL:   OFF

//******************** FREQUENCY MODEL ********************

FREQUENCY MODEL:    REFERENCE

MODEL NAME:         "Test4_Freq"

SYNC TO SCAN:       NO

//********************** SCAN MODEL ***********************

SCAN NOTES:         ""

SCAN MODEL:         LORO

AZIMUTH OFFSET:     0.000 DEG
ELEVATION OFFSET:   0.000 DEG

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL *********************

ANTENNA MODEL:      REFERENCE

MODEL NAME:         "Test4_Ant"

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO
