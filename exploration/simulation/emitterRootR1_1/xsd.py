# ./data/ceesim/schema/simulation/emitterRootR1_1/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:32:05.170770 by PyXB version 1.2.6 using Python 3.6.9.final.0
# Namespace http://www.amherst.com/CEESIM/XML

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:32824a3e-715f-11eb-ab42-00155debab14')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.amherst.com/CEESIM/XML', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDateCreationDate
class stDateCreationDate (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDateCreationDate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 74, 2)
    _Documentation = ''
stDateCreationDate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stDateCreationDate', stDateCreationDate)
_module_typeBindings.stDateCreationDate = stDateCreationDate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDateModificationDate
class stDateModificationDate (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDateModificationDate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 83, 2)
    _Documentation = ''
stDateModificationDate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stDateModificationDate', stDateModificationDate)
_module_typeBindings.stDateModificationDate = stDateModificationDate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAltitude
class stDoubleAltitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAltitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 92, 2)
    _Documentation = ''
stDoubleAltitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAltitude, value=pyxb.binding.datatypes.double(-5000000.0))
stDoubleAltitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAltitude, value=pyxb.binding.datatypes.double(5000000.0))
stDoubleAltitude._InitializeFacetMap(stDoubleAltitude._CF_minInclusive,
   stDoubleAltitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAltitude', stDoubleAltitude)
_module_typeBindings.stDoubleAltitude = stDoubleAltitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLatitude
class stDoubleLatitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLatitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 104, 2)
    _Documentation = ''
stDoubleLatitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLatitude, value=pyxb.binding.datatypes.double(-90.0))
stDoubleLatitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLatitude, value=pyxb.binding.datatypes.double(90.0))
stDoubleLatitude._InitializeFacetMap(stDoubleLatitude._CF_minInclusive,
   stDoubleLatitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLatitude', stDoubleLatitude)
_module_typeBindings.stDoubleLatitude = stDoubleLatitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLongitude
class stDoubleLongitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLongitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 116, 2)
    _Documentation = ''
stDoubleLongitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLongitude, value=pyxb.binding.datatypes.double(-180.0))
stDoubleLongitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLongitude, value=pyxb.binding.datatypes.double(180.0))
stDoubleLongitude._InitializeFacetMap(stDoubleLongitude._CF_minInclusive,
   stDoubleLongitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLongitude', stDoubleLongitude)
_module_typeBindings.stDoubleLongitude = stDoubleLongitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleX
class stDoubleX (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleX')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 128, 2)
    _Documentation = ''
stDoubleX._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleX, value=pyxb.binding.datatypes.double(-5000000.0))
stDoubleX._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleX, value=pyxb.binding.datatypes.double(5000000.0))
stDoubleX._InitializeFacetMap(stDoubleX._CF_minInclusive,
   stDoubleX._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleX', stDoubleX)
_module_typeBindings.stDoubleX = stDoubleX

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleY
class stDoubleY (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleY')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 140, 2)
    _Documentation = ''
stDoubleY._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleY, value=pyxb.binding.datatypes.double(-5000000.0))
stDoubleY._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleY, value=pyxb.binding.datatypes.double(5000000.0))
stDoubleY._InitializeFacetMap(stDoubleY._CF_minInclusive,
   stDoubleY._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleY', stDoubleY)
_module_typeBindings.stDoubleY = stDoubleY

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleZ
class stDoubleZ (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleZ')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 152, 2)
    _Documentation = ''
stDoubleZ._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleZ, value=pyxb.binding.datatypes.double(-5000000.0))
stDoubleZ._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleZ, value=pyxb.binding.datatypes.double(5000000.0))
stDoubleZ._InitializeFacetMap(stDoubleZ._CF_minInclusive,
   stDoubleZ._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleZ', stDoubleZ)
_module_typeBindings.stDoubleZ = stDoubleZ

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntTrackPlatformNumber
class stIntTrackPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntTrackPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 164, 2)
    _Documentation = ''
stIntTrackPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntTrackPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntTrackPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntTrackPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntTrackPlatformNumber._InitializeFacetMap(stIntTrackPlatformNumber._CF_minInclusive,
   stIntTrackPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntTrackPlatformNumber', stIntTrackPlatformNumber)
_module_typeBindings.stIntTrackPlatformNumber = stIntTrackPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntUserPlatformNumber
class stIntUserPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntUserPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 176, 2)
    _Documentation = ''
stIntUserPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntUserPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntUserPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntUserPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntUserPlatformNumber._InitializeFacetMap(stIntUserPlatformNumber._CF_minInclusive,
   stIntUserPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntUserPlatformNumber', stIntUserPlatformNumber)
_module_typeBindings.stIntUserPlatformNumber = stIntUserPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringEmitterName
class stStringEmitterName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringEmitterName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 188, 2)
    _Documentation = ''
stStringEmitterName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringEmitterName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(22))
stStringEmitterName._InitializeFacetMap(stStringEmitterName._CF_minLength,
   stStringEmitterName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringEmitterName', stStringEmitterName)
_module_typeBindings.stStringEmitterName = stStringEmitterName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextCommentHeader
class stTextCommentHeader (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextCommentHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 200, 2)
    _Documentation = ''
stTextCommentHeader._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextCommentHeader', stTextCommentHeader)
_module_typeBindings.stTextCommentHeader = stTextCommentHeader

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolChangeTracking
class stBoolChangeTracking (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolChangeTracking')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 162, 2)
    _Documentation = ''
stBoolChangeTracking._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolChangeTracking', stBoolChangeTracking)
_module_typeBindings.stBoolChangeTracking = stBoolChangeTracking

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolGeneratorActive
class stBoolGeneratorActive (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolGeneratorActive')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 171, 2)
    _Documentation = ''
stBoolGeneratorActive._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolGeneratorActive', stBoolGeneratorActive)
_module_typeBindings.stBoolGeneratorActive = stBoolGeneratorActive

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolGeneratorEventDefined
class stBoolGeneratorEventDefined (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolGeneratorEventDefined')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 180, 2)
    _Documentation = ''
stBoolGeneratorEventDefined._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolGeneratorEventDefined', stBoolGeneratorEventDefined)
_module_typeBindings.stBoolGeneratorEventDefined = stBoolGeneratorEventDefined

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterruptActive
class stBoolInterruptActive (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterruptActive')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 189, 2)
    _Documentation = ''
stBoolInterruptActive._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterruptActive', stBoolInterruptActive)
_module_typeBindings.stBoolInterruptActive = stBoolInterruptActive

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOldTrackDataValid
class stBoolOldTrackDataValid (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOldTrackDataValid')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 198, 2)
    _Documentation = ''
stBoolOldTrackDataValid._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOldTrackDataValid', stBoolOldTrackDataValid)
_module_typeBindings.stBoolOldTrackDataValid = stBoolOldTrackDataValid

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOldTrackIsSut
class stBoolOldTrackIsSut (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOldTrackIsSut')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 207, 2)
    _Documentation = ''
stBoolOldTrackIsSut._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOldTrackIsSut', stBoolOldTrackIsSut)
_module_typeBindings.stBoolOldTrackIsSut = stBoolOldTrackIsSut

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOverrideInterruptGenerators
class stBoolOverrideInterruptGenerators (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOverrideInterruptGenerators')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 216, 2)
    _Documentation = ''
stBoolOverrideInterruptGenerators._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOverrideInterruptGenerators', stBoolOverrideInterruptGenerators)
_module_typeBindings.stBoolOverrideInterruptGenerators = stBoolOverrideInterruptGenerators

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOverrideScanInterrupts
class stBoolOverrideScanInterrupts (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOverrideScanInterrupts')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 225, 2)
    _Documentation = ''
stBoolOverrideScanInterrupts._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOverrideScanInterrupts', stBoolOverrideScanInterrupts)
_module_typeBindings.stBoolOverrideScanInterrupts = stBoolOverrideScanInterrupts

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOverrideTrack
class stBoolOverrideTrack (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOverrideTrack')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 234, 2)
    _Documentation = ''
stBoolOverrideTrack._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOverrideTrack', stBoolOverrideTrack)
_module_typeBindings.stBoolOverrideTrack = stBoolOverrideTrack

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRadiationEnable
class stBoolRadiationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRadiationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 243, 2)
    _Documentation = ''
stBoolRadiationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRadiationEnable', stBoolRadiationEnable)
_module_typeBindings.stBoolRadiationEnable = stBoolRadiationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRadiationState
class stBoolRadiationState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRadiationState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 252, 2)
    _Documentation = ''
stBoolRadiationState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRadiationState', stBoolRadiationState)
_module_typeBindings.stBoolRadiationState = stBoolRadiationState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRangeRadiationState
class stBoolRangeRadiationState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRangeRadiationState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 261, 2)
    _Documentation = ''
stBoolRangeRadiationState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRangeRadiationState', stBoolRangeRadiationState)
_module_typeBindings.stBoolRangeRadiationState = stBoolRangeRadiationState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRangeResyncOnModeChangeState
class stBoolRangeResyncOnModeChangeState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRangeResyncOnModeChangeState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 270, 2)
    _Documentation = ''
stBoolRangeResyncOnModeChangeState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRangeResyncOnModeChangeState', stBoolRangeResyncOnModeChangeState)
_module_typeBindings.stBoolRangeResyncOnModeChangeState = stBoolRangeResyncOnModeChangeState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolResyncOnModeChangeState
class stBoolResyncOnModeChangeState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolResyncOnModeChangeState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 279, 2)
    _Documentation = ''
stBoolResyncOnModeChangeState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolResyncOnModeChangeState', stBoolResyncOnModeChangeState)
_module_typeBindings.stBoolResyncOnModeChangeState = stBoolResyncOnModeChangeState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDwellDurationScript
class stDoubleDwellDurationScript (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDwellDurationScript')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 288, 2)
    _Documentation = ''
stDoubleDwellDurationScript._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDwellDurationScript, value=pyxb.binding.datatypes.double(1e-06))
stDoubleDwellDurationScript._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDwellDurationScript, value=pyxb.binding.datatypes.double(137438.953471))
stDoubleDwellDurationScript._InitializeFacetMap(stDoubleDwellDurationScript._CF_minInclusive,
   stDoubleDwellDurationScript._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDwellDurationScript', stDoubleDwellDurationScript)
_module_typeBindings.stDoubleDwellDurationScript = stDoubleDwellDurationScript

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEventTime
class stDoubleEventTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEventTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 300, 2)
    _Documentation = ''
stDoubleEventTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEventTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleEventTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEventTime, value=pyxb.binding.datatypes.double(137438.953471))
stDoubleEventTime._InitializeFacetMap(stDoubleEventTime._CF_minInclusive,
   stDoubleEventTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEventTime', stDoubleEventTime)
_module_typeBindings.stDoubleEventTime = stDoubleEventTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleHighRange
class stDoubleHighRange (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleHighRange')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 312, 2)
    _Documentation = ''
stDoubleHighRange._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleHighRange, value=pyxb.binding.datatypes.double(0.0))
stDoubleHighRange._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleHighRange, value=pyxb.binding.datatypes.double(14724656.0))
stDoubleHighRange._InitializeFacetMap(stDoubleHighRange._CF_minInclusive,
   stDoubleHighRange._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleHighRange', stDoubleHighRange)
_module_typeBindings.stDoubleHighRange = stDoubleHighRange

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleXOffset
class stDoubleXOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleXOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 324, 2)
    _Documentation = ''
stDoubleXOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleXOffset, value=pyxb.binding.datatypes.double(-999999.999))
stDoubleXOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleXOffset, value=pyxb.binding.datatypes.double(999999.999))
stDoubleXOffset._InitializeFacetMap(stDoubleXOffset._CF_minInclusive,
   stDoubleXOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleXOffset', stDoubleXOffset)
_module_typeBindings.stDoubleXOffset = stDoubleXOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleYOffset
class stDoubleYOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleYOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 336, 2)
    _Documentation = ''
stDoubleYOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleYOffset, value=pyxb.binding.datatypes.double(-999999.999))
stDoubleYOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleYOffset, value=pyxb.binding.datatypes.double(999999.999))
stDoubleYOffset._InitializeFacetMap(stDoubleYOffset._CF_minInclusive,
   stDoubleYOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleYOffset', stDoubleYOffset)
_module_typeBindings.stDoubleYOffset = stDoubleYOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleZOffset
class stDoubleZOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleZOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 348, 2)
    _Documentation = ''
stDoubleZOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleZOffset, value=pyxb.binding.datatypes.double(-999999.999))
stDoubleZOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleZOffset, value=pyxb.binding.datatypes.double(999999.999))
stDoubleZOffset._InitializeFacetMap(stDoubleZOffset._CF_minInclusive,
   stDoubleZOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleZOffset', stDoubleZOffset)
_module_typeBindings.stDoubleZOffset = stDoubleZOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumEventType
class stEnumEventType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumEventType')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 360, 2)
    _Documentation = ''
stEnumEventType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumEventType, enum_prefix=None)
stEnumEventType.Activate = stEnumEventType._CF_enumeration.addEnumeration(unicode_value='Activate', tag='Activate')
stEnumEventType.Change_Mode = stEnumEventType._CF_enumeration.addEnumeration(unicode_value='Change_Mode', tag='Change_Mode')
stEnumEventType.Deactivate = stEnumEventType._CF_enumeration.addEnumeration(unicode_value='Deactivate', tag='Deactivate')
stEnumEventType.Disable_Radiation = stEnumEventType._CF_enumeration.addEnumeration(unicode_value='Disable_Radiation', tag='Disable_Radiation')
stEnumEventType.Enable_Radiation = stEnumEventType._CF_enumeration.addEnumeration(unicode_value='Enable_Radiation', tag='Enable_Radiation')
stEnumEventType.Range_Base_Mode_Change = stEnumEventType._CF_enumeration.addEnumeration(unicode_value='Range_Base_Mode_Change', tag='Range_Base_Mode_Change')
stEnumEventType.Mode_Dwell = stEnumEventType._CF_enumeration.addEnumeration(unicode_value='Mode_Dwell', tag='Mode_Dwell')
stEnumEventType._InitializeFacetMap(stEnumEventType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumEventType', stEnumEventType)
_module_typeBindings.stEnumEventType = stEnumEventType

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntEventNumber
class stIntEventNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntEventNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 377, 2)
    _Documentation = ''
stIntEventNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntEventNumber, value=pyxb.binding.datatypes.int(1))
stIntEventNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntEventNumber, value=pyxb.binding.datatypes.int(2147483647))
stIntEventNumber._InitializeFacetMap(stIntEventNumber._CF_minInclusive,
   stIntEventNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntEventNumber', stIntEventNumber)
_module_typeBindings.stIntEventNumber = stIntEventNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntInterruptGeneratorNumber
class stIntInterruptGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntInterruptGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 389, 2)
    _Documentation = ''
stIntInterruptGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntInterruptGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntInterruptGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntInterruptGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntInterruptGeneratorNumber._InitializeFacetMap(stIntInterruptGeneratorNumber._CF_minInclusive,
   stIntInterruptGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntInterruptGeneratorNumber', stIntInterruptGeneratorNumber)
_module_typeBindings.stIntInterruptGeneratorNumber = stIntInterruptGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntPlatformTrackNumber
class stIntPlatformTrackNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntPlatformTrackNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 401, 2)
    _Documentation = ''
stIntPlatformTrackNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntPlatformTrackNumber, value=pyxb.binding.datatypes.int(1))
stIntPlatformTrackNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntPlatformTrackNumber, value=pyxb.binding.datatypes.int(32767))
stIntPlatformTrackNumber._InitializeFacetMap(stIntPlatformTrackNumber._CF_minInclusive,
   stIntPlatformTrackNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntPlatformTrackNumber', stIntPlatformTrackNumber)
_module_typeBindings.stIntPlatformTrackNumber = stIntPlatformTrackNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntScriptGeneratorNumber
class stIntScriptGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntScriptGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 413, 2)
    _Documentation = ''
stIntScriptGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntScriptGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntScriptGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntScriptGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntScriptGeneratorNumber._InitializeFacetMap(stIntScriptGeneratorNumber._CF_minInclusive,
   stIntScriptGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntScriptGeneratorNumber', stIntScriptGeneratorNumber)
_module_typeBindings.stIntScriptGeneratorNumber = stIntScriptGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntUserEmitterNumber
class stIntUserEmitterNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntUserEmitterNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 425, 2)
    _Documentation = ''
stIntUserEmitterNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntUserEmitterNumber, value=pyxb.binding.datatypes.int(1))
stIntUserEmitterNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntUserEmitterNumber, value=pyxb.binding.datatypes.int(32767))
stIntUserEmitterNumber._InitializeFacetMap(stIntUserEmitterNumber._CF_minInclusive,
   stIntUserEmitterNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntUserEmitterNumber', stIntUserEmitterNumber)
_module_typeBindings.stIntUserEmitterNumber = stIntUserEmitterNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringAssociatedSubmodeName
class stStringAssociatedSubmodeName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringAssociatedSubmodeName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 437, 2)
    _Documentation = ''
stStringAssociatedSubmodeName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringAssociatedSubmodeName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(22))
stStringAssociatedSubmodeName._InitializeFacetMap(stStringAssociatedSubmodeName._CF_minLength,
   stStringAssociatedSubmodeName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringAssociatedSubmodeName', stStringAssociatedSubmodeName)
_module_typeBindings.stStringAssociatedSubmodeName = stStringAssociatedSubmodeName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringEmitterId
class stStringEmitterId (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringEmitterId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 449, 2)
    _Documentation = ''
stStringEmitterId._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringEmitterId._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
stStringEmitterId._InitializeFacetMap(stStringEmitterId._CF_minLength,
   stStringEmitterId._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringEmitterId', stStringEmitterId)
_module_typeBindings.stStringEmitterId = stStringEmitterId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringModeNameScript
class stStringModeNameScript (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringModeNameScript')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 462, 2)
    _Documentation = ''
stStringModeNameScript._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringModeNameScript._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(22))
stStringModeNameScript._InitializeFacetMap(stStringModeNameScript._CF_minLength,
   stStringModeNameScript._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringModeNameScript', stStringModeNameScript)
_module_typeBindings.stStringModeNameScript = stStringModeNameScript

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringRangeModeName
class stStringRangeModeName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringRangeModeName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 474, 2)
    _Documentation = ''
stStringRangeModeName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringRangeModeName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(22))
stStringRangeModeName._InitializeFacetMap(stStringRangeModeName._CF_minLength,
   stStringRangeModeName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringRangeModeName', stStringRangeModeName)
_module_typeBindings.stStringRangeModeName = stStringRangeModeName

# Complex type {http://www.amherst.com/CEESIM/XML}ctFlatEarthPoint with content type ELEMENT_ONLY
class ctFlatEarthPoint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctFlatEarthPoint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctFlatEarthPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 41, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}X uses Python identifier X
    __X = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'X'), 'X', '__httpwww_amherst_comCEESIMXML_ctFlatEarthPoint_httpwww_amherst_comCEESIMXMLX', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 43, 6), )

    
    X = property(__X.value, __X.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Y uses Python identifier Y
    __Y = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Y'), 'Y', '__httpwww_amherst_comCEESIMXML_ctFlatEarthPoint_httpwww_amherst_comCEESIMXMLY', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 44, 6), )

    
    Y = property(__Y.value, __Y.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Z uses Python identifier Z
    __Z = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Z'), 'Z', '__httpwww_amherst_comCEESIMXML_ctFlatEarthPoint_httpwww_amherst_comCEESIMXMLZ', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 45, 6), )

    
    Z = property(__Z.value, __Z.set, None, None)

    _ElementMap.update({
        __X.name() : __X,
        __Y.name() : __Y,
        __Z.name() : __Z
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctFlatEarthPoint = ctFlatEarthPoint
Namespace.addCategoryObject('typeBinding', 'ctFlatEarthPoint', ctFlatEarthPoint)


# Complex type {http://www.amherst.com/CEESIM/XML}ctModificationHeader with content type ELEMENT_ONLY
class ctModificationHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctModificationHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctModificationHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 49, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreationDate'), 'CreationDate', '__httpwww_amherst_comCEESIMXML_ctModificationHeader_httpwww_amherst_comCEESIMXMLCreationDate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 51, 6), )

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ModificationDate uses Python identifier ModificationDate
    __ModificationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ModificationDate'), 'ModificationDate', '__httpwww_amherst_comCEESIMXML_ctModificationHeader_httpwww_amherst_comCEESIMXMLModificationDate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 52, 6), )

    
    ModificationDate = property(__ModificationDate.value, __ModificationDate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpwww_amherst_comCEESIMXML_ctModificationHeader_httpwww_amherst_comCEESIMXMLComment', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 53, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    _ElementMap.update({
        __CreationDate.name() : __CreationDate,
        __ModificationDate.name() : __ModificationDate,
        __Comment.name() : __Comment
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctModificationHeader = ctModificationHeader
Namespace.addCategoryObject('typeBinding', 'ctModificationHeader', ctModificationHeader)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPoint with content type ELEMENT_ONLY
class ctPoint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPoint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 57, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}FlatEarthPoint uses Python identifier FlatEarthPoint
    __FlatEarthPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FlatEarthPoint'), 'FlatEarthPoint', '__httpwww_amherst_comCEESIMXML_ctPoint_httpwww_amherst_comCEESIMXMLFlatEarthPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 59, 6), )

    
    FlatEarthPoint = property(__FlatEarthPoint.value, __FlatEarthPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RoundEarthPoint uses Python identifier RoundEarthPoint
    __RoundEarthPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RoundEarthPoint'), 'RoundEarthPoint', '__httpwww_amherst_comCEESIMXML_ctPoint_httpwww_amherst_comCEESIMXMLRoundEarthPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 60, 6), )

    
    RoundEarthPoint = property(__RoundEarthPoint.value, __RoundEarthPoint.set, None, None)

    _ElementMap.update({
        __FlatEarthPoint.name() : __FlatEarthPoint,
        __RoundEarthPoint.name() : __RoundEarthPoint
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPoint = ctPoint
Namespace.addCategoryObject('typeBinding', 'ctPoint', ctPoint)


# Complex type {http://www.amherst.com/CEESIM/XML}ctRoundEarthPoint with content type ELEMENT_ONLY
class ctRoundEarthPoint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctRoundEarthPoint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctRoundEarthPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 64, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Latitude uses Python identifier Latitude
    __Latitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Latitude'), 'Latitude', '__httpwww_amherst_comCEESIMXML_ctRoundEarthPoint_httpwww_amherst_comCEESIMXMLLatitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 66, 6), )

    
    Latitude = property(__Latitude.value, __Latitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Longitude uses Python identifier Longitude
    __Longitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Longitude'), 'Longitude', '__httpwww_amherst_comCEESIMXML_ctRoundEarthPoint_httpwww_amherst_comCEESIMXMLLongitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 67, 6), )

    
    Longitude = property(__Longitude.value, __Longitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Altitude uses Python identifier Altitude
    __Altitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Altitude'), 'Altitude', '__httpwww_amherst_comCEESIMXML_ctRoundEarthPoint_httpwww_amherst_comCEESIMXMLAltitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 68, 6), )

    
    Altitude = property(__Altitude.value, __Altitude.set, None, None)

    _ElementMap.update({
        __Latitude.name() : __Latitude,
        __Longitude.name() : __Longitude,
        __Altitude.name() : __Altitude
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctRoundEarthPoint = ctRoundEarthPoint
Namespace.addCategoryObject('typeBinding', 'ctRoundEarthPoint', ctRoundEarthPoint)


# Complex type {http://www.amherst.com/CEESIM/XML}ctEmitterData with content type ELEMENT_ONLY
class ctEmitterData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctEmitterData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctEmitterData')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 41, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterHeader uses Python identifier EmitterHeader
    __EmitterHeader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterHeader'), 'EmitterHeader', '__httpwww_amherst_comCEESIMXML_ctEmitterData_httpwww_amherst_comCEESIMXMLEmitterHeader', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 43, 6), )

    
    EmitterHeader = property(__EmitterHeader.value, __EmitterHeader.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterScript uses Python identifier EmitterScript
    __EmitterScript = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterScript'), 'EmitterScript', '__httpwww_amherst_comCEESIMXML_ctEmitterData_httpwww_amherst_comCEESIMXMLEmitterScript', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 44, 6), )

    
    EmitterScript = property(__EmitterScript.value, __EmitterScript.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctEmitterData_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 51, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 51, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __EmitterHeader.name() : __EmitterHeader,
        __EmitterScript.name() : __EmitterScript
    })
    _AttributeMap.update({
        __PerId.name() : __PerId
    })
_module_typeBindings.ctEmitterData = ctEmitterData
Namespace.addCategoryObject('typeBinding', 'ctEmitterData', ctEmitterData)


# Complex type {http://www.amherst.com/CEESIM/XML}ctEmitterHeader with content type ELEMENT_ONLY
class ctEmitterHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctEmitterHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctEmitterHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}UserEmitterNumber uses Python identifier UserEmitterNumber
    __UserEmitterNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UserEmitterNumber'), 'UserEmitterNumber', '__httpwww_amherst_comCEESIMXML_ctEmitterHeader_httpwww_amherst_comCEESIMXMLUserEmitterNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 56, 6), )

    
    UserEmitterNumber = property(__UserEmitterNumber.value, __UserEmitterNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterId uses Python identifier EmitterId
    __EmitterId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterId'), 'EmitterId', '__httpwww_amherst_comCEESIMXML_ctEmitterHeader_httpwww_amherst_comCEESIMXMLEmitterId', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 57, 6), )

    
    EmitterId = property(__EmitterId.value, __EmitterId.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterName uses Python identifier EmitterName
    __EmitterName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterName'), 'EmitterName', '__httpwww_amherst_comCEESIMXML_ctEmitterHeader_httpwww_amherst_comCEESIMXMLEmitterName', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 58, 6), )

    
    EmitterName = property(__EmitterName.value, __EmitterName.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}XOffset uses Python identifier XOffset
    __XOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'XOffset'), 'XOffset', '__httpwww_amherst_comCEESIMXML_ctEmitterHeader_httpwww_amherst_comCEESIMXMLXOffset', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 59, 6), )

    
    XOffset = property(__XOffset.value, __XOffset.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}YOffset uses Python identifier YOffset
    __YOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'YOffset'), 'YOffset', '__httpwww_amherst_comCEESIMXML_ctEmitterHeader_httpwww_amherst_comCEESIMXMLYOffset', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 60, 6), )

    
    YOffset = property(__YOffset.value, __YOffset.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ZOffset uses Python identifier ZOffset
    __ZOffset = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ZOffset'), 'ZOffset', '__httpwww_amherst_comCEESIMXML_ctEmitterHeader_httpwww_amherst_comCEESIMXMLZOffset', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 61, 6), )

    
    ZOffset = property(__ZOffset.value, __ZOffset.set, None, None)

    _ElementMap.update({
        __UserEmitterNumber.name() : __UserEmitterNumber,
        __EmitterId.name() : __EmitterId,
        __EmitterName.name() : __EmitterName,
        __XOffset.name() : __XOffset,
        __YOffset.name() : __YOffset,
        __ZOffset.name() : __ZOffset
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctEmitterHeader = ctEmitterHeader
Namespace.addCategoryObject('typeBinding', 'ctEmitterHeader', ctEmitterHeader)


# Complex type {http://www.amherst.com/CEESIM/XML}ctEmitterScriptEventList with content type ELEMENT_ONLY
class ctEmitterScriptEventList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctEmitterScriptEventList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctEmitterScriptEventList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 65, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterScriptEvent uses Python identifier EmitterScriptEvent
    __EmitterScriptEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterScriptEvent'), 'EmitterScriptEvent', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEventList_httpwww_amherst_comCEESIMXMLEmitterScriptEvent', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 67, 6), )

    
    EmitterScriptEvent = property(__EmitterScriptEvent.value, __EmitterScriptEvent.set, None, None)

    _ElementMap.update({
        __EmitterScriptEvent.name() : __EmitterScriptEvent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctEmitterScriptEventList = ctEmitterScriptEventList
Namespace.addCategoryObject('typeBinding', 'ctEmitterScriptEventList', ctEmitterScriptEventList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctEmitterScriptEvent with content type ELEMENT_ONLY
class ctEmitterScriptEvent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctEmitterScriptEvent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctEmitterScriptEvent')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 71, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}EventNumber uses Python identifier EventNumber
    __EventNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EventNumber'), 'EventNumber', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLEventNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 73, 6), )

    
    EventNumber = property(__EventNumber.value, __EventNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EventTime uses Python identifier EventTime
    __EventTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EventTime'), 'EventTime', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLEventTime', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 74, 6), )

    
    EventTime = property(__EventTime.value, __EventTime.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EventType uses Python identifier EventType
    __EventType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EventType'), 'EventType', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLEventType', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 75, 6), )

    
    EventType = property(__EventType.value, __EventType.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ModeName uses Python identifier ModeName
    __ModeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ModeName'), 'ModeName', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLModeName', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 76, 6), )

    
    ModeName = property(__ModeName.value, __ModeName.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RadiationState uses Python identifier RadiationState
    __RadiationState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RadiationState'), 'RadiationState', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLRadiationState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 77, 6), )

    
    RadiationState = property(__RadiationState.value, __RadiationState.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ResyncOnModeChangeState uses Python identifier ResyncOnModeChangeState
    __ResyncOnModeChangeState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResyncOnModeChangeState'), 'ResyncOnModeChangeState', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLResyncOnModeChangeState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 78, 6), )

    
    ResyncOnModeChangeState = property(__ResyncOnModeChangeState.value, __ResyncOnModeChangeState.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ChangeTracking uses Python identifier ChangeTracking
    __ChangeTracking = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChangeTracking'), 'ChangeTracking', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLChangeTracking', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 79, 6), )

    
    ChangeTracking = property(__ChangeTracking.value, __ChangeTracking.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DwellDuration uses Python identifier DwellDuration
    __DwellDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DwellDuration'), 'DwellDuration', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLDwellDuration', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 80, 6), )

    
    DwellDuration = property(__DwellDuration.value, __DwellDuration.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TrackPlatformNumbers uses Python identifier TrackPlatformNumbers
    __TrackPlatformNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TrackPlatformNumbers'), 'TrackPlatformNumbers', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLTrackPlatformNumbers', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 81, 6), )

    
    TrackPlatformNumbers = property(__TrackPlatformNumbers.value, __TrackPlatformNumbers.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeneratorEventDefined uses Python identifier GeneratorEventDefined
    __GeneratorEventDefined = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeneratorEventDefined'), 'GeneratorEventDefined', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLGeneratorEventDefined', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 82, 6), )

    
    GeneratorEventDefined = property(__GeneratorEventDefined.value, __GeneratorEventDefined.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RangeEvents uses Python identifier RangeEvents
    __RangeEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RangeEvents'), 'RangeEvents', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLRangeEvents', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 84, 6), )

    
    RangeEvents = property(__RangeEvents.value, __RangeEvents.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeneratorScriptEvents uses Python identifier GeneratorScriptEvents
    __GeneratorScriptEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeneratorScriptEvents'), 'GeneratorScriptEvents', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLGeneratorScriptEvents', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 85, 6), )

    
    GeneratorScriptEvents = property(__GeneratorScriptEvents.value, __GeneratorScriptEvents.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}AssociatedSubmodeName uses Python identifier AssociatedSubmodeName
    __AssociatedSubmodeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AssociatedSubmodeName'), 'AssociatedSubmodeName', '__httpwww_amherst_comCEESIMXML_ctEmitterScriptEvent_httpwww_amherst_comCEESIMXMLAssociatedSubmodeName', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 86, 6), )

    
    AssociatedSubmodeName = property(__AssociatedSubmodeName.value, __AssociatedSubmodeName.set, None, None)

    _ElementMap.update({
        __EventNumber.name() : __EventNumber,
        __EventTime.name() : __EventTime,
        __EventType.name() : __EventType,
        __ModeName.name() : __ModeName,
        __RadiationState.name() : __RadiationState,
        __ResyncOnModeChangeState.name() : __ResyncOnModeChangeState,
        __ChangeTracking.name() : __ChangeTracking,
        __DwellDuration.name() : __DwellDuration,
        __TrackPlatformNumbers.name() : __TrackPlatformNumbers,
        __GeneratorEventDefined.name() : __GeneratorEventDefined,
        __RangeEvents.name() : __RangeEvents,
        __GeneratorScriptEvents.name() : __GeneratorScriptEvents,
        __AssociatedSubmodeName.name() : __AssociatedSubmodeName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctEmitterScriptEvent = ctEmitterScriptEvent
Namespace.addCategoryObject('typeBinding', 'ctEmitterScriptEvent', ctEmitterScriptEvent)


# Complex type {http://www.amherst.com/CEESIM/XML}ctTrackPlatformNumberList with content type ELEMENT_ONLY
class ctTrackPlatformNumberList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTrackPlatformNumberList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTrackPlatformNumberList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 91, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}TrackPlatformNumber uses Python identifier TrackPlatformNumber
    __TrackPlatformNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TrackPlatformNumber'), 'TrackPlatformNumber', '__httpwww_amherst_comCEESIMXML_ctTrackPlatformNumberList_httpwww_amherst_comCEESIMXMLTrackPlatformNumber', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 93, 6), )

    
    TrackPlatformNumber = property(__TrackPlatformNumber.value, __TrackPlatformNumber.set, None, None)

    _ElementMap.update({
        __TrackPlatformNumber.name() : __TrackPlatformNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctTrackPlatformNumberList = ctTrackPlatformNumberList
Namespace.addCategoryObject('typeBinding', 'ctTrackPlatformNumberList', ctTrackPlatformNumberList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctRangeEventList with content type ELEMENT_ONLY
class ctRangeEventList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctRangeEventList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctRangeEventList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 97, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}RangeEvent uses Python identifier RangeEvent
    __RangeEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RangeEvent'), 'RangeEvent', '__httpwww_amherst_comCEESIMXML_ctRangeEventList_httpwww_amherst_comCEESIMXMLRangeEvent', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 99, 6), )

    
    RangeEvent = property(__RangeEvent.value, __RangeEvent.set, None, None)

    _ElementMap.update({
        __RangeEvent.name() : __RangeEvent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctRangeEventList = ctRangeEventList
Namespace.addCategoryObject('typeBinding', 'ctRangeEventList', ctRangeEventList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctGeneratorScriptEventList with content type ELEMENT_ONLY
class ctGeneratorScriptEventList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctGeneratorScriptEventList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctGeneratorScriptEventList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 103, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}GeneratorScriptEvent uses Python identifier GeneratorScriptEvent
    __GeneratorScriptEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeneratorScriptEvent'), 'GeneratorScriptEvent', '__httpwww_amherst_comCEESIMXML_ctGeneratorScriptEventList_httpwww_amherst_comCEESIMXMLGeneratorScriptEvent', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 105, 6), )

    
    GeneratorScriptEvent = property(__GeneratorScriptEvent.value, __GeneratorScriptEvent.set, None, None)

    _ElementMap.update({
        __GeneratorScriptEvent.name() : __GeneratorScriptEvent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctGeneratorScriptEventList = ctGeneratorScriptEventList
Namespace.addCategoryObject('typeBinding', 'ctGeneratorScriptEventList', ctGeneratorScriptEventList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctRangeEvent with content type ELEMENT_ONLY
class ctRangeEvent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctRangeEvent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctRangeEvent')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 109, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}HighRange uses Python identifier HighRange
    __HighRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HighRange'), 'HighRange', '__httpwww_amherst_comCEESIMXML_ctRangeEvent_httpwww_amherst_comCEESIMXMLHighRange', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 111, 6), )

    
    HighRange = property(__HighRange.value, __HighRange.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RangeModeName uses Python identifier RangeModeName
    __RangeModeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RangeModeName'), 'RangeModeName', '__httpwww_amherst_comCEESIMXML_ctRangeEvent_httpwww_amherst_comCEESIMXMLRangeModeName', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 112, 6), )

    
    RangeModeName = property(__RangeModeName.value, __RangeModeName.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RangeRadiationState uses Python identifier RangeRadiationState
    __RangeRadiationState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RangeRadiationState'), 'RangeRadiationState', '__httpwww_amherst_comCEESIMXML_ctRangeEvent_httpwww_amherst_comCEESIMXMLRangeRadiationState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 113, 6), )

    
    RangeRadiationState = property(__RangeRadiationState.value, __RangeRadiationState.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RangeResyncOnModeChangeState uses Python identifier RangeResyncOnModeChangeState
    __RangeResyncOnModeChangeState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RangeResyncOnModeChangeState'), 'RangeResyncOnModeChangeState', '__httpwww_amherst_comCEESIMXML_ctRangeEvent_httpwww_amherst_comCEESIMXMLRangeResyncOnModeChangeState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 114, 6), )

    
    RangeResyncOnModeChangeState = property(__RangeResyncOnModeChangeState.value, __RangeResyncOnModeChangeState.set, None, None)

    _ElementMap.update({
        __HighRange.name() : __HighRange,
        __RangeModeName.name() : __RangeModeName,
        __RangeRadiationState.name() : __RangeRadiationState,
        __RangeResyncOnModeChangeState.name() : __RangeResyncOnModeChangeState
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctRangeEvent = ctRangeEvent
Namespace.addCategoryObject('typeBinding', 'ctRangeEvent', ctRangeEvent)


# Complex type {http://www.amherst.com/CEESIM/XML}ctGeneratorScriptEvent with content type ELEMENT_ONLY
class ctGeneratorScriptEvent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctGeneratorScriptEvent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctGeneratorScriptEvent')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 118, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}GeneratorNumber uses Python identifier GeneratorNumber
    __GeneratorNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeneratorNumber'), 'GeneratorNumber', '__httpwww_amherst_comCEESIMXML_ctGeneratorScriptEvent_httpwww_amherst_comCEESIMXMLGeneratorNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 120, 6), )

    
    GeneratorNumber = property(__GeneratorNumber.value, __GeneratorNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeneratorActive uses Python identifier GeneratorActive
    __GeneratorActive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeneratorActive'), 'GeneratorActive', '__httpwww_amherst_comCEESIMXML_ctGeneratorScriptEvent_httpwww_amherst_comCEESIMXMLGeneratorActive', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 121, 6), )

    
    GeneratorActive = property(__GeneratorActive.value, __GeneratorActive.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RadiationEnable uses Python identifier RadiationEnable
    __RadiationEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RadiationEnable'), 'RadiationEnable', '__httpwww_amherst_comCEESIMXML_ctGeneratorScriptEvent_httpwww_amherst_comCEESIMXMLRadiationEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 122, 6), )

    
    RadiationEnable = property(__RadiationEnable.value, __RadiationEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}OverrideTrack uses Python identifier OverrideTrack
    __OverrideTrack = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack'), 'OverrideTrack', '__httpwww_amherst_comCEESIMXML_ctGeneratorScriptEvent_httpwww_amherst_comCEESIMXMLOverrideTrack', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 123, 6), )

    
    OverrideTrack = property(__OverrideTrack.value, __OverrideTrack.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TrackEvents uses Python identifier TrackEvents
    __TrackEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TrackEvents'), 'TrackEvents', '__httpwww_amherst_comCEESIMXML_ctGeneratorScriptEvent_httpwww_amherst_comCEESIMXMLTrackEvents', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 124, 6), )

    
    TrackEvents = property(__TrackEvents.value, __TrackEvents.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}OverrideScanInterrupts uses Python identifier OverrideScanInterrupts
    __OverrideScanInterrupts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OverrideScanInterrupts'), 'OverrideScanInterrupts', '__httpwww_amherst_comCEESIMXML_ctGeneratorScriptEvent_httpwww_amherst_comCEESIMXMLOverrideScanInterrupts', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 125, 6), )

    
    OverrideScanInterrupts = property(__OverrideScanInterrupts.value, __OverrideScanInterrupts.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}InterruptRecords uses Python identifier InterruptRecords
    __InterruptRecords = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterruptRecords'), 'InterruptRecords', '__httpwww_amherst_comCEESIMXML_ctGeneratorScriptEvent_httpwww_amherst_comCEESIMXMLInterruptRecords', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 126, 6), )

    
    InterruptRecords = property(__InterruptRecords.value, __InterruptRecords.set, None, None)

    _ElementMap.update({
        __GeneratorNumber.name() : __GeneratorNumber,
        __GeneratorActive.name() : __GeneratorActive,
        __RadiationEnable.name() : __RadiationEnable,
        __OverrideTrack.name() : __OverrideTrack,
        __TrackEvents.name() : __TrackEvents,
        __OverrideScanInterrupts.name() : __OverrideScanInterrupts,
        __InterruptRecords.name() : __InterruptRecords
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctGeneratorScriptEvent = ctGeneratorScriptEvent
Namespace.addCategoryObject('typeBinding', 'ctGeneratorScriptEvent', ctGeneratorScriptEvent)


# Complex type {http://www.amherst.com/CEESIM/XML}ctTrackEventList with content type ELEMENT_ONLY
class ctTrackEventList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTrackEventList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTrackEventList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 130, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}TrackEvent uses Python identifier TrackEvent
    __TrackEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TrackEvent'), 'TrackEvent', '__httpwww_amherst_comCEESIMXML_ctTrackEventList_httpwww_amherst_comCEESIMXMLTrackEvent', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 132, 6), )

    
    TrackEvent = property(__TrackEvent.value, __TrackEvent.set, None, None)

    _ElementMap.update({
        __TrackEvent.name() : __TrackEvent
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctTrackEventList = ctTrackEventList
Namespace.addCategoryObject('typeBinding', 'ctTrackEventList', ctTrackEventList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctTrackEvent with content type ELEMENT_ONLY
class ctTrackEvent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTrackEvent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTrackEvent')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 136, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}OverrideTrack uses Python identifier OverrideTrack
    __OverrideTrack = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack'), 'OverrideTrack', '__httpwww_amherst_comCEESIMXML_ctTrackEvent_httpwww_amherst_comCEESIMXMLOverrideTrack', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 138, 6), )

    
    OverrideTrack = property(__OverrideTrack.value, __OverrideTrack.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NewTrackPlatform uses Python identifier NewTrackPlatform
    __NewTrackPlatform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NewTrackPlatform'), 'NewTrackPlatform', '__httpwww_amherst_comCEESIMXML_ctTrackEvent_httpwww_amherst_comCEESIMXMLNewTrackPlatform', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 139, 6), )

    
    NewTrackPlatform = property(__NewTrackPlatform.value, __NewTrackPlatform.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}OldTrackDataValid uses Python identifier OldTrackDataValid
    __OldTrackDataValid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OldTrackDataValid'), 'OldTrackDataValid', '__httpwww_amherst_comCEESIMXML_ctTrackEvent_httpwww_amherst_comCEESIMXMLOldTrackDataValid', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 140, 6), )

    
    OldTrackDataValid = property(__OldTrackDataValid.value, __OldTrackDataValid.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}OldTrackIsSut uses Python identifier OldTrackIsSut
    __OldTrackIsSut = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OldTrackIsSut'), 'OldTrackIsSut', '__httpwww_amherst_comCEESIMXML_ctTrackEvent_httpwww_amherst_comCEESIMXMLOldTrackIsSut', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 141, 6), )

    
    OldTrackIsSut = property(__OldTrackIsSut.value, __OldTrackIsSut.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}OldTrackPlatform uses Python identifier OldTrackPlatform
    __OldTrackPlatform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OldTrackPlatform'), 'OldTrackPlatform', '__httpwww_amherst_comCEESIMXML_ctTrackEvent_httpwww_amherst_comCEESIMXMLOldTrackPlatform', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 142, 6), )

    
    OldTrackPlatform = property(__OldTrackPlatform.value, __OldTrackPlatform.set, None, None)

    _ElementMap.update({
        __OverrideTrack.name() : __OverrideTrack,
        __NewTrackPlatform.name() : __NewTrackPlatform,
        __OldTrackDataValid.name() : __OldTrackDataValid,
        __OldTrackIsSut.name() : __OldTrackIsSut,
        __OldTrackPlatform.name() : __OldTrackPlatform
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctTrackEvent = ctTrackEvent
Namespace.addCategoryObject('typeBinding', 'ctTrackEvent', ctTrackEvent)


# Complex type {http://www.amherst.com/CEESIM/XML}ctInterruptRecordList with content type ELEMENT_ONLY
class ctInterruptRecordList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctInterruptRecordList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctInterruptRecordList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 146, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}InterruptRecord uses Python identifier InterruptRecord
    __InterruptRecord = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterruptRecord'), 'InterruptRecord', '__httpwww_amherst_comCEESIMXML_ctInterruptRecordList_httpwww_amherst_comCEESIMXMLInterruptRecord', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 148, 6), )

    
    InterruptRecord = property(__InterruptRecord.value, __InterruptRecord.set, None, None)

    _ElementMap.update({
        __InterruptRecord.name() : __InterruptRecord
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctInterruptRecordList = ctInterruptRecordList
Namespace.addCategoryObject('typeBinding', 'ctInterruptRecordList', ctInterruptRecordList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctInterruptRecord with content type ELEMENT_ONLY
class ctInterruptRecord (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctInterruptRecord with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctInterruptRecord')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 152, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}OverrideInterruptGenerators uses Python identifier OverrideInterruptGenerators
    __OverrideInterruptGenerators = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OverrideInterruptGenerators'), 'OverrideInterruptGenerators', '__httpwww_amherst_comCEESIMXML_ctInterruptRecord_httpwww_amherst_comCEESIMXMLOverrideInterruptGenerators', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 154, 6), )

    
    OverrideInterruptGenerators = property(__OverrideInterruptGenerators.value, __OverrideInterruptGenerators.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}InterruptActive uses Python identifier InterruptActive
    __InterruptActive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterruptActive'), 'InterruptActive', '__httpwww_amherst_comCEESIMXML_ctInterruptRecord_httpwww_amherst_comCEESIMXMLInterruptActive', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 155, 6), )

    
    InterruptActive = property(__InterruptActive.value, __InterruptActive.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}InterruptGeneratorNumber uses Python identifier InterruptGeneratorNumber
    __InterruptGeneratorNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterruptGeneratorNumber'), 'InterruptGeneratorNumber', '__httpwww_amherst_comCEESIMXML_ctInterruptRecord_httpwww_amherst_comCEESIMXMLInterruptGeneratorNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 156, 6), )

    
    InterruptGeneratorNumber = property(__InterruptGeneratorNumber.value, __InterruptGeneratorNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}OverrideTrack uses Python identifier OverrideTrack
    __OverrideTrack = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack'), 'OverrideTrack', '__httpwww_amherst_comCEESIMXML_ctInterruptRecord_httpwww_amherst_comCEESIMXMLOverrideTrack', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 157, 6), )

    
    OverrideTrack = property(__OverrideTrack.value, __OverrideTrack.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TrackEvents uses Python identifier TrackEvents
    __TrackEvents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TrackEvents'), 'TrackEvents', '__httpwww_amherst_comCEESIMXML_ctInterruptRecord_httpwww_amherst_comCEESIMXMLTrackEvents', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 158, 6), )

    
    TrackEvents = property(__TrackEvents.value, __TrackEvents.set, None, None)

    _ElementMap.update({
        __OverrideInterruptGenerators.name() : __OverrideInterruptGenerators,
        __InterruptActive.name() : __InterruptActive,
        __InterruptGeneratorNumber.name() : __InterruptGeneratorNumber,
        __OverrideTrack.name() : __OverrideTrack,
        __TrackEvents.name() : __TrackEvents
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctInterruptRecord = ctInterruptRecord
Namespace.addCategoryObject('typeBinding', 'ctInterruptRecord', ctInterruptRecord)


Emitter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Emitter'), ctEmitterData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterRootR1-1.xsd', 39, 2))
Namespace.addCategoryObject('elementBinding', Emitter.name().localName(), Emitter)



ctFlatEarthPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'X'), stDoubleX, scope=ctFlatEarthPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 43, 6)))

ctFlatEarthPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Y'), stDoubleY, scope=ctFlatEarthPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 44, 6)))

ctFlatEarthPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Z'), stDoubleZ, scope=ctFlatEarthPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 45, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 43, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctFlatEarthPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'X')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 43, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 44, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctFlatEarthPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Y')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 44, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 45, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctFlatEarthPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Z')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 45, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 43, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 44, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 45, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 42, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctFlatEarthPoint._Automaton = _BuildAutomaton()




ctModificationHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreationDate'), stDateCreationDate, scope=ctModificationHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 51, 6)))

ctModificationHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModificationDate'), stDateModificationDate, scope=ctModificationHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 52, 6)))

ctModificationHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), stTextCommentHeader, scope=ctModificationHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 53, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 51, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctModificationHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreationDate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 51, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 52, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctModificationHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ModificationDate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 52, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 53, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctModificationHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 53, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 51, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 52, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 53, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 50, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctModificationHeader._Automaton = _BuildAutomaton_4()




ctPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FlatEarthPoint'), ctFlatEarthPoint, scope=ctPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 59, 6)))

ctPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RoundEarthPoint'), ctRoundEarthPoint, scope=ctPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 60, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 58, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 59, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 60, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ctPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FlatEarthPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 59, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ctPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RoundEarthPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 60, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctPoint._Automaton = _BuildAutomaton_8()




ctRoundEarthPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Latitude'), stDoubleLatitude, scope=ctRoundEarthPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 66, 6)))

ctRoundEarthPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Longitude'), stDoubleLongitude, scope=ctRoundEarthPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 67, 6)))

ctRoundEarthPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Altitude'), stDoubleAltitude, scope=ctRoundEarthPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 68, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 66, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctRoundEarthPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Latitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 66, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 67, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctRoundEarthPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Longitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 67, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 68, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctRoundEarthPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Altitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 68, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 66, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 67, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 68, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_10())
    sub_automata.append(_BuildAutomaton_11())
    sub_automata.append(_BuildAutomaton_12())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonTypesR1-1.xsd', 65, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctRoundEarthPoint._Automaton = _BuildAutomaton_9()




ctEmitterData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterHeader'), ctEmitterHeader, scope=ctEmitterData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 43, 6)))

ctEmitterData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterScript'), ctEmitterScriptEventList, scope=ctEmitterData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 44, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctEmitterData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterHeader')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 43, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 44, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterScript')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 44, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 44, 6))
    counters.add(cc_0)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_14())
    sub_automata.append(_BuildAutomaton_15())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 42, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctEmitterData._Automaton = _BuildAutomaton_13()




ctEmitterHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UserEmitterNumber'), stIntUserEmitterNumber, scope=ctEmitterHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 56, 6)))

ctEmitterHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterId'), stStringEmitterId, scope=ctEmitterHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 57, 6)))

ctEmitterHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterName'), stStringEmitterName, scope=ctEmitterHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 58, 6)))

ctEmitterHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'XOffset'), stDoubleXOffset, scope=ctEmitterHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 59, 6)))

ctEmitterHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'YOffset'), stDoubleYOffset, scope=ctEmitterHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 60, 6)))

ctEmitterHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ZOffset'), stDoubleZOffset, scope=ctEmitterHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 61, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctEmitterHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UserEmitterNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 56, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctEmitterHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterId')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 57, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctEmitterHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 58, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 59, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'XOffset')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 59, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 60, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'YOffset')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 60, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 61, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ZOffset')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 61, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 59, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 60, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 61, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 55, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctEmitterHeader._Automaton = _BuildAutomaton_16()




ctEmitterScriptEventList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterScriptEvent'), ctEmitterScriptEvent, scope=ctEmitterScriptEventList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 67, 6)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 66, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEventList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterScriptEvent')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 67, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctEmitterScriptEventList._Automaton = _BuildAutomaton_23()




ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EventNumber'), stIntEventNumber, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 73, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EventTime'), stDoubleEventTime, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 74, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EventType'), stEnumEventType, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 75, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModeName'), stStringModeNameScript, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 76, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RadiationState'), stBoolRadiationState, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 77, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResyncOnModeChangeState'), stBoolResyncOnModeChangeState, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 78, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChangeTracking'), stBoolChangeTracking, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 79, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DwellDuration'), stDoubleDwellDurationScript, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 80, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TrackPlatformNumbers'), ctTrackPlatformNumberList, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 81, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeneratorEventDefined'), stBoolGeneratorEventDefined, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 82, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RangeEvents'), ctRangeEventList, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 84, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeneratorScriptEvents'), ctGeneratorScriptEventList, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 85, 6)))

ctEmitterScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AssociatedSubmodeName'), stStringAssociatedSubmodeName, scope=ctEmitterScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 86, 6)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 73, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EventNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 73, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 74, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EventTime')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 74, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 75, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EventType')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 75, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 76, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ModeName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 76, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 77, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RadiationState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 77, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 78, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResyncOnModeChangeState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 78, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 79, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChangeTracking')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 79, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 80, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DwellDuration')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 80, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 81, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TrackPlatformNumbers')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 81, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 82, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeneratorEventDefined')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 82, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 84, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RangeEvents')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 84, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 85, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeneratorScriptEvents')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 85, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 86, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctEmitterScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AssociatedSubmodeName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 86, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 73, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 74, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 75, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 76, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 77, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 78, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 79, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 80, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 81, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 82, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 84, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 85, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 86, 6))
    counters.add(cc_12)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_25())
    sub_automata.append(_BuildAutomaton_26())
    sub_automata.append(_BuildAutomaton_27())
    sub_automata.append(_BuildAutomaton_28())
    sub_automata.append(_BuildAutomaton_29())
    sub_automata.append(_BuildAutomaton_30())
    sub_automata.append(_BuildAutomaton_31())
    sub_automata.append(_BuildAutomaton_32())
    sub_automata.append(_BuildAutomaton_33())
    sub_automata.append(_BuildAutomaton_34())
    sub_automata.append(_BuildAutomaton_35())
    sub_automata.append(_BuildAutomaton_36())
    sub_automata.append(_BuildAutomaton_37())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 72, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctEmitterScriptEvent._Automaton = _BuildAutomaton_24()




ctTrackPlatformNumberList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TrackPlatformNumber'), stIntTrackPlatformNumber, scope=ctTrackPlatformNumberList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 93, 6)))

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=32, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 92, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTrackPlatformNumberList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TrackPlatformNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 93, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctTrackPlatformNumberList._Automaton = _BuildAutomaton_38()




ctRangeEventList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RangeEvent'), ctRangeEvent, scope=ctRangeEventList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 99, 6)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 98, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctRangeEventList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RangeEvent')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 99, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctRangeEventList._Automaton = _BuildAutomaton_39()




ctGeneratorScriptEventList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeneratorScriptEvent'), ctGeneratorScriptEvent, scope=ctGeneratorScriptEventList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 105, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 104, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGeneratorScriptEventList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeneratorScriptEvent')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 105, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctGeneratorScriptEventList._Automaton = _BuildAutomaton_40()




ctRangeEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HighRange'), stDoubleHighRange, scope=ctRangeEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 111, 6)))

ctRangeEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RangeModeName'), stStringRangeModeName, scope=ctRangeEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 112, 6)))

ctRangeEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RangeRadiationState'), stBoolRangeRadiationState, scope=ctRangeEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 113, 6)))

ctRangeEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RangeResyncOnModeChangeState'), stBoolRangeResyncOnModeChangeState, scope=ctRangeEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 114, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 111, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctRangeEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HighRange')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 111, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 112, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctRangeEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RangeModeName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 112, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 113, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctRangeEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RangeRadiationState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 113, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 114, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctRangeEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RangeResyncOnModeChangeState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 114, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 111, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 112, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 113, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 114, 6))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_42())
    sub_automata.append(_BuildAutomaton_43())
    sub_automata.append(_BuildAutomaton_44())
    sub_automata.append(_BuildAutomaton_45())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 110, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctRangeEvent._Automaton = _BuildAutomaton_41()




ctGeneratorScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeneratorNumber'), stIntScriptGeneratorNumber, scope=ctGeneratorScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 120, 6)))

ctGeneratorScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeneratorActive'), stBoolGeneratorActive, scope=ctGeneratorScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 121, 6)))

ctGeneratorScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RadiationEnable'), stBoolRadiationEnable, scope=ctGeneratorScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 122, 6)))

ctGeneratorScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack'), stBoolOverrideTrack, scope=ctGeneratorScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 123, 6)))

ctGeneratorScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TrackEvents'), ctTrackEventList, scope=ctGeneratorScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 124, 6)))

ctGeneratorScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OverrideScanInterrupts'), stBoolOverrideScanInterrupts, scope=ctGeneratorScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 125, 6)))

ctGeneratorScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterruptRecords'), ctInterruptRecordList, scope=ctGeneratorScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 126, 6)))

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 120, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGeneratorScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeneratorNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 120, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 121, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGeneratorScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeneratorActive')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 121, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 122, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGeneratorScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RadiationEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 122, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 123, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGeneratorScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 123, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 124, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGeneratorScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TrackEvents')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 124, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 125, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGeneratorScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OverrideScanInterrupts')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 125, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 126, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGeneratorScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterruptRecords')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 126, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 120, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 121, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 122, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 123, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 124, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 125, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 126, 6))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_47())
    sub_automata.append(_BuildAutomaton_48())
    sub_automata.append(_BuildAutomaton_49())
    sub_automata.append(_BuildAutomaton_50())
    sub_automata.append(_BuildAutomaton_51())
    sub_automata.append(_BuildAutomaton_52())
    sub_automata.append(_BuildAutomaton_53())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 119, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctGeneratorScriptEvent._Automaton = _BuildAutomaton_46()




