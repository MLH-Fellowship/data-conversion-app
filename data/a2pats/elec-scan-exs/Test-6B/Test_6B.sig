//***************** SIGNAL DEFINITION FILE ******************
//
// Model:   Test_6B			<xsd:elemenname="EmitterId" 
//
// Created: Thu Mar 4, 2021  12:42 PM <xsd:elementname="LastUpdateDate"

//***************** SIGNAL IDENTIFICATION *******************

ID NOTES:           ""			Always (Template)

DATABASE NAME:      ""			Always (Template)
CLASSIFICATION:     "UNCLASSIFIED"	Always (Template)
NATO NAME:          "NSIN"		<xsd:elemenname="EmitterId" 
SYSTEM NAME:        "68EWS"	<xsd:element name="EmitterName"
VERSION:            "TES"		<xsd:element name="ModeName" 
MODE:               "T6B"		<xsd:element name="ModeName"

//******************** SPECIAL FEATURES *********************

ENABLE DOPPLER:     NO		Always (Template)
ENABLE MULTIPATH:   NO		Always (Template)

//********************** PULSE MODEL **********************

PULSE MODEL:        SEQUENCE REFERENCE	Always (Template)

MODEL NAME:         "Test6B_Seq"
USE REF FREQUENCY:  Yes
USE REF SCAN:       Yes

NON-COHERENT:       NO		Always (Template)

//******************* INTRAPULSE MODEL ********************

INTRAPULSE NOTES:   ""		Always (Template)

INTRAPULSE MODEL:   OFF

//******************** FREQUENCY MODEL ********************

FREQUENCY MODEL:    REFERENCE

MODEL NAME:         "Test6B_Freq"

SYNC TO SCAN:       NO		Always (Template)

//********************** SCAN MODEL ***********************

SCAN MODEL:         REFERENCE

MODEL NAME:         "Test6B_Scan"

SCAN PERSPECTIVE:   TARGET		Always (Template)

DEFAULT OFFSET:     0.0000 DBM	Always (Template)

//********************* ANTENNA MODEL *********************

ANTENNA MODEL:      REFERENCE

MODEL NAME:         "Test6B_ANT"

//******************** MULTIPLE SIMULTANEOUS SIGNALS *********************

ENABLE MSS:         NO		Always (Template)
