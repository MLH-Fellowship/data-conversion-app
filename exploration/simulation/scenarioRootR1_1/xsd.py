# ./data/ceesim/schema/simulation/scenarioRootR1_1/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:33:02.557680 by PyXB version 1.2.6 using Python 3.6.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:54a980e6-715f-11eb-8cf0-00155debab14')

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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAtmosphericAbsorptionAttenuationEnable
class stBoolAtmosphericAbsorptionAttenuationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAtmosphericAbsorptionAttenuationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 386, 2)
    _Documentation = ''
stBoolAtmosphericAbsorptionAttenuationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAtmosphericAbsorptionAttenuationEnable', stBoolAtmosphericAbsorptionAttenuationEnable)
_module_typeBindings.stBoolAtmosphericAbsorptionAttenuationEnable = stBoolAtmosphericAbsorptionAttenuationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolCircularBufferCollection
class stBoolCircularBufferCollection (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolCircularBufferCollection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 395, 2)
    _Documentation = ''
stBoolCircularBufferCollection._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolCircularBufferCollection', stBoolCircularBufferCollection)
_module_typeBindings.stBoolCircularBufferCollection = stBoolCircularBufferCollection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolCwInterruptEnable
class stBoolCwInterruptEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolCwInterruptEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 404, 2)
    _Documentation = ''
stBoolCwInterruptEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolCwInterruptEnable', stBoolCwInterruptEnable)
_module_typeBindings.stBoolCwInterruptEnable = stBoolCwInterruptEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDataRecordingEnable
class stBoolDataRecordingEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDataRecordingEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 413, 2)
    _Documentation = ''
stBoolDataRecordingEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDataRecordingEnable', stBoolDataRecordingEnable)
_module_typeBindings.stBoolDataRecordingEnable = stBoolDataRecordingEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayBarriers
class stBoolDisplayBarriers (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayBarriers')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 422, 2)
    _Documentation = ''
stBoolDisplayBarriers._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayBarriers', stBoolDisplayBarriers)
_module_typeBindings.stBoolDisplayBarriers = stBoolDisplayBarriers

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayCanals
class stBoolDisplayCanals (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayCanals')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 431, 2)
    _Documentation = ''
stBoolDisplayCanals._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayCanals', stBoolDisplayCanals)
_module_typeBindings.stBoolDisplayCanals = stBoolDisplayCanals

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayCoastline
class stBoolDisplayCoastline (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayCoastline')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 440, 2)
    _Documentation = ''
stBoolDisplayCoastline._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayCoastline', stBoolDisplayCoastline)
_module_typeBindings.stBoolDisplayCoastline = stBoolDisplayCoastline

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayDepthLines
class stBoolDisplayDepthLines (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayDepthLines')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 449, 2)
    _Documentation = ''
stBoolDisplayDepthLines._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayDepthLines', stBoolDisplayDepthLines)
_module_typeBindings.stBoolDisplayDepthLines = stBoolDisplayDepthLines

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayGeopolitical
class stBoolDisplayGeopolitical (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayGeopolitical')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 458, 2)
    _Documentation = ''
stBoolDisplayGeopolitical._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayGeopolitical', stBoolDisplayGeopolitical)
_module_typeBindings.stBoolDisplayGeopolitical = stBoolDisplayGeopolitical

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayGrids
class stBoolDisplayGrids (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayGrids')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 467, 2)
    _Documentation = ''
stBoolDisplayGrids._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayGrids', stBoolDisplayGrids)
_module_typeBindings.stBoolDisplayGrids = stBoolDisplayGrids

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayHud
class stBoolDisplayHud (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayHud')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 476, 2)
    _Documentation = ''
stBoolDisplayHud._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayHud', stBoolDisplayHud)
_module_typeBindings.stBoolDisplayHud = stBoolDisplayHud

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayInactivePlatforms
class stBoolDisplayInactivePlatforms (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayInactivePlatforms')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 485, 2)
    _Documentation = ''
stBoolDisplayInactivePlatforms._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayInactivePlatforms', stBoolDisplayInactivePlatforms)
_module_typeBindings.stBoolDisplayInactivePlatforms = stBoolDisplayInactivePlatforms

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayLandforms
class stBoolDisplayLandforms (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayLandforms')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 494, 2)
    _Documentation = ''
stBoolDisplayLandforms._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayLandforms', stBoolDisplayLandforms)
_module_typeBindings.stBoolDisplayLandforms = stBoolDisplayLandforms

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPipelines
class stBoolDisplayPipelines (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPipelines')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 503, 2)
    _Documentation = ''
stBoolDisplayPipelines._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPipelines', stBoolDisplayPipelines)
_module_typeBindings.stBoolDisplayPipelines = stBoolDisplayPipelines

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPoliticalLines
class stBoolDisplayPoliticalLines (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPoliticalLines')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 512, 2)
    _Documentation = ''
stBoolDisplayPoliticalLines._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPoliticalLines', stBoolDisplayPoliticalLines)
_module_typeBindings.stBoolDisplayPoliticalLines = stBoolDisplayPoliticalLines

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPath
class stBoolDisplayPath (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPath')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 521, 2)
    _Documentation = ''
stBoolDisplayPath._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPath', stBoolDisplayPath)
_module_typeBindings.stBoolDisplayPath = stBoolDisplayPath

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPathHistory
class stBoolDisplayPathHistory (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPathHistory')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 530, 2)
    _Documentation = ''
stBoolDisplayPathHistory._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPathHistory', stBoolDisplayPathHistory)
_module_typeBindings.stBoolDisplayPathHistory = stBoolDisplayPathHistory

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPlatform
class stBoolDisplayPlatform (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPlatform')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 539, 2)
    _Documentation = ''
stBoolDisplayPlatform._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPlatform', stBoolDisplayPlatform)
_module_typeBindings.stBoolDisplayPlatform = stBoolDisplayPlatform

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPlatformDetails
class stBoolDisplayPlatformDetails (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPlatformDetails')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 548, 2)
    _Documentation = ''
stBoolDisplayPlatformDetails._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPlatformDetails', stBoolDisplayPlatformDetails)
_module_typeBindings.stBoolDisplayPlatformDetails = stBoolDisplayPlatformDetails

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayProjectedPath
class stBoolDisplayProjectedPath (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayProjectedPath')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 557, 2)
    _Documentation = ''
stBoolDisplayProjectedPath._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayProjectedPath', stBoolDisplayProjectedPath)
_module_typeBindings.stBoolDisplayProjectedPath = stBoolDisplayProjectedPath

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayRailroads
class stBoolDisplayRailroads (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayRailroads')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 566, 2)
    _Documentation = ''
stBoolDisplayRailroads._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayRailroads', stBoolDisplayRailroads)
_module_typeBindings.stBoolDisplayRailroads = stBoolDisplayRailroads

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayRoads
class stBoolDisplayRoads (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayRoads')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 575, 2)
    _Documentation = ''
stBoolDisplayRoads._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayRoads', stBoolDisplayRoads)
_module_typeBindings.stBoolDisplayRoads = stBoolDisplayRoads

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayRoughness
class stBoolDisplayRoughness (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayRoughness')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 584, 2)
    _Documentation = ''
stBoolDisplayRoughness._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayRoughness', stBoolDisplayRoughness)
_module_typeBindings.stBoolDisplayRoughness = stBoolDisplayRoughness

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayRoughnessLegend
class stBoolDisplayRoughnessLegend (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayRoughnessLegend')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 593, 2)
    _Documentation = ''
stBoolDisplayRoughnessLegend._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayRoughnessLegend', stBoolDisplayRoughnessLegend)
_module_typeBindings.stBoolDisplayRoughnessLegend = stBoolDisplayRoughnessLegend

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayStructures
class stBoolDisplayStructures (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayStructures')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 602, 2)
    _Documentation = ''
stBoolDisplayStructures._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayStructures', stBoolDisplayStructures)
_module_typeBindings.stBoolDisplayStructures = stBoolDisplayStructures

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplaySymbol
class stBoolDisplaySymbol (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplaySymbol')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 611, 2)
    _Documentation = ''
stBoolDisplaySymbol._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplaySymbol', stBoolDisplaySymbol)
_module_typeBindings.stBoolDisplaySymbol = stBoolDisplaySymbol

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplaySymbolLegend
class stBoolDisplaySymbolLegend (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplaySymbolLegend')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 620, 2)
    _Documentation = ''
stBoolDisplaySymbolLegend._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplaySymbolLegend', stBoolDisplaySymbolLegend)
_module_typeBindings.stBoolDisplaySymbolLegend = stBoolDisplaySymbolLegend

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayTerrain
class stBoolDisplayTerrain (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayTerrain')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 629, 2)
    _Documentation = ''
stBoolDisplayTerrain._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayTerrain', stBoolDisplayTerrain)
_module_typeBindings.stBoolDisplayTerrain = stBoolDisplayTerrain

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayTerrainLegend
class stBoolDisplayTerrainLegend (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayTerrainLegend')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 638, 2)
    _Documentation = ''
stBoolDisplayTerrainLegend._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayTerrainLegend', stBoolDisplayTerrainLegend)
_module_typeBindings.stBoolDisplayTerrainLegend = stBoolDisplayTerrainLegend

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayTrails
class stBoolDisplayTrails (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayTrails')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 647, 2)
    _Documentation = ''
stBoolDisplayTrails._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayTrails', stBoolDisplayTrails)
_module_typeBindings.stBoolDisplayTrails = stBoolDisplayTrails

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayUtilities
class stBoolDisplayUtilities (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayUtilities')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 656, 2)
    _Documentation = ''
stBoolDisplayUtilities._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayUtilities', stBoolDisplayUtilities)
_module_typeBindings.stBoolDisplayUtilities = stBoolDisplayUtilities

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayVisibility
class stBoolDisplayVisibility (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayVisibility')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 665, 2)
    _Documentation = ''
stBoolDisplayVisibility._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayVisibility', stBoolDisplayVisibility)
_module_typeBindings.stBoolDisplayVisibility = stBoolDisplayVisibility

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayVmapLegend
class stBoolDisplayVmapLegend (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayVmapLegend')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 674, 2)
    _Documentation = ''
stBoolDisplayVmapLegend._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayVmapLegend', stBoolDisplayVmapLegend)
_module_typeBindings.stBoolDisplayVmapLegend = stBoolDisplayVmapLegend

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayWaterways
class stBoolDisplayWaterways (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayWaterways')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 683, 2)
    _Documentation = ''
stBoolDisplayWaterways._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayWaterways', stBoolDisplayWaterways)
_module_typeBindings.stBoolDisplayWaterways = stBoolDisplayWaterways

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDpmBoardCollectionEnable
class stBoolDpmBoardCollectionEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDpmBoardCollectionEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 692, 2)
    _Documentation = ''
stBoolDpmBoardCollectionEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDpmBoardCollectionEnable', stBoolDpmBoardCollectionEnable)
_module_typeBindings.stBoolDpmBoardCollectionEnable = stBoolDpmBoardCollectionEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDuctingEnable
class stBoolDuctingEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDuctingEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 701, 2)
    _Documentation = ''
stBoolDuctingEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDuctingEnable', stBoolDuctingEnable)
_module_typeBindings.stBoolDuctingEnable = stBoolDuctingEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolEmitterLibraryEnable
class stBoolEmitterLibraryEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolEmitterLibraryEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 710, 2)
    _Documentation = ''
stBoolEmitterLibraryEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolEmitterLibraryEnable', stBoolEmitterLibraryEnable)
_module_typeBindings.stBoolEmitterLibraryEnable = stBoolEmitterLibraryEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolExternalSutFlag
class stBoolExternalSutFlag (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolExternalSutFlag')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 719, 2)
    _Documentation = ''
stBoolExternalSutFlag._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolExternalSutFlag', stBoolExternalSutFlag)
_module_typeBindings.stBoolExternalSutFlag = stBoolExternalSutFlag

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolFrequencyAttenuationEnable
class stBoolFrequencyAttenuationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolFrequencyAttenuationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 728, 2)
    _Documentation = ''
stBoolFrequencyAttenuationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolFrequencyAttenuationEnable', stBoolFrequencyAttenuationEnable)
_module_typeBindings.stBoolFrequencyAttenuationEnable = stBoolFrequencyAttenuationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolFrequencyDopplerShiftEnable
class stBoolFrequencyDopplerShiftEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolFrequencyDopplerShiftEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 737, 2)
    _Documentation = ''
stBoolFrequencyDopplerShiftEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolFrequencyDopplerShiftEnable', stBoolFrequencyDopplerShiftEnable)
_module_typeBindings.stBoolFrequencyDopplerShiftEnable = stBoolFrequencyDopplerShiftEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolGeotiffEnable
class stBoolGeotiffEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolGeotiffEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 746, 2)
    _Documentation = ''
stBoolGeotiffEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolGeotiffEnable', stBoolGeotiffEnable)
_module_typeBindings.stBoolGeotiffEnable = stBoolGeotiffEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolHorizonMaskingEnable
class stBoolHorizonMaskingEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolHorizonMaskingEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 755, 2)
    _Documentation = ''
stBoolHorizonMaskingEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolHorizonMaskingEnable', stBoolHorizonMaskingEnable)
_module_typeBindings.stBoolHorizonMaskingEnable = stBoolHorizonMaskingEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInvalidPdwsFlag
class stBoolInvalidPdwsFlag (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInvalidPdwsFlag')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 764, 2)
    _Documentation = ''
stBoolInvalidPdwsFlag._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInvalidPdwsFlag', stBoolInvalidPdwsFlag)
_module_typeBindings.stBoolInvalidPdwsFlag = stBoolInvalidPdwsFlag

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolMultipathEnable
class stBoolMultipathEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolMultipathEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 773, 2)
    _Documentation = ''
stBoolMultipathEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolMultipathEnable', stBoolMultipathEnable)
_module_typeBindings.stBoolMultipathEnable = stBoolMultipathEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolNavIfEnable
class stBoolNavIfEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolNavIfEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 782, 2)
    _Documentation = ''
stBoolNavIfEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolNavIfEnable', stBoolNavIfEnable)
_module_typeBindings.stBoolNavIfEnable = stBoolNavIfEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPulseTruncationEnable
class stBoolPulseTruncationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPulseTruncationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 791, 2)
    _Documentation = ''
stBoolPulseTruncationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPulseTruncationEnable', stBoolPulseTruncationEnable)
_module_typeBindings.stBoolPulseTruncationEnable = stBoolPulseTruncationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRangeAndPriDopplerShiftEnable
class stBoolRangeAndPriDopplerShiftEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRangeAndPriDopplerShiftEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 800, 2)
    _Documentation = ''
stBoolRangeAndPriDopplerShiftEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRangeAndPriDopplerShiftEnable', stBoolRangeAndPriDopplerShiftEnable)
_module_typeBindings.stBoolRangeAndPriDopplerShiftEnable = stBoolRangeAndPriDopplerShiftEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRangeAttenuationEnable
class stBoolRangeAttenuationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRangeAttenuationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 809, 2)
    _Documentation = ''
stBoolRangeAttenuationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRangeAttenuationEnable', stBoolRangeAttenuationEnable)
_module_typeBindings.stBoolRangeAttenuationEnable = stBoolRangeAttenuationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordEmitterEventsEnable
class stBoolRecordEmitterEventsEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordEmitterEventsEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 818, 2)
    _Documentation = ''
stBoolRecordEmitterEventsEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordEmitterEventsEnable', stBoolRecordEmitterEventsEnable)
_module_typeBindings.stBoolRecordEmitterEventsEnable = stBoolRecordEmitterEventsEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordEmitterStatusEnable
class stBoolRecordEmitterStatusEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordEmitterStatusEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 827, 2)
    _Documentation = ''
stBoolRecordEmitterStatusEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordEmitterStatusEnable', stBoolRecordEmitterStatusEnable)
_module_typeBindings.stBoolRecordEmitterStatusEnable = stBoolRecordEmitterStatusEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordPlatformEventsEnable
class stBoolRecordPlatformEventsEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordPlatformEventsEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 836, 2)
    _Documentation = ''
stBoolRecordPlatformEventsEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordPlatformEventsEnable', stBoolRecordPlatformEventsEnable)
_module_typeBindings.stBoolRecordPlatformEventsEnable = stBoolRecordPlatformEventsEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordPlatformStatusEnable
class stBoolRecordPlatformStatusEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordPlatformStatusEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 845, 2)
    _Documentation = ''
stBoolRecordPlatformStatusEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordPlatformStatusEnable', stBoolRecordPlatformStatusEnable)
_module_typeBindings.stBoolRecordPlatformStatusEnable = stBoolRecordPlatformStatusEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordPulseCountsEnable
class stBoolRecordPulseCountsEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordPulseCountsEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 854, 2)
    _Documentation = ''
stBoolRecordPulseCountsEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordPulseCountsEnable', stBoolRecordPulseCountsEnable)
_module_typeBindings.stBoolRecordPulseCountsEnable = stBoolRecordPulseCountsEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRoughnessEnable
class stBoolRoughnessEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRoughnessEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 863, 2)
    _Documentation = ''
stBoolRoughnessEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRoughnessEnable', stBoolRoughnessEnable)
_module_typeBindings.stBoolRoughnessEnable = stBoolRoughnessEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolScenarioElementLibraryEnable
class stBoolScenarioElementLibraryEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolScenarioElementLibraryEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 872, 2)
    _Documentation = ''
stBoolScenarioElementLibraryEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolScenarioElementLibraryEnable', stBoolScenarioElementLibraryEnable)
_module_typeBindings.stBoolScenarioElementLibraryEnable = stBoolScenarioElementLibraryEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSensitivityThresholdEnable
class stBoolSensitivityThresholdEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSensitivityThresholdEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 881, 2)
    _Documentation = ''
stBoolSensitivityThresholdEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSensitivityThresholdEnable', stBoolSensitivityThresholdEnable)
_module_typeBindings.stBoolSensitivityThresholdEnable = stBoolSensitivityThresholdEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSutEmitterEarthReflectionEnable
class stBoolSutEmitterEarthReflectionEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSutEmitterEarthReflectionEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 890, 2)
    _Documentation = ''
stBoolSutEmitterEarthReflectionEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSutEmitterEarthReflectionEnable', stBoolSutEmitterEarthReflectionEnable)
_module_typeBindings.stBoolSutEmitterEarthReflectionEnable = stBoolSutEmitterEarthReflectionEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolTerrainEnable
class stBoolTerrainEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolTerrainEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 899, 2)
    _Documentation = ''
stBoolTerrainEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolTerrainEnable', stBoolTerrainEnable)
_module_typeBindings.stBoolTerrainEnable = stBoolTerrainEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolTerrainMaskingAttenuationEnable
class stBoolTerrainMaskingAttenuationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolTerrainMaskingAttenuationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 908, 2)
    _Documentation = ''
stBoolTerrainMaskingAttenuationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolTerrainMaskingAttenuationEnable', stBoolTerrainMaskingAttenuationEnable)
_module_typeBindings.stBoolTerrainMaskingAttenuationEnable = stBoolTerrainMaskingAttenuationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolVmapEnable
class stBoolVmapEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolVmapEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 917, 2)
    _Documentation = ''
stBoolVmapEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolVmapEnable', stBoolVmapEnable)
_module_typeBindings.stBoolVmapEnable = stBoolVmapEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolWaveSplashEnable
class stBoolWaveSplashEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolWaveSplashEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 926, 2)
    _Documentation = ''
stBoolWaveSplashEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolWaveSplashEnable', stBoolWaveSplashEnable)
_module_typeBindings.stBoolWaveSplashEnable = stBoolWaveSplashEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDisplayIntensity
class stDoubleDisplayIntensity (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDisplayIntensity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 935, 2)
    _Documentation = ''
stDoubleDisplayIntensity._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDisplayIntensity, value=pyxb.binding.datatypes.double(0.01))
stDoubleDisplayIntensity._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDisplayIntensity, value=pyxb.binding.datatypes.double(1.0))
stDoubleDisplayIntensity._InitializeFacetMap(stDoubleDisplayIntensity._CF_minInclusive,
   stDoubleDisplayIntensity._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDisplayIntensity', stDoubleDisplayIntensity)
_module_typeBindings.stDoubleDisplayIntensity = stDoubleDisplayIntensity

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDisplayScale
class stDoubleDisplayScale (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDisplayScale')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 947, 2)
    _Documentation = ''
stDoubleDisplayScale._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDisplayScale, value=pyxb.binding.datatypes.double(0.01))
stDoubleDisplayScale._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDisplayScale, value=pyxb.binding.datatypes.double(8.0))
stDoubleDisplayScale._InitializeFacetMap(stDoubleDisplayScale._CF_minInclusive,
   stDoubleDisplayScale._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDisplayScale', stDoubleDisplayScale)
_module_typeBindings.stDoubleDisplayScale = stDoubleDisplayScale

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDuctingHeight
class stDoubleDuctingHeight (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDuctingHeight')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 959, 2)
    _Documentation = ''
stDoubleDuctingHeight._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDuctingHeight, value=pyxb.binding.datatypes.double(0.0))
stDoubleDuctingHeight._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDuctingHeight, value=pyxb.binding.datatypes.double(1000000.0))
stDoubleDuctingHeight._InitializeFacetMap(stDoubleDuctingHeight._CF_minInclusive,
   stDoubleDuctingHeight._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDuctingHeight', stDoubleDuctingHeight)
_module_typeBindings.stDoubleDuctingHeight = stDoubleDuctingHeight

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDuctingRefractivity
class stDoubleDuctingRefractivity (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDuctingRefractivity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 971, 2)
    _Documentation = ''
stDoubleDuctingRefractivity._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDuctingRefractivity, value=pyxb.binding.datatypes.double(0.0))
stDoubleDuctingRefractivity._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDuctingRefractivity, value=pyxb.binding.datatypes.double(32.0))
stDoubleDuctingRefractivity._InitializeFacetMap(stDoubleDuctingRefractivity._CF_minInclusive,
   stDoubleDuctingRefractivity._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDuctingRefractivity', stDoubleDuctingRefractivity)
_module_typeBindings.stDoubleDuctingRefractivity = stDoubleDuctingRefractivity

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEarthRadiusFactor
class stDoubleEarthRadiusFactor (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEarthRadiusFactor')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 983, 2)
    _Documentation = ''
stDoubleEarthRadiusFactor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEarthRadiusFactor, value=pyxb.binding.datatypes.double(0.1))
stDoubleEarthRadiusFactor._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEarthRadiusFactor, value=pyxb.binding.datatypes.double(1000.0))
stDoubleEarthRadiusFactor._InitializeFacetMap(stDoubleEarthRadiusFactor._CF_minInclusive,
   stDoubleEarthRadiusFactor._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEarthRadiusFactor', stDoubleEarthRadiusFactor)
_module_typeBindings.stDoubleEarthRadiusFactor = stDoubleEarthRadiusFactor

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEastLongitude
class stDoubleEastLongitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEastLongitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 995, 2)
    _Documentation = ''
stDoubleEastLongitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEastLongitude, value=pyxb.binding.datatypes.double(0.0))
stDoubleEastLongitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEastLongitude, value=pyxb.binding.datatypes.double(180.0))
stDoubleEastLongitude._InitializeFacetMap(stDoubleEastLongitude._CF_minInclusive,
   stDoubleEastLongitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEastLongitude', stDoubleEastLongitude)
_module_typeBindings.stDoubleEastLongitude = stDoubleEastLongitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleGeopoliticalCenterLatitude
class stDoubleGeopoliticalCenterLatitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleGeopoliticalCenterLatitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1007, 2)
    _Documentation = ''
stDoubleGeopoliticalCenterLatitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleGeopoliticalCenterLatitude, value=pyxb.binding.datatypes.double(-90.0))
stDoubleGeopoliticalCenterLatitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleGeopoliticalCenterLatitude, value=pyxb.binding.datatypes.double(90.0))
stDoubleGeopoliticalCenterLatitude._InitializeFacetMap(stDoubleGeopoliticalCenterLatitude._CF_minInclusive,
   stDoubleGeopoliticalCenterLatitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleGeopoliticalCenterLatitude', stDoubleGeopoliticalCenterLatitude)
_module_typeBindings.stDoubleGeopoliticalCenterLatitude = stDoubleGeopoliticalCenterLatitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleGeopoliticalCenterLongitude
class stDoubleGeopoliticalCenterLongitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleGeopoliticalCenterLongitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1019, 2)
    _Documentation = ''
stDoubleGeopoliticalCenterLongitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleGeopoliticalCenterLongitude, value=pyxb.binding.datatypes.double(-180.0))
stDoubleGeopoliticalCenterLongitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleGeopoliticalCenterLongitude, value=pyxb.binding.datatypes.double(180.0))
stDoubleGeopoliticalCenterLongitude._InitializeFacetMap(stDoubleGeopoliticalCenterLongitude._CF_minInclusive,
   stDoubleGeopoliticalCenterLongitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleGeopoliticalCenterLongitude', stDoubleGeopoliticalCenterLongitude)
_module_typeBindings.stDoubleGeopoliticalCenterLongitude = stDoubleGeopoliticalCenterLongitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleIntensity
class stDoubleIntensity (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleIntensity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1031, 2)
    _Documentation = ''
stDoubleIntensity._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleIntensity, value=pyxb.binding.datatypes.double(0.0))
stDoubleIntensity._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleIntensity, value=pyxb.binding.datatypes.double(1.0))
stDoubleIntensity._InitializeFacetMap(stDoubleIntensity._CF_minInclusive,
   stDoubleIntensity._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleIntensity', stDoubleIntensity)
_module_typeBindings.stDoubleIntensity = stDoubleIntensity

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerAz
class stDoubleLowerAz (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerAz')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1043, 2)
    _Documentation = ''
stDoubleLowerAz._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerAz, value=pyxb.binding.datatypes.double(0.0))
stDoubleLowerAz._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerAz, value=pyxb.binding.datatypes.double(360.0))
stDoubleLowerAz._InitializeFacetMap(stDoubleLowerAz._CF_minInclusive,
   stDoubleLowerAz._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerAz', stDoubleLowerAz)
_module_typeBindings.stDoubleLowerAz = stDoubleLowerAz

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerElevation
class stDoubleLowerElevation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerElevation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1055, 2)
    _Documentation = ''
stDoubleLowerElevation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerElevation, value=pyxb.binding.datatypes.double(-90.0))
stDoubleLowerElevation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerElevation, value=pyxb.binding.datatypes.double(90.0))
stDoubleLowerElevation._InitializeFacetMap(stDoubleLowerElevation._CF_minInclusive,
   stDoubleLowerElevation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerElevation', stDoubleLowerElevation)
_module_typeBindings.stDoubleLowerElevation = stDoubleLowerElevation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerFrequency
class stDoubleLowerFrequency (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerFrequency')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1067, 2)
    _Documentation = ''
stDoubleLowerFrequency._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerFrequency, value=pyxb.binding.datatypes.double(0.0))
stDoubleLowerFrequency._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerFrequency, value=pyxb.binding.datatypes.double(131071000000.0))
stDoubleLowerFrequency._InitializeFacetMap(stDoubleLowerFrequency._CF_minInclusive,
   stDoubleLowerFrequency._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerFrequency', stDoubleLowerFrequency)
_module_typeBindings.stDoubleLowerFrequency = stDoubleLowerFrequency

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerPower
class stDoubleLowerPower (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerPower')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1079, 2)
    _Documentation = ''
stDoubleLowerPower._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerPower, value=pyxb.binding.datatypes.double(-256.0))
stDoubleLowerPower._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerPower, value=pyxb.binding.datatypes.double(255.75))
stDoubleLowerPower._InitializeFacetMap(stDoubleLowerPower._CF_minInclusive,
   stDoubleLowerPower._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerPower', stDoubleLowerPower)
_module_typeBindings.stDoubleLowerPower = stDoubleLowerPower

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerPulseWidth
class stDoubleLowerPulseWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerPulseWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1091, 2)
    _Documentation = ''
stDoubleLowerPulseWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerPulseWidth, value=pyxb.binding.datatypes.double(0.0))
stDoubleLowerPulseWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerPulseWidth, value=pyxb.binding.datatypes.double(0.131071))
stDoubleLowerPulseWidth._InitializeFacetMap(stDoubleLowerPulseWidth._CF_minInclusive,
   stDoubleLowerPulseWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerPulseWidth', stDoubleLowerPulseWidth)
_module_typeBindings.stDoubleLowerPulseWidth = stDoubleLowerPulseWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerTime
class stDoubleLowerTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1103, 2)
    _Documentation = ''
stDoubleLowerTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleLowerTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerTime, value=pyxb.binding.datatypes.double(137438.0))
stDoubleLowerTime._InitializeFacetMap(stDoubleLowerTime._CF_minInclusive,
   stDoubleLowerTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerTime', stDoubleLowerTime)
_module_typeBindings.stDoubleLowerTime = stDoubleLowerTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleNorthLatitude
class stDoubleNorthLatitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleNorthLatitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1115, 2)
    _Documentation = ''
stDoubleNorthLatitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleNorthLatitude, value=pyxb.binding.datatypes.double(0.0))
stDoubleNorthLatitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleNorthLatitude, value=pyxb.binding.datatypes.double(90.0))
stDoubleNorthLatitude._InitializeFacetMap(stDoubleNorthLatitude._CF_minInclusive,
   stDoubleNorthLatitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleNorthLatitude', stDoubleNorthLatitude)
_module_typeBindings.stDoubleNorthLatitude = stDoubleNorthLatitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleScale
class stDoubleScale (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleScale')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1127, 2)
    _Documentation = ''
stDoubleScale._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleScale, value=pyxb.binding.datatypes.double(0.0))
stDoubleScale._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleScale, value=pyxb.binding.datatypes.double(1.0))
stDoubleScale._InitializeFacetMap(stDoubleScale._CF_minInclusive,
   stDoubleScale._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleScale', stDoubleScale)
_module_typeBindings.stDoubleScale = stDoubleScale

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSouthLatitude
class stDoubleSouthLatitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSouthLatitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1139, 2)
    _Documentation = ''
stDoubleSouthLatitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSouthLatitude, value=pyxb.binding.datatypes.double(0.0))
stDoubleSouthLatitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSouthLatitude, value=pyxb.binding.datatypes.double(90.0))
stDoubleSouthLatitude._InitializeFacetMap(stDoubleSouthLatitude._CF_minInclusive,
   stDoubleSouthLatitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSouthLatitude', stDoubleSouthLatitude)
_module_typeBindings.stDoubleSouthLatitude = stDoubleSouthLatitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperAz
class stDoubleUpperAz (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperAz')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1151, 2)
    _Documentation = ''
stDoubleUpperAz._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperAz, value=pyxb.binding.datatypes.double(0.0))
stDoubleUpperAz._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperAz, value=pyxb.binding.datatypes.double(360.0))
stDoubleUpperAz._InitializeFacetMap(stDoubleUpperAz._CF_minInclusive,
   stDoubleUpperAz._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperAz', stDoubleUpperAz)
_module_typeBindings.stDoubleUpperAz = stDoubleUpperAz

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperElevation
class stDoubleUpperElevation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperElevation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1163, 2)
    _Documentation = ''
stDoubleUpperElevation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperElevation, value=pyxb.binding.datatypes.double(-90.0))
stDoubleUpperElevation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperElevation, value=pyxb.binding.datatypes.double(90.0))
stDoubleUpperElevation._InitializeFacetMap(stDoubleUpperElevation._CF_minInclusive,
   stDoubleUpperElevation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperElevation', stDoubleUpperElevation)
_module_typeBindings.stDoubleUpperElevation = stDoubleUpperElevation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperFrequency
class stDoubleUpperFrequency (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperFrequency')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1175, 2)
    _Documentation = ''
stDoubleUpperFrequency._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperFrequency, value=pyxb.binding.datatypes.double(0.0))
stDoubleUpperFrequency._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperFrequency, value=pyxb.binding.datatypes.double(131071000000.0))
stDoubleUpperFrequency._InitializeFacetMap(stDoubleUpperFrequency._CF_minInclusive,
   stDoubleUpperFrequency._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperFrequency', stDoubleUpperFrequency)
_module_typeBindings.stDoubleUpperFrequency = stDoubleUpperFrequency

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperPower
class stDoubleUpperPower (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperPower')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1187, 2)
    _Documentation = ''
stDoubleUpperPower._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperPower, value=pyxb.binding.datatypes.double(-256.0))
stDoubleUpperPower._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperPower, value=pyxb.binding.datatypes.double(255.75))
stDoubleUpperPower._InitializeFacetMap(stDoubleUpperPower._CF_minInclusive,
   stDoubleUpperPower._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperPower', stDoubleUpperPower)
_module_typeBindings.stDoubleUpperPower = stDoubleUpperPower

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperPulseWidth
class stDoubleUpperPulseWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperPulseWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1199, 2)
    _Documentation = ''
stDoubleUpperPulseWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperPulseWidth, value=pyxb.binding.datatypes.double(0.0))
stDoubleUpperPulseWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperPulseWidth, value=pyxb.binding.datatypes.double(0.131071))
stDoubleUpperPulseWidth._InitializeFacetMap(stDoubleUpperPulseWidth._CF_minInclusive,
   stDoubleUpperPulseWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperPulseWidth', stDoubleUpperPulseWidth)
_module_typeBindings.stDoubleUpperPulseWidth = stDoubleUpperPulseWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperTime
class stDoubleUpperTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1211, 2)
    _Documentation = ''
stDoubleUpperTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleUpperTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperTime, value=pyxb.binding.datatypes.double(137438.0))
stDoubleUpperTime._InitializeFacetMap(stDoubleUpperTime._CF_minInclusive,
   stDoubleUpperTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperTime', stDoubleUpperTime)
_module_typeBindings.stDoubleUpperTime = stDoubleUpperTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleVelocityVectorDuration
class stDoubleVelocityVectorDuration (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleVelocityVectorDuration')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1223, 2)
    _Documentation = ''
stDoubleVelocityVectorDuration._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleVelocityVectorDuration, value=pyxb.binding.datatypes.double(0.0))
stDoubleVelocityVectorDuration._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleVelocityVectorDuration, value=pyxb.binding.datatypes.double(600.0))
stDoubleVelocityVectorDuration._InitializeFacetMap(stDoubleVelocityVectorDuration._CF_minInclusive,
   stDoubleVelocityVectorDuration._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleVelocityVectorDuration', stDoubleVelocityVectorDuration)
_module_typeBindings.stDoubleVelocityVectorDuration = stDoubleVelocityVectorDuration

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleWestLongitude
class stDoubleWestLongitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleWestLongitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1235, 2)
    _Documentation = ''
stDoubleWestLongitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleWestLongitude, value=pyxb.binding.datatypes.double(0.0))
stDoubleWestLongitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleWestLongitude, value=pyxb.binding.datatypes.double(180.0))
stDoubleWestLongitude._InitializeFacetMap(stDoubleWestLongitude._CF_minInclusive,
   stDoubleWestLongitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleWestLongitude', stDoubleWestLongitude)
_module_typeBindings.stDoubleWestLongitude = stDoubleWestLongitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDgsVideoStateKind
class stEnumDgsVideoStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDgsVideoStateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1247, 2)
    _Documentation = ''
stEnumDgsVideoStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDgsVideoStateKind, enum_prefix=None)
stEnumDgsVideoStateKind.Ignore = stEnumDgsVideoStateKind._CF_enumeration.addEnumeration(unicode_value='Ignore', tag='Ignore')
stEnumDgsVideoStateKind.Store_Only_Video_Enabled_Pulses = stEnumDgsVideoStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Video_Enabled_Pulses', tag='Store_Only_Video_Enabled_Pulses')
stEnumDgsVideoStateKind._InitializeFacetMap(stEnumDgsVideoStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDgsVideoStateKind', stEnumDgsVideoStateKind)
_module_typeBindings.stEnumDgsVideoStateKind = stEnumDgsVideoStateKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDisplayCenterKind
class stEnumDisplayCenterKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDisplayCenterKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1259, 2)
    _Documentation = ''
stEnumDisplayCenterKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDisplayCenterKind, enum_prefix=None)
stEnumDisplayCenterKind.On_Sut = stEnumDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='On_Sut', tag='On_Sut')
stEnumDisplayCenterKind.On_Platform = stEnumDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='On_Platform', tag='On_Platform')
stEnumDisplayCenterKind.At_Fixed_Point = stEnumDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='At_Fixed_Point', tag='At_Fixed_Point')
stEnumDisplayCenterKind._InitializeFacetMap(stEnumDisplayCenterKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDisplayCenterKind', stEnumDisplayCenterKind)
_module_typeBindings.stEnumDisplayCenterKind = stEnumDisplayCenterKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDisplayGridKind
class stEnumDisplayGridKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDisplayGridKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1272, 2)
    _Documentation = ''
stEnumDisplayGridKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDisplayGridKind, enum_prefix=None)
stEnumDisplayGridKind.Decimal = stEnumDisplayGridKind._CF_enumeration.addEnumeration(unicode_value='Decimal', tag='Decimal')
stEnumDisplayGridKind.Deg_Min_Sec = stEnumDisplayGridKind._CF_enumeration.addEnumeration(unicode_value='Deg_Min_Sec', tag='Deg_Min_Sec')
stEnumDisplayGridKind._InitializeFacetMap(stEnumDisplayGridKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDisplayGridKind', stEnumDisplayGridKind)
_module_typeBindings.stEnumDisplayGridKind = stEnumDisplayGridKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDistanceUnits
class stEnumDistanceUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDistanceUnits')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1284, 2)
    _Documentation = ''
stEnumDistanceUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDistanceUnits, enum_prefix=None)
stEnumDistanceUnits.Kilometers = stEnumDistanceUnits._CF_enumeration.addEnumeration(unicode_value='Kilometers', tag='Kilometers')
stEnumDistanceUnits.Nautical_Miles = stEnumDistanceUnits._CF_enumeration.addEnumeration(unicode_value='Nautical_Miles', tag='Nautical_Miles')
stEnumDistanceUnits._InitializeFacetMap(stEnumDistanceUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDistanceUnits', stEnumDistanceUnits)
_module_typeBindings.stEnumDistanceUnits = stEnumDistanceUnits

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDuctingBoundaryKind
class stEnumDuctingBoundaryKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDuctingBoundaryKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1296, 2)
    _Documentation = ''
stEnumDuctingBoundaryKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDuctingBoundaryKind, enum_prefix=None)
stEnumDuctingBoundaryKind.Independent_Of_Surface_Type = stEnumDuctingBoundaryKind._CF_enumeration.addEnumeration(unicode_value='Independent_Of_Surface_Type', tag='Independent_Of_Surface_Type')
stEnumDuctingBoundaryKind.Land_Sea_Boundaries = stEnumDuctingBoundaryKind._CF_enumeration.addEnumeration(unicode_value='Land_Sea_Boundaries', tag='Land_Sea_Boundaries')
stEnumDuctingBoundaryKind._InitializeFacetMap(stEnumDuctingBoundaryKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDuctingBoundaryKind', stEnumDuctingBoundaryKind)
_module_typeBindings.stEnumDuctingBoundaryKind = stEnumDuctingBoundaryKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumEastWestDirectionKind
class stEnumEastWestDirectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumEastWestDirectionKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1308, 2)
    _Documentation = ''
stEnumEastWestDirectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumEastWestDirectionKind, enum_prefix=None)
stEnumEastWestDirectionKind.East = stEnumEastWestDirectionKind._CF_enumeration.addEnumeration(unicode_value='East', tag='East')
stEnumEastWestDirectionKind.West = stEnumEastWestDirectionKind._CF_enumeration.addEnumeration(unicode_value='West', tag='West')
stEnumEastWestDirectionKind._InitializeFacetMap(stEnumEastWestDirectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumEastWestDirectionKind', stEnumEastWestDirectionKind)
_module_typeBindings.stEnumEastWestDirectionKind = stEnumEastWestDirectionKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumEnvironmentKind
class stEnumEnvironmentKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumEnvironmentKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1320, 2)
    _Documentation = ''
stEnumEnvironmentKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumEnvironmentKind, enum_prefix=None)
stEnumEnvironmentKind.Round = stEnumEnvironmentKind._CF_enumeration.addEnumeration(unicode_value='Round', tag='Round')
stEnumEnvironmentKind.Flat = stEnumEnvironmentKind._CF_enumeration.addEnumeration(unicode_value='Flat', tag='Flat')
stEnumEnvironmentKind._InitializeFacetMap(stEnumEnvironmentKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumEnvironmentKind', stEnumEnvironmentKind)
_module_typeBindings.stEnumEnvironmentKind = stEnumEnvironmentKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumExternalGatingStateKind
class stEnumExternalGatingStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumExternalGatingStateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1332, 2)
    _Documentation = ''
stEnumExternalGatingStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumExternalGatingStateKind, enum_prefix=None)
stEnumExternalGatingStateKind.Ignore = stEnumExternalGatingStateKind._CF_enumeration.addEnumeration(unicode_value='Ignore', tag='Ignore')
stEnumExternalGatingStateKind.Store_Only_Gated_Pulses = stEnumExternalGatingStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Gated_Pulses', tag='Store_Only_Gated_Pulses')
stEnumExternalGatingStateKind._InitializeFacetMap(stEnumExternalGatingStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumExternalGatingStateKind', stEnumExternalGatingStateKind)
_module_typeBindings.stEnumExternalGatingStateKind = stEnumExternalGatingStateKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumGuiDisplayModeKind
class stEnumGuiDisplayModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumGuiDisplayModeKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1344, 2)
    _Documentation = ''
stEnumGuiDisplayModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumGuiDisplayModeKind, enum_prefix=None)
stEnumGuiDisplayModeKind.Plan_View = stEnumGuiDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Plan_View', tag='Plan_View')
stEnumGuiDisplayModeKind.Threed_View = stEnumGuiDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Threed_View', tag='Threed_View')
stEnumGuiDisplayModeKind.Polar_View = stEnumGuiDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Polar_View', tag='Polar_View')
stEnumGuiDisplayModeKind._InitializeFacetMap(stEnumGuiDisplayModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumGuiDisplayModeKind', stEnumGuiDisplayModeKind)
_module_typeBindings.stEnumGuiDisplayModeKind = stEnumGuiDisplayModeKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNavIf1553BusKind
class stEnumNavIf1553BusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNavIf1553BusKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1357, 2)
    _Documentation = ''
stEnumNavIf1553BusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNavIf1553BusKind, enum_prefix=None)
stEnumNavIf1553BusKind.Bus_A = stEnumNavIf1553BusKind._CF_enumeration.addEnumeration(unicode_value='Bus_A', tag='Bus_A')
stEnumNavIf1553BusKind.Bus_B = stEnumNavIf1553BusKind._CF_enumeration.addEnumeration(unicode_value='Bus_B', tag='Bus_B')
stEnumNavIf1553BusKind._InitializeFacetMap(stEnumNavIf1553BusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNavIf1553BusKind', stEnumNavIf1553BusKind)
_module_typeBindings.stEnumNavIf1553BusKind = stEnumNavIf1553BusKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNavIfPhysicalIfKind
class stEnumNavIfPhysicalIfKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNavIfPhysicalIfKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1369, 2)
    _Documentation = ''
stEnumNavIfPhysicalIfKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNavIfPhysicalIfKind, enum_prefix=None)
stEnumNavIfPhysicalIfKind.Nav_1553b = stEnumNavIfPhysicalIfKind._CF_enumeration.addEnumeration(unicode_value='Nav_1553b', tag='Nav_1553b')
stEnumNavIfPhysicalIfKind.Nav_Ethernet = stEnumNavIfPhysicalIfKind._CF_enumeration.addEnumeration(unicode_value='Nav_Ethernet', tag='Nav_Ethernet')
stEnumNavIfPhysicalIfKind.Nav_Rm = stEnumNavIfPhysicalIfKind._CF_enumeration.addEnumeration(unicode_value='Nav_Rm', tag='Nav_Rm')
stEnumNavIfPhysicalIfKind._InitializeFacetMap(stEnumNavIfPhysicalIfKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNavIfPhysicalIfKind', stEnumNavIfPhysicalIfKind)
_module_typeBindings.stEnumNavIfPhysicalIfKind = stEnumNavIfPhysicalIfKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNavIfTransferDirection
class stEnumNavIfTransferDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNavIfTransferDirection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1382, 2)
    _Documentation = ''
stEnumNavIfTransferDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNavIfTransferDirection, enum_prefix=None)
stEnumNavIfTransferDirection.Receive = stEnumNavIfTransferDirection._CF_enumeration.addEnumeration(unicode_value='Receive', tag='Receive')
stEnumNavIfTransferDirection.Transmit = stEnumNavIfTransferDirection._CF_enumeration.addEnumeration(unicode_value='Transmit', tag='Transmit')
stEnumNavIfTransferDirection._InitializeFacetMap(stEnumNavIfTransferDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNavIfTransferDirection', stEnumNavIfTransferDirection)
_module_typeBindings.stEnumNavIfTransferDirection = stEnumNavIfTransferDirection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNavIfUpdateInterval
class stEnumNavIfUpdateInterval (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNavIfUpdateInterval')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1394, 2)
    _Documentation = ''
stEnumNavIfUpdateInterval._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNavIfUpdateInterval, enum_prefix=None)
stEnumNavIfUpdateInterval.Nav_Interval_1_Ms = stEnumNavIfUpdateInterval._CF_enumeration.addEnumeration(unicode_value='Nav_Interval_1_Ms', tag='Nav_Interval_1_Ms')
stEnumNavIfUpdateInterval.Nav_Interval_2_Ms = stEnumNavIfUpdateInterval._CF_enumeration.addEnumeration(unicode_value='Nav_Interval_2_Ms', tag='Nav_Interval_2_Ms')
stEnumNavIfUpdateInterval.Nav_Interval_5_Ms = stEnumNavIfUpdateInterval._CF_enumeration.addEnumeration(unicode_value='Nav_Interval_5_Ms', tag='Nav_Interval_5_Ms')
stEnumNavIfUpdateInterval.Nav_Interval_10_Ms = stEnumNavIfUpdateInterval._CF_enumeration.addEnumeration(unicode_value='Nav_Interval_10_Ms', tag='Nav_Interval_10_Ms')
stEnumNavIfUpdateInterval.Nav_Interval_20_Ms = stEnumNavIfUpdateInterval._CF_enumeration.addEnumeration(unicode_value='Nav_Interval_20_Ms', tag='Nav_Interval_20_Ms')
stEnumNavIfUpdateInterval.Nav_Interval_30_Ms = stEnumNavIfUpdateInterval._CF_enumeration.addEnumeration(unicode_value='Nav_Interval_30_Ms', tag='Nav_Interval_30_Ms')
stEnumNavIfUpdateInterval.Nav_Interval_40_Ms = stEnumNavIfUpdateInterval._CF_enumeration.addEnumeration(unicode_value='Nav_Interval_40_Ms', tag='Nav_Interval_40_Ms')
stEnumNavIfUpdateInterval.Nav_Interval_50_Ms = stEnumNavIfUpdateInterval._CF_enumeration.addEnumeration(unicode_value='Nav_Interval_50_Ms', tag='Nav_Interval_50_Ms')
stEnumNavIfUpdateInterval._InitializeFacetMap(stEnumNavIfUpdateInterval._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNavIfUpdateInterval', stEnumNavIfUpdateInterval)
_module_typeBindings.stEnumNavIfUpdateInterval = stEnumNavIfUpdateInterval

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNorthSouthDirectionKind
class stEnumNorthSouthDirectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNorthSouthDirectionKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1412, 2)
    _Documentation = ''
stEnumNorthSouthDirectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNorthSouthDirectionKind, enum_prefix=None)
stEnumNorthSouthDirectionKind.North = stEnumNorthSouthDirectionKind._CF_enumeration.addEnumeration(unicode_value='North', tag='North')
stEnumNorthSouthDirectionKind.South = stEnumNorthSouthDirectionKind._CF_enumeration.addEnumeration(unicode_value='South', tag='South')
stEnumNorthSouthDirectionKind._InitializeFacetMap(stEnumNorthSouthDirectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNorthSouthDirectionKind', stEnumNorthSouthDirectionKind)
_module_typeBindings.stEnumNorthSouthDirectionKind = stEnumNorthSouthDirectionKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPdwKind
class stEnumPdwKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPdwKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1424, 2)
    _Documentation = ''
stEnumPdwKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPdwKind, enum_prefix=None)
stEnumPdwKind.Gp = stEnumPdwKind._CF_enumeration.addEnumeration(unicode_value='Gp', tag='Gp')
stEnumPdwKind.Ntp = stEnumPdwKind._CF_enumeration.addEnumeration(unicode_value='Ntp', tag='Ntp')
stEnumPdwKind.Ntp_With_Rp = stEnumPdwKind._CF_enumeration.addEnumeration(unicode_value='Ntp_With_Rp', tag='Ntp_With_Rp')
stEnumPdwKind.Ntp_With_Spinner = stEnumPdwKind._CF_enumeration.addEnumeration(unicode_value='Ntp_With_Spinner', tag='Ntp_With_Spinner')
stEnumPdwKind.Ntp_With_Esa = stEnumPdwKind._CF_enumeration.addEnumeration(unicode_value='Ntp_With_Esa', tag='Ntp_With_Esa')
stEnumPdwKind.Prb = stEnumPdwKind._CF_enumeration.addEnumeration(unicode_value='Prb', tag='Prb')
stEnumPdwKind._InitializeFacetMap(stEnumPdwKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPdwKind', stEnumPdwKind)
_module_typeBindings.stEnumPdwKind = stEnumPdwKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPulseContendedStateKind
class stEnumPulseContendedStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPulseContendedStateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1440, 2)
    _Documentation = ''
stEnumPulseContendedStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPulseContendedStateKind, enum_prefix=None)
stEnumPulseContendedStateKind.Ignore = stEnumPulseContendedStateKind._CF_enumeration.addEnumeration(unicode_value='Ignore', tag='Ignore')
stEnumPulseContendedStateKind.Store_Only_Pulses_Contended = stEnumPulseContendedStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Pulses_Contended', tag='Store_Only_Pulses_Contended')
stEnumPulseContendedStateKind.Store_Only_Pulses_Not_Contended = stEnumPulseContendedStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Pulses_Not_Contended', tag='Store_Only_Pulses_Not_Contended')
stEnumPulseContendedStateKind._InitializeFacetMap(stEnumPulseContendedStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPulseContendedStateKind', stEnumPulseContendedStateKind)
_module_typeBindings.stEnumPulseContendedStateKind = stEnumPulseContendedStateKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPulseInhibitStateKind
class stEnumPulseInhibitStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPulseInhibitStateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1453, 2)
    _Documentation = ''
stEnumPulseInhibitStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPulseInhibitStateKind, enum_prefix=None)
stEnumPulseInhibitStateKind.Ignore = stEnumPulseInhibitStateKind._CF_enumeration.addEnumeration(unicode_value='Ignore', tag='Ignore')
stEnumPulseInhibitStateKind.Store_Only_Pulses_Inhibited = stEnumPulseInhibitStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Pulses_Inhibited', tag='Store_Only_Pulses_Inhibited')
stEnumPulseInhibitStateKind.Store_Only_Pulses_Not_Inhibited = stEnumPulseInhibitStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Pulses_Not_Inhibited', tag='Store_Only_Pulses_Not_Inhibited')
stEnumPulseInhibitStateKind._InitializeFacetMap(stEnumPulseInhibitStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPulseInhibitStateKind', stEnumPulseInhibitStateKind)
_module_typeBindings.stEnumPulseInhibitStateKind = stEnumPulseInhibitStateKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumRainfallRateKind
class stEnumRainfallRateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumRainfallRateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1466, 2)
    _Documentation = ''
stEnumRainfallRateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumRainfallRateKind, enum_prefix=None)
stEnumRainfallRateKind.No_Rain = stEnumRainfallRateKind._CF_enumeration.addEnumeration(unicode_value='No_Rain', tag='No_Rain')
stEnumRainfallRateKind.Drizzle = stEnumRainfallRateKind._CF_enumeration.addEnumeration(unicode_value='Drizzle', tag='Drizzle')
stEnumRainfallRateKind.Light_Rain = stEnumRainfallRateKind._CF_enumeration.addEnumeration(unicode_value='Light_Rain', tag='Light_Rain')
stEnumRainfallRateKind.Medium_Rain = stEnumRainfallRateKind._CF_enumeration.addEnumeration(unicode_value='Medium_Rain', tag='Medium_Rain')
stEnumRainfallRateKind.Heavy_Rain = stEnumRainfallRateKind._CF_enumeration.addEnumeration(unicode_value='Heavy_Rain', tag='Heavy_Rain')
stEnumRainfallRateKind.Tropical_Downpour = stEnumRainfallRateKind._CF_enumeration.addEnumeration(unicode_value='Tropical_Downpour', tag='Tropical_Downpour')
stEnumRainfallRateKind._InitializeFacetMap(stEnumRainfallRateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumRainfallRateKind', stEnumRainfallRateKind)
_module_typeBindings.stEnumRainfallRateKind = stEnumRainfallRateKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSituationDisplayCenterKind
class stEnumSituationDisplayCenterKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSituationDisplayCenterKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1482, 2)
    _Documentation = ''
stEnumSituationDisplayCenterKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumSituationDisplayCenterKind, enum_prefix=None)
stEnumSituationDisplayCenterKind.On_Sut = stEnumSituationDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='On_Sut', tag='On_Sut')
stEnumSituationDisplayCenterKind.At_Point = stEnumSituationDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='At_Point', tag='At_Point')
stEnumSituationDisplayCenterKind._InitializeFacetMap(stEnumSituationDisplayCenterKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumSituationDisplayCenterKind', stEnumSituationDisplayCenterKind)
_module_typeBindings.stEnumSituationDisplayCenterKind = stEnumSituationDisplayCenterKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSituationDisplayModeKind
class stEnumSituationDisplayModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSituationDisplayModeKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1494, 2)
    _Documentation = ''
stEnumSituationDisplayModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumSituationDisplayModeKind, enum_prefix=None)
stEnumSituationDisplayModeKind.Rectangular = stEnumSituationDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Rectangular', tag='Rectangular')
stEnumSituationDisplayModeKind.Polar = stEnumSituationDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Polar', tag='Polar')
stEnumSituationDisplayModeKind._InitializeFacetMap(stEnumSituationDisplayModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumSituationDisplayModeKind', stEnumSituationDisplayModeKind)
_module_typeBindings.stEnumSituationDisplayModeKind = stEnumSituationDisplayModeKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSurfaceKind
class stEnumSurfaceKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSurfaceKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1506, 2)
    _Documentation = ''
stEnumSurfaceKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumSurfaceKind, enum_prefix=None)
stEnumSurfaceKind.Calm_Sea = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Calm_Sea', tag='Calm_Sea')
stEnumSurfaceKind.Smooth_Sea = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Smooth_Sea', tag='Smooth_Sea')
stEnumSurfaceKind.Slight_Sea = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Slight_Sea', tag='Slight_Sea')
stEnumSurfaceKind.Moderate_Sea = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Moderate_Sea', tag='Moderate_Sea')
stEnumSurfaceKind.Rough_Sea = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Rough_Sea', tag='Rough_Sea')
stEnumSurfaceKind.Very_Rough_Sea = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Very_Rough_Sea', tag='Very_Rough_Sea')
stEnumSurfaceKind.High_Sea = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='High_Sea', tag='High_Sea')
stEnumSurfaceKind.Very_High_Sea = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Very_High_Sea', tag='Very_High_Sea')
stEnumSurfaceKind.Smooth_Land = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Smooth_Land', tag='Smooth_Land')
stEnumSurfaceKind.Rough_Land = stEnumSurfaceKind._CF_enumeration.addEnumeration(unicode_value='Rough_Land', tag='Rough_Land')
stEnumSurfaceKind._InitializeFacetMap(stEnumSurfaceKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumSurfaceKind', stEnumSurfaceKind)
_module_typeBindings.stEnumSurfaceKind = stEnumSurfaceKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumTerrainDtedKind
class stEnumTerrainDtedKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumTerrainDtedKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1526, 2)
    _Documentation = ''
stEnumTerrainDtedKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumTerrainDtedKind, enum_prefix=None)
stEnumTerrainDtedKind.Level_0 = stEnumTerrainDtedKind._CF_enumeration.addEnumeration(unicode_value='Level_0', tag='Level_0')
stEnumTerrainDtedKind.Level_1 = stEnumTerrainDtedKind._CF_enumeration.addEnumeration(unicode_value='Level_1', tag='Level_1')
stEnumTerrainDtedKind.Ceesim_Elv = stEnumTerrainDtedKind._CF_enumeration.addEnumeration(unicode_value='Ceesim_Elv', tag='Ceesim_Elv')
stEnumTerrainDtedKind._InitializeFacetMap(stEnumTerrainDtedKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumTerrainDtedKind', stEnumTerrainDtedKind)
_module_typeBindings.stEnumTerrainDtedKind = stEnumTerrainDtedKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntDisplayId
class stIntDisplayId (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntDisplayId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1539, 2)
    _Documentation = ''
stIntDisplayId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stIntDisplayId', stIntDisplayId)
_module_typeBindings.stIntDisplayId = stIntDisplayId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntDisplayServer
class stIntDisplayServer (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntDisplayServer')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1548, 2)
    _Documentation = ''
stIntDisplayServer._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stIntDisplayServer', stIntDisplayServer)
_module_typeBindings.stIntDisplayServer = stIntDisplayServer

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntLowerEmitterNumber
class stIntLowerEmitterNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntLowerEmitterNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1557, 2)
    _Documentation = ''
stIntLowerEmitterNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntLowerEmitterNumber, value=pyxb.binding.datatypes.int(1))
stIntLowerEmitterNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntLowerEmitterNumber, value=pyxb.binding.datatypes.int(32767))
stIntLowerEmitterNumber._InitializeFacetMap(stIntLowerEmitterNumber._CF_minInclusive,
   stIntLowerEmitterNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntLowerEmitterNumber', stIntLowerEmitterNumber)
_module_typeBindings.stIntLowerEmitterNumber = stIntLowerEmitterNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntLowerGeneratorNumber
class stIntLowerGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntLowerGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1569, 2)
    _Documentation = ''
stIntLowerGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntLowerGeneratorNumber, value=pyxb.binding.datatypes.int(0))
stIntLowerGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntLowerGeneratorNumber, value=pyxb.binding.datatypes.int(2047))
stIntLowerGeneratorNumber._InitializeFacetMap(stIntLowerGeneratorNumber._CF_minInclusive,
   stIntLowerGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntLowerGeneratorNumber', stIntLowerGeneratorNumber)
_module_typeBindings.stIntLowerGeneratorNumber = stIntLowerGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntNavIfRtAddress
class stIntNavIfRtAddress (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntNavIfRtAddress')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1581, 2)
    _Documentation = ''
stIntNavIfRtAddress._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntNavIfRtAddress, value=pyxb.binding.datatypes.int(0))
stIntNavIfRtAddress._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntNavIfRtAddress, value=pyxb.binding.datatypes.int(31))
stIntNavIfRtAddress._InitializeFacetMap(stIntNavIfRtAddress._CF_minInclusive,
   stIntNavIfRtAddress._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntNavIfRtAddress', stIntNavIfRtAddress)
_module_typeBindings.stIntNavIfRtAddress = stIntNavIfRtAddress

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntNavIfRtSubAddress
class stIntNavIfRtSubAddress (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntNavIfRtSubAddress')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1593, 2)
    _Documentation = ''
stIntNavIfRtSubAddress._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntNavIfRtSubAddress, value=pyxb.binding.datatypes.int(0))
stIntNavIfRtSubAddress._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntNavIfRtSubAddress, value=pyxb.binding.datatypes.int(31))
stIntNavIfRtSubAddress._InitializeFacetMap(stIntNavIfRtSubAddress._CF_minInclusive,
   stIntNavIfRtSubAddress._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntNavIfRtSubAddress', stIntNavIfRtSubAddress)
_module_typeBindings.stIntNavIfRtSubAddress = stIntNavIfRtSubAddress

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntScenarioRevision
class stIntScenarioRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntScenarioRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1605, 2)
    _Documentation = ''
stIntScenarioRevision._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stIntScenarioRevision', stIntScenarioRevision)
_module_typeBindings.stIntScenarioRevision = stIntScenarioRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSoftwareReleaseOfLastHeaderEdit
class stIntSoftwareReleaseOfLastHeaderEdit (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSoftwareReleaseOfLastHeaderEdit')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1614, 2)
    _Documentation = ''
stIntSoftwareReleaseOfLastHeaderEdit._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stIntSoftwareReleaseOfLastHeaderEdit', stIntSoftwareReleaseOfLastHeaderEdit)
_module_typeBindings.stIntSoftwareReleaseOfLastHeaderEdit = stIntSoftwareReleaseOfLastHeaderEdit

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSutPlatformNumber
class stIntSutPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSutPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1623, 2)
    _Documentation = ''
stIntSutPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntSutPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntSutPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntSutPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntSutPlatformNumber._InitializeFacetMap(stIntSutPlatformNumber._CF_minInclusive,
   stIntSutPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntSutPlatformNumber', stIntSutPlatformNumber)
_module_typeBindings.stIntSutPlatformNumber = stIntSutPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntUpperEmitterNumber
class stIntUpperEmitterNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntUpperEmitterNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1635, 2)
    _Documentation = ''
stIntUpperEmitterNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntUpperEmitterNumber, value=pyxb.binding.datatypes.int(1))
stIntUpperEmitterNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntUpperEmitterNumber, value=pyxb.binding.datatypes.int(32767))
stIntUpperEmitterNumber._InitializeFacetMap(stIntUpperEmitterNumber._CF_minInclusive,
   stIntUpperEmitterNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntUpperEmitterNumber', stIntUpperEmitterNumber)
_module_typeBindings.stIntUpperEmitterNumber = stIntUpperEmitterNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntUpperGeneratorNumber
class stIntUpperGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntUpperGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1647, 2)
    _Documentation = ''
stIntUpperGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntUpperGeneratorNumber, value=pyxb.binding.datatypes.int(0))
stIntUpperGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntUpperGeneratorNumber, value=pyxb.binding.datatypes.int(2047))
stIntUpperGeneratorNumber._InitializeFacetMap(stIntUpperGeneratorNumber._CF_minInclusive,
   stIntUpperGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntUpperGeneratorNumber', stIntUpperGeneratorNumber)
_module_typeBindings.stIntUpperGeneratorNumber = stIntUpperGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringCommentScenarioHeader
class stStringCommentScenarioHeader (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringCommentScenarioHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1659, 2)
    _Documentation = ''
stStringCommentScenarioHeader._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringCommentScenarioHeader._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringCommentScenarioHeader._InitializeFacetMap(stStringCommentScenarioHeader._CF_minLength,
   stStringCommentScenarioHeader._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringCommentScenarioHeader', stStringCommentScenarioHeader)
_module_typeBindings.stStringCommentScenarioHeader = stStringCommentScenarioHeader

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringDuctingFileName
class stStringDuctingFileName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringDuctingFileName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1671, 2)
    _Documentation = ''
stStringDuctingFileName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringDuctingFileName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
stStringDuctingFileName._InitializeFacetMap(stStringDuctingFileName._CF_minLength,
   stStringDuctingFileName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringDuctingFileName', stStringDuctingFileName)
_module_typeBindings.stStringDuctingFileName = stStringDuctingFileName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringDxFileName
class stStringDxFileName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringDxFileName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1683, 2)
    _Documentation = ''
stStringDxFileName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringDxFileName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
stStringDxFileName._InitializeFacetMap(stStringDxFileName._CF_minLength,
   stStringDxFileName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringDxFileName', stStringDxFileName)
_module_typeBindings.stStringDxFileName = stStringDxFileName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringEmitterLibraryName
class stStringEmitterLibraryName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringEmitterLibraryName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1695, 2)
    _Documentation = ''
stStringEmitterLibraryName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringEmitterLibraryName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
stStringEmitterLibraryName._InitializeFacetMap(stStringEmitterLibraryName._CF_minLength,
   stStringEmitterLibraryName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringEmitterLibraryName', stStringEmitterLibraryName)
_module_typeBindings.stStringEmitterLibraryName = stStringEmitterLibraryName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextGeotiffPath
class stTextGeotiffPath (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextGeotiffPath')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1707, 2)
    _Documentation = ''
stTextGeotiffPath._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextGeotiffPath', stTextGeotiffPath)
_module_typeBindings.stTextGeotiffPath = stTextGeotiffPath

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextScenarioElementLibraryName
class stTextScenarioElementLibraryName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextScenarioElementLibraryName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 1716, 2)
    _Documentation = ''
stTextScenarioElementLibraryName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextScenarioElementLibraryName', stTextScenarioElementLibraryName)
_module_typeBindings.stTextScenarioElementLibraryName = stTextScenarioElementLibraryName

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


# Complex type {http://www.amherst.com/CEESIM/XML}ctScenarioData with content type ELEMENT_ONLY
class ctScenarioData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctScenarioData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctScenarioData')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 41, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}ScenarioHeader uses Python identifier ScenarioHeader
    __ScenarioHeader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScenarioHeader'), 'ScenarioHeader', '__httpwww_amherst_comCEESIMXML_ctScenarioData_httpwww_amherst_comCEESIMXMLScenarioHeader', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 43, 6), )

    
    ScenarioHeader = property(__ScenarioHeader.value, __ScenarioHeader.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctScenarioData_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 45, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 45, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __ScenarioHeader.name() : __ScenarioHeader
    })
    _AttributeMap.update({
        __PerId.name() : __PerId
    })
_module_typeBindings.ctScenarioData = ctScenarioData
Namespace.addCategoryObject('typeBinding', 'ctScenarioData', ctScenarioData)


# Complex type {http://www.amherst.com/CEESIM/XML}ctScenarioHeader with content type ELEMENT_ONLY
class ctScenarioHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctScenarioHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctScenarioHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 48, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}CreationDate uses Python identifier CreationDate
    __CreationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreationDate'), 'CreationDate', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLCreationDate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 50, 6), )

    
    CreationDate = property(__CreationDate.value, __CreationDate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ModificationDate uses Python identifier ModificationDate
    __ModificationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ModificationDate'), 'ModificationDate', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLModificationDate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 51, 6), )

    
    ModificationDate = property(__ModificationDate.value, __ModificationDate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ScenarioRevision uses Python identifier ScenarioRevision
    __ScenarioRevision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScenarioRevision'), 'ScenarioRevision', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLScenarioRevision', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 52, 6), )

    
    ScenarioRevision = property(__ScenarioRevision.value, __ScenarioRevision.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SoftwareReleaseOfLastHeaderEdit uses Python identifier SoftwareReleaseOfLastHeaderEdit
    __SoftwareReleaseOfLastHeaderEdit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SoftwareReleaseOfLastHeaderEdit'), 'SoftwareReleaseOfLastHeaderEdit', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLSoftwareReleaseOfLastHeaderEdit', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 53, 6), )

    
    SoftwareReleaseOfLastHeaderEdit = property(__SoftwareReleaseOfLastHeaderEdit.value, __SoftwareReleaseOfLastHeaderEdit.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DistanceUnits uses Python identifier DistanceUnits
    __DistanceUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DistanceUnits'), 'DistanceUnits', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLDistanceUnits', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 54, 6), )

    
    DistanceUnits = property(__DistanceUnits.value, __DistanceUnits.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EnvironmentKind uses Python identifier EnvironmentKind
    __EnvironmentKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EnvironmentKind'), 'EnvironmentKind', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLEnvironmentKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 55, 6), )

    
    EnvironmentKind = property(__EnvironmentKind.value, __EnvironmentKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLComment', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 56, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SutPlatformNumbers uses Python identifier SutPlatformNumbers
    __SutPlatformNumbers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SutPlatformNumbers'), 'SutPlatformNumbers', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLSutPlatformNumbers', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 57, 6), )

    
    SutPlatformNumbers = property(__SutPlatformNumbers.value, __SutPlatformNumbers.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ExternalSutFlag uses Python identifier ExternalSutFlag
    __ExternalSutFlag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalSutFlag'), 'ExternalSutFlag', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLExternalSutFlag', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 58, 6), )

    
    ExternalSutFlag = property(__ExternalSutFlag.value, __ExternalSutFlag.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}HorizonMaskingEnable uses Python identifier HorizonMaskingEnable
    __HorizonMaskingEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HorizonMaskingEnable'), 'HorizonMaskingEnable', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLHorizonMaskingEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 59, 6), )

    
    HorizonMaskingEnable = property(__HorizonMaskingEnable.value, __HorizonMaskingEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EarthRadiusFactor uses Python identifier EarthRadiusFactor
    __EarthRadiusFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EarthRadiusFactor'), 'EarthRadiusFactor', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLEarthRadiusFactor', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 60, 6), )

    
    EarthRadiusFactor = property(__EarthRadiusFactor.value, __EarthRadiusFactor.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DataRecording uses Python identifier DataRecording
    __DataRecording = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataRecording'), 'DataRecording', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLDataRecording', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 61, 6), )

    
    DataRecording = property(__DataRecording.value, __DataRecording.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterLibraryEnable uses Python identifier EmitterLibraryEnable
    __EmitterLibraryEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterLibraryEnable'), 'EmitterLibraryEnable', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLEmitterLibraryEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 62, 6), )

    
    EmitterLibraryEnable = property(__EmitterLibraryEnable.value, __EmitterLibraryEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterLibraryName uses Python identifier EmitterLibraryName
    __EmitterLibraryName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterLibraryName'), 'EmitterLibraryName', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLEmitterLibraryName', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 63, 6), )

    
    EmitterLibraryName = property(__EmitterLibraryName.value, __EmitterLibraryName.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ScenarioElementLibraryEnable uses Python identifier ScenarioElementLibraryEnable
    __ScenarioElementLibraryEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScenarioElementLibraryEnable'), 'ScenarioElementLibraryEnable', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLScenarioElementLibraryEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 64, 6), )

    
    ScenarioElementLibraryEnable = property(__ScenarioElementLibraryEnable.value, __ScenarioElementLibraryEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ScenarioElementLibraryName uses Python identifier ScenarioElementLibraryName
    __ScenarioElementLibraryName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScenarioElementLibraryName'), 'ScenarioElementLibraryName', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLScenarioElementLibraryName', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 65, 6), )

    
    ScenarioElementLibraryName = property(__ScenarioElementLibraryName.value, __ScenarioElementLibraryName.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Terrain uses Python identifier Terrain
    __Terrain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Terrain'), 'Terrain', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLTerrain', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 66, 6), )

    
    Terrain = property(__Terrain.value, __Terrain.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SurfaceEffects uses Python identifier SurfaceEffects
    __SurfaceEffects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SurfaceEffects'), 'SurfaceEffects', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLSurfaceEffects', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 67, 6), )

    
    SurfaceEffects = property(__SurfaceEffects.value, __SurfaceEffects.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PropagationEffects uses Python identifier PropagationEffects
    __PropagationEffects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PropagationEffects'), 'PropagationEffects', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLPropagationEffects', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 68, 6), )

    
    PropagationEffects = property(__PropagationEffects.value, __PropagationEffects.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SpacialAndDopplerEffects uses Python identifier SpacialAndDopplerEffects
    __SpacialAndDopplerEffects = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SpacialAndDopplerEffects'), 'SpacialAndDopplerEffects', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLSpacialAndDopplerEffects', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 69, 6), )

    
    SpacialAndDopplerEffects = property(__SpacialAndDopplerEffects.value, __SpacialAndDopplerEffects.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}HardwareResourceOptimizations uses Python identifier HardwareResourceOptimizations
    __HardwareResourceOptimizations = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'HardwareResourceOptimizations'), 'HardwareResourceOptimizations', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLHardwareResourceOptimizations', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 70, 6), )

    
    HardwareResourceOptimizations = property(__HardwareResourceOptimizations.value, __HardwareResourceOptimizations.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Dpms uses Python identifier Dpms
    __Dpms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dpms'), 'Dpms', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLDpms', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 71, 6), )

    
    Dpms = property(__Dpms.value, __Dpms.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NavigationInterfaceSettings uses Python identifier NavigationInterfaceSettings
    __NavigationInterfaceSettings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavigationInterfaceSettings'), 'NavigationInterfaceSettings', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLNavigationInterfaceSettings', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 72, 6), )

    
    NavigationInterfaceSettings = property(__NavigationInterfaceSettings.value, __NavigationInterfaceSettings.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SituationDisplayData uses Python identifier SituationDisplayData
    __SituationDisplayData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayData'), 'SituationDisplayData', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLSituationDisplayData', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 73, 6), )

    
    SituationDisplayData = property(__SituationDisplayData.value, __SituationDisplayData.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GuiDisplaySettings uses Python identifier GuiDisplaySettings
    __GuiDisplaySettings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplaySettings'), 'GuiDisplaySettings', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_httpwww_amherst_comCEESIMXMLGuiDisplaySettings', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 74, 6), )

    
    GuiDisplaySettings = property(__GuiDisplaySettings.value, __GuiDisplaySettings.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctScenarioHeader_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 76, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 76, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __CreationDate.name() : __CreationDate,
        __ModificationDate.name() : __ModificationDate,
        __ScenarioRevision.name() : __ScenarioRevision,
        __SoftwareReleaseOfLastHeaderEdit.name() : __SoftwareReleaseOfLastHeaderEdit,
        __DistanceUnits.name() : __DistanceUnits,
        __EnvironmentKind.name() : __EnvironmentKind,
        __Comment.name() : __Comment,
        __SutPlatformNumbers.name() : __SutPlatformNumbers,
        __ExternalSutFlag.name() : __ExternalSutFlag,
        __HorizonMaskingEnable.name() : __HorizonMaskingEnable,
        __EarthRadiusFactor.name() : __EarthRadiusFactor,
        __DataRecording.name() : __DataRecording,
        __EmitterLibraryEnable.name() : __EmitterLibraryEnable,
        __EmitterLibraryName.name() : __EmitterLibraryName,
        __ScenarioElementLibraryEnable.name() : __ScenarioElementLibraryEnable,
        __ScenarioElementLibraryName.name() : __ScenarioElementLibraryName,
        __Terrain.name() : __Terrain,
        __SurfaceEffects.name() : __SurfaceEffects,
        __PropagationEffects.name() : __PropagationEffects,
        __SpacialAndDopplerEffects.name() : __SpacialAndDopplerEffects,
        __HardwareResourceOptimizations.name() : __HardwareResourceOptimizations,
        __Dpms.name() : __Dpms,
        __NavigationInterfaceSettings.name() : __NavigationInterfaceSettings,
        __SituationDisplayData.name() : __SituationDisplayData,
        __GuiDisplaySettings.name() : __GuiDisplaySettings
    })
    _AttributeMap.update({
        __PerId.name() : __PerId
    })
_module_typeBindings.ctScenarioHeader = ctScenarioHeader
Namespace.addCategoryObject('typeBinding', 'ctScenarioHeader', ctScenarioHeader)


# Complex type {http://www.amherst.com/CEESIM/XML}ctSutPlatformNumberList with content type ELEMENT_ONLY
class ctSutPlatformNumberList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctSutPlatformNumberList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctSutPlatformNumberList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 79, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}SutPlatformNumber uses Python identifier SutPlatformNumber
    __SutPlatformNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SutPlatformNumber'), 'SutPlatformNumber', '__httpwww_amherst_comCEESIMXML_ctSutPlatformNumberList_httpwww_amherst_comCEESIMXMLSutPlatformNumber', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 81, 6), )

    
    SutPlatformNumber = property(__SutPlatformNumber.value, __SutPlatformNumber.set, None, None)

    _ElementMap.update({
        __SutPlatformNumber.name() : __SutPlatformNumber
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctSutPlatformNumberList = ctSutPlatformNumberList
Namespace.addCategoryObject('typeBinding', 'ctSutPlatformNumberList', ctSutPlatformNumberList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDataRecording with content type ELEMENT_ONLY
class ctDataRecording (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDataRecording with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDataRecording')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 85, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}DataRecordingEnable uses Python identifier DataRecordingEnable
    __DataRecordingEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DataRecordingEnable'), 'DataRecordingEnable', '__httpwww_amherst_comCEESIMXML_ctDataRecording_httpwww_amherst_comCEESIMXMLDataRecordingEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 87, 6), )

    
    DataRecordingEnable = property(__DataRecordingEnable.value, __DataRecordingEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DxFileName uses Python identifier DxFileName
    __DxFileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DxFileName'), 'DxFileName', '__httpwww_amherst_comCEESIMXML_ctDataRecording_httpwww_amherst_comCEESIMXMLDxFileName', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 88, 6), )

    
    DxFileName = property(__DxFileName.value, __DxFileName.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RecordPlatformEventsEnable uses Python identifier RecordPlatformEventsEnable
    __RecordPlatformEventsEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordPlatformEventsEnable'), 'RecordPlatformEventsEnable', '__httpwww_amherst_comCEESIMXML_ctDataRecording_httpwww_amherst_comCEESIMXMLRecordPlatformEventsEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 89, 6), )

    
    RecordPlatformEventsEnable = property(__RecordPlatformEventsEnable.value, __RecordPlatformEventsEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RecordEmitterEventsEnable uses Python identifier RecordEmitterEventsEnable
    __RecordEmitterEventsEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordEmitterEventsEnable'), 'RecordEmitterEventsEnable', '__httpwww_amherst_comCEESIMXML_ctDataRecording_httpwww_amherst_comCEESIMXMLRecordEmitterEventsEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 90, 6), )

    
    RecordEmitterEventsEnable = property(__RecordEmitterEventsEnable.value, __RecordEmitterEventsEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RecordPulseCountsEnable uses Python identifier RecordPulseCountsEnable
    __RecordPulseCountsEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordPulseCountsEnable'), 'RecordPulseCountsEnable', '__httpwww_amherst_comCEESIMXML_ctDataRecording_httpwww_amherst_comCEESIMXMLRecordPulseCountsEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 91, 6), )

    
    RecordPulseCountsEnable = property(__RecordPulseCountsEnable.value, __RecordPulseCountsEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RecordPlatformStatusEnable uses Python identifier RecordPlatformStatusEnable
    __RecordPlatformStatusEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordPlatformStatusEnable'), 'RecordPlatformStatusEnable', '__httpwww_amherst_comCEESIMXML_ctDataRecording_httpwww_amherst_comCEESIMXMLRecordPlatformStatusEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 92, 6), )

    
    RecordPlatformStatusEnable = property(__RecordPlatformStatusEnable.value, __RecordPlatformStatusEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RecordEmitterStatusEnable uses Python identifier RecordEmitterStatusEnable
    __RecordEmitterStatusEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RecordEmitterStatusEnable'), 'RecordEmitterStatusEnable', '__httpwww_amherst_comCEESIMXML_ctDataRecording_httpwww_amherst_comCEESIMXMLRecordEmitterStatusEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 93, 6), )

    
    RecordEmitterStatusEnable = property(__RecordEmitterStatusEnable.value, __RecordEmitterStatusEnable.set, None, None)

    _ElementMap.update({
        __DataRecordingEnable.name() : __DataRecordingEnable,
        __DxFileName.name() : __DxFileName,
        __RecordPlatformEventsEnable.name() : __RecordPlatformEventsEnable,
        __RecordEmitterEventsEnable.name() : __RecordEmitterEventsEnable,
        __RecordPulseCountsEnable.name() : __RecordPulseCountsEnable,
        __RecordPlatformStatusEnable.name() : __RecordPlatformStatusEnable,
        __RecordEmitterStatusEnable.name() : __RecordEmitterStatusEnable
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDataRecording = ctDataRecording
Namespace.addCategoryObject('typeBinding', 'ctDataRecording', ctDataRecording)


# Complex type {http://www.amherst.com/CEESIM/XML}ctTerrain with content type ELEMENT_ONLY
class ctTerrain (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTerrain with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTerrain')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 97, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}TerrainEnable uses Python identifier TerrainEnable
    __TerrainEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TerrainEnable'), 'TerrainEnable', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLTerrainEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 99, 6), )

    
    TerrainEnable = property(__TerrainEnable.value, __TerrainEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TerrainMaskingAttenuationEnable uses Python identifier TerrainMaskingAttenuationEnable
    __TerrainMaskingAttenuationEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TerrainMaskingAttenuationEnable'), 'TerrainMaskingAttenuationEnable', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLTerrainMaskingAttenuationEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 100, 6), )

    
    TerrainMaskingAttenuationEnable = property(__TerrainMaskingAttenuationEnable.value, __TerrainMaskingAttenuationEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TerrainDtedKind uses Python identifier TerrainDtedKind
    __TerrainDtedKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TerrainDtedKind'), 'TerrainDtedKind', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLTerrainDtedKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 101, 6), )

    
    TerrainDtedKind = property(__TerrainDtedKind.value, __TerrainDtedKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NorthLatitude uses Python identifier NorthLatitude
    __NorthLatitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NorthLatitude'), 'NorthLatitude', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLNorthLatitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 102, 6), )

    
    NorthLatitude = property(__NorthLatitude.value, __NorthLatitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NorthDirection uses Python identifier NorthDirection
    __NorthDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NorthDirection'), 'NorthDirection', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLNorthDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 103, 6), )

    
    NorthDirection = property(__NorthDirection.value, __NorthDirection.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}WestLongitude uses Python identifier WestLongitude
    __WestLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WestLongitude'), 'WestLongitude', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLWestLongitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 104, 6), )

    
    WestLongitude = property(__WestLongitude.value, __WestLongitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}WestDirection uses Python identifier WestDirection
    __WestDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WestDirection'), 'WestDirection', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLWestDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 105, 6), )

    
    WestDirection = property(__WestDirection.value, __WestDirection.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SouthLatitude uses Python identifier SouthLatitude
    __SouthLatitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SouthLatitude'), 'SouthLatitude', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLSouthLatitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 106, 6), )

    
    SouthLatitude = property(__SouthLatitude.value, __SouthLatitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SouthDirection uses Python identifier SouthDirection
    __SouthDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SouthDirection'), 'SouthDirection', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLSouthDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 107, 6), )

    
    SouthDirection = property(__SouthDirection.value, __SouthDirection.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EastLongitude uses Python identifier EastLongitude
    __EastLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EastLongitude'), 'EastLongitude', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLEastLongitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 108, 6), )

    
    EastLongitude = property(__EastLongitude.value, __EastLongitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EastDirection uses Python identifier EastDirection
    __EastDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EastDirection'), 'EastDirection', '__httpwww_amherst_comCEESIMXML_ctTerrain_httpwww_amherst_comCEESIMXMLEastDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 109, 6), )

    
    EastDirection = property(__EastDirection.value, __EastDirection.set, None, None)

    _ElementMap.update({
        __TerrainEnable.name() : __TerrainEnable,
        __TerrainMaskingAttenuationEnable.name() : __TerrainMaskingAttenuationEnable,
        __TerrainDtedKind.name() : __TerrainDtedKind,
        __NorthLatitude.name() : __NorthLatitude,
        __NorthDirection.name() : __NorthDirection,
        __WestLongitude.name() : __WestLongitude,
        __WestDirection.name() : __WestDirection,
        __SouthLatitude.name() : __SouthLatitude,
        __SouthDirection.name() : __SouthDirection,
        __EastLongitude.name() : __EastLongitude,
        __EastDirection.name() : __EastDirection
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctTerrain = ctTerrain
Namespace.addCategoryObject('typeBinding', 'ctTerrain', ctTerrain)


# Complex type {http://www.amherst.com/CEESIM/XML}ctSurfaceEffects with content type ELEMENT_ONLY
class ctSurfaceEffects (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctSurfaceEffects with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctSurfaceEffects')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 113, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}MultipathEnable uses Python identifier MultipathEnable
    __MultipathEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MultipathEnable'), 'MultipathEnable', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLMultipathEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 115, 6), )

    
    MultipathEnable = property(__MultipathEnable.value, __MultipathEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}WaveSplashEnable uses Python identifier WaveSplashEnable
    __WaveSplashEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WaveSplashEnable'), 'WaveSplashEnable', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLWaveSplashEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 116, 6), )

    
    WaveSplashEnable = property(__WaveSplashEnable.value, __WaveSplashEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SutEmitterEarthReflectionEnable uses Python identifier SutEmitterEarthReflectionEnable
    __SutEmitterEarthReflectionEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SutEmitterEarthReflectionEnable'), 'SutEmitterEarthReflectionEnable', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLSutEmitterEarthReflectionEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 117, 6), )

    
    SutEmitterEarthReflectionEnable = property(__SutEmitterEarthReflectionEnable.value, __SutEmitterEarthReflectionEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SurfaceKind uses Python identifier SurfaceKind
    __SurfaceKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SurfaceKind'), 'SurfaceKind', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLSurfaceKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 118, 6), )

    
    SurfaceKind = property(__SurfaceKind.value, __SurfaceKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NorthLatitude uses Python identifier NorthLatitude
    __NorthLatitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NorthLatitude'), 'NorthLatitude', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLNorthLatitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 119, 6), )

    
    NorthLatitude = property(__NorthLatitude.value, __NorthLatitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NorthDirection uses Python identifier NorthDirection
    __NorthDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NorthDirection'), 'NorthDirection', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLNorthDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 120, 6), )

    
    NorthDirection = property(__NorthDirection.value, __NorthDirection.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}WestLongitude uses Python identifier WestLongitude
    __WestLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WestLongitude'), 'WestLongitude', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLWestLongitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 121, 6), )

    
    WestLongitude = property(__WestLongitude.value, __WestLongitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}WestDirection uses Python identifier WestDirection
    __WestDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'WestDirection'), 'WestDirection', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLWestDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 122, 6), )

    
    WestDirection = property(__WestDirection.value, __WestDirection.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SouthLatitude uses Python identifier SouthLatitude
    __SouthLatitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SouthLatitude'), 'SouthLatitude', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLSouthLatitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 123, 6), )

    
    SouthLatitude = property(__SouthLatitude.value, __SouthLatitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SouthDirection uses Python identifier SouthDirection
    __SouthDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SouthDirection'), 'SouthDirection', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLSouthDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 124, 6), )

    
    SouthDirection = property(__SouthDirection.value, __SouthDirection.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EastLongitude uses Python identifier EastLongitude
    __EastLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EastLongitude'), 'EastLongitude', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLEastLongitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 125, 6), )

    
    EastLongitude = property(__EastLongitude.value, __EastLongitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EastDirection uses Python identifier EastDirection
    __EastDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EastDirection'), 'EastDirection', '__httpwww_amherst_comCEESIMXML_ctSurfaceEffects_httpwww_amherst_comCEESIMXMLEastDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 126, 6), )

    
    EastDirection = property(__EastDirection.value, __EastDirection.set, None, None)

    _ElementMap.update({
        __MultipathEnable.name() : __MultipathEnable,
        __WaveSplashEnable.name() : __WaveSplashEnable,
        __SutEmitterEarthReflectionEnable.name() : __SutEmitterEarthReflectionEnable,
        __SurfaceKind.name() : __SurfaceKind,
        __NorthLatitude.name() : __NorthLatitude,
        __NorthDirection.name() : __NorthDirection,
        __WestLongitude.name() : __WestLongitude,
        __WestDirection.name() : __WestDirection,
        __SouthLatitude.name() : __SouthLatitude,
        __SouthDirection.name() : __SouthDirection,
        __EastLongitude.name() : __EastLongitude,
        __EastDirection.name() : __EastDirection
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctSurfaceEffects = ctSurfaceEffects
Namespace.addCategoryObject('typeBinding', 'ctSurfaceEffects', ctSurfaceEffects)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPropagationEffects with content type ELEMENT_ONLY
class ctPropagationEffects (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPropagationEffects with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPropagationEffects')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 130, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}AtmosphericAbsorptionAttenuationEnable uses Python identifier AtmosphericAbsorptionAttenuationEnable
    __AtmosphericAbsorptionAttenuationEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AtmosphericAbsorptionAttenuationEnable'), 'AtmosphericAbsorptionAttenuationEnable', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLAtmosphericAbsorptionAttenuationEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 132, 6), )

    
    AtmosphericAbsorptionAttenuationEnable = property(__AtmosphericAbsorptionAttenuationEnable.value, __AtmosphericAbsorptionAttenuationEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RainfallRateKind uses Python identifier RainfallRateKind
    __RainfallRateKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RainfallRateKind'), 'RainfallRateKind', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLRainfallRateKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 133, 6), )

    
    RainfallRateKind = property(__RainfallRateKind.value, __RainfallRateKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DuctingEnable uses Python identifier DuctingEnable
    __DuctingEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DuctingEnable'), 'DuctingEnable', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLDuctingEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 134, 6), )

    
    DuctingEnable = property(__DuctingEnable.value, __DuctingEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DuctingBoundaryKind uses Python identifier DuctingBoundaryKind
    __DuctingBoundaryKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DuctingBoundaryKind'), 'DuctingBoundaryKind', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLDuctingBoundaryKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 135, 6), )

    
    DuctingBoundaryKind = property(__DuctingBoundaryKind.value, __DuctingBoundaryKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DuctingHeight uses Python identifier DuctingHeight
    __DuctingHeight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DuctingHeight'), 'DuctingHeight', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLDuctingHeight', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 136, 6), )

    
    DuctingHeight = property(__DuctingHeight.value, __DuctingHeight.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DuctingRefractivity uses Python identifier DuctingRefractivity
    __DuctingRefractivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DuctingRefractivity'), 'DuctingRefractivity', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLDuctingRefractivity', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 137, 6), )

    
    DuctingRefractivity = property(__DuctingRefractivity.value, __DuctingRefractivity.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DuctingFileName uses Python identifier DuctingFileName
    __DuctingFileName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DuctingFileName'), 'DuctingFileName', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLDuctingFileName', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 138, 6), )

    
    DuctingFileName = property(__DuctingFileName.value, __DuctingFileName.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RangeAttenuationEnable uses Python identifier RangeAttenuationEnable
    __RangeAttenuationEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RangeAttenuationEnable'), 'RangeAttenuationEnable', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLRangeAttenuationEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 139, 6), )

    
    RangeAttenuationEnable = property(__RangeAttenuationEnable.value, __RangeAttenuationEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}FrequencyAttenuationEnable uses Python identifier FrequencyAttenuationEnable
    __FrequencyAttenuationEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrequencyAttenuationEnable'), 'FrequencyAttenuationEnable', '__httpwww_amherst_comCEESIMXML_ctPropagationEffects_httpwww_amherst_comCEESIMXMLFrequencyAttenuationEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 140, 6), )

    
    FrequencyAttenuationEnable = property(__FrequencyAttenuationEnable.value, __FrequencyAttenuationEnable.set, None, None)

    _ElementMap.update({
        __AtmosphericAbsorptionAttenuationEnable.name() : __AtmosphericAbsorptionAttenuationEnable,
        __RainfallRateKind.name() : __RainfallRateKind,
        __DuctingEnable.name() : __DuctingEnable,
        __DuctingBoundaryKind.name() : __DuctingBoundaryKind,
        __DuctingHeight.name() : __DuctingHeight,
        __DuctingRefractivity.name() : __DuctingRefractivity,
        __DuctingFileName.name() : __DuctingFileName,
        __RangeAttenuationEnable.name() : __RangeAttenuationEnable,
        __FrequencyAttenuationEnable.name() : __FrequencyAttenuationEnable
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPropagationEffects = ctPropagationEffects
Namespace.addCategoryObject('typeBinding', 'ctPropagationEffects', ctPropagationEffects)


# Complex type {http://www.amherst.com/CEESIM/XML}ctSpacialAndDopplerEffects with content type ELEMENT_ONLY
class ctSpacialAndDopplerEffects (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctSpacialAndDopplerEffects with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctSpacialAndDopplerEffects')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 144, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}FrequencyDopplerShiftEnable uses Python identifier FrequencyDopplerShiftEnable
    __FrequencyDopplerShiftEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FrequencyDopplerShiftEnable'), 'FrequencyDopplerShiftEnable', '__httpwww_amherst_comCEESIMXML_ctSpacialAndDopplerEffects_httpwww_amherst_comCEESIMXMLFrequencyDopplerShiftEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 146, 6), )

    
    FrequencyDopplerShiftEnable = property(__FrequencyDopplerShiftEnable.value, __FrequencyDopplerShiftEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RangeAndPriDopplerShiftEnable uses Python identifier RangeAndPriDopplerShiftEnable
    __RangeAndPriDopplerShiftEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RangeAndPriDopplerShiftEnable'), 'RangeAndPriDopplerShiftEnable', '__httpwww_amherst_comCEESIMXML_ctSpacialAndDopplerEffects_httpwww_amherst_comCEESIMXMLRangeAndPriDopplerShiftEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 147, 6), )

    
    RangeAndPriDopplerShiftEnable = property(__RangeAndPriDopplerShiftEnable.value, __RangeAndPriDopplerShiftEnable.set, None, None)

    _ElementMap.update({
        __FrequencyDopplerShiftEnable.name() : __FrequencyDopplerShiftEnable,
        __RangeAndPriDopplerShiftEnable.name() : __RangeAndPriDopplerShiftEnable
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctSpacialAndDopplerEffects = ctSpacialAndDopplerEffects
Namespace.addCategoryObject('typeBinding', 'ctSpacialAndDopplerEffects', ctSpacialAndDopplerEffects)


# Complex type {http://www.amherst.com/CEESIM/XML}ctHardwareResourceOptimizations with content type ELEMENT_ONLY
class ctHardwareResourceOptimizations (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctHardwareResourceOptimizations with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctHardwareResourceOptimizations')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 151, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}PulseTruncationEnable uses Python identifier PulseTruncationEnable
    __PulseTruncationEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PulseTruncationEnable'), 'PulseTruncationEnable', '__httpwww_amherst_comCEESIMXML_ctHardwareResourceOptimizations_httpwww_amherst_comCEESIMXMLPulseTruncationEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 153, 6), )

    
    PulseTruncationEnable = property(__PulseTruncationEnable.value, __PulseTruncationEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}CwInterruptEnable uses Python identifier CwInterruptEnable
    __CwInterruptEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CwInterruptEnable'), 'CwInterruptEnable', '__httpwww_amherst_comCEESIMXML_ctHardwareResourceOptimizations_httpwww_amherst_comCEESIMXMLCwInterruptEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 154, 6), )

    
    CwInterruptEnable = property(__CwInterruptEnable.value, __CwInterruptEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SensitivityThresholdEnable uses Python identifier SensitivityThresholdEnable
    __SensitivityThresholdEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SensitivityThresholdEnable'), 'SensitivityThresholdEnable', '__httpwww_amherst_comCEESIMXML_ctHardwareResourceOptimizations_httpwww_amherst_comCEESIMXMLSensitivityThresholdEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 155, 6), )

    
    SensitivityThresholdEnable = property(__SensitivityThresholdEnable.value, __SensitivityThresholdEnable.set, None, None)

    _ElementMap.update({
        __PulseTruncationEnable.name() : __PulseTruncationEnable,
        __CwInterruptEnable.name() : __CwInterruptEnable,
        __SensitivityThresholdEnable.name() : __SensitivityThresholdEnable
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctHardwareResourceOptimizations = ctHardwareResourceOptimizations
Namespace.addCategoryObject('typeBinding', 'ctHardwareResourceOptimizations', ctHardwareResourceOptimizations)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmDataList with content type ELEMENT_ONLY
class ctDpmDataList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmDataList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmDataList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 159, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Dpm uses Python identifier Dpm
    __Dpm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dpm'), 'Dpm', '__httpwww_amherst_comCEESIMXML_ctDpmDataList_httpwww_amherst_comCEESIMXMLDpm', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 161, 6), )

    
    Dpm = property(__Dpm.value, __Dpm.set, None, None)

    _ElementMap.update({
        __Dpm.name() : __Dpm
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmDataList = ctDpmDataList
Namespace.addCategoryObject('typeBinding', 'ctDpmDataList', ctDpmDataList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmData with content type ELEMENT_ONLY
class ctDpmData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmData')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 165, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}DpmBoardCollectionEnable uses Python identifier DpmBoardCollectionEnable
    __DpmBoardCollectionEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DpmBoardCollectionEnable'), 'DpmBoardCollectionEnable', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLDpmBoardCollectionEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 167, 6), )

    
    DpmBoardCollectionEnable = property(__DpmBoardCollectionEnable.value, __DpmBoardCollectionEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PulseContendedState uses Python identifier PulseContendedState
    __PulseContendedState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PulseContendedState'), 'PulseContendedState', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLPulseContendedState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 168, 6), )

    
    PulseContendedState = property(__PulseContendedState.value, __PulseContendedState.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PulseInhibitState uses Python identifier PulseInhibitState
    __PulseInhibitState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PulseInhibitState'), 'PulseInhibitState', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLPulseInhibitState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 169, 6), )

    
    PulseInhibitState = property(__PulseInhibitState.value, __PulseInhibitState.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}CircularBufferCollection uses Python identifier CircularBufferCollection
    __CircularBufferCollection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CircularBufferCollection'), 'CircularBufferCollection', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLCircularBufferCollection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 170, 6), )

    
    CircularBufferCollection = property(__CircularBufferCollection.value, __CircularBufferCollection.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ExternalGatingState uses Python identifier ExternalGatingState
    __ExternalGatingState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ExternalGatingState'), 'ExternalGatingState', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLExternalGatingState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 171, 6), )

    
    ExternalGatingState = property(__ExternalGatingState.value, __ExternalGatingState.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DgsVideoState uses Python identifier DgsVideoState
    __DgsVideoState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DgsVideoState'), 'DgsVideoState', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLDgsVideoState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 172, 6), )

    
    DgsVideoState = property(__DgsVideoState.value, __DgsVideoState.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PdwKind uses Python identifier PdwKind
    __PdwKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PdwKind'), 'PdwKind', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLPdwKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 173, 6), )

    
    PdwKind = property(__PdwKind.value, __PdwKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}InvalidPdwsFlag uses Python identifier InvalidPdwsFlag
    __InvalidPdwsFlag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InvalidPdwsFlag'), 'InvalidPdwsFlag', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLInvalidPdwsFlag', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 174, 6), )

    
    InvalidPdwsFlag = property(__InvalidPdwsFlag.value, __InvalidPdwsFlag.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DpmFilters uses Python identifier DpmFilters
    __DpmFilters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DpmFilters'), 'DpmFilters', '__httpwww_amherst_comCEESIMXML_ctDpmData_httpwww_amherst_comCEESIMXMLDpmFilters', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 175, 6), )

    
    DpmFilters = property(__DpmFilters.value, __DpmFilters.set, None, None)

    _ElementMap.update({
        __DpmBoardCollectionEnable.name() : __DpmBoardCollectionEnable,
        __PulseContendedState.name() : __PulseContendedState,
        __PulseInhibitState.name() : __PulseInhibitState,
        __CircularBufferCollection.name() : __CircularBufferCollection,
        __ExternalGatingState.name() : __ExternalGatingState,
        __DgsVideoState.name() : __DgsVideoState,
        __PdwKind.name() : __PdwKind,
        __InvalidPdwsFlag.name() : __InvalidPdwsFlag,
        __DpmFilters.name() : __DpmFilters
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmData = ctDpmData
Namespace.addCategoryObject('typeBinding', 'ctDpmData', ctDpmData)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilter with content type ELEMENT_ONLY
class ctDpmFilter (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilter with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilter')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 179, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}AzAoa uses Python identifier AzAoa
    __AzAoa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AzAoa'), 'AzAoa', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLAzAoa', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 181, 6), )

    
    AzAoa = property(__AzAoa.value, __AzAoa.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ElAoa uses Python identifier ElAoa
    __ElAoa = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ElAoa'), 'ElAoa', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLElAoa', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 182, 6), )

    
    ElAoa = property(__ElAoa.value, __ElAoa.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterNumber uses Python identifier EmitterNumber
    __EmitterNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterNumber'), 'EmitterNumber', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLEmitterNumber', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 183, 6), )

    
    EmitterNumber = property(__EmitterNumber.value, __EmitterNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Frequency uses Python identifier Frequency
    __Frequency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Frequency'), 'Frequency', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLFrequency', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 184, 6), )

    
    Frequency = property(__Frequency.value, __Frequency.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Generator uses Python identifier Generator
    __Generator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Generator'), 'Generator', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLGenerator', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 185, 6), )

    
    Generator = property(__Generator.value, __Generator.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EmitterName uses Python identifier EmitterName
    __EmitterName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EmitterName'), 'EmitterName', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLEmitterName', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 186, 6), )

    
    EmitterName = property(__EmitterName.value, __EmitterName.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PulseWidth uses Python identifier PulseWidth
    __PulseWidth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PulseWidth'), 'PulseWidth', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLPulseWidth', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 187, 6), )

    
    PulseWidth = property(__PulseWidth.value, __PulseWidth.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Power uses Python identifier Power
    __Power = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Power'), 'Power', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLPower', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 188, 6), )

    
    Power = property(__Power.value, __Power.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ScenarioTime uses Python identifier ScenarioTime
    __ScenarioTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScenarioTime'), 'ScenarioTime', '__httpwww_amherst_comCEESIMXML_ctDpmFilter_httpwww_amherst_comCEESIMXMLScenarioTime', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 189, 6), )

    
    ScenarioTime = property(__ScenarioTime.value, __ScenarioTime.set, None, None)

    _ElementMap.update({
        __AzAoa.name() : __AzAoa,
        __ElAoa.name() : __ElAoa,
        __EmitterNumber.name() : __EmitterNumber,
        __Frequency.name() : __Frequency,
        __Generator.name() : __Generator,
        __EmitterName.name() : __EmitterName,
        __PulseWidth.name() : __PulseWidth,
        __Power.name() : __Power,
        __ScenarioTime.name() : __ScenarioTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilter = ctDpmFilter
Namespace.addCategoryObject('typeBinding', 'ctDpmFilter', ctDpmFilter)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterAzAoa with content type ELEMENT_ONLY
class ctDpmFilterAzAoa (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterAzAoa with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilterAzAoa')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 193, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}LowerAzimuth uses Python identifier LowerAzimuth
    __LowerAzimuth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerAzimuth'), 'LowerAzimuth', '__httpwww_amherst_comCEESIMXML_ctDpmFilterAzAoa_httpwww_amherst_comCEESIMXMLLowerAzimuth', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 195, 6), )

    
    LowerAzimuth = property(__LowerAzimuth.value, __LowerAzimuth.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpperAzimuth uses Python identifier UpperAzimuth
    __UpperAzimuth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperAzimuth'), 'UpperAzimuth', '__httpwww_amherst_comCEESIMXML_ctDpmFilterAzAoa_httpwww_amherst_comCEESIMXMLUpperAzimuth', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 196, 6), )

    
    UpperAzimuth = property(__UpperAzimuth.value, __UpperAzimuth.set, None, None)

    _ElementMap.update({
        __LowerAzimuth.name() : __LowerAzimuth,
        __UpperAzimuth.name() : __UpperAzimuth
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilterAzAoa = ctDpmFilterAzAoa
Namespace.addCategoryObject('typeBinding', 'ctDpmFilterAzAoa', ctDpmFilterAzAoa)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterElAoa with content type ELEMENT_ONLY
class ctDpmFilterElAoa (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterElAoa with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilterElAoa')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 200, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}LowerElevation uses Python identifier LowerElevation
    __LowerElevation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerElevation'), 'LowerElevation', '__httpwww_amherst_comCEESIMXML_ctDpmFilterElAoa_httpwww_amherst_comCEESIMXMLLowerElevation', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 202, 6), )

    
    LowerElevation = property(__LowerElevation.value, __LowerElevation.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpperElevation uses Python identifier UpperElevation
    __UpperElevation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperElevation'), 'UpperElevation', '__httpwww_amherst_comCEESIMXML_ctDpmFilterElAoa_httpwww_amherst_comCEESIMXMLUpperElevation', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 203, 6), )

    
    UpperElevation = property(__UpperElevation.value, __UpperElevation.set, None, None)

    _ElementMap.update({
        __LowerElevation.name() : __LowerElevation,
        __UpperElevation.name() : __UpperElevation
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilterElAoa = ctDpmFilterElAoa
Namespace.addCategoryObject('typeBinding', 'ctDpmFilterElAoa', ctDpmFilterElAoa)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterEmitterNumber with content type ELEMENT_ONLY
class ctDpmFilterEmitterNumber (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterEmitterNumber with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilterEmitterNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 207, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}LowerEmitter uses Python identifier LowerEmitter
    __LowerEmitter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerEmitter'), 'LowerEmitter', '__httpwww_amherst_comCEESIMXML_ctDpmFilterEmitterNumber_httpwww_amherst_comCEESIMXMLLowerEmitter', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 209, 6), )

    
    LowerEmitter = property(__LowerEmitter.value, __LowerEmitter.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpperEmitter uses Python identifier UpperEmitter
    __UpperEmitter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperEmitter'), 'UpperEmitter', '__httpwww_amherst_comCEESIMXML_ctDpmFilterEmitterNumber_httpwww_amherst_comCEESIMXMLUpperEmitter', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 210, 6), )

    
    UpperEmitter = property(__UpperEmitter.value, __UpperEmitter.set, None, None)

    _ElementMap.update({
        __LowerEmitter.name() : __LowerEmitter,
        __UpperEmitter.name() : __UpperEmitter
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilterEmitterNumber = ctDpmFilterEmitterNumber
Namespace.addCategoryObject('typeBinding', 'ctDpmFilterEmitterNumber', ctDpmFilterEmitterNumber)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterFrequency with content type ELEMENT_ONLY
class ctDpmFilterFrequency (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterFrequency with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilterFrequency')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 214, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}LowerFrequency uses Python identifier LowerFrequency
    __LowerFrequency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerFrequency'), 'LowerFrequency', '__httpwww_amherst_comCEESIMXML_ctDpmFilterFrequency_httpwww_amherst_comCEESIMXMLLowerFrequency', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 216, 6), )

    
    LowerFrequency = property(__LowerFrequency.value, __LowerFrequency.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpperFrequency uses Python identifier UpperFrequency
    __UpperFrequency = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperFrequency'), 'UpperFrequency', '__httpwww_amherst_comCEESIMXML_ctDpmFilterFrequency_httpwww_amherst_comCEESIMXMLUpperFrequency', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 217, 6), )

    
    UpperFrequency = property(__UpperFrequency.value, __UpperFrequency.set, None, None)

    _ElementMap.update({
        __LowerFrequency.name() : __LowerFrequency,
        __UpperFrequency.name() : __UpperFrequency
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilterFrequency = ctDpmFilterFrequency
Namespace.addCategoryObject('typeBinding', 'ctDpmFilterFrequency', ctDpmFilterFrequency)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterGenerator with content type ELEMENT_ONLY
class ctDpmFilterGenerator (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterGenerator with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilterGenerator')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 221, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}LowerGenerator uses Python identifier LowerGenerator
    __LowerGenerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerGenerator'), 'LowerGenerator', '__httpwww_amherst_comCEESIMXML_ctDpmFilterGenerator_httpwww_amherst_comCEESIMXMLLowerGenerator', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 223, 6), )

    
    LowerGenerator = property(__LowerGenerator.value, __LowerGenerator.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpperGenerator uses Python identifier UpperGenerator
    __UpperGenerator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperGenerator'), 'UpperGenerator', '__httpwww_amherst_comCEESIMXML_ctDpmFilterGenerator_httpwww_amherst_comCEESIMXMLUpperGenerator', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 224, 6), )

    
    UpperGenerator = property(__UpperGenerator.value, __UpperGenerator.set, None, None)

    _ElementMap.update({
        __LowerGenerator.name() : __LowerGenerator,
        __UpperGenerator.name() : __UpperGenerator
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilterGenerator = ctDpmFilterGenerator
Namespace.addCategoryObject('typeBinding', 'ctDpmFilterGenerator', ctDpmFilterGenerator)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterPulseWidth with content type ELEMENT_ONLY
class ctDpmFilterPulseWidth (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterPulseWidth with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilterPulseWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 228, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}LowerPulseWidth uses Python identifier LowerPulseWidth
    __LowerPulseWidth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerPulseWidth'), 'LowerPulseWidth', '__httpwww_amherst_comCEESIMXML_ctDpmFilterPulseWidth_httpwww_amherst_comCEESIMXMLLowerPulseWidth', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 230, 6), )

    
    LowerPulseWidth = property(__LowerPulseWidth.value, __LowerPulseWidth.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpperPulseWidth uses Python identifier UpperPulseWidth
    __UpperPulseWidth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperPulseWidth'), 'UpperPulseWidth', '__httpwww_amherst_comCEESIMXML_ctDpmFilterPulseWidth_httpwww_amherst_comCEESIMXMLUpperPulseWidth', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 231, 6), )

    
    UpperPulseWidth = property(__UpperPulseWidth.value, __UpperPulseWidth.set, None, None)

    _ElementMap.update({
        __LowerPulseWidth.name() : __LowerPulseWidth,
        __UpperPulseWidth.name() : __UpperPulseWidth
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilterPulseWidth = ctDpmFilterPulseWidth
Namespace.addCategoryObject('typeBinding', 'ctDpmFilterPulseWidth', ctDpmFilterPulseWidth)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterPower with content type ELEMENT_ONLY
class ctDpmFilterPower (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterPower with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilterPower')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 235, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}LowerPower uses Python identifier LowerPower
    __LowerPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerPower'), 'LowerPower', '__httpwww_amherst_comCEESIMXML_ctDpmFilterPower_httpwww_amherst_comCEESIMXMLLowerPower', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 237, 6), )

    
    LowerPower = property(__LowerPower.value, __LowerPower.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpperPower uses Python identifier UpperPower
    __UpperPower = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperPower'), 'UpperPower', '__httpwww_amherst_comCEESIMXML_ctDpmFilterPower_httpwww_amherst_comCEESIMXMLUpperPower', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 238, 6), )

    
    UpperPower = property(__UpperPower.value, __UpperPower.set, None, None)

    _ElementMap.update({
        __LowerPower.name() : __LowerPower,
        __UpperPower.name() : __UpperPower
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilterPower = ctDpmFilterPower
Namespace.addCategoryObject('typeBinding', 'ctDpmFilterPower', ctDpmFilterPower)


# Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterScenarioTime with content type ELEMENT_ONLY
class ctDpmFilterScenarioTime (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctDpmFilterScenarioTime with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctDpmFilterScenarioTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 242, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}LowerTime uses Python identifier LowerTime
    __LowerTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LowerTime'), 'LowerTime', '__httpwww_amherst_comCEESIMXML_ctDpmFilterScenarioTime_httpwww_amherst_comCEESIMXMLLowerTime', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 244, 6), )

    
    LowerTime = property(__LowerTime.value, __LowerTime.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpperTime uses Python identifier UpperTime
    __UpperTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpperTime'), 'UpperTime', '__httpwww_amherst_comCEESIMXML_ctDpmFilterScenarioTime_httpwww_amherst_comCEESIMXMLUpperTime', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 245, 6), )

    
    UpperTime = property(__UpperTime.value, __UpperTime.set, None, None)

    _ElementMap.update({
        __LowerTime.name() : __LowerTime,
        __UpperTime.name() : __UpperTime
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctDpmFilterScenarioTime = ctDpmFilterScenarioTime
Namespace.addCategoryObject('typeBinding', 'ctDpmFilterScenarioTime', ctDpmFilterScenarioTime)


# Complex type {http://www.amherst.com/CEESIM/XML}ctNavigationInterfaceSettings with content type ELEMENT_ONLY
class ctNavigationInterfaceSettings (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctNavigationInterfaceSettings with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctNavigationInterfaceSettings')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 249, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfEnable uses Python identifier NavIfEnable
    __NavIfEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfEnable'), 'NavIfEnable', '__httpwww_amherst_comCEESIMXML_ctNavigationInterfaceSettings_httpwww_amherst_comCEESIMXMLNavIfEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 251, 6), )

    
    NavIfEnable = property(__NavIfEnable.value, __NavIfEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfPhysicalIfKind uses Python identifier NavIfPhysicalIfKind
    __NavIfPhysicalIfKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfPhysicalIfKind'), 'NavIfPhysicalIfKind', '__httpwww_amherst_comCEESIMXML_ctNavigationInterfaceSettings_httpwww_amherst_comCEESIMXMLNavIfPhysicalIfKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 252, 6), )

    
    NavIfPhysicalIfKind = property(__NavIfPhysicalIfKind.value, __NavIfPhysicalIfKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NavIf1553BusKind uses Python identifier NavIf1553BusKind
    __NavIf1553BusKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIf1553BusKind'), 'NavIf1553BusKind', '__httpwww_amherst_comCEESIMXML_ctNavigationInterfaceSettings_httpwww_amherst_comCEESIMXMLNavIf1553BusKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 253, 6), )

    
    NavIf1553BusKind = property(__NavIf1553BusKind.value, __NavIf1553BusKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfUpdateInterval uses Python identifier NavIfUpdateInterval
    __NavIfUpdateInterval = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfUpdateInterval'), 'NavIfUpdateInterval', '__httpwww_amherst_comCEESIMXML_ctNavigationInterfaceSettings_httpwww_amherst_comCEESIMXMLNavIfUpdateInterval', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 254, 6), )

    
    NavIfUpdateInterval = property(__NavIfUpdateInterval.value, __NavIfUpdateInterval.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfPlatforms uses Python identifier NavIfPlatforms
    __NavIfPlatforms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfPlatforms'), 'NavIfPlatforms', '__httpwww_amherst_comCEESIMXML_ctNavigationInterfaceSettings_httpwww_amherst_comCEESIMXMLNavIfPlatforms', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 255, 6), )

    
    NavIfPlatforms = property(__NavIfPlatforms.value, __NavIfPlatforms.set, None, None)

    _ElementMap.update({
        __NavIfEnable.name() : __NavIfEnable,
        __NavIfPhysicalIfKind.name() : __NavIfPhysicalIfKind,
        __NavIf1553BusKind.name() : __NavIf1553BusKind,
        __NavIfUpdateInterval.name() : __NavIfUpdateInterval,
        __NavIfPlatforms.name() : __NavIfPlatforms
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctNavigationInterfaceSettings = ctNavigationInterfaceSettings
Namespace.addCategoryObject('typeBinding', 'ctNavigationInterfaceSettings', ctNavigationInterfaceSettings)


# Complex type {http://www.amherst.com/CEESIM/XML}ctNavIfPlatformsList with content type ELEMENT_ONLY
class ctNavIfPlatformsList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctNavIfPlatformsList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctNavIfPlatformsList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 259, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfPlatform uses Python identifier NavIfPlatform
    __NavIfPlatform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfPlatform'), 'NavIfPlatform', '__httpwww_amherst_comCEESIMXML_ctNavIfPlatformsList_httpwww_amherst_comCEESIMXMLNavIfPlatform', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 261, 6), )

    
    NavIfPlatform = property(__NavIfPlatform.value, __NavIfPlatform.set, None, None)

    _ElementMap.update({
        __NavIfPlatform.name() : __NavIfPlatform
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctNavIfPlatformsList = ctNavIfPlatformsList
Namespace.addCategoryObject('typeBinding', 'ctNavIfPlatformsList', ctNavIfPlatformsList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctNavIfPlatform with content type ELEMENT_ONLY
class ctNavIfPlatform (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctNavIfPlatform with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctNavIfPlatform')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 265, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfUserPlatformNumber uses Python identifier NavIfUserPlatformNumber
    __NavIfUserPlatformNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfUserPlatformNumber'), 'NavIfUserPlatformNumber', '__httpwww_amherst_comCEESIMXML_ctNavIfPlatform_httpwww_amherst_comCEESIMXMLNavIfUserPlatformNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 267, 6), )

    
    NavIfUserPlatformNumber = property(__NavIfUserPlatformNumber.value, __NavIfUserPlatformNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfRtAddress uses Python identifier NavIfRtAddress
    __NavIfRtAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfRtAddress'), 'NavIfRtAddress', '__httpwww_amherst_comCEESIMXML_ctNavIfPlatform_httpwww_amherst_comCEESIMXMLNavIfRtAddress', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 268, 6), )

    
    NavIfRtAddress = property(__NavIfRtAddress.value, __NavIfRtAddress.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfRtSubAddress uses Python identifier NavIfRtSubAddress
    __NavIfRtSubAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfRtSubAddress'), 'NavIfRtSubAddress', '__httpwww_amherst_comCEESIMXML_ctNavIfPlatform_httpwww_amherst_comCEESIMXMLNavIfRtSubAddress', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 269, 6), )

    
    NavIfRtSubAddress = property(__NavIfRtSubAddress.value, __NavIfRtSubAddress.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}NavIfTransferDirection uses Python identifier NavIfTransferDirection
    __NavIfTransferDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NavIfTransferDirection'), 'NavIfTransferDirection', '__httpwww_amherst_comCEESIMXML_ctNavIfPlatform_httpwww_amherst_comCEESIMXMLNavIfTransferDirection', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 270, 6), )

    
    NavIfTransferDirection = property(__NavIfTransferDirection.value, __NavIfTransferDirection.set, None, None)

    _ElementMap.update({
        __NavIfUserPlatformNumber.name() : __NavIfUserPlatformNumber,
        __NavIfRtAddress.name() : __NavIfRtAddress,
        __NavIfRtSubAddress.name() : __NavIfRtSubAddress,
        __NavIfTransferDirection.name() : __NavIfTransferDirection
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctNavIfPlatform = ctNavIfPlatform
Namespace.addCategoryObject('typeBinding', 'ctNavIfPlatform', ctNavIfPlatform)


# Complex type {http://www.amherst.com/CEESIM/XML}ctSituationDisplayDataList with content type ELEMENT_ONLY
class ctSituationDisplayDataList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctSituationDisplayDataList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctSituationDisplayDataList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 274, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}SituationDisplaySettings uses Python identifier SituationDisplaySettings
    __SituationDisplaySettings = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplaySettings'), 'SituationDisplaySettings', '__httpwww_amherst_comCEESIMXML_ctSituationDisplayDataList_httpwww_amherst_comCEESIMXMLSituationDisplaySettings', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 276, 6), )

    
    SituationDisplaySettings = property(__SituationDisplaySettings.value, __SituationDisplaySettings.set, None, None)

    _ElementMap.update({
        __SituationDisplaySettings.name() : __SituationDisplaySettings
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctSituationDisplayDataList = ctSituationDisplayDataList
Namespace.addCategoryObject('typeBinding', 'ctSituationDisplayDataList', ctSituationDisplayDataList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctSituationDisplaySettings with content type ELEMENT_ONLY
class ctSituationDisplaySettings (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctSituationDisplaySettings with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctSituationDisplaySettings')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 280, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayServer uses Python identifier DisplayServer
    __DisplayServer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayServer'), 'DisplayServer', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayServer', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 282, 6), )

    
    DisplayServer = property(__DisplayServer.value, __DisplayServer.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayId uses Python identifier DisplayId
    __DisplayId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayId'), 'DisplayId', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayId', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 283, 6), )

    
    DisplayId = property(__DisplayId.value, __DisplayId.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayVisibility uses Python identifier DisplayVisibility
    __DisplayVisibility = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayVisibility'), 'DisplayVisibility', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayVisibility', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 284, 6), )

    
    DisplayVisibility = property(__DisplayVisibility.value, __DisplayVisibility.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SituationDisplayCenter uses Python identifier SituationDisplayCenter
    __SituationDisplayCenter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayCenter'), 'SituationDisplayCenter', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLSituationDisplayCenter', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 285, 6), )

    
    SituationDisplayCenter = property(__SituationDisplayCenter.value, __SituationDisplayCenter.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Center uses Python identifier Center
    __Center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Center'), 'Center', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLCenter', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 286, 6), )

    
    Center = property(__Center.value, __Center.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SituationDisplayMode uses Python identifier SituationDisplayMode
    __SituationDisplayMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayMode'), 'SituationDisplayMode', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLSituationDisplayMode', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 287, 6), )

    
    SituationDisplayMode = property(__SituationDisplayMode.value, __SituationDisplayMode.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayScale uses Python identifier DisplayScale
    __DisplayScale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayScale'), 'DisplayScale', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayScale', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 288, 6), )

    
    DisplayScale = property(__DisplayScale.value, __DisplayScale.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayIntensity uses Python identifier DisplayIntensity
    __DisplayIntensity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayIntensity'), 'DisplayIntensity', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayIntensity', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 289, 6), )

    
    DisplayIntensity = property(__DisplayIntensity.value, __DisplayIntensity.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}VelocityVectorDuration uses Python identifier VelocityVectorDuration
    __VelocityVectorDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'VelocityVectorDuration'), 'VelocityVectorDuration', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLVelocityVectorDuration', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 290, 6), )

    
    VelocityVectorDuration = property(__VelocityVectorDuration.value, __VelocityVectorDuration.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayTerrain uses Python identifier DisplayTerrain
    __DisplayTerrain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayTerrain'), 'DisplayTerrain', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayTerrain', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 291, 6), )

    
    DisplayTerrain = property(__DisplayTerrain.value, __DisplayTerrain.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayRoughness uses Python identifier DisplayRoughness
    __DisplayRoughness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoughness'), 'DisplayRoughness', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayRoughness', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 292, 6), )

    
    DisplayRoughness = property(__DisplayRoughness.value, __DisplayRoughness.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayGeopolitical uses Python identifier DisplayGeopolitical
    __DisplayGeopolitical = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayGeopolitical'), 'DisplayGeopolitical', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayGeopolitical', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 293, 6), )

    
    DisplayGeopolitical = property(__DisplayGeopolitical.value, __DisplayGeopolitical.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeopoliticalCenterLatitude uses Python identifier GeopoliticalCenterLatitude
    __GeopoliticalCenterLatitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLatitude'), 'GeopoliticalCenterLatitude', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLGeopoliticalCenterLatitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 294, 6), )

    
    GeopoliticalCenterLatitude = property(__GeopoliticalCenterLatitude.value, __GeopoliticalCenterLatitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeopoliticalCenterLongitude uses Python identifier GeopoliticalCenterLongitude
    __GeopoliticalCenterLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLongitude'), 'GeopoliticalCenterLongitude', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLGeopoliticalCenterLongitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 295, 6), )

    
    GeopoliticalCenterLongitude = property(__GeopoliticalCenterLongitude.value, __GeopoliticalCenterLongitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayBarriers uses Python identifier DisplayBarriers
    __DisplayBarriers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayBarriers'), 'DisplayBarriers', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayBarriers', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 296, 6), )

    
    DisplayBarriers = property(__DisplayBarriers.value, __DisplayBarriers.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayCoastline uses Python identifier DisplayCoastline
    __DisplayCoastline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayCoastline'), 'DisplayCoastline', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayCoastline', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 297, 6), )

    
    DisplayCoastline = property(__DisplayCoastline.value, __DisplayCoastline.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayDepthLines uses Python identifier DisplayDepthLines
    __DisplayDepthLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayDepthLines'), 'DisplayDepthLines', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayDepthLines', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 298, 6), )

    
    DisplayDepthLines = property(__DisplayDepthLines.value, __DisplayDepthLines.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPoliticalLines uses Python identifier DisplayPoliticalLines
    __DisplayPoliticalLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPoliticalLines'), 'DisplayPoliticalLines', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayPoliticalLines', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 299, 6), )

    
    DisplayPoliticalLines = property(__DisplayPoliticalLines.value, __DisplayPoliticalLines.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayCanals uses Python identifier DisplayCanals
    __DisplayCanals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayCanals'), 'DisplayCanals', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayCanals', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 300, 6), )

    
    DisplayCanals = property(__DisplayCanals.value, __DisplayCanals.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayWaterways uses Python identifier DisplayWaterways
    __DisplayWaterways = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayWaterways'), 'DisplayWaterways', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayWaterways', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 301, 6), )

    
    DisplayWaterways = property(__DisplayWaterways.value, __DisplayWaterways.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayLandforms uses Python identifier DisplayLandforms
    __DisplayLandforms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayLandforms'), 'DisplayLandforms', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayLandforms', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 302, 6), )

    
    DisplayLandforms = property(__DisplayLandforms.value, __DisplayLandforms.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayRailroads uses Python identifier DisplayRailroads
    __DisplayRailroads = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayRailroads'), 'DisplayRailroads', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayRailroads', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 303, 6), )

    
    DisplayRailroads = property(__DisplayRailroads.value, __DisplayRailroads.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayRoads uses Python identifier DisplayRoads
    __DisplayRoads = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoads'), 'DisplayRoads', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayRoads', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 304, 6), )

    
    DisplayRoads = property(__DisplayRoads.value, __DisplayRoads.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayTrails uses Python identifier DisplayTrails
    __DisplayTrails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayTrails'), 'DisplayTrails', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayTrails', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 305, 6), )

    
    DisplayTrails = property(__DisplayTrails.value, __DisplayTrails.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayStructures uses Python identifier DisplayStructures
    __DisplayStructures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayStructures'), 'DisplayStructures', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayStructures', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 306, 6), )

    
    DisplayStructures = property(__DisplayStructures.value, __DisplayStructures.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPipelines uses Python identifier DisplayPipelines
    __DisplayPipelines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPipelines'), 'DisplayPipelines', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayPipelines', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 307, 6), )

    
    DisplayPipelines = property(__DisplayPipelines.value, __DisplayPipelines.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayUtilities uses Python identifier DisplayUtilities
    __DisplayUtilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayUtilities'), 'DisplayUtilities', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayUtilities', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 308, 6), )

    
    DisplayUtilities = property(__DisplayUtilities.value, __DisplayUtilities.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformDisplayOptionsList uses Python identifier PlatformDisplayOptionsList
    __PlatformDisplayOptionsList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptionsList'), 'PlatformDisplayOptionsList', '__httpwww_amherst_comCEESIMXML_ctSituationDisplaySettings_httpwww_amherst_comCEESIMXMLPlatformDisplayOptionsList', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 309, 6), )

    
    PlatformDisplayOptionsList = property(__PlatformDisplayOptionsList.value, __PlatformDisplayOptionsList.set, None, None)

    _ElementMap.update({
        __DisplayServer.name() : __DisplayServer,
        __DisplayId.name() : __DisplayId,
        __DisplayVisibility.name() : __DisplayVisibility,
        __SituationDisplayCenter.name() : __SituationDisplayCenter,
        __Center.name() : __Center,
        __SituationDisplayMode.name() : __SituationDisplayMode,
        __DisplayScale.name() : __DisplayScale,
        __DisplayIntensity.name() : __DisplayIntensity,
        __VelocityVectorDuration.name() : __VelocityVectorDuration,
        __DisplayTerrain.name() : __DisplayTerrain,
        __DisplayRoughness.name() : __DisplayRoughness,
        __DisplayGeopolitical.name() : __DisplayGeopolitical,
        __GeopoliticalCenterLatitude.name() : __GeopoliticalCenterLatitude,
        __GeopoliticalCenterLongitude.name() : __GeopoliticalCenterLongitude,
        __DisplayBarriers.name() : __DisplayBarriers,
        __DisplayCoastline.name() : __DisplayCoastline,
        __DisplayDepthLines.name() : __DisplayDepthLines,
        __DisplayPoliticalLines.name() : __DisplayPoliticalLines,
        __DisplayCanals.name() : __DisplayCanals,
        __DisplayWaterways.name() : __DisplayWaterways,
        __DisplayLandforms.name() : __DisplayLandforms,
        __DisplayRailroads.name() : __DisplayRailroads,
        __DisplayRoads.name() : __DisplayRoads,
        __DisplayTrails.name() : __DisplayTrails,
        __DisplayStructures.name() : __DisplayStructures,
        __DisplayPipelines.name() : __DisplayPipelines,
        __DisplayUtilities.name() : __DisplayUtilities,
        __PlatformDisplayOptionsList.name() : __PlatformDisplayOptionsList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctSituationDisplaySettings = ctSituationDisplaySettings
Namespace.addCategoryObject('typeBinding', 'ctSituationDisplaySettings', ctSituationDisplaySettings)


# Complex type {http://www.amherst.com/CEESIM/XML}ctGuiDisplaySettings with content type ELEMENT_ONLY
class ctGuiDisplaySettings (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctGuiDisplaySettings with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctGuiDisplaySettings')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 313, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}GuiDisplayMode uses Python identifier GuiDisplayMode
    __GuiDisplayMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplayMode'), 'GuiDisplayMode', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLGuiDisplayMode', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 315, 6), )

    
    GuiDisplayMode = property(__GuiDisplayMode.value, __GuiDisplayMode.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayGridKind uses Python identifier DisplayGridKind
    __DisplayGridKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayGridKind'), 'DisplayGridKind', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayGridKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 316, 6), )

    
    DisplayGridKind = property(__DisplayGridKind.value, __DisplayGridKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GuiDisplayCenter uses Python identifier GuiDisplayCenter
    __GuiDisplayCenter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplayCenter'), 'GuiDisplayCenter', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLGuiDisplayCenter', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 317, 6), )

    
    GuiDisplayCenter = property(__GuiDisplayCenter.value, __GuiDisplayCenter.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Center uses Python identifier Center
    __Center = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Center'), 'Center', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLCenter', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 318, 6), )

    
    Center = property(__Center.value, __Center.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}CenterPlatformNumber uses Python identifier CenterPlatformNumber
    __CenterPlatformNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CenterPlatformNumber'), 'CenterPlatformNumber', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLCenterPlatformNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 319, 6), )

    
    CenterPlatformNumber = property(__CenterPlatformNumber.value, __CenterPlatformNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Scale uses Python identifier Scale
    __Scale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Scale'), 'Scale', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLScale', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 320, 6), )

    
    Scale = property(__Scale.value, __Scale.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Intensity uses Python identifier Intensity
    __Intensity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Intensity'), 'Intensity', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLIntensity', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 321, 6), )

    
    Intensity = property(__Intensity.value, __Intensity.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}VelocityVectorDuration uses Python identifier VelocityVectorDuration
    __VelocityVectorDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'VelocityVectorDuration'), 'VelocityVectorDuration', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLVelocityVectorDuration', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 322, 6), )

    
    VelocityVectorDuration = property(__VelocityVectorDuration.value, __VelocityVectorDuration.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayHud uses Python identifier DisplayHud
    __DisplayHud = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayHud'), 'DisplayHud', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayHud', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 323, 6), )

    
    DisplayHud = property(__DisplayHud.value, __DisplayHud.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPlatformDetails uses Python identifier DisplayPlatformDetails
    __DisplayPlatformDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPlatformDetails'), 'DisplayPlatformDetails', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayPlatformDetails', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 324, 6), )

    
    DisplayPlatformDetails = property(__DisplayPlatformDetails.value, __DisplayPlatformDetails.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayTerrainLegend uses Python identifier DisplayTerrainLegend
    __DisplayTerrainLegend = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayTerrainLegend'), 'DisplayTerrainLegend', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayTerrainLegend', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 325, 6), )

    
    DisplayTerrainLegend = property(__DisplayTerrainLegend.value, __DisplayTerrainLegend.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayGrids uses Python identifier DisplayGrids
    __DisplayGrids = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayGrids'), 'DisplayGrids', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayGrids', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 326, 6), )

    
    DisplayGrids = property(__DisplayGrids.value, __DisplayGrids.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayProjectedPath uses Python identifier DisplayProjectedPath
    __DisplayProjectedPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayProjectedPath'), 'DisplayProjectedPath', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayProjectedPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 327, 6), )

    
    DisplayProjectedPath = property(__DisplayProjectedPath.value, __DisplayProjectedPath.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPathHistory uses Python identifier DisplayPathHistory
    __DisplayPathHistory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPathHistory'), 'DisplayPathHistory', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayPathHistory', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 328, 6), )

    
    DisplayPathHistory = property(__DisplayPathHistory.value, __DisplayPathHistory.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayInactivePlatforms uses Python identifier DisplayInactivePlatforms
    __DisplayInactivePlatforms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayInactivePlatforms'), 'DisplayInactivePlatforms', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayInactivePlatforms', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 329, 6), )

    
    DisplayInactivePlatforms = property(__DisplayInactivePlatforms.value, __DisplayInactivePlatforms.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplaySymbolLegend uses Python identifier DisplaySymbolLegend
    __DisplaySymbolLegend = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplaySymbolLegend'), 'DisplaySymbolLegend', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplaySymbolLegend', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 330, 6), )

    
    DisplaySymbolLegend = property(__DisplaySymbolLegend.value, __DisplaySymbolLegend.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayRoughnessLegend uses Python identifier DisplayRoughnessLegend
    __DisplayRoughnessLegend = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoughnessLegend'), 'DisplayRoughnessLegend', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayRoughnessLegend', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 331, 6), )

    
    DisplayRoughnessLegend = property(__DisplayRoughnessLegend.value, __DisplayRoughnessLegend.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayVmapLegend uses Python identifier DisplayVmapLegend
    __DisplayVmapLegend = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayVmapLegend'), 'DisplayVmapLegend', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayVmapLegend', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 332, 6), )

    
    DisplayVmapLegend = property(__DisplayVmapLegend.value, __DisplayVmapLegend.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TerrainEnable uses Python identifier TerrainEnable
    __TerrainEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TerrainEnable'), 'TerrainEnable', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLTerrainEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 333, 6), )

    
    TerrainEnable = property(__TerrainEnable.value, __TerrainEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RoughnessEnable uses Python identifier RoughnessEnable
    __RoughnessEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RoughnessEnable'), 'RoughnessEnable', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLRoughnessEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 334, 6), )

    
    RoughnessEnable = property(__RoughnessEnable.value, __RoughnessEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}VmapEnable uses Python identifier VmapEnable
    __VmapEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'VmapEnable'), 'VmapEnable', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLVmapEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 335, 6), )

    
    VmapEnable = property(__VmapEnable.value, __VmapEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeopoliticalCenterLatitude uses Python identifier GeopoliticalCenterLatitude
    __GeopoliticalCenterLatitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLatitude'), 'GeopoliticalCenterLatitude', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLGeopoliticalCenterLatitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 336, 6), )

    
    GeopoliticalCenterLatitude = property(__GeopoliticalCenterLatitude.value, __GeopoliticalCenterLatitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeopoliticalCenterLongitude uses Python identifier GeopoliticalCenterLongitude
    __GeopoliticalCenterLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLongitude'), 'GeopoliticalCenterLongitude', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLGeopoliticalCenterLongitude', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 337, 6), )

    
    GeopoliticalCenterLongitude = property(__GeopoliticalCenterLongitude.value, __GeopoliticalCenterLongitude.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayBarriers uses Python identifier DisplayBarriers
    __DisplayBarriers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayBarriers'), 'DisplayBarriers', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayBarriers', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 338, 6), )

    
    DisplayBarriers = property(__DisplayBarriers.value, __DisplayBarriers.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayCoastline uses Python identifier DisplayCoastline
    __DisplayCoastline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayCoastline'), 'DisplayCoastline', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayCoastline', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 339, 6), )

    
    DisplayCoastline = property(__DisplayCoastline.value, __DisplayCoastline.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayDepthLines uses Python identifier DisplayDepthLines
    __DisplayDepthLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayDepthLines'), 'DisplayDepthLines', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayDepthLines', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 340, 6), )

    
    DisplayDepthLines = property(__DisplayDepthLines.value, __DisplayDepthLines.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPoliticalLines uses Python identifier DisplayPoliticalLines
    __DisplayPoliticalLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPoliticalLines'), 'DisplayPoliticalLines', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayPoliticalLines', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 341, 6), )

    
    DisplayPoliticalLines = property(__DisplayPoliticalLines.value, __DisplayPoliticalLines.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayCanals uses Python identifier DisplayCanals
    __DisplayCanals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayCanals'), 'DisplayCanals', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayCanals', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 342, 6), )

    
    DisplayCanals = property(__DisplayCanals.value, __DisplayCanals.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayWaterways uses Python identifier DisplayWaterways
    __DisplayWaterways = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayWaterways'), 'DisplayWaterways', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayWaterways', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 343, 6), )

    
    DisplayWaterways = property(__DisplayWaterways.value, __DisplayWaterways.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayLandforms uses Python identifier DisplayLandforms
    __DisplayLandforms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayLandforms'), 'DisplayLandforms', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayLandforms', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 344, 6), )

    
    DisplayLandforms = property(__DisplayLandforms.value, __DisplayLandforms.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayRailroads uses Python identifier DisplayRailroads
    __DisplayRailroads = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayRailroads'), 'DisplayRailroads', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayRailroads', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 345, 6), )

    
    DisplayRailroads = property(__DisplayRailroads.value, __DisplayRailroads.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayRoads uses Python identifier DisplayRoads
    __DisplayRoads = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoads'), 'DisplayRoads', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayRoads', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 346, 6), )

    
    DisplayRoads = property(__DisplayRoads.value, __DisplayRoads.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayTrails uses Python identifier DisplayTrails
    __DisplayTrails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayTrails'), 'DisplayTrails', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayTrails', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 347, 6), )

    
    DisplayTrails = property(__DisplayTrails.value, __DisplayTrails.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayStructures uses Python identifier DisplayStructures
    __DisplayStructures = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayStructures'), 'DisplayStructures', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayStructures', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 348, 6), )

    
    DisplayStructures = property(__DisplayStructures.value, __DisplayStructures.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPipelines uses Python identifier DisplayPipelines
    __DisplayPipelines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPipelines'), 'DisplayPipelines', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayPipelines', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 349, 6), )

    
    DisplayPipelines = property(__DisplayPipelines.value, __DisplayPipelines.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayUtilities uses Python identifier DisplayUtilities
    __DisplayUtilities = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayUtilities'), 'DisplayUtilities', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLDisplayUtilities', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 350, 6), )

    
    DisplayUtilities = property(__DisplayUtilities.value, __DisplayUtilities.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeotiffEnable uses Python identifier GeotiffEnable
    __GeotiffEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeotiffEnable'), 'GeotiffEnable', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLGeotiffEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 351, 6), )

    
    GeotiffEnable = property(__GeotiffEnable.value, __GeotiffEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GeotiffPath uses Python identifier GeotiffPath
    __GeotiffPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GeotiffPath'), 'GeotiffPath', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLGeotiffPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 352, 6), )

    
    GeotiffPath = property(__GeotiffPath.value, __GeotiffPath.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformDisplayOptionsList uses Python identifier PlatformDisplayOptionsList
    __PlatformDisplayOptionsList = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptionsList'), 'PlatformDisplayOptionsList', '__httpwww_amherst_comCEESIMXML_ctGuiDisplaySettings_httpwww_amherst_comCEESIMXMLPlatformDisplayOptionsList', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 353, 6), )

    
    PlatformDisplayOptionsList = property(__PlatformDisplayOptionsList.value, __PlatformDisplayOptionsList.set, None, None)

    _ElementMap.update({
        __GuiDisplayMode.name() : __GuiDisplayMode,
        __DisplayGridKind.name() : __DisplayGridKind,
        __GuiDisplayCenter.name() : __GuiDisplayCenter,
        __Center.name() : __Center,
        __CenterPlatformNumber.name() : __CenterPlatformNumber,
        __Scale.name() : __Scale,
        __Intensity.name() : __Intensity,
        __VelocityVectorDuration.name() : __VelocityVectorDuration,
        __DisplayHud.name() : __DisplayHud,
        __DisplayPlatformDetails.name() : __DisplayPlatformDetails,
        __DisplayTerrainLegend.name() : __DisplayTerrainLegend,
        __DisplayGrids.name() : __DisplayGrids,
        __DisplayProjectedPath.name() : __DisplayProjectedPath,
        __DisplayPathHistory.name() : __DisplayPathHistory,
        __DisplayInactivePlatforms.name() : __DisplayInactivePlatforms,
        __DisplaySymbolLegend.name() : __DisplaySymbolLegend,
        __DisplayRoughnessLegend.name() : __DisplayRoughnessLegend,
        __DisplayVmapLegend.name() : __DisplayVmapLegend,
        __TerrainEnable.name() : __TerrainEnable,
        __RoughnessEnable.name() : __RoughnessEnable,
        __VmapEnable.name() : __VmapEnable,
        __GeopoliticalCenterLatitude.name() : __GeopoliticalCenterLatitude,
        __GeopoliticalCenterLongitude.name() : __GeopoliticalCenterLongitude,
        __DisplayBarriers.name() : __DisplayBarriers,
        __DisplayCoastline.name() : __DisplayCoastline,
        __DisplayDepthLines.name() : __DisplayDepthLines,
        __DisplayPoliticalLines.name() : __DisplayPoliticalLines,
        __DisplayCanals.name() : __DisplayCanals,
        __DisplayWaterways.name() : __DisplayWaterways,
        __DisplayLandforms.name() : __DisplayLandforms,
        __DisplayRailroads.name() : __DisplayRailroads,
        __DisplayRoads.name() : __DisplayRoads,
        __DisplayTrails.name() : __DisplayTrails,
        __DisplayStructures.name() : __DisplayStructures,
        __DisplayPipelines.name() : __DisplayPipelines,
        __DisplayUtilities.name() : __DisplayUtilities,
        __GeotiffEnable.name() : __GeotiffEnable,
        __GeotiffPath.name() : __GeotiffPath,
        __PlatformDisplayOptionsList.name() : __PlatformDisplayOptionsList
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctGuiDisplaySettings = ctGuiDisplaySettings
Namespace.addCategoryObject('typeBinding', 'ctGuiDisplaySettings', ctGuiDisplaySettings)


# Complex type {http://www.amherst.com/CEESIM/XML}ctSituationDisplayPlatformOptionsList with content type ELEMENT_ONLY
class ctSituationDisplayPlatformOptionsList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctSituationDisplayPlatformOptionsList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctSituationDisplayPlatformOptionsList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 357, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformDisplayOptions uses Python identifier PlatformDisplayOptions
    __PlatformDisplayOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptions'), 'PlatformDisplayOptions', '__httpwww_amherst_comCEESIMXML_ctSituationDisplayPlatformOptionsList_httpwww_amherst_comCEESIMXMLPlatformDisplayOptions', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 359, 6), )

    
    PlatformDisplayOptions = property(__PlatformDisplayOptions.value, __PlatformDisplayOptions.set, None, None)

    _ElementMap.update({
        __PlatformDisplayOptions.name() : __PlatformDisplayOptions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctSituationDisplayPlatformOptionsList = ctSituationDisplayPlatformOptionsList
Namespace.addCategoryObject('typeBinding', 'ctSituationDisplayPlatformOptionsList', ctSituationDisplayPlatformOptionsList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctSituationDisplayPlatformOptions with content type ELEMENT_ONLY
class ctSituationDisplayPlatformOptions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctSituationDisplayPlatformOptions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctSituationDisplayPlatformOptions')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 363, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformNumber uses Python identifier PlatformNumber
    __PlatformNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformNumber'), 'PlatformNumber', '__httpwww_amherst_comCEESIMXML_ctSituationDisplayPlatformOptions_httpwww_amherst_comCEESIMXMLPlatformNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 365, 6), )

    
    PlatformNumber = property(__PlatformNumber.value, __PlatformNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPlatform uses Python identifier DisplayPlatform
    __DisplayPlatform = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPlatform'), 'DisplayPlatform', '__httpwww_amherst_comCEESIMXML_ctSituationDisplayPlatformOptions_httpwww_amherst_comCEESIMXMLDisplayPlatform', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 366, 6), )

    
    DisplayPlatform = property(__DisplayPlatform.value, __DisplayPlatform.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPath uses Python identifier DisplayPath
    __DisplayPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPath'), 'DisplayPath', '__httpwww_amherst_comCEESIMXML_ctSituationDisplayPlatformOptions_httpwww_amherst_comCEESIMXMLDisplayPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 367, 6), )

    
    DisplayPath = property(__DisplayPath.value, __DisplayPath.set, None, None)

    _ElementMap.update({
        __PlatformNumber.name() : __PlatformNumber,
        __DisplayPlatform.name() : __DisplayPlatform,
        __DisplayPath.name() : __DisplayPath
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctSituationDisplayPlatformOptions = ctSituationDisplayPlatformOptions
Namespace.addCategoryObject('typeBinding', 'ctSituationDisplayPlatformOptions', ctSituationDisplayPlatformOptions)


# Complex type {http://www.amherst.com/CEESIM/XML}ctGuiPlatformOptionsList with content type ELEMENT_ONLY
class ctGuiPlatformOptionsList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctGuiPlatformOptionsList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctGuiPlatformOptionsList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 371, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformDisplayOptions uses Python identifier PlatformDisplayOptions
    __PlatformDisplayOptions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptions'), 'PlatformDisplayOptions', '__httpwww_amherst_comCEESIMXML_ctGuiPlatformOptionsList_httpwww_amherst_comCEESIMXMLPlatformDisplayOptions', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 373, 6), )

    
    PlatformDisplayOptions = property(__PlatformDisplayOptions.value, __PlatformDisplayOptions.set, None, None)

    _ElementMap.update({
        __PlatformDisplayOptions.name() : __PlatformDisplayOptions
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctGuiPlatformOptionsList = ctGuiPlatformOptionsList
Namespace.addCategoryObject('typeBinding', 'ctGuiPlatformOptionsList', ctGuiPlatformOptionsList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctGuiPlatformOptions with content type ELEMENT_ONLY
class ctGuiPlatformOptions (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctGuiPlatformOptions with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctGuiPlatformOptions')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 377, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformNumber uses Python identifier PlatformNumber
    __PlatformNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformNumber'), 'PlatformNumber', '__httpwww_amherst_comCEESIMXML_ctGuiPlatformOptions_httpwww_amherst_comCEESIMXMLPlatformNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 379, 6), )

    
    PlatformNumber = property(__PlatformNumber.value, __PlatformNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplaySymbol uses Python identifier DisplaySymbol
    __DisplaySymbol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplaySymbol'), 'DisplaySymbol', '__httpwww_amherst_comCEESIMXML_ctGuiPlatformOptions_httpwww_amherst_comCEESIMXMLDisplaySymbol', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 380, 6), )

    
    DisplaySymbol = property(__DisplaySymbol.value, __DisplaySymbol.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayPathHistory uses Python identifier DisplayPathHistory
    __DisplayPathHistory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayPathHistory'), 'DisplayPathHistory', '__httpwww_amherst_comCEESIMXML_ctGuiPlatformOptions_httpwww_amherst_comCEESIMXMLDisplayPathHistory', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 381, 6), )

    
    DisplayPathHistory = property(__DisplayPathHistory.value, __DisplayPathHistory.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DisplayProjectedPath uses Python identifier DisplayProjectedPath
    __DisplayProjectedPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DisplayProjectedPath'), 'DisplayProjectedPath', '__httpwww_amherst_comCEESIMXML_ctGuiPlatformOptions_httpwww_amherst_comCEESIMXMLDisplayProjectedPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 382, 6), )

    
    DisplayProjectedPath = property(__DisplayProjectedPath.value, __DisplayProjectedPath.set, None, None)

    _ElementMap.update({
        __PlatformNumber.name() : __PlatformNumber,
        __DisplaySymbol.name() : __DisplaySymbol,
        __DisplayPathHistory.name() : __DisplayPathHistory,
        __DisplayProjectedPath.name() : __DisplayProjectedPath
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctGuiPlatformOptions = ctGuiPlatformOptions
Namespace.addCategoryObject('typeBinding', 'ctGuiPlatformOptions', ctGuiPlatformOptions)


Scenario = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Scenario'), ctScenarioData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioRootR1-1.xsd', 38, 2))
Namespace.addCategoryObject('elementBinding', Scenario.name().localName(), Scenario)



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




ctScenarioData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScenarioHeader'), ctScenarioHeader, scope=ctScenarioData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 43, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 43, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScenarioHeader')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 43, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctScenarioData._Automaton = _BuildAutomaton_13()




ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreationDate'), stDateCreationDate, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 50, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ModificationDate'), stDateModificationDate, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 51, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScenarioRevision'), stIntScenarioRevision, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 52, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SoftwareReleaseOfLastHeaderEdit'), stIntSoftwareReleaseOfLastHeaderEdit, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 53, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DistanceUnits'), stEnumDistanceUnits, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 54, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EnvironmentKind'), stEnumEnvironmentKind, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 55, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), stStringCommentScenarioHeader, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 56, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SutPlatformNumbers'), ctSutPlatformNumberList, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 57, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalSutFlag'), stBoolExternalSutFlag, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 58, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HorizonMaskingEnable'), stBoolHorizonMaskingEnable, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 59, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EarthRadiusFactor'), stDoubleEarthRadiusFactor, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 60, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataRecording'), ctDataRecording, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 61, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterLibraryEnable'), stBoolEmitterLibraryEnable, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 62, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterLibraryName'), stStringEmitterLibraryName, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 63, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScenarioElementLibraryEnable'), stBoolScenarioElementLibraryEnable, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 64, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScenarioElementLibraryName'), stTextScenarioElementLibraryName, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 65, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Terrain'), ctTerrain, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 66, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SurfaceEffects'), ctSurfaceEffects, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 67, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PropagationEffects'), ctPropagationEffects, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 68, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpacialAndDopplerEffects'), ctSpacialAndDopplerEffects, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 69, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HardwareResourceOptimizations'), ctHardwareResourceOptimizations, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 70, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dpms'), ctDpmDataList, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 71, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavigationInterfaceSettings'), ctNavigationInterfaceSettings, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 72, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayData'), ctSituationDisplayDataList, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 73, 6)))

ctScenarioHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplaySettings'), ctGuiDisplaySettings, scope=ctScenarioHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 74, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 50, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreationDate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 50, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 51, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ModificationDate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 51, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 52, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScenarioRevision')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 52, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 53, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SoftwareReleaseOfLastHeaderEdit')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 53, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 54, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DistanceUnits')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 54, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 55, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EnvironmentKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 55, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 56, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 56, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 57, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SutPlatformNumbers')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 57, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 58, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalSutFlag')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 58, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 59, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HorizonMaskingEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 59, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 60, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EarthRadiusFactor')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 60, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 61, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataRecording')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 61, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 62, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterLibraryEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 62, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 63, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterLibraryName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 63, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 64, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScenarioElementLibraryEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 64, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 65, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScenarioElementLibraryName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 65, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 66, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Terrain')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 66, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 67, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SurfaceEffects')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 67, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 68, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PropagationEffects')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 68, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 69, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SpacialAndDopplerEffects')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 69, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 70, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'HardwareResourceOptimizations')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 70, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 71, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dpms')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 71, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 72, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavigationInterfaceSettings')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 72, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 73, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayData')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 73, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 74, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctScenarioHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplaySettings')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 74, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 51, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 52, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 53, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 54, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 55, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 56, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 57, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 58, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 59, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 60, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 61, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 62, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 63, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 64, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 65, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 66, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 67, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 68, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 69, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 70, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 71, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 72, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 73, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 74, 6))
    counters.add(cc_24)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    sub_automata.append(_BuildAutomaton_21())
    sub_automata.append(_BuildAutomaton_22())
    sub_automata.append(_BuildAutomaton_23())
    sub_automata.append(_BuildAutomaton_24())
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
    sub_automata.append(_BuildAutomaton_38())
    sub_automata.append(_BuildAutomaton_39())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 49, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctScenarioHeader._Automaton = _BuildAutomaton_14()




ctSutPlatformNumberList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SutPlatformNumber'), stIntSutPlatformNumber, scope=ctSutPlatformNumberList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 81, 6)))

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=4, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 80, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSutPlatformNumberList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SutPlatformNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 81, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctSutPlatformNumberList._Automaton = _BuildAutomaton_40()




ctDataRecording._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DataRecordingEnable'), stBoolDataRecordingEnable, scope=ctDataRecording, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 87, 6)))

ctDataRecording._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DxFileName'), stStringDxFileName, scope=ctDataRecording, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 88, 6)))

ctDataRecording._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordPlatformEventsEnable'), stBoolRecordPlatformEventsEnable, scope=ctDataRecording, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 89, 6)))

ctDataRecording._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordEmitterEventsEnable'), stBoolRecordEmitterEventsEnable, scope=ctDataRecording, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 90, 6)))

ctDataRecording._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordPulseCountsEnable'), stBoolRecordPulseCountsEnable, scope=ctDataRecording, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 91, 6)))

ctDataRecording._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordPlatformStatusEnable'), stBoolRecordPlatformStatusEnable, scope=ctDataRecording, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 92, 6)))

ctDataRecording._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RecordEmitterStatusEnable'), stBoolRecordEmitterStatusEnable, scope=ctDataRecording, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 93, 6)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 87, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDataRecording._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DataRecordingEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 87, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 88, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDataRecording._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DxFileName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 88, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 89, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDataRecording._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordPlatformEventsEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 89, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 90, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDataRecording._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordEmitterEventsEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 90, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 91, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDataRecording._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordPulseCountsEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 91, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 92, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDataRecording._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordPlatformStatusEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 92, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 93, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDataRecording._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RecordEmitterStatusEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 93, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 87, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 88, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 89, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 90, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 91, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 92, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 93, 6))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_42())
    sub_automata.append(_BuildAutomaton_43())
    sub_automata.append(_BuildAutomaton_44())
    sub_automata.append(_BuildAutomaton_45())
    sub_automata.append(_BuildAutomaton_46())
    sub_automata.append(_BuildAutomaton_47())
    sub_automata.append(_BuildAutomaton_48())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 86, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDataRecording._Automaton = _BuildAutomaton_41()




ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TerrainEnable'), stBoolTerrainEnable, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 99, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TerrainMaskingAttenuationEnable'), stBoolTerrainMaskingAttenuationEnable, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 100, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TerrainDtedKind'), stEnumTerrainDtedKind, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 101, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NorthLatitude'), stDoubleNorthLatitude, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 102, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NorthDirection'), stEnumNorthSouthDirectionKind, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 103, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WestLongitude'), stDoubleWestLongitude, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 104, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WestDirection'), stEnumEastWestDirectionKind, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 105, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SouthLatitude'), stDoubleSouthLatitude, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 106, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SouthDirection'), stEnumNorthSouthDirectionKind, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 107, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EastLongitude'), stDoubleEastLongitude, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 108, 6)))

ctTerrain._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EastDirection'), stEnumEastWestDirectionKind, scope=ctTerrain, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 109, 6)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 99, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TerrainEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 99, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 100, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TerrainMaskingAttenuationEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 100, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 101, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TerrainDtedKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 101, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 102, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NorthLatitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 102, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 103, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NorthDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 103, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 104, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WestLongitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 104, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 105, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WestDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 105, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 106, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SouthLatitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 106, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 107, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SouthDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 107, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 108, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EastLongitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 108, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 109, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTerrain._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EastDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 109, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 99, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 100, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 101, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 102, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 103, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 104, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 105, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 106, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 107, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 108, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 109, 6))
    counters.add(cc_10)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_50())
    sub_automata.append(_BuildAutomaton_51())
    sub_automata.append(_BuildAutomaton_52())
    sub_automata.append(_BuildAutomaton_53())
    sub_automata.append(_BuildAutomaton_54())
    sub_automata.append(_BuildAutomaton_55())
    sub_automata.append(_BuildAutomaton_56())
    sub_automata.append(_BuildAutomaton_57())
    sub_automata.append(_BuildAutomaton_58())
    sub_automata.append(_BuildAutomaton_59())
    sub_automata.append(_BuildAutomaton_60())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 98, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctTerrain._Automaton = _BuildAutomaton_49()




ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MultipathEnable'), stBoolMultipathEnable, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 115, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WaveSplashEnable'), stBoolWaveSplashEnable, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 116, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SutEmitterEarthReflectionEnable'), stBoolSutEmitterEarthReflectionEnable, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 117, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SurfaceKind'), stEnumSurfaceKind, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 118, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NorthLatitude'), stDoubleNorthLatitude, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 119, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NorthDirection'), stEnumNorthSouthDirectionKind, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 120, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WestLongitude'), stDoubleWestLongitude, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 121, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WestDirection'), stEnumEastWestDirectionKind, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 122, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SouthLatitude'), stDoubleSouthLatitude, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 123, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SouthDirection'), stEnumNorthSouthDirectionKind, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 124, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EastLongitude'), stDoubleEastLongitude, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 125, 6)))

ctSurfaceEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EastDirection'), stEnumEastWestDirectionKind, scope=ctSurfaceEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 126, 6)))

def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 115, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MultipathEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 115, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 116, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WaveSplashEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 116, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 117, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SutEmitterEarthReflectionEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 117, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 118, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SurfaceKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 118, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 119, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NorthLatitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 119, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 120, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NorthDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 120, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 121, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WestLongitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 121, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 122, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'WestDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 122, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 123, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SouthLatitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 123, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 124, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SouthDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 124, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 125, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EastLongitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 125, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 126, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSurfaceEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EastDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 126, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 115, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 116, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 117, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 118, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 119, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 120, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 121, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 122, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 123, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 124, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 125, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 126, 6))
    counters.add(cc_11)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_62())
    sub_automata.append(_BuildAutomaton_63())
    sub_automata.append(_BuildAutomaton_64())
    sub_automata.append(_BuildAutomaton_65())
    sub_automata.append(_BuildAutomaton_66())
    sub_automata.append(_BuildAutomaton_67())
    sub_automata.append(_BuildAutomaton_68())
    sub_automata.append(_BuildAutomaton_69())
    sub_automata.append(_BuildAutomaton_70())
    sub_automata.append(_BuildAutomaton_71())
    sub_automata.append(_BuildAutomaton_72())
    sub_automata.append(_BuildAutomaton_73())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 114, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctSurfaceEffects._Automaton = _BuildAutomaton_61()




ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AtmosphericAbsorptionAttenuationEnable'), stBoolAtmosphericAbsorptionAttenuationEnable, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 132, 6)))

ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RainfallRateKind'), stEnumRainfallRateKind, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 133, 6)))

ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DuctingEnable'), stBoolDuctingEnable, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 134, 6)))

ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DuctingBoundaryKind'), stEnumDuctingBoundaryKind, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 135, 6)))

ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DuctingHeight'), stDoubleDuctingHeight, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 136, 6)))

ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DuctingRefractivity'), stDoubleDuctingRefractivity, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 137, 6)))

ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DuctingFileName'), stStringDuctingFileName, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 138, 6)))

ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RangeAttenuationEnable'), stBoolRangeAttenuationEnable, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 139, 6)))

ctPropagationEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrequencyAttenuationEnable'), stBoolFrequencyAttenuationEnable, scope=ctPropagationEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 140, 6)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 132, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AtmosphericAbsorptionAttenuationEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 132, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 133, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RainfallRateKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 133, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 134, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DuctingEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 134, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 135, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DuctingBoundaryKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 135, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 136, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DuctingHeight')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 136, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 137, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DuctingRefractivity')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 137, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 138, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DuctingFileName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 138, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_82 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_82
    del _BuildAutomaton_82
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 139, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RangeAttenuationEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 139, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_83 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_83
    del _BuildAutomaton_83
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 140, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPropagationEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrequencyAttenuationEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 140, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 132, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 133, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 134, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 135, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 136, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 137, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 138, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 139, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 140, 6))
    counters.add(cc_8)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_75())
    sub_automata.append(_BuildAutomaton_76())
    sub_automata.append(_BuildAutomaton_77())
    sub_automata.append(_BuildAutomaton_78())
    sub_automata.append(_BuildAutomaton_79())
    sub_automata.append(_BuildAutomaton_80())
    sub_automata.append(_BuildAutomaton_81())
    sub_automata.append(_BuildAutomaton_82())
    sub_automata.append(_BuildAutomaton_83())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 131, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctPropagationEffects._Automaton = _BuildAutomaton_74()




ctSpacialAndDopplerEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FrequencyDopplerShiftEnable'), stBoolFrequencyDopplerShiftEnable, scope=ctSpacialAndDopplerEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 146, 6)))

ctSpacialAndDopplerEffects._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RangeAndPriDopplerShiftEnable'), stBoolRangeAndPriDopplerShiftEnable, scope=ctSpacialAndDopplerEffects, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 147, 6)))

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 146, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSpacialAndDopplerEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FrequencyDopplerShiftEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 146, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_86 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_86
    del _BuildAutomaton_86
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 147, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSpacialAndDopplerEffects._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RangeAndPriDopplerShiftEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 147, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_84 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_84
    del _BuildAutomaton_84
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 146, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 147, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_85())
    sub_automata.append(_BuildAutomaton_86())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 145, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctSpacialAndDopplerEffects._Automaton = _BuildAutomaton_84()




ctHardwareResourceOptimizations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PulseTruncationEnable'), stBoolPulseTruncationEnable, scope=ctHardwareResourceOptimizations, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 153, 6)))

ctHardwareResourceOptimizations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CwInterruptEnable'), stBoolCwInterruptEnable, scope=ctHardwareResourceOptimizations, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 154, 6)))

ctHardwareResourceOptimizations._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SensitivityThresholdEnable'), stBoolSensitivityThresholdEnable, scope=ctHardwareResourceOptimizations, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 155, 6)))

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 153, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHardwareResourceOptimizations._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PulseTruncationEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 153, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_89 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_89
    del _BuildAutomaton_89
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 154, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHardwareResourceOptimizations._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CwInterruptEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 154, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_90 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_90
    del _BuildAutomaton_90
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 155, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHardwareResourceOptimizations._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SensitivityThresholdEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 155, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_87 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_87
    del _BuildAutomaton_87
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 153, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 154, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 155, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_88())
    sub_automata.append(_BuildAutomaton_89())
    sub_automata.append(_BuildAutomaton_90())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 152, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctHardwareResourceOptimizations._Automaton = _BuildAutomaton_87()




ctDpmDataList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dpm'), ctDpmData, scope=ctDpmDataList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 161, 6)))

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 160, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmDataList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dpm')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 161, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmDataList._Automaton = _BuildAutomaton_91()




ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DpmBoardCollectionEnable'), stBoolDpmBoardCollectionEnable, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 167, 6)))

ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PulseContendedState'), stEnumPulseContendedStateKind, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 168, 6)))

ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PulseInhibitState'), stEnumPulseInhibitStateKind, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 169, 6)))

ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CircularBufferCollection'), stBoolCircularBufferCollection, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 170, 6)))

ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ExternalGatingState'), stEnumExternalGatingStateKind, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 171, 6)))

ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DgsVideoState'), stEnumDgsVideoStateKind, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 172, 6)))

ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PdwKind'), stEnumPdwKind, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 173, 6)))

ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InvalidPdwsFlag'), stBoolInvalidPdwsFlag, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 174, 6)))

ctDpmData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DpmFilters'), ctDpmFilter, scope=ctDpmData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 175, 6)))

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 167, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DpmBoardCollectionEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 167, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 168, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PulseContendedState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 168, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 169, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PulseInhibitState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 169, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_96 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_96
    del _BuildAutomaton_96
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 170, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CircularBufferCollection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 170, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_97 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_97
    del _BuildAutomaton_97
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 171, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ExternalGatingState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 171, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_98 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 172, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DgsVideoState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 172, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_99 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_99
    del _BuildAutomaton_99
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 173, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PdwKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 173, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_100 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_100
    del _BuildAutomaton_100
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 174, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InvalidPdwsFlag')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 174, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_101 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_101
    del _BuildAutomaton_101
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 175, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DpmFilters')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 175, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_92 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_92
    del _BuildAutomaton_92
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 167, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 168, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 169, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 170, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 171, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 172, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 173, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 174, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 175, 6))
    counters.add(cc_8)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_93())
    sub_automata.append(_BuildAutomaton_94())
    sub_automata.append(_BuildAutomaton_95())
    sub_automata.append(_BuildAutomaton_96())
    sub_automata.append(_BuildAutomaton_97())
    sub_automata.append(_BuildAutomaton_98())
    sub_automata.append(_BuildAutomaton_99())
    sub_automata.append(_BuildAutomaton_100())
    sub_automata.append(_BuildAutomaton_101())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 166, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmData._Automaton = _BuildAutomaton_92()




ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AzAoa'), ctDpmFilterAzAoa, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 181, 6)))

ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ElAoa'), ctDpmFilterElAoa, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 182, 6)))

ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterNumber'), ctDpmFilterEmitterNumber, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 183, 6)))

ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Frequency'), ctDpmFilterFrequency, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 184, 6)))

ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Generator'), ctDpmFilterGenerator, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 185, 6)))

ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EmitterName'), stStringEmitterName, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 186, 6)))

ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PulseWidth'), ctDpmFilterPulseWidth, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 187, 6)))

ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Power'), ctDpmFilterPower, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 188, 6)))

ctDpmFilter._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScenarioTime'), ctDpmFilterScenarioTime, scope=ctDpmFilter, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 189, 6)))

def _BuildAutomaton_102 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_102
    del _BuildAutomaton_102
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 180, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 181, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 182, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 183, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 184, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 185, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 186, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 187, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 188, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 189, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AzAoa')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 181, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ElAoa')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 182, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 183, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Frequency')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 184, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Generator')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 185, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EmitterName')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 186, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PulseWidth')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 187, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Power')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 188, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilter._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScenarioTime')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 189, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_2, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_3, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_4, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_5, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_7, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_8, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True),
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilter._Automaton = _BuildAutomaton_102()




ctDpmFilterAzAoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerAzimuth'), stDoubleLowerAz, scope=ctDpmFilterAzAoa, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 195, 6)))

ctDpmFilterAzAoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperAzimuth'), stDoubleUpperAz, scope=ctDpmFilterAzAoa, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 196, 6)))

def _BuildAutomaton_104 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_104
    del _BuildAutomaton_104
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 195, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterAzAoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerAzimuth')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 195, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_105 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_105
    del _BuildAutomaton_105
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 196, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterAzAoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperAzimuth')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 196, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_103 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_103
    del _BuildAutomaton_103
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 195, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 196, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_104())
    sub_automata.append(_BuildAutomaton_105())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 194, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilterAzAoa._Automaton = _BuildAutomaton_103()




ctDpmFilterElAoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerElevation'), stDoubleLowerElevation, scope=ctDpmFilterElAoa, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 202, 6)))

ctDpmFilterElAoa._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperElevation'), stDoubleUpperElevation, scope=ctDpmFilterElAoa, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 203, 6)))

def _BuildAutomaton_107 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_107
    del _BuildAutomaton_107
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 202, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterElAoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerElevation')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 202, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_108 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_108
    del _BuildAutomaton_108
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 203, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterElAoa._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperElevation')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 203, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_106 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_106
    del _BuildAutomaton_106
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 202, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 203, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_107())
    sub_automata.append(_BuildAutomaton_108())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 201, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilterElAoa._Automaton = _BuildAutomaton_106()




ctDpmFilterEmitterNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerEmitter'), stIntLowerEmitterNumber, scope=ctDpmFilterEmitterNumber, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 209, 6)))

ctDpmFilterEmitterNumber._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperEmitter'), stIntUpperEmitterNumber, scope=ctDpmFilterEmitterNumber, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 210, 6)))

def _BuildAutomaton_110 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_110
    del _BuildAutomaton_110
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 209, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterEmitterNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerEmitter')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 209, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_111 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_111
    del _BuildAutomaton_111
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 210, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterEmitterNumber._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperEmitter')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 210, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_109 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_109
    del _BuildAutomaton_109
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 209, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 210, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_110())
    sub_automata.append(_BuildAutomaton_111())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 208, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilterEmitterNumber._Automaton = _BuildAutomaton_109()




ctDpmFilterFrequency._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerFrequency'), stDoubleLowerFrequency, scope=ctDpmFilterFrequency, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 216, 6)))

ctDpmFilterFrequency._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperFrequency'), stDoubleUpperFrequency, scope=ctDpmFilterFrequency, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 217, 6)))

def _BuildAutomaton_113 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_113
    del _BuildAutomaton_113
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 216, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterFrequency._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerFrequency')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 216, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_114 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_114
    del _BuildAutomaton_114
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 217, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterFrequency._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperFrequency')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 217, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_112 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_112
    del _BuildAutomaton_112
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 216, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 217, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_113())
    sub_automata.append(_BuildAutomaton_114())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 215, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilterFrequency._Automaton = _BuildAutomaton_112()




ctDpmFilterGenerator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerGenerator'), stIntLowerGeneratorNumber, scope=ctDpmFilterGenerator, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 223, 6)))

ctDpmFilterGenerator._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperGenerator'), stIntUpperGeneratorNumber, scope=ctDpmFilterGenerator, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 224, 6)))

def _BuildAutomaton_116 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_116
    del _BuildAutomaton_116
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 223, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerGenerator')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 223, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_117 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_117
    del _BuildAutomaton_117
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 224, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterGenerator._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperGenerator')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 224, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_115 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_115
    del _BuildAutomaton_115
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 223, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 224, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_116())
    sub_automata.append(_BuildAutomaton_117())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 222, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilterGenerator._Automaton = _BuildAutomaton_115()




ctDpmFilterPulseWidth._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerPulseWidth'), stDoubleLowerPulseWidth, scope=ctDpmFilterPulseWidth, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 230, 6)))

ctDpmFilterPulseWidth._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperPulseWidth'), stDoubleUpperPulseWidth, scope=ctDpmFilterPulseWidth, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 231, 6)))

def _BuildAutomaton_119 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_119
    del _BuildAutomaton_119
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 230, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterPulseWidth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerPulseWidth')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 230, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_120 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_120
    del _BuildAutomaton_120
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 231, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterPulseWidth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperPulseWidth')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 231, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_118 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_118
    del _BuildAutomaton_118
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 230, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 231, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_119())
    sub_automata.append(_BuildAutomaton_120())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 229, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilterPulseWidth._Automaton = _BuildAutomaton_118()




ctDpmFilterPower._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerPower'), stDoubleLowerPower, scope=ctDpmFilterPower, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 237, 6)))

ctDpmFilterPower._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperPower'), stDoubleUpperPower, scope=ctDpmFilterPower, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 238, 6)))

def _BuildAutomaton_122 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_122
    del _BuildAutomaton_122
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 237, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterPower._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerPower')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 237, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_123 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_123
    del _BuildAutomaton_123
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 238, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterPower._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperPower')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 238, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_121 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_121
    del _BuildAutomaton_121
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 237, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 238, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_122())
    sub_automata.append(_BuildAutomaton_123())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 236, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilterPower._Automaton = _BuildAutomaton_121()




ctDpmFilterScenarioTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LowerTime'), stDoubleLowerTime, scope=ctDpmFilterScenarioTime, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 244, 6)))

ctDpmFilterScenarioTime._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpperTime'), stDoubleUpperTime, scope=ctDpmFilterScenarioTime, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 245, 6)))

def _BuildAutomaton_125 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_125
    del _BuildAutomaton_125
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 244, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterScenarioTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LowerTime')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 244, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_126 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_126
    del _BuildAutomaton_126
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 245, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctDpmFilterScenarioTime._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpperTime')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 245, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_124 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_124
    del _BuildAutomaton_124
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 244, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 245, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_125())
    sub_automata.append(_BuildAutomaton_126())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 243, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctDpmFilterScenarioTime._Automaton = _BuildAutomaton_124()




ctNavigationInterfaceSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfEnable'), stBoolNavIfEnable, scope=ctNavigationInterfaceSettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 251, 6)))

ctNavigationInterfaceSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfPhysicalIfKind'), stEnumNavIfPhysicalIfKind, scope=ctNavigationInterfaceSettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 252, 6)))

ctNavigationInterfaceSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIf1553BusKind'), stEnumNavIf1553BusKind, scope=ctNavigationInterfaceSettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 253, 6)))

ctNavigationInterfaceSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfUpdateInterval'), stEnumNavIfUpdateInterval, scope=ctNavigationInterfaceSettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 254, 6)))

ctNavigationInterfaceSettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfPlatforms'), ctNavIfPlatformsList, scope=ctNavigationInterfaceSettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 255, 6)))

def _BuildAutomaton_128 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_128
    del _BuildAutomaton_128
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 251, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavigationInterfaceSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 251, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_129 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_129
    del _BuildAutomaton_129
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 252, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavigationInterfaceSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfPhysicalIfKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 252, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_130 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_130
    del _BuildAutomaton_130
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 253, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavigationInterfaceSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIf1553BusKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 253, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_131 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_131
    del _BuildAutomaton_131
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 254, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavigationInterfaceSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfUpdateInterval')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 254, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_132 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_132
    del _BuildAutomaton_132
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 255, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavigationInterfaceSettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfPlatforms')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 255, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_127 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_127
    del _BuildAutomaton_127
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 251, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 252, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 253, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 254, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 255, 6))
    counters.add(cc_4)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_128())
    sub_automata.append(_BuildAutomaton_129())
    sub_automata.append(_BuildAutomaton_130())
    sub_automata.append(_BuildAutomaton_131())
    sub_automata.append(_BuildAutomaton_132())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 250, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctNavigationInterfaceSettings._Automaton = _BuildAutomaton_127()




ctNavIfPlatformsList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfPlatform'), ctNavIfPlatform, scope=ctNavIfPlatformsList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 261, 6)))

def _BuildAutomaton_133 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_133
    del _BuildAutomaton_133
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=6, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 260, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavIfPlatformsList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfPlatform')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 261, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctNavIfPlatformsList._Automaton = _BuildAutomaton_133()




ctNavIfPlatform._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfUserPlatformNumber'), stIntUserPlatformNumber, scope=ctNavIfPlatform, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 267, 6)))

ctNavIfPlatform._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfRtAddress'), stIntNavIfRtAddress, scope=ctNavIfPlatform, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 268, 6)))

ctNavIfPlatform._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfRtSubAddress'), stIntNavIfRtSubAddress, scope=ctNavIfPlatform, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 269, 6)))

ctNavIfPlatform._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NavIfTransferDirection'), stEnumNavIfTransferDirection, scope=ctNavIfPlatform, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 270, 6)))

def _BuildAutomaton_135 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_135
    del _BuildAutomaton_135
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 267, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavIfPlatform._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfUserPlatformNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 267, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_136 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_136
    del _BuildAutomaton_136
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 268, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavIfPlatform._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfRtAddress')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 268, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_137 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_137
    del _BuildAutomaton_137
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 269, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavIfPlatform._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfRtSubAddress')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 269, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_138 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_138
    del _BuildAutomaton_138
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 270, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctNavIfPlatform._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NavIfTransferDirection')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 270, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_134 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_134
    del _BuildAutomaton_134
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 267, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 268, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 269, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 270, 6))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_135())
    sub_automata.append(_BuildAutomaton_136())
    sub_automata.append(_BuildAutomaton_137())
    sub_automata.append(_BuildAutomaton_138())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 266, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctNavIfPlatform._Automaton = _BuildAutomaton_134()




ctSituationDisplayDataList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplaySettings'), ctSituationDisplaySettings, scope=ctSituationDisplayDataList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 276, 6)))

def _BuildAutomaton_139 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_139
    del _BuildAutomaton_139
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 275, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplayDataList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplaySettings')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 276, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctSituationDisplayDataList._Automaton = _BuildAutomaton_139()




ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayServer'), stIntDisplayServer, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 282, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayId'), stIntDisplayId, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 283, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayVisibility'), stBoolDisplayVisibility, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 284, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayCenter'), stEnumSituationDisplayCenterKind, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 285, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Center'), ctPoint, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 286, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayMode'), stEnumSituationDisplayModeKind, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 287, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayScale'), stDoubleDisplayScale, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 288, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayIntensity'), stDoubleDisplayIntensity, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 289, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VelocityVectorDuration'), stDoubleVelocityVectorDuration, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 290, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayTerrain'), stBoolDisplayTerrain, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 291, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoughness'), stBoolDisplayRoughness, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 292, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayGeopolitical'), stBoolDisplayGeopolitical, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 293, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLatitude'), stDoubleGeopoliticalCenterLatitude, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 294, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLongitude'), stDoubleGeopoliticalCenterLongitude, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 295, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayBarriers'), stBoolDisplayBarriers, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 296, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayCoastline'), stBoolDisplayCoastline, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 297, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayDepthLines'), stBoolDisplayDepthLines, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 298, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPoliticalLines'), stBoolDisplayPoliticalLines, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 299, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayCanals'), stBoolDisplayCanals, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 300, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayWaterways'), stBoolDisplayWaterways, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 301, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayLandforms'), stBoolDisplayLandforms, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 302, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayRailroads'), stBoolDisplayRailroads, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 303, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoads'), stBoolDisplayRoads, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 304, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayTrails'), stBoolDisplayTrails, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 305, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayStructures'), stBoolDisplayStructures, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 306, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPipelines'), stBoolDisplayPipelines, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 307, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayUtilities'), stBoolDisplayUtilities, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 308, 6)))

ctSituationDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptionsList'), ctSituationDisplayPlatformOptionsList, scope=ctSituationDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 309, 6)))

def _BuildAutomaton_141 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_141
    del _BuildAutomaton_141
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 282, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayServer')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 282, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_142 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_142
    del _BuildAutomaton_142
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 283, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayId')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 283, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_143 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_143
    del _BuildAutomaton_143
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 284, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayVisibility')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 284, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_144 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_144
    del _BuildAutomaton_144
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 285, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayCenter')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 285, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_145 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_145
    del _BuildAutomaton_145
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 286, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Center')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 286, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_146 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_146
    del _BuildAutomaton_146
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 287, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SituationDisplayMode')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 287, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_147 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_147
    del _BuildAutomaton_147
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 288, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayScale')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 288, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_148 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_148
    del _BuildAutomaton_148
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 289, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayIntensity')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 289, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_149 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_149
    del _BuildAutomaton_149
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 290, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'VelocityVectorDuration')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 290, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_150 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_150
    del _BuildAutomaton_150
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 291, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayTerrain')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 291, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_151 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_151
    del _BuildAutomaton_151
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 292, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoughness')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 292, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_152 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_152
    del _BuildAutomaton_152
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 293, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayGeopolitical')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 293, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_153 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_153
    del _BuildAutomaton_153
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 294, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLatitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 294, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_154 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_154
    del _BuildAutomaton_154
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 295, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLongitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 295, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_155 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_155
    del _BuildAutomaton_155
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 296, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayBarriers')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 296, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_156 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_156
    del _BuildAutomaton_156
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 297, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayCoastline')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 297, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_157 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_157
    del _BuildAutomaton_157
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 298, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayDepthLines')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 298, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_158 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_158
    del _BuildAutomaton_158
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 299, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPoliticalLines')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 299, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_159 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_159
    del _BuildAutomaton_159
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 300, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayCanals')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 300, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_160 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_160
    del _BuildAutomaton_160
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 301, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayWaterways')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 301, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_161 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_161
    del _BuildAutomaton_161
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 302, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayLandforms')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 302, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_162 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_162
    del _BuildAutomaton_162
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 303, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayRailroads')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 303, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_163 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_163
    del _BuildAutomaton_163
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 304, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoads')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 304, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_164 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_164
    del _BuildAutomaton_164
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 305, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayTrails')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 305, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_165 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_165
    del _BuildAutomaton_165
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 306, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayStructures')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 306, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_166 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_166
    del _BuildAutomaton_166
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 307, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPipelines')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 307, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_167 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_167
    del _BuildAutomaton_167
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 308, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayUtilities')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 308, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_168 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_168
    del _BuildAutomaton_168
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 309, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptionsList')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 309, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_140 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_140
    del _BuildAutomaton_140
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 282, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 283, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 284, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 285, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 286, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 287, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 288, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 289, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 290, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 291, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 292, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 293, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 294, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 295, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 296, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 297, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 298, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 299, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 300, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 301, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 302, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 303, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 304, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 305, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 306, 6))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 307, 6))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 308, 6))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 309, 6))
    counters.add(cc_27)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_141())
    sub_automata.append(_BuildAutomaton_142())
    sub_automata.append(_BuildAutomaton_143())
    sub_automata.append(_BuildAutomaton_144())
    sub_automata.append(_BuildAutomaton_145())
    sub_automata.append(_BuildAutomaton_146())
    sub_automata.append(_BuildAutomaton_147())
    sub_automata.append(_BuildAutomaton_148())
    sub_automata.append(_BuildAutomaton_149())
    sub_automata.append(_BuildAutomaton_150())
    sub_automata.append(_BuildAutomaton_151())
    sub_automata.append(_BuildAutomaton_152())
    sub_automata.append(_BuildAutomaton_153())
    sub_automata.append(_BuildAutomaton_154())
    sub_automata.append(_BuildAutomaton_155())
    sub_automata.append(_BuildAutomaton_156())
    sub_automata.append(_BuildAutomaton_157())
    sub_automata.append(_BuildAutomaton_158())
    sub_automata.append(_BuildAutomaton_159())
    sub_automata.append(_BuildAutomaton_160())
    sub_automata.append(_BuildAutomaton_161())
    sub_automata.append(_BuildAutomaton_162())
    sub_automata.append(_BuildAutomaton_163())
    sub_automata.append(_BuildAutomaton_164())
    sub_automata.append(_BuildAutomaton_165())
    sub_automata.append(_BuildAutomaton_166())
    sub_automata.append(_BuildAutomaton_167())
    sub_automata.append(_BuildAutomaton_168())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 281, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctSituationDisplaySettings._Automaton = _BuildAutomaton_140()




ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplayMode'), stEnumGuiDisplayModeKind, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 315, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayGridKind'), stEnumDisplayGridKind, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 316, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplayCenter'), stEnumDisplayCenterKind, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 317, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Center'), ctPoint, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 318, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CenterPlatformNumber'), stIntUserPlatformNumber, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 319, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Scale'), stDoubleScale, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 320, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Intensity'), stDoubleIntensity, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 321, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VelocityVectorDuration'), stDoubleVelocityVectorDuration, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 322, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayHud'), stBoolDisplayHud, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 323, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPlatformDetails'), stBoolDisplayPlatformDetails, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 324, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayTerrainLegend'), stBoolDisplayTerrainLegend, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 325, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayGrids'), stBoolDisplayGrids, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 326, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayProjectedPath'), stBoolDisplayProjectedPath, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 327, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPathHistory'), stBoolDisplayPathHistory, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 328, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayInactivePlatforms'), stBoolDisplayInactivePlatforms, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 329, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplaySymbolLegend'), stBoolDisplaySymbolLegend, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 330, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoughnessLegend'), stBoolDisplayRoughnessLegend, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 331, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayVmapLegend'), stBoolDisplayVmapLegend, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 332, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TerrainEnable'), stBoolTerrainEnable, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 333, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RoughnessEnable'), stBoolRoughnessEnable, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 334, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'VmapEnable'), stBoolVmapEnable, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 335, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLatitude'), stDoubleGeopoliticalCenterLatitude, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 336, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLongitude'), stDoubleGeopoliticalCenterLongitude, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 337, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayBarriers'), stBoolDisplayBarriers, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 338, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayCoastline'), stBoolDisplayCoastline, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 339, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayDepthLines'), stBoolDisplayDepthLines, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 340, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPoliticalLines'), stBoolDisplayPoliticalLines, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 341, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayCanals'), stBoolDisplayCanals, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 342, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayWaterways'), stBoolDisplayWaterways, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 343, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayLandforms'), stBoolDisplayLandforms, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 344, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayRailroads'), stBoolDisplayRailroads, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 345, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoads'), stBoolDisplayRoads, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 346, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayTrails'), stBoolDisplayTrails, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 347, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayStructures'), stBoolDisplayStructures, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 348, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPipelines'), stBoolDisplayPipelines, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 349, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayUtilities'), stBoolDisplayUtilities, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 350, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeotiffEnable'), stBoolGeotiffEnable, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 351, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GeotiffPath'), stTextGeotiffPath, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 352, 6)))

ctGuiDisplaySettings._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptionsList'), ctGuiPlatformOptionsList, scope=ctGuiDisplaySettings, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 353, 6)))

def _BuildAutomaton_170 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_170
    del _BuildAutomaton_170
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 315, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplayMode')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 315, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_171 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_171
    del _BuildAutomaton_171
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 316, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayGridKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 316, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_172 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_172
    del _BuildAutomaton_172
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 317, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GuiDisplayCenter')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 317, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_173 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_173
    del _BuildAutomaton_173
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 318, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Center')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 318, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_174 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_174
    del _BuildAutomaton_174
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 319, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CenterPlatformNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 319, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_175 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_175
    del _BuildAutomaton_175
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 320, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Scale')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 320, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_176 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_176
    del _BuildAutomaton_176
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 321, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Intensity')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 321, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_177 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_177
    del _BuildAutomaton_177
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 322, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'VelocityVectorDuration')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 322, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_178 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_178
    del _BuildAutomaton_178
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 323, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayHud')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 323, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_179 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_179
    del _BuildAutomaton_179
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 324, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPlatformDetails')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 324, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_180 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_180
    del _BuildAutomaton_180
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 325, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayTerrainLegend')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 325, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_181 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_181
    del _BuildAutomaton_181
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 326, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayGrids')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 326, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_182 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_182
    del _BuildAutomaton_182
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 327, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayProjectedPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 327, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_183 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_183
    del _BuildAutomaton_183
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 328, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPathHistory')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 328, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_184 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_184
    del _BuildAutomaton_184
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 329, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayInactivePlatforms')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 329, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_185 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_185
    del _BuildAutomaton_185
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 330, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplaySymbolLegend')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 330, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_186 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_186
    del _BuildAutomaton_186
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 331, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoughnessLegend')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 331, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_187 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_187
    del _BuildAutomaton_187
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 332, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayVmapLegend')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 332, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_188 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_188
    del _BuildAutomaton_188
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 333, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TerrainEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 333, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_189 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_189
    del _BuildAutomaton_189
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 334, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RoughnessEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 334, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_190 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_190
    del _BuildAutomaton_190
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 335, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'VmapEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 335, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_191 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_191
    del _BuildAutomaton_191
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 336, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLatitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 336, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_192 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_192
    del _BuildAutomaton_192
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 337, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeopoliticalCenterLongitude')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 337, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_193 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_193
    del _BuildAutomaton_193
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 338, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayBarriers')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 338, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_194 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_194
    del _BuildAutomaton_194
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 339, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayCoastline')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 339, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_195 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_195
    del _BuildAutomaton_195
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 340, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayDepthLines')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 340, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_196 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_196
    del _BuildAutomaton_196
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 341, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPoliticalLines')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 341, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_197 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_197
    del _BuildAutomaton_197
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 342, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayCanals')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 342, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_198 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_198
    del _BuildAutomaton_198
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 343, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayWaterways')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 343, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_199 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_199
    del _BuildAutomaton_199
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 344, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayLandforms')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 344, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_200 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_200
    del _BuildAutomaton_200
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 345, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayRailroads')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 345, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_201 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_201
    del _BuildAutomaton_201
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 346, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayRoads')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 346, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_202 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_202
    del _BuildAutomaton_202
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 347, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayTrails')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 347, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_203 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_203
    del _BuildAutomaton_203
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 348, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayStructures')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 348, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_204 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_204
    del _BuildAutomaton_204
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 349, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPipelines')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 349, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_205 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_205
    del _BuildAutomaton_205
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 350, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayUtilities')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 350, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_206 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_206
    del _BuildAutomaton_206
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 351, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeotiffEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 351, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_207 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_207
    del _BuildAutomaton_207
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 352, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GeotiffPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 352, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_208 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_208
    del _BuildAutomaton_208
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 353, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiDisplaySettings._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptionsList')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 353, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_169 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_169
    del _BuildAutomaton_169
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 315, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 316, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 317, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 318, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 319, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 320, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 321, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 322, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 323, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 324, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 325, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 326, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 327, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 328, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 329, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 330, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 331, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 332, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 333, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 334, 6))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 335, 6))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 336, 6))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 337, 6))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 338, 6))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 339, 6))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 340, 6))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 341, 6))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 342, 6))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 343, 6))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 344, 6))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 345, 6))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 346, 6))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 347, 6))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 348, 6))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 349, 6))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 350, 6))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 351, 6))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 352, 6))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 353, 6))
    counters.add(cc_38)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_170())
    sub_automata.append(_BuildAutomaton_171())
    sub_automata.append(_BuildAutomaton_172())
    sub_automata.append(_BuildAutomaton_173())
    sub_automata.append(_BuildAutomaton_174())
    sub_automata.append(_BuildAutomaton_175())
    sub_automata.append(_BuildAutomaton_176())
    sub_automata.append(_BuildAutomaton_177())
    sub_automata.append(_BuildAutomaton_178())
    sub_automata.append(_BuildAutomaton_179())
    sub_automata.append(_BuildAutomaton_180())
    sub_automata.append(_BuildAutomaton_181())
    sub_automata.append(_BuildAutomaton_182())
    sub_automata.append(_BuildAutomaton_183())
    sub_automata.append(_BuildAutomaton_184())
    sub_automata.append(_BuildAutomaton_185())
    sub_automata.append(_BuildAutomaton_186())
    sub_automata.append(_BuildAutomaton_187())
    sub_automata.append(_BuildAutomaton_188())
    sub_automata.append(_BuildAutomaton_189())
    sub_automata.append(_BuildAutomaton_190())
    sub_automata.append(_BuildAutomaton_191())
    sub_automata.append(_BuildAutomaton_192())
    sub_automata.append(_BuildAutomaton_193())
    sub_automata.append(_BuildAutomaton_194())
    sub_automata.append(_BuildAutomaton_195())
    sub_automata.append(_BuildAutomaton_196())
    sub_automata.append(_BuildAutomaton_197())
    sub_automata.append(_BuildAutomaton_198())
    sub_automata.append(_BuildAutomaton_199())
    sub_automata.append(_BuildAutomaton_200())
    sub_automata.append(_BuildAutomaton_201())
    sub_automata.append(_BuildAutomaton_202())
    sub_automata.append(_BuildAutomaton_203())
    sub_automata.append(_BuildAutomaton_204())
    sub_automata.append(_BuildAutomaton_205())
    sub_automata.append(_BuildAutomaton_206())
    sub_automata.append(_BuildAutomaton_207())
    sub_automata.append(_BuildAutomaton_208())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 314, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctGuiDisplaySettings._Automaton = _BuildAutomaton_169()




ctSituationDisplayPlatformOptionsList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptions'), ctSituationDisplayPlatformOptions, scope=ctSituationDisplayPlatformOptionsList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 359, 6)))

def _BuildAutomaton_209 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_209
    del _BuildAutomaton_209
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 358, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplayPlatformOptionsList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptions')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 359, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctSituationDisplayPlatformOptionsList._Automaton = _BuildAutomaton_209()




ctSituationDisplayPlatformOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformNumber'), stIntUserPlatformNumber, scope=ctSituationDisplayPlatformOptions, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 365, 6)))

ctSituationDisplayPlatformOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPlatform'), stBoolDisplayPlatform, scope=ctSituationDisplayPlatformOptions, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 366, 6)))

ctSituationDisplayPlatformOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPath'), stBoolDisplayPath, scope=ctSituationDisplayPlatformOptions, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 367, 6)))

def _BuildAutomaton_211 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_211
    del _BuildAutomaton_211
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 365, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplayPlatformOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 365, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_212 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_212
    del _BuildAutomaton_212
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 366, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplayPlatformOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPlatform')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 366, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_213 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_213
    del _BuildAutomaton_213
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 367, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctSituationDisplayPlatformOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 367, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_210 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_210
    del _BuildAutomaton_210
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 365, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 366, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 367, 6))
    counters.add(cc_2)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_211())
    sub_automata.append(_BuildAutomaton_212())
    sub_automata.append(_BuildAutomaton_213())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 364, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctSituationDisplayPlatformOptions._Automaton = _BuildAutomaton_210()




ctGuiPlatformOptionsList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptions'), ctGuiPlatformOptions, scope=ctGuiPlatformOptionsList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 373, 6)))

def _BuildAutomaton_214 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_214
    del _BuildAutomaton_214
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 372, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiPlatformOptionsList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformDisplayOptions')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 373, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctGuiPlatformOptionsList._Automaton = _BuildAutomaton_214()




ctGuiPlatformOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformNumber'), stIntUserPlatformNumber, scope=ctGuiPlatformOptions, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 379, 6)))

ctGuiPlatformOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplaySymbol'), stBoolDisplaySymbol, scope=ctGuiPlatformOptions, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 380, 6)))

ctGuiPlatformOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayPathHistory'), stBoolDisplayPathHistory, scope=ctGuiPlatformOptions, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 381, 6)))

ctGuiPlatformOptions._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DisplayProjectedPath'), stBoolDisplayProjectedPath, scope=ctGuiPlatformOptions, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 382, 6)))

def _BuildAutomaton_216 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_216
    del _BuildAutomaton_216
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 379, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiPlatformOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 379, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_217 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_217
    del _BuildAutomaton_217
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 380, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiPlatformOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplaySymbol')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 380, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_218 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_218
    del _BuildAutomaton_218
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 381, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiPlatformOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayPathHistory')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 381, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_219 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_219
    del _BuildAutomaton_219
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 382, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctGuiPlatformOptions._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DisplayProjectedPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 382, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_215 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_215
    del _BuildAutomaton_215
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 379, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 380, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 381, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 382, 6))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_216())
    sub_automata.append(_BuildAutomaton_217())
    sub_automata.append(_BuildAutomaton_218())
    sub_automata.append(_BuildAutomaton_219())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/scenarioDataR1-1.xsd', 378, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctGuiPlatformOptions._Automaton = _BuildAutomaton_215()