ctTrackEventList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TrackEvent'), ctTrackEvent, scope=ctTrackEventList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 132, 6)))

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 131, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTrackEventList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TrackEvent')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 132, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctTrackEventList._Automaton = _BuildAutomaton_54()




ctTrackEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack'), stBoolOverrideTrack, scope=ctTrackEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 138, 6)))

ctTrackEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NewTrackPlatform'), stIntPlatformTrackNumber, scope=ctTrackEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 139, 6)))

ctTrackEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OldTrackDataValid'), stBoolOldTrackDataValid, scope=ctTrackEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 140, 6)))

ctTrackEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OldTrackIsSut'), stBoolOldTrackIsSut, scope=ctTrackEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 141, 6)))

ctTrackEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OldTrackPlatform'), stIntPlatformTrackNumber, scope=ctTrackEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 142, 6)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 138, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTrackEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 138, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 139, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTrackEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NewTrackPlatform')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 139, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 140, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTrackEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OldTrackDataValid')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 140, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 141, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTrackEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OldTrackIsSut')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 141, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 142, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTrackEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OldTrackPlatform')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 142, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 138, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 139, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 140, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 141, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 142, 6))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_56())
    sub_automata.append(_BuildAutomaton_57())
    sub_automata.append(_BuildAutomaton_58())
    sub_automata.append(_BuildAutomaton_59())
    sub_automata.append(_BuildAutomaton_60())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 137, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctTrackEvent._Automaton = _BuildAutomaton_55()




ctInterruptRecordList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterruptRecord'), ctInterruptRecord, scope=ctInterruptRecordList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 148, 6)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 147, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterruptRecordList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterruptRecord')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 148, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctInterruptRecordList._Automaton = _BuildAutomaton_61()




ctInterruptRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OverrideInterruptGenerators'), stBoolOverrideInterruptGenerators, scope=ctInterruptRecord, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 154, 6)))

ctInterruptRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterruptActive'), stBoolInterruptActive, scope=ctInterruptRecord, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 155, 6)))

ctInterruptRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterruptGeneratorNumber'), stIntInterruptGeneratorNumber, scope=ctInterruptRecord, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 156, 6)))

ctInterruptRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack'), stBoolOverrideTrack, scope=ctInterruptRecord, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 157, 6)))

ctInterruptRecord._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TrackEvents'), ctTrackEventList, scope=ctInterruptRecord, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 158, 6)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 154, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterruptRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OverrideInterruptGenerators')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 154, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 155, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterruptRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterruptActive')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 155, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 156, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterruptRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterruptGeneratorNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 156, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 157, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterruptRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OverrideTrack')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 157, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 158, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterruptRecord._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TrackEvents')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 158, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 154, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 155, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 156, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 157, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 158, 6))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_63())
    sub_automata.append(_BuildAutomaton_64())
    sub_automata.append(_BuildAutomaton_65())
    sub_automata.append(_BuildAutomaton_66())
    sub_automata.append(_BuildAutomaton_67())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/emitterDataR1-1.xsd', 153, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctInterruptRecord._Automaton = _BuildAutomaton_62()

