//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test_Sig3
//
// Created: Thu Jan 21, 2021  11:05 AM

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "TOUR OF DUTY EXAMPLE SIGNAL 3"
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "NSIN1"
SYSTEM NAME:        "68EWS"
VERSION:            "3"
MODE:               "3"

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO
ENABLE MULTIPATH:   NO

//********************** PULSE MODEL **********************

PULSE NOTES:        ""

PULSE MODEL:        STAGGER

PRI TIMING MODE:    TIME

PW TIMING MODE:     TIME

        PRI              PW                                                                                                                                   INTRAPULSE                                                                                                                                PULSE             DWELL           ATTENUATION     FREQUENCY    
       (USEC)          (USEC)                                                                                                                                    NAME                                                                                                                                  REPEAT             (MSEC)             (DB)           (MHZ)      
          50.00000       10.00000  "Test3_Intra_Pulse_1_2"                                                                                                                                                                                                                                                   100           N/A               0.0000     5500.0000000000
          50.00000       10.00000  "Test3_Intra_Pulse_1_2"                                                                                                                                                                                                                                                    90           N/A               0.0000     5600.0000000000
          48.00000        9.60000  "Test3_Intra_Pulse_3_4"                                                                                                                                                                                                                                                    90           N/A               0.0000     5750.0000000000
          48.00000        9.60000  "Test3_Intra_Pulse_3_4"                                                                                                                                                                                                                                                    80           N/A               0.0000     5806.0000000000
          40.00000        8.00000  "Test3_Intra_Pulse_5"                                                                                                                                                                                                                                                      80           N/A               0.0000     5859.0000000000
          36.00000        7.00000  "Test3_Intra_Pulse_6"                                                                                                                                                                                                                                                      70           N/A               0.0000     5990.0000000000
          28.00000        5.60000  "Test3_Intra_Pulse_7"                                                                                                                                                                                                                                                      70           N/A               0.0000     6420.0000000000
          20.00000        4.00000  "Test3_Intra_Pulse_8"                                                                                                                                                                                                                                                      60           N/A               0.0000     6870.0000000000
          15.00000        3.00000  "Test3_Intra_Pulse_9"                                                                                                                                                                                                                                                      60           N/A               0.0000     7000.0000000000

USE LOCAL FREQ:     YES

PRI FILL:           NONE

PW FILL:            NONE

PULSE REPEAT FILL:  NONE

DWELL TIME FILL:    NONE

ATTENUATION FILL:   NONE

FREQUENCY FILL:     NONE

NON-COHERENT:       NO

SYNC TO SCAN:       NO

//******************* INTRAPULSE MODEL ********************

INTRAPULSE NOTES:   ""

INTRAPULSE MODEL:   OFF

//******************** FREQUENCY MODEL ********************

FREQUENCY NOTES:    ""

FREQUENCY MODEL:    STABLE

FREQUENCY:          100.0000000000 MHZ

SYNC TO SCAN:       NO

//********************** SCAN MODEL ***********************

SCAN NOTES:         ""

SCAN MODEL:         CIRCULAR

AZIMUTH OFFSET:     0.000 DEG
ELEVATION OFFSET:   7.500 DEG
SCAN PERIOD:        10.00000 SEC
ROTATION:           CW

PULSE TRIG ON REV:  NO

OVERLAY MODEL:      SCRIPT

SCRIPT:             "el_begin;|rpos(1.5,0.005);|rpos(3.0,0.0045);|rpos(4.5,0.00432);|rpos(6.0,0.00384);|rpos(7.5,0.0032);|rpos(9.0,0.00252);|rpos(10.5,0.00196);|rpos(12,0.0012);|rpos(13.5,0.0009);|rel_end;"

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL *********************

ANTENNA NOTES:      ""

ANTENNA MODEL:      RECTANGULAR

BEAM MODEL:         AZIMUTH

MAIN LOBE WIDTH:    2.200 DEG
DISTRIBUTION:       SIN X/X
PHASED ARRAY:       NO

            LOBE       LOBE      LOBE      LOBE 
         ATTENUATION  WIDTH   SEPARATION  REPEAT
            (DB)      (DEG)     (DEG)     COUNT 
  +/-    15.0000     N/A       3.000        1 
  +/-    25.0000     N/A       2.000        1 

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

BEAM MODEL:         ELEVATION

MAIN LOBE WIDTH:    2.000 DEG
DISTRIBUTION:       SIN X/X
PHASED ARRAY:       NO

            LOBE       LOBE      LOBE      LOBE 
         ATTENUATION  WIDTH   SEPARATION  REPEAT
            (DB)      (DEG)     (DEG)     COUNT 
  +/-    15.0000     N/A       3.000        1 
  +/-    25.0000     N/A       2.000        1 

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO
