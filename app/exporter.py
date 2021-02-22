from types import SimpleNamespace

sample_data = {"ModeName":"A123Z_TEST01", "CreationDate": "2021-01-21T17:26:11", "EmitterId": "A123Z",
    "EmitterName": "NSIN-EMITTER", "ComplexPriState": "false", "DwellStatus": "false", "Pri": 0.0001, "PulseWidth": 5e-06,
    "ModStatus": "false", "Frequency": 5000000000, "AzScanKind": "Circular", "AzInitialBeamOffset": 0, "ElInitialBeamOffset": 0,
    "AzScanPeriod": 1, "AzDirection": "Clockwise", "ElScanMotion": "Unidirectional", "ElDirection": "Up", "ElTrackOffset": 0,
    "ElSectorWidth": 90, "ElScanPeriod": 1.048576, "AntennaModelKind": "Elliptical", "AzScanShape": "Sin(x)/x R1", "AzBeamwidth": 2.9443359375,
    "AzSidelobeRatio": -24, "ElBeamWidth": 2.5937594433, "ElSidelobeRatio": -24, "ElScanShape": "Sin(x)/x R1"
    }

# Certain units for numerical values need adjustment. Furthermore, the data needs to change format
# Boolean strings need switching to Python boolean

def simple_file_writes(xml_dictionary):
    n = SimpleNamespace(**xml_dictionary)
    with open("SigName.sig", "wt") as sig:
        sig.write(f"""//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   {n.ModeName}
//
// Created: {n.CreationDate}

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""

DATABASE NAME:      "{n.EmitterId}"
CLASSIFICATION:     "UNCLASSIFIED"
NATO NAME:          "{n.EmitterName}"
SYSTEM NAME:        "{n.ModeName}"
VERSION:            "{n.ModeName}"
MODE:               "{n.ModeName}"

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

FREQUENCY:          {n.Frequency} MHZ

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
""")

    with open("PulName.pul", "wt") as pul:
        pul.write(f"""//****************** PULSE DEFINITION FILE ******************
//
// Model:   {n.ModeName}
//
// Created: {n.CreationDate}


//********************** PULSE MODEL **********************

PULSE NOTES:        ""

PULSE MODEL:        {n.ComplexPriState}

PRI TIMING MODE:    {n.ComplexPriState}

PW TIMING MODE:     {n.DwellStatus}

        PRI              PW                                                                                                                                   INTRAPULSE                                                                                                                                PULSE             DWELL           ATTENUATION     FREQUENCY    
       (USEC)          (USEC)                                                                                                                                    NAME                                                                                                                                  REPEAT             (MSEC)             (DB)           (MHZ)      
         {n.Pri}        {n.PulseWidth}                                                                                                                                N/A                                                                                                                                           1           N/A               0.0000     5000.0000000000

USE LOCAL FREQ:     YES

PRI FILL:           NONE

PW FILL:            NONE

PULSE REPEAT FILL:  NONE

DWELL TIME FILL:    NONE

ATTENUATION FILL:   NONE

FREQUENCY FILL:     NONE
""")

    with open("PulSeqName.pulseq", "wt") as pulseq:
        pulseq.write(f"""//************** PULSE SEQUENCE DEFINITION FILE *************
//
// Model:   {n.ModeName}
//
// Created: {n.CreationDate}

PULSE NOTES:        ""

SCAN MODEL:         ""
USE LOCAL SCAN:     NO

                                                                                                                               PULSE                                                                                                                                                      PULSE                          GROUP          DWELL TIME             SCAN       AZIMUTH   ELEVATION    CELL    TRACK  ATTENUATION
                                                                                                                               MODEL                                                                                                                                                      GROUP                          REPEAT           (MSEC)             COMMAND       (DEG)      (DEG)     NUMBER    ID       (DB)    

  "PulName"                                                                                                                                                                                                                                                       ""                                                         2              0.00000000       NONE          0.000     0.000          0     0      0.0000  """)

# Shouldn't Scan Model use ModeName like everything else?

    with open("ScanName.scan", "wt") as scan:
        scan.write(f"""//****************** SCAN DEFINITION FILE *******************
//
// Model:   {n.ModeName}
//
// Created: {n.CreationDate}


//********************** SCAN MODEL ***********************

SCAN NOTES:         ""

SCAN MODEL:         {n.AzScanKind}

AZIMUTH OFFSET:     {n.AzInitialBeamOffset}
ELEVATION OFFSET:   {n.ElInitialBeamOffset}
SCAN PERIOD:        {n.AzScanPeriod} SEC
ROTATION:           {n.AzDirection}

PULSE TRIG ON REV:  NO

OVERLAY MODEL:      {n.ElScanMotion}
TYPE:               {n.ElDirection}
DIRECTION:          {n.ElDirection}
ORIGIN:             {n.ElTrackOffset}
SPAN:               {n.ElSectorWidth} DEG
SCAN RATE:          {n.ElScanPeriod} HZ

SCAN PERSPECTIVE:   TARGET

DEFAULT OFFSET:     0.0000 DBM
""") 

    with open("AntName.ant", "wt") as ant:
        ant.write(f"""//***************** ANTENNA DEFINITION FILE *****************
//
// Model:   {n.ModeName}
//
// Created: {n.CreationDate}


//********************* ANTENNA MODEL *********************

ANTENNA NOTES:      ""

ANTENNA MODEL:      {n.AntennaModelKind}

BEAM MODEL:         {n.AzScanShape}

MAIN LOBE WIDTH:    {n.AzBeamwidth} DEG
DISTRIBUTION:       {n.AzScanShape}
PHASED ARRAY:       NO

            LOBE       LOBE      LOBE      LOBE 
         ATTENUATION  WIDTH   SEPARATION  REPEAT
            (DB)      (DEG)     (DEG)     COUNT 
  +/-    {n.AzSidelobeRatio}     N/A       2.000        1 
  +/-    29.0000     N/A       1.200        1 

DEPTH OF NULLS DEPTH : 127.8250 DB

DEPTH OF NULLS SPAN : 0.000 DEG

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED

BEAM MODEL:         {n.ElScanShape}

MAIN LOBE WIDTH:    {n.ElBeamWidth} DEG
DISTRIBUTION:       {n.ElScanShape}
PHASED ARRAY:       NO

            LOBE       LOBE      LOBE      LOBE 
         ATTENUATION  WIDTH   SEPARATION  REPEAT
            (DB)      (DEG)     (DEG)     COUNT 
  +/-    {n.ElSidelobeRatio}     N/A       2.000        1 
  +/-    29.0000     N/A       1.200        1 

DEPTH OF NULLS DEPTH : 127.8250 DB

DEPTH OF NULLS SPAN : 0.000 DEG

LOW RESOLUTION:     10 POINTS PER DEG
HIGH RESOLUTION:    DISABLED
""")



simple_file_writes(sample_data)