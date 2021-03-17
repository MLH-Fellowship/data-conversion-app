//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test_Sig4
//
// Created: Thu Jan 21, 2021  11:11 AM

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "TOUR OF DUTY EXAMPLE SIGNAL 4"
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "NSIN1"
SYSTEM NAME:        "68EWS"
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

FREQUENCY NOTES:    ""

FREQUENCY MODEL:    STAGGER

     FREQUENCY      REPEAT COUNT
       (MHZ)      
   5400.0000000000           10 
   5450.0000000000           10 
   5550.0000000000           10 
   5500.0000000000           10 
   5600.0000000000           10 
   5650.0000000000           10 
   5700.0000000000           10 
   6750.0000000000           10 
   5800.0000000000           10 
   6000.0000000000           10 

FREQUENCY FILL:     NONE

REPEAT COUNT FILL:  NONE

SYNC TO SCAN:       NO

//********************** SCAN MODEL ***********************

SCAN NOTES:         ""

SCAN MODEL:         LORO

AZIMUTH OFFSET:     0.000 DEG
ELEVATION OFFSET:   0.000 DEG

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL *********************

ANTENNA NOTES:      ""

ANTENNA MODEL:      RECTANGULAR

BEAM MODEL:         AZIMUTH

MAIN LOBE WIDTH:    5.000 DEG
DISTRIBUTION:       SIN X/X
PHASED ARRAY:       NO

            LOBE       LOBE    LOBE 
         ATTENUATION  WIDTH   REPEAT
            (DB)      (DEG)   COUNT 
  +/-    20.0000     N/A        1 
  +/-    25.0000     N/A        1 

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

BEAM MODEL:         ELEVATION

MAIN LOBE WIDTH:    5.000 DEG
DISTRIBUTION:       SIN X/X
PHASED ARRAY:       NO

            LOBE       LOBE    LOBE 
         ATTENUATION  WIDTH   REPEAT
            (DB)      (DEG)   COUNT 
  +/-    20.0000     N/A        1 
  +/-    25.0000     N/A        1 

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO
