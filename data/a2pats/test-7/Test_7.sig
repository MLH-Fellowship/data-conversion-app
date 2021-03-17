//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test_7						<xsd:elemenname="EmitterId" 
//
// Created: Thu Mar 4, 2021  12:46 PM

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""					Always (Template)

DATABASE NAME:      ""					Always (Template)
CLASSIFICATION:     "UNCLASSIFIED"			Always (Template)
NATO NAME:          "NSIN7"				<xsd:elemenname="EmitterId" 
SYSTEM NAME:        "68EWS"				<xsd:element name="EmitterName"
VERSION:            "TES"					<xsd:element name="ModeName" 
MODE:               "T07"					<xsd:element name="ModeName" 

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO					Always (Template)
ENABLE MULTIPATH:   NO					Always (Template)

//********************** PULSE MODEL **********************

PULSE MODEL:        SEQUENCE REFERENCE		Always (Template)

MODEL NAME:         "Test7_Seq"
USE REF FREQUENCY:  YES
USE REF SCAN:       YES

NON-COHERENT:       NO					Always (Template)

//******************* INTRAPULSE MODEL ********************

INTRAPULSE NOTES:   ""					Always (Template)

INTRAPULSE MODEL:   OFF

//******************** FREQUENCY MODEL ********************

FREQUENCY MODEL:    REFERENCE

MODEL NAME:         "Test7_Freq"

SYNC TO SCAN:       NO					Always (Template)

//********************** SCAN MODEL ***********************

SCAN MODEL:         REFERENCE

MODEL NAME:         "Test7_Scan"

SCAN PERSPECTIVE:   TARGET					Always (Template)

DEFAULT OFFSET:     0.0000 DBM				Always (Template)

//********************* ANTENNA MODEL *********************

ANTENNA MODEL:      REFERENCE

MODEL NAME:         "Test7_ANT"

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO					Always (Template)
