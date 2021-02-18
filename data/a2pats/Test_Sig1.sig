//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test_Sig1
//
// Created: Thu Jan 21, 2021  10:42 AM

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "TOUR OF DUTY EXAMPLE SIG 1"
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "NSIN1"
SYSTEM NAME:        "68EWS"
VERSION:            "1"
MODE:               "1"

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO
ENABLE MULTIPATH:   NO

//********************** PULSE MODEL **********************

PULSE NOTES:        ""

PULSE MODEL:        PRI/PW

PRI TIMING MODE:    TIME

PW TIMING MODE:     TIME

PRI MODEL:          STABLE

PRI:                100.00000 USEC

PW MODEL:           STABLE

PW:                 5.00000 USEC

NON-COHERENT:       NO

SYNC TO SCAN:       NO

//******************* INTRAPULSE MODEL ********************

INTRAPULSE NOTES:   ""

INTRAPULSE MODEL:   OFF

//******************** FREQUENCY MODEL ********************

FREQUENCY NOTES:    ""

FREQUENCY MODEL:    STABLE

FREQUENCY:          5000.0000000000 MHZ

SYNC TO SCAN:       NO

//********************** SCAN MODEL ***********************

SCAN NOTES:         ""

SCAN MODEL:         CIRCULAR

AZIMUTH OFFSET:     0.000 DEG
ELEVATION OFFSET:   0.000 DEG
SCAN PERIOD:        1.00000 SEC
ROTATION:           CW

PULSE TRIG ON REV:  NO

OVERLAY MODEL:      OFF

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL *********************

ANTENNA NOTES:      ""

ANTENNA MODEL:      RECTANGULAR

BEAM MODEL:         AZIMUTH

MAIN LOBE WIDTH:    3.000 DEG
DISTRIBUTION:       SIN X/X
PHASED ARRAY:       NO

            LOBE       LOBE      LOBE      LOBE 
         ATTENUATION  WIDTH   SEPARATION  REPEAT
            (DB)      (DEG)     (DEG)     COUNT 
  +/-    23.0000     N/A       2.000        1 
  +/-    29.0000     N/A       1.200        1 

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

BEAM MODEL:         ELEVATION

MAIN LOBE WIDTH:    3.000 DEG
DISTRIBUTION:       SIN X/X
PHASED ARRAY:       NO

            LOBE       LOBE      LOBE      LOBE 
         ATTENUATION  WIDTH   SEPARATION  REPEAT
            (DB)      (DEG)     (DEG)     COUNT 
  +/-    23.0000     N/A       2.000        1 
  +/-    29.0000     N/A       1.200        1 

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO
