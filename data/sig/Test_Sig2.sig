//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test_Sig2
//
// Created: Thu Jan 21, 2021  10:42 AM

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "TOUR OF DUTY EXAMPLE SIGNAL 2"
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "NSIN1"
SYSTEM NAME:        "68EWS"
VERSION:            "2"
MODE:               "2"

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO
ENABLE MULTIPATH:   NO

//********************** PULSE MODEL **********************

PULSE NOTES:        ""

PULSE MODEL:        PRI/PW

PRI TIMING MODE:    TIME

PW TIMING MODE:     TIME

PRI MODEL:          STAGGER

        PRI           REPEAT             DWELL         
       (USEC)          COUNT             (USEC)        
         500.00000            1           N/A          
         495.00000            1           N/A          
         490.00000            1           N/A          
         485.00000            1           N/A          
         480.00000            1           N/A          
         475.00000            1           N/A          
         470.00000            1           N/A          
         465.00000            1           N/A          
         460.00000            1           N/A          
         455.00000            1           N/A          
         450.00000            1           N/A          
         445.00000            1           N/A          
         440.00000            1           N/A          
         435.00000            1           N/A          
         430.00000            1           N/A          
         425.00000            1           N/A          
         420.00000            1           N/A          
         415.00000            1           N/A          
         410.00000            1           N/A          
         405.00000            1           N/A          

PRI FILL:           NONE

REPEAT COUNT FILL:  NONE

DWELL TIME FILL:    NONE

PW MODEL:           STABLE

PW:                 10.00000 USEC

NON-COHERENT:       NO

SYNC TO SCAN:       NO

//******************* INTRAPULSE MODEL ********************

INTRAPULSE NOTES:   ""

INTRAPULSE MODEL:   FM LINEAR

TYPE:               RAMP AND HOLD
MODE:               START ON CARRIER
DEVIATION:          1.5000000 MHZ
RATE:               0.150000 MHZ/USEC
INVERT:             NO

//******************** FREQUENCY MODEL ********************

FREQUENCY NOTES:    ""

FREQUENCY MODEL:    AGILE

MODULATION:         RAMP
RISE TIME:          100.00 %
INVERT:             NO
LOWER LIMIT:        8500.0000000000 MHZ
UPPER LIMIT:        9800.0000000000 MHZ
FREQUENCIES:        15
QUANTIZATION:       10.0000000000 MHZ

SYNC TO SCAN:       NO

//********************** SCAN MODEL ***********************

SCAN NOTES:         ""

SCAN MODEL:         RASTER

AZIMUTH OFFSET:     0.000 DEG
ELEVATION OFFSET:   0.000 DEG
MODE:               LEVEL
ORIENTATION:        HORIZONTAL
AZ WIDTH:           45.000 DEG
EL WIDTH:           30.000 DEG
LEVELS:             5

     SWEEP     SWEEP  SWEEP     TRANS     TRANS  TRANS  LEVEL      BAR   
     TIME      BLANK  TRIG      TIME      BLANK  TRIG   NUMBER  DIRECTION
    (MSEC)                     (MSEC)   
     1500.000   NO     NO        100.000   YES    NO       1    UP-RIGHT 
     1500.000   NO     NO        100.000   YES    NO       2    DOWN-LEFT
     1500.000   NO     NO        100.000   YES    NO       3    UP-RIGHT 
     1500.000   NO     NO        100.000   YES    NO       4    DOWN-LEFT
     1500.000   NO     NO        100.000   YES    NO       5    UP-RIGHT 


PULSE TRIG ENABLE:  NO

OVERLAY MODEL:      OFF

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM

//********************* ANTENNA MODEL *********************

ANTENNA NOTES:      ""

ANTENNA MODEL:      RECTANGULAR

BEAM MODEL:         AZIMUTH

MAIN LOBE WIDTH:    3.500 DEG
DISTRIBUTION:       SIN X/X
PHASED ARRAY:       NO

            LOBE       LOBE      LOBE      LOBE 
         ATTENUATION  WIDTH   SEPARATION  REPEAT
            (DB)      (DEG)     (DEG)     COUNT 
  +/-    25.0000     N/A       7.000        1 
  +/-    30.0000     N/A      10.000        1 
  +/-    33.0000     N/A      15.000        1 

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

BEAM MODEL:         ELEVATION

MAIN LOBE WIDTH:    5.000 DEG
DISTRIBUTION:       SIN X/X
PHASED ARRAY:       NO

            LOBE       LOBE      LOBE      LOBE 
         ATTENUATION  WIDTH   SEPARATION  REPEAT
            (DB)      (DEG)     (DEG)     COUNT 
  +/-    20.0000     N/A       9.000        1 
  +/-    35.0000     N/A      14.000        1 
  +/-    40.0000     N/A      18.000        1 

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO
