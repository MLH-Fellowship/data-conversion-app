# ./data/ceesim/schema/simulation/platformScriptDataR1_1/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:32:46.696253 by PyXB version 1.2.6 using Python 3.6.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4b5467e0-715f-11eb-ae2a-00155debab14')

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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolCoupledMotionEnable
class stBoolCoupledMotionEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolCoupledMotionEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 193, 2)
    _Documentation = ''
stBoolCoupledMotionEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolCoupledMotionEnable', stBoolCoupledMotionEnable)
_module_typeBindings.stBoolCoupledMotionEnable = stBoolCoupledMotionEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDeactivate
class stBoolDeactivate (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDeactivate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 202, 2)
    _Documentation = ''
stBoolDeactivate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDeactivate', stBoolDeactivate)
_module_typeBindings.stBoolDeactivate = stBoolDeactivate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolFirstSegmentOnPath
class stBoolFirstSegmentOnPath (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolFirstSegmentOnPath')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 211, 2)
    _Documentation = ''
stBoolFirstSegmentOnPath._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolFirstSegmentOnPath', stBoolFirstSegmentOnPath)
_module_typeBindings.stBoolFirstSegmentOnPath = stBoolFirstSegmentOnPath

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolLimitDurationFlag
class stBoolLimitDurationFlag (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolLimitDurationFlag')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 220, 2)
    _Documentation = ''
stBoolLimitDurationFlag._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolLimitDurationFlag', stBoolLimitDurationFlag)
_module_typeBindings.stBoolLimitDurationFlag = stBoolLimitDurationFlag

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolTargetSutFlag
class stBoolTargetSutFlag (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolTargetSutFlag')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 229, 2)
    _Documentation = ''
stBoolTargetSutFlag._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolTargetSutFlag', stBoolTargetSutFlag)
_module_typeBindings.stBoolTargetSutFlag = stBoolTargetSutFlag

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBankAngle
class stDoubleBankAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBankAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 238, 2)
    _Documentation = ''
stDoubleBankAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBankAngle, value=pyxb.binding.datatypes.double(-90.0))
stDoubleBankAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBankAngle, value=pyxb.binding.datatypes.double(90.0))
stDoubleBankAngle._InitializeFacetMap(stDoubleBankAngle._CF_minInclusive,
   stDoubleBankAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBankAngle', stDoubleBankAngle)
_module_typeBindings.stDoubleBankAngle = stDoubleBankAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleClimbAngle
class stDoubleClimbAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleClimbAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 250, 2)
    _Documentation = ''
stDoubleClimbAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleClimbAngle, value=pyxb.binding.datatypes.double(-90.0))
stDoubleClimbAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleClimbAngle, value=pyxb.binding.datatypes.double(90.0))
stDoubleClimbAngle._InitializeFacetMap(stDoubleClimbAngle._CF_minInclusive,
   stDoubleClimbAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleClimbAngle', stDoubleClimbAngle)
_module_typeBindings.stDoubleClimbAngle = stDoubleClimbAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDuration
class stDoubleDuration (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDuration')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 262, 2)
    _Documentation = ''
stDoubleDuration._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDuration, value=pyxb.binding.datatypes.double(2.0))
stDoubleDuration._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDuration, value=pyxb.binding.datatypes.double(3600.0))
stDoubleDuration._InitializeFacetMap(stDoubleDuration._CF_minInclusive,
   stDoubleDuration._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDuration', stDoubleDuration)
_module_typeBindings.stDoubleDuration = stDoubleDuration

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndPitch
class stDoubleEndPitch (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndPitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 274, 2)
    _Documentation = ''
stDoubleEndPitch._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndPitch, value=pyxb.binding.datatypes.double(-180.0))
stDoubleEndPitch._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndPitch, value=pyxb.binding.datatypes.double(180.0))
stDoubleEndPitch._InitializeFacetMap(stDoubleEndPitch._CF_minInclusive,
   stDoubleEndPitch._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndPitch', stDoubleEndPitch)
_module_typeBindings.stDoubleEndPitch = stDoubleEndPitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndPitchRate
class stDoubleEndPitchRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndPitchRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 286, 2)
    _Documentation = ''
stDoubleEndPitchRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndPitchRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleEndPitchRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndPitchRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleEndPitchRate._InitializeFacetMap(stDoubleEndPitchRate._CF_minInclusive,
   stDoubleEndPitchRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndPitchRate', stDoubleEndPitchRate)
_module_typeBindings.stDoubleEndPitchRate = stDoubleEndPitchRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndRoll
class stDoubleEndRoll (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndRoll')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 298, 2)
    _Documentation = ''
stDoubleEndRoll._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndRoll, value=pyxb.binding.datatypes.double(-180.0))
stDoubleEndRoll._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndRoll, value=pyxb.binding.datatypes.double(180.0))
stDoubleEndRoll._InitializeFacetMap(stDoubleEndRoll._CF_minInclusive,
   stDoubleEndRoll._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndRoll', stDoubleEndRoll)
_module_typeBindings.stDoubleEndRoll = stDoubleEndRoll

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndRollRate
class stDoubleEndRollRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndRollRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 310, 2)
    _Documentation = ''
stDoubleEndRollRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndRollRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleEndRollRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndRollRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleEndRollRate._InitializeFacetMap(stDoubleEndRollRate._CF_minInclusive,
   stDoubleEndRollRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndRollRate', stDoubleEndRollRate)
_module_typeBindings.stDoubleEndRollRate = stDoubleEndRollRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndSpeed
class stDoubleEndSpeed (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndSpeed')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 322, 2)
    _Documentation = ''
stDoubleEndSpeed._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndSpeed, value=pyxb.binding.datatypes.double(0.0))
stDoubleEndSpeed._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndSpeed, value=pyxb.binding.datatypes.double(2777.77777777778))
stDoubleEndSpeed._InitializeFacetMap(stDoubleEndSpeed._CF_minInclusive,
   stDoubleEndSpeed._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndSpeed', stDoubleEndSpeed)
_module_typeBindings.stDoubleEndSpeed = stDoubleEndSpeed

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndYaw
class stDoubleEndYaw (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndYaw')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 334, 2)
    _Documentation = ''
stDoubleEndYaw._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndYaw, value=pyxb.binding.datatypes.double(-180.0))
stDoubleEndYaw._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndYaw, value=pyxb.binding.datatypes.double(180.0))
stDoubleEndYaw._InitializeFacetMap(stDoubleEndYaw._CF_minInclusive,
   stDoubleEndYaw._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndYaw', stDoubleEndYaw)
_module_typeBindings.stDoubleEndYaw = stDoubleEndYaw

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndYawRate
class stDoubleEndYawRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndYawRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 346, 2)
    _Documentation = ''
stDoubleEndYawRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndYawRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleEndYawRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndYawRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleEndYawRate._InitializeFacetMap(stDoubleEndYawRate._CF_minInclusive,
   stDoubleEndYawRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndYawRate', stDoubleEndYawRate)
_module_typeBindings.stDoubleEndYawRate = stDoubleEndYawRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleHeading
class stDoubleHeading (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleHeading')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 358, 2)
    _Documentation = ''
stDoubleHeading._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleHeading, value=pyxb.binding.datatypes.double(-180.0))
stDoubleHeading._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleHeading, value=pyxb.binding.datatypes.double(180.0))
stDoubleHeading._InitializeFacetMap(stDoubleHeading._CF_minInclusive,
   stDoubleHeading._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleHeading', stDoubleHeading)
_module_typeBindings.stDoubleHeading = stDoubleHeading

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLoadFactor
class stDoubleLoadFactor (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLoadFactor')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 370, 2)
    _Documentation = ''
stDoubleLoadFactor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLoadFactor, value=pyxb.binding.datatypes.double(0.0))
stDoubleLoadFactor._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLoadFactor, value=pyxb.binding.datatypes.double(100.0))
stDoubleLoadFactor._InitializeFacetMap(stDoubleLoadFactor._CF_minInclusive,
   stDoubleLoadFactor._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLoadFactor', stDoubleLoadFactor)
_module_typeBindings.stDoubleLoadFactor = stDoubleLoadFactor

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePitchRate
class stDoublePitchRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePitchRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 382, 2)
    _Documentation = ''
stDoublePitchRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePitchRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoublePitchRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePitchRate, value=pyxb.binding.datatypes.double(1000.0))
stDoublePitchRate._InitializeFacetMap(stDoublePitchRate._CF_minInclusive,
   stDoublePitchRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePitchRate', stDoublePitchRate)
_module_typeBindings.stDoublePitchRate = stDoublePitchRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleRange
class stDoubleRange (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleRange')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 394, 2)
    _Documentation = ''
stDoubleRange._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleRange, value=pyxb.binding.datatypes.double(10.0))
stDoubleRange._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleRange, value=pyxb.binding.datatypes.double(20000.0))
stDoubleRange._InitializeFacetMap(stDoubleRange._CF_minInclusive,
   stDoubleRange._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleRange', stDoubleRange)
_module_typeBindings.stDoubleRange = stDoubleRange

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleRollRate
class stDoubleRollRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleRollRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 406, 2)
    _Documentation = ''
stDoubleRollRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleRollRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleRollRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleRollRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleRollRate._InitializeFacetMap(stDoubleRollRate._CF_minInclusive,
   stDoubleRollRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleRollRate', stDoubleRollRate)
_module_typeBindings.stDoubleRollRate = stDoubleRollRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSpeed
class stDoubleSpeed (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSpeed')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 418, 2)
    _Documentation = ''
stDoubleSpeed._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSpeed, value=pyxb.binding.datatypes.double(0.277777))
stDoubleSpeed._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSpeed, value=pyxb.binding.datatypes.double(2777.777777))
stDoubleSpeed._InitializeFacetMap(stDoubleSpeed._CF_minInclusive,
   stDoubleSpeed._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSpeed', stDoubleSpeed)
_module_typeBindings.stDoubleSpeed = stDoubleSpeed

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartPitch
class stDoubleStartPitch (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartPitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 430, 2)
    _Documentation = ''
stDoubleStartPitch._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartPitch, value=pyxb.binding.datatypes.double(-180.0))
stDoubleStartPitch._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartPitch, value=pyxb.binding.datatypes.double(180.0))
stDoubleStartPitch._InitializeFacetMap(stDoubleStartPitch._CF_minInclusive,
   stDoubleStartPitch._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartPitch', stDoubleStartPitch)
_module_typeBindings.stDoubleStartPitch = stDoubleStartPitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartRoll
class stDoubleStartRoll (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartRoll')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 442, 2)
    _Documentation = ''
stDoubleStartRoll._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartRoll, value=pyxb.binding.datatypes.double(-180.0))
stDoubleStartRoll._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartRoll, value=pyxb.binding.datatypes.double(180.0))
stDoubleStartRoll._InitializeFacetMap(stDoubleStartRoll._CF_minInclusive,
   stDoubleStartRoll._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartRoll', stDoubleStartRoll)
_module_typeBindings.stDoubleStartRoll = stDoubleStartRoll

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartSpeed
class stDoubleStartSpeed (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartSpeed')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 454, 2)
    _Documentation = ''
stDoubleStartSpeed._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartSpeed, value=pyxb.binding.datatypes.double(0.0))
stDoubleStartSpeed._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartSpeed, value=pyxb.binding.datatypes.double(2777.77777777778))
stDoubleStartSpeed._InitializeFacetMap(stDoubleStartSpeed._CF_minInclusive,
   stDoubleStartSpeed._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartSpeed', stDoubleStartSpeed)
_module_typeBindings.stDoubleStartSpeed = stDoubleStartSpeed

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartTime
class stDoubleStartTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 466, 2)
    _Documentation = ''
stDoubleStartTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleStartTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartTime, value=pyxb.binding.datatypes.double(86400.0))
stDoubleStartTime._InitializeFacetMap(stDoubleStartTime._CF_minInclusive,
   stDoubleStartTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartTime', stDoubleStartTime)
_module_typeBindings.stDoubleStartTime = stDoubleStartTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartYaw
class stDoubleStartYaw (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartYaw')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 478, 2)
    _Documentation = ''
stDoubleStartYaw._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartYaw, value=pyxb.binding.datatypes.double(-180.0))
stDoubleStartYaw._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartYaw, value=pyxb.binding.datatypes.double(180.0))
stDoubleStartYaw._InitializeFacetMap(stDoubleStartYaw._CF_minInclusive,
   stDoubleStartYaw._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartYaw', stDoubleStartYaw)
_module_typeBindings.stDoubleStartYaw = stDoubleStartYaw

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleYawRate
class stDoubleYawRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleYawRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 490, 2)
    _Documentation = ''
stDoubleYawRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleYawRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleYawRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleYawRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleYawRate._InitializeFacetMap(stDoubleYawRate._CF_minInclusive,
   stDoubleYawRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleYawRate', stDoubleYawRate)
_module_typeBindings.stDoubleYawRate = stDoubleYawRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumAltitudeKind
class stEnumAltitudeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumAltitudeKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 502, 2)
    _Documentation = ''
stEnumAltitudeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumAltitudeKind, enum_prefix=None)
stEnumAltitudeKind.Km_Above_Sea_Level = stEnumAltitudeKind._CF_enumeration.addEnumeration(unicode_value='Km_Above_Sea_Level', tag='Km_Above_Sea_Level')
stEnumAltitudeKind.Km_Above_Terrain = stEnumAltitudeKind._CF_enumeration.addEnumeration(unicode_value='Km_Above_Terrain', tag='Km_Above_Terrain')
stEnumAltitudeKind._InitializeFacetMap(stEnumAltitudeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumAltitudeKind', stEnumAltitudeKind)
_module_typeBindings.stEnumAltitudeKind = stEnumAltitudeKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumEndActionKind
class stEnumEndActionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumEndActionKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 514, 2)
    _Documentation = ''
stEnumEndActionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumEndActionKind, enum_prefix=None)
stEnumEndActionKind.Continue_In_Final_Direction = stEnumEndActionKind._CF_enumeration.addEnumeration(unicode_value='Continue_In_Final_Direction', tag='Continue_In_Final_Direction')
stEnumEndActionKind.Stop = stEnumEndActionKind._CF_enumeration.addEnumeration(unicode_value='Stop', tag='Stop')
stEnumEndActionKind.Deactivate = stEnumEndActionKind._CF_enumeration.addEnumeration(unicode_value='Deactivate', tag='Deactivate')
stEnumEndActionKind._InitializeFacetMap(stEnumEndActionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumEndActionKind', stEnumEndActionKind)
_module_typeBindings.stEnumEndActionKind = stEnumEndActionKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumInterceptKind
class stEnumInterceptKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumInterceptKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 527, 2)
    _Documentation = ''
stEnumInterceptKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumInterceptKind, enum_prefix=None)
stEnumInterceptKind.Constant_Speed = stEnumInterceptKind._CF_enumeration.addEnumeration(unicode_value='Constant_Speed', tag='Constant_Speed')
stEnumInterceptKind.Time_Based = stEnumInterceptKind._CF_enumeration.addEnumeration(unicode_value='Time_Based', tag='Time_Based')
stEnumInterceptKind._InitializeFacetMap(stEnumInterceptKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumInterceptKind', stEnumInterceptKind)
_module_typeBindings.stEnumInterceptKind = stEnumInterceptKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPitchKind
class stEnumPitchKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPitchKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 539, 2)
    _Documentation = ''
stEnumPitchKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPitchKind, enum_prefix=None)
stEnumPitchKind.Absolute = stEnumPitchKind._CF_enumeration.addEnumeration(unicode_value='Absolute', tag='Absolute')
stEnumPitchKind.Relative = stEnumPitchKind._CF_enumeration.addEnumeration(unicode_value='Relative', tag='Relative')
stEnumPitchKind._InitializeFacetMap(stEnumPitchKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPitchKind', stEnumPitchKind)
_module_typeBindings.stEnumPitchKind = stEnumPitchKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumTurnKind
class stEnumTurnKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumTurnKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 551, 2)
    _Documentation = ''
stEnumTurnKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumTurnKind, enum_prefix=None)
stEnumTurnKind.Load_Factor = stEnumTurnKind._CF_enumeration.addEnumeration(unicode_value='Load_Factor', tag='Load_Factor')
stEnumTurnKind.Radius = stEnumTurnKind._CF_enumeration.addEnumeration(unicode_value='Radius', tag='Radius')
stEnumTurnKind._InitializeFacetMap(stEnumTurnKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumTurnKind', stEnumTurnKind)
_module_typeBindings.stEnumTurnKind = stEnumTurnKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntTargetPlatformNumber
class stIntTargetPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntTargetPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 563, 2)
    _Documentation = ''
stIntTargetPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntTargetPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntTargetPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntTargetPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntTargetPlatformNumber._InitializeFacetMap(stIntTargetPlatformNumber._CF_minInclusive,
   stIntTargetPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntTargetPlatformNumber', stIntTargetPlatformNumber)
_module_typeBindings.stIntTargetPlatformNumber = stIntTargetPlatformNumber

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


# Complex type {http://www.amherst.com/CEESIM/XML}ctPlatformScriptEventList with content type ELEMENT_ONLY
class ctPlatformScriptEventList (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPlatformScriptEventList with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPlatformScriptEventList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 42, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformScriptEvent uses Python identifier PlatformScriptEvent
    __PlatformScriptEvent = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformScriptEvent'), 'PlatformScriptEvent', '__httpwww_amherst_comCEESIMXML_ctPlatformScriptEventList_httpwww_amherst_comCEESIMXMLPlatformScriptEvent', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 44, 6), )

    
    PlatformScriptEvent = property(__PlatformScriptEvent.value, __PlatformScriptEvent.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctPlatformScriptEventList_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 46, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 46, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __PlatformScriptEvent.name() : __PlatformScriptEvent
    })
    _AttributeMap.update({
        __PerId.name() : __PerId
    })
_module_typeBindings.ctPlatformScriptEventList = ctPlatformScriptEventList
Namespace.addCategoryObject('typeBinding', 'ctPlatformScriptEventList', ctPlatformScriptEventList)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPlatformScriptEvent with content type ELEMENT_ONLY
class ctPlatformScriptEvent (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPlatformScriptEvent with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPlatformScriptEvent')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 49, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}StartTime uses Python identifier StartTime
    __StartTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), 'StartTime', '__httpwww_amherst_comCEESIMXML_ctPlatformScriptEvent_httpwww_amherst_comCEESIMXMLStartTime', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 51, 6), )

    
    StartTime = property(__StartTime.value, __StartTime.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Deactivate uses Python identifier Deactivate
    __Deactivate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Deactivate'), 'Deactivate', '__httpwww_amherst_comCEESIMXML_ctPlatformScriptEvent_httpwww_amherst_comCEESIMXMLDeactivate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 52, 6), )

    
    Deactivate = property(__Deactivate.value, __Deactivate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Segment uses Python identifier Segment
    __Segment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Segment'), 'Segment', '__httpwww_amherst_comCEESIMXML_ctPlatformScriptEvent_httpwww_amherst_comCEESIMXMLSegment', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 53, 6), )

    
    Segment = property(__Segment.value, __Segment.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Intercept uses Python identifier Intercept
    __Intercept = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Intercept'), 'Intercept', '__httpwww_amherst_comCEESIMXML_ctPlatformScriptEvent_httpwww_amherst_comCEESIMXMLIntercept', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 54, 6), )

    
    Intercept = property(__Intercept.value, __Intercept.set, None, None)

    _ElementMap.update({
        __StartTime.name() : __StartTime,
        __Deactivate.name() : __Deactivate,
        __Segment.name() : __Segment,
        __Intercept.name() : __Intercept
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPlatformScriptEvent = ctPlatformScriptEvent
Namespace.addCategoryObject('typeBinding', 'ctPlatformScriptEvent', ctPlatformScriptEvent)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPathSegment with content type ELEMENT_ONLY
class ctPathSegment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPathSegment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPathSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 58, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Point uses Python identifier Point
    __Point = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Point'), 'Point', '__httpwww_amherst_comCEESIMXML_ctPathSegment_httpwww_amherst_comCEESIMXMLPoint', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 60, 6), )

    
    Point = property(__Point.value, __Point.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Line uses Python identifier Line
    __Line = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Line'), 'Line', '__httpwww_amherst_comCEESIMXML_ctPathSegment_httpwww_amherst_comCEESIMXMLLine', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 61, 6), )

    
    Line = property(__Line.value, __Line.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Arc uses Python identifier Arc
    __Arc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Arc'), 'Arc', '__httpwww_amherst_comCEESIMXML_ctPathSegment_httpwww_amherst_comCEESIMXMLArc', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 62, 6), )

    
    Arc = property(__Arc.value, __Arc.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Compound uses Python identifier Compound
    __Compound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Compound'), 'Compound', '__httpwww_amherst_comCEESIMXML_ctPathSegment_httpwww_amherst_comCEESIMXMLCompound', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 63, 6), )

    
    Compound = property(__Compound.value, __Compound.set, None, None)

    _ElementMap.update({
        __Point.name() : __Point,
        __Line.name() : __Line,
        __Arc.name() : __Arc,
        __Compound.name() : __Compound
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPathSegment = ctPathSegment
Namespace.addCategoryObject('typeBinding', 'ctPathSegment', ctPathSegment)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPointSegment with content type ELEMENT_ONLY
class ctPointSegment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPointSegment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPointSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 67, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}AltitudeKind uses Python identifier AltitudeKind
    __AltitudeKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind'), 'AltitudeKind', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLAltitudeKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 69, 6), )

    
    AltitudeKind = property(__AltitudeKind.value, __AltitudeKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}FirstSegmentOnPath uses Python identifier FirstSegmentOnPath
    __FirstSegmentOnPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath'), 'FirstSegmentOnPath', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLFirstSegmentOnPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 70, 6), )

    
    FirstSegmentOnPath = property(__FirstSegmentOnPath.value, __FirstSegmentOnPath.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartPoint uses Python identifier StartPoint
    __StartPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartPoint'), 'StartPoint', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLStartPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 71, 6), )

    
    StartPoint = property(__StartPoint.value, __StartPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}CoupledMotionEnable uses Python identifier CoupledMotionEnable
    __CoupledMotionEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CoupledMotionEnable'), 'CoupledMotionEnable', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLCoupledMotionEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 72, 6), )

    
    CoupledMotionEnable = property(__CoupledMotionEnable.value, __CoupledMotionEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartRoll uses Python identifier StartRoll
    __StartRoll = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartRoll'), 'StartRoll', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLStartRoll', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 73, 6), )

    
    StartRoll = property(__StartRoll.value, __StartRoll.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartPitch uses Python identifier StartPitch
    __StartPitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartPitch'), 'StartPitch', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLStartPitch', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 74, 6), )

    
    StartPitch = property(__StartPitch.value, __StartPitch.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartYaw uses Python identifier StartYaw
    __StartYaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartYaw'), 'StartYaw', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLStartYaw', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 75, 6), )

    
    StartYaw = property(__StartYaw.value, __StartYaw.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RollRate uses Python identifier RollRate
    __RollRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RollRate'), 'RollRate', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLRollRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 76, 6), )

    
    RollRate = property(__RollRate.value, __RollRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PitchRate uses Python identifier PitchRate
    __PitchRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PitchRate'), 'PitchRate', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLPitchRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 77, 6), )

    
    PitchRate = property(__PitchRate.value, __PitchRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}YawRate uses Python identifier YawRate
    __YawRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'YawRate'), 'YawRate', '__httpwww_amherst_comCEESIMXML_ctPointSegment_httpwww_amherst_comCEESIMXMLYawRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 78, 6), )

    
    YawRate = property(__YawRate.value, __YawRate.set, None, None)

    _ElementMap.update({
        __AltitudeKind.name() : __AltitudeKind,
        __FirstSegmentOnPath.name() : __FirstSegmentOnPath,
        __StartPoint.name() : __StartPoint,
        __CoupledMotionEnable.name() : __CoupledMotionEnable,
        __StartRoll.name() : __StartRoll,
        __StartPitch.name() : __StartPitch,
        __StartYaw.name() : __StartYaw,
        __RollRate.name() : __RollRate,
        __PitchRate.name() : __PitchRate,
        __YawRate.name() : __YawRate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPointSegment = ctPointSegment
Namespace.addCategoryObject('typeBinding', 'ctPointSegment', ctPointSegment)


# Complex type {http://www.amherst.com/CEESIM/XML}ctLineSegment with content type ELEMENT_ONLY
class ctLineSegment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctLineSegment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctLineSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 82, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}AltitudeKind uses Python identifier AltitudeKind
    __AltitudeKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind'), 'AltitudeKind', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLAltitudeKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 84, 6), )

    
    AltitudeKind = property(__AltitudeKind.value, __AltitudeKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}FirstSegmentOnPath uses Python identifier FirstSegmentOnPath
    __FirstSegmentOnPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath'), 'FirstSegmentOnPath', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLFirstSegmentOnPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 85, 6), )

    
    FirstSegmentOnPath = property(__FirstSegmentOnPath.value, __FirstSegmentOnPath.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartPoint uses Python identifier StartPoint
    __StartPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartPoint'), 'StartPoint', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLStartPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 87, 6), )

    
    StartPoint = property(__StartPoint.value, __StartPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndPoint uses Python identifier EndPoint
    __EndPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndPoint'), 'EndPoint', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLEndPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 88, 6), )

    
    EndPoint = property(__EndPoint.value, __EndPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}CoupledMotionEnable uses Python identifier CoupledMotionEnable
    __CoupledMotionEnable = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CoupledMotionEnable'), 'CoupledMotionEnable', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLCoupledMotionEnable', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 89, 6), )

    
    CoupledMotionEnable = property(__CoupledMotionEnable.value, __CoupledMotionEnable.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartRoll uses Python identifier StartRoll
    __StartRoll = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartRoll'), 'StartRoll', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLStartRoll', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 91, 6), )

    
    StartRoll = property(__StartRoll.value, __StartRoll.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartPitch uses Python identifier StartPitch
    __StartPitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartPitch'), 'StartPitch', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLStartPitch', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 92, 6), )

    
    StartPitch = property(__StartPitch.value, __StartPitch.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartYaw uses Python identifier StartYaw
    __StartYaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartYaw'), 'StartYaw', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLStartYaw', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 93, 6), )

    
    StartYaw = property(__StartYaw.value, __StartYaw.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndRoll uses Python identifier EndRoll
    __EndRoll = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndRoll'), 'EndRoll', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLEndRoll', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 95, 6), )

    
    EndRoll = property(__EndRoll.value, __EndRoll.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndPitch uses Python identifier EndPitch
    __EndPitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndPitch'), 'EndPitch', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLEndPitch', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 96, 6), )

    
    EndPitch = property(__EndPitch.value, __EndPitch.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndYaw uses Python identifier EndYaw
    __EndYaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndYaw'), 'EndYaw', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLEndYaw', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 97, 6), )

    
    EndYaw = property(__EndYaw.value, __EndYaw.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RollRate uses Python identifier RollRate
    __RollRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RollRate'), 'RollRate', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLRollRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 99, 6), )

    
    RollRate = property(__RollRate.value, __RollRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PitchRate uses Python identifier PitchRate
    __PitchRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PitchRate'), 'PitchRate', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLPitchRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 100, 6), )

    
    PitchRate = property(__PitchRate.value, __PitchRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}YawRate uses Python identifier YawRate
    __YawRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'YawRate'), 'YawRate', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLYawRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 101, 6), )

    
    YawRate = property(__YawRate.value, __YawRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndRollRate uses Python identifier EndRollRate
    __EndRollRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndRollRate'), 'EndRollRate', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLEndRollRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 103, 6), )

    
    EndRollRate = property(__EndRollRate.value, __EndRollRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndPitchRate uses Python identifier EndPitchRate
    __EndPitchRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndPitchRate'), 'EndPitchRate', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLEndPitchRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 104, 6), )

    
    EndPitchRate = property(__EndPitchRate.value, __EndPitchRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndYawRate uses Python identifier EndYawRate
    __EndYawRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndYawRate'), 'EndYawRate', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLEndYawRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 105, 6), )

    
    EndYawRate = property(__EndYawRate.value, __EndYawRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartSpeed uses Python identifier StartSpeed
    __StartSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed'), 'StartSpeed', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLStartSpeed', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 107, 6), )

    
    StartSpeed = property(__StartSpeed.value, __StartSpeed.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndSpeed uses Python identifier EndSpeed
    __EndSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed'), 'EndSpeed', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLEndSpeed', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 108, 6), )

    
    EndSpeed = property(__EndSpeed.value, __EndSpeed.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PitchKind uses Python identifier PitchKind
    __PitchKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PitchKind'), 'PitchKind', '__httpwww_amherst_comCEESIMXML_ctLineSegment_httpwww_amherst_comCEESIMXMLPitchKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 109, 6), )

    
    PitchKind = property(__PitchKind.value, __PitchKind.set, None, None)

    _ElementMap.update({
        __AltitudeKind.name() : __AltitudeKind,
        __FirstSegmentOnPath.name() : __FirstSegmentOnPath,
        __StartPoint.name() : __StartPoint,
        __EndPoint.name() : __EndPoint,
        __CoupledMotionEnable.name() : __CoupledMotionEnable,
        __StartRoll.name() : __StartRoll,
        __StartPitch.name() : __StartPitch,
        __StartYaw.name() : __StartYaw,
        __EndRoll.name() : __EndRoll,
        __EndPitch.name() : __EndPitch,
        __EndYaw.name() : __EndYaw,
        __RollRate.name() : __RollRate,
        __PitchRate.name() : __PitchRate,
        __YawRate.name() : __YawRate,
        __EndRollRate.name() : __EndRollRate,
        __EndPitchRate.name() : __EndPitchRate,
        __EndYawRate.name() : __EndYawRate,
        __StartSpeed.name() : __StartSpeed,
        __EndSpeed.name() : __EndSpeed,
        __PitchKind.name() : __PitchKind
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctLineSegment = ctLineSegment
Namespace.addCategoryObject('typeBinding', 'ctLineSegment', ctLineSegment)


# Complex type {http://www.amherst.com/CEESIM/XML}ctArcSegment with content type ELEMENT_ONLY
class ctArcSegment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctArcSegment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctArcSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 113, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}AltitudeKind uses Python identifier AltitudeKind
    __AltitudeKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind'), 'AltitudeKind', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLAltitudeKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 115, 6), )

    
    AltitudeKind = property(__AltitudeKind.value, __AltitudeKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}FirstSegmentOnPath uses Python identifier FirstSegmentOnPath
    __FirstSegmentOnPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath'), 'FirstSegmentOnPath', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLFirstSegmentOnPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 116, 6), )

    
    FirstSegmentOnPath = property(__FirstSegmentOnPath.value, __FirstSegmentOnPath.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartPoint uses Python identifier StartPoint
    __StartPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartPoint'), 'StartPoint', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLStartPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 118, 6), )

    
    StartPoint = property(__StartPoint.value, __StartPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}CenterPoint uses Python identifier CenterPoint
    __CenterPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CenterPoint'), 'CenterPoint', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLCenterPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 119, 6), )

    
    CenterPoint = property(__CenterPoint.value, __CenterPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndPoint uses Python identifier EndPoint
    __EndPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndPoint'), 'EndPoint', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLEndPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 120, 6), )

    
    EndPoint = property(__EndPoint.value, __EndPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartRoll uses Python identifier StartRoll
    __StartRoll = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartRoll'), 'StartRoll', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLStartRoll', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 122, 6), )

    
    StartRoll = property(__StartRoll.value, __StartRoll.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartPitch uses Python identifier StartPitch
    __StartPitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartPitch'), 'StartPitch', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLStartPitch', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 123, 6), )

    
    StartPitch = property(__StartPitch.value, __StartPitch.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartYaw uses Python identifier StartYaw
    __StartYaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartYaw'), 'StartYaw', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLStartYaw', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 124, 6), )

    
    StartYaw = property(__StartYaw.value, __StartYaw.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndRoll uses Python identifier EndRoll
    __EndRoll = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndRoll'), 'EndRoll', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLEndRoll', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 126, 6), )

    
    EndRoll = property(__EndRoll.value, __EndRoll.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndPitch uses Python identifier EndPitch
    __EndPitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndPitch'), 'EndPitch', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLEndPitch', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 127, 6), )

    
    EndPitch = property(__EndPitch.value, __EndPitch.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndYaw uses Python identifier EndYaw
    __EndYaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndYaw'), 'EndYaw', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLEndYaw', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 128, 6), )

    
    EndYaw = property(__EndYaw.value, __EndYaw.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartSpeed uses Python identifier StartSpeed
    __StartSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed'), 'StartSpeed', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLStartSpeed', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 130, 6), )

    
    StartSpeed = property(__StartSpeed.value, __StartSpeed.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndSpeed uses Python identifier EndSpeed
    __EndSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed'), 'EndSpeed', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLEndSpeed', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 131, 6), )

    
    EndSpeed = property(__EndSpeed.value, __EndSpeed.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PitchKind uses Python identifier PitchKind
    __PitchKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PitchKind'), 'PitchKind', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLPitchKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 133, 6), )

    
    PitchKind = property(__PitchKind.value, __PitchKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TurnKind uses Python identifier TurnKind
    __TurnKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TurnKind'), 'TurnKind', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLTurnKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 134, 6), )

    
    TurnKind = property(__TurnKind.value, __TurnKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}LoadFactor uses Python identifier LoadFactor
    __LoadFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LoadFactor'), 'LoadFactor', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLLoadFactor', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 136, 6), )

    
    LoadFactor = property(__LoadFactor.value, __LoadFactor.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RollRate uses Python identifier RollRate
    __RollRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RollRate'), 'RollRate', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLRollRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 138, 6), )

    
    RollRate = property(__RollRate.value, __RollRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}BankAngle uses Python identifier BankAngle
    __BankAngle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BankAngle'), 'BankAngle', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLBankAngle', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 140, 6), )

    
    BankAngle = property(__BankAngle.value, __BankAngle.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Heading uses Python identifier Heading
    __Heading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Heading'), 'Heading', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLHeading', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 141, 6), )

    
    Heading = property(__Heading.value, __Heading.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ClimbAngle uses Python identifier ClimbAngle
    __ClimbAngle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClimbAngle'), 'ClimbAngle', '__httpwww_amherst_comCEESIMXML_ctArcSegment_httpwww_amherst_comCEESIMXMLClimbAngle', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 142, 6), )

    
    ClimbAngle = property(__ClimbAngle.value, __ClimbAngle.set, None, None)

    _ElementMap.update({
        __AltitudeKind.name() : __AltitudeKind,
        __FirstSegmentOnPath.name() : __FirstSegmentOnPath,
        __StartPoint.name() : __StartPoint,
        __CenterPoint.name() : __CenterPoint,
        __EndPoint.name() : __EndPoint,
        __StartRoll.name() : __StartRoll,
        __StartPitch.name() : __StartPitch,
        __StartYaw.name() : __StartYaw,
        __EndRoll.name() : __EndRoll,
        __EndPitch.name() : __EndPitch,
        __EndYaw.name() : __EndYaw,
        __StartSpeed.name() : __StartSpeed,
        __EndSpeed.name() : __EndSpeed,
        __PitchKind.name() : __PitchKind,
        __TurnKind.name() : __TurnKind,
        __LoadFactor.name() : __LoadFactor,
        __RollRate.name() : __RollRate,
        __BankAngle.name() : __BankAngle,
        __Heading.name() : __Heading,
        __ClimbAngle.name() : __ClimbAngle
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctArcSegment = ctArcSegment
Namespace.addCategoryObject('typeBinding', 'ctArcSegment', ctArcSegment)


# Complex type {http://www.amherst.com/CEESIM/XML}ctCompoundSegment with content type ELEMENT_ONLY
class ctCompoundSegment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctCompoundSegment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctCompoundSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 146, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}AltitudeKind uses Python identifier AltitudeKind
    __AltitudeKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind'), 'AltitudeKind', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLAltitudeKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 148, 6), )

    
    AltitudeKind = property(__AltitudeKind.value, __AltitudeKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}FirstSegmentOnPath uses Python identifier FirstSegmentOnPath
    __FirstSegmentOnPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath'), 'FirstSegmentOnPath', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLFirstSegmentOnPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 149, 6), )

    
    FirstSegmentOnPath = property(__FirstSegmentOnPath.value, __FirstSegmentOnPath.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartPoint uses Python identifier StartPoint
    __StartPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartPoint'), 'StartPoint', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLStartPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 151, 6), )

    
    StartPoint = property(__StartPoint.value, __StartPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndPoint uses Python identifier EndPoint
    __EndPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndPoint'), 'EndPoint', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLEndPoint', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 152, 6), )

    
    EndPoint = property(__EndPoint.value, __EndPoint.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartRoll uses Python identifier StartRoll
    __StartRoll = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartRoll'), 'StartRoll', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLStartRoll', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 154, 6), )

    
    StartRoll = property(__StartRoll.value, __StartRoll.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartPitch uses Python identifier StartPitch
    __StartPitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartPitch'), 'StartPitch', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLStartPitch', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 155, 6), )

    
    StartPitch = property(__StartPitch.value, __StartPitch.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartYaw uses Python identifier StartYaw
    __StartYaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartYaw'), 'StartYaw', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLStartYaw', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 156, 6), )

    
    StartYaw = property(__StartYaw.value, __StartYaw.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndRoll uses Python identifier EndRoll
    __EndRoll = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndRoll'), 'EndRoll', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLEndRoll', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 158, 6), )

    
    EndRoll = property(__EndRoll.value, __EndRoll.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndPitch uses Python identifier EndPitch
    __EndPitch = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndPitch'), 'EndPitch', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLEndPitch', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 159, 6), )

    
    EndPitch = property(__EndPitch.value, __EndPitch.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndYaw uses Python identifier EndYaw
    __EndYaw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndYaw'), 'EndYaw', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLEndYaw', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 160, 6), )

    
    EndYaw = property(__EndYaw.value, __EndYaw.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}StartSpeed uses Python identifier StartSpeed
    __StartSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed'), 'StartSpeed', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLStartSpeed', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 162, 6), )

    
    StartSpeed = property(__StartSpeed.value, __StartSpeed.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EndSpeed uses Python identifier EndSpeed
    __EndSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed'), 'EndSpeed', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLEndSpeed', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 163, 6), )

    
    EndSpeed = property(__EndSpeed.value, __EndSpeed.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PitchKind uses Python identifier PitchKind
    __PitchKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PitchKind'), 'PitchKind', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLPitchKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 165, 6), )

    
    PitchKind = property(__PitchKind.value, __PitchKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TurnKind uses Python identifier TurnKind
    __TurnKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TurnKind'), 'TurnKind', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLTurnKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 166, 6), )

    
    TurnKind = property(__TurnKind.value, __TurnKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}LoadFactor uses Python identifier LoadFactor
    __LoadFactor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LoadFactor'), 'LoadFactor', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLLoadFactor', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 168, 6), )

    
    LoadFactor = property(__LoadFactor.value, __LoadFactor.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}RollRate uses Python identifier RollRate
    __RollRate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RollRate'), 'RollRate', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLRollRate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 170, 6), )

    
    RollRate = property(__RollRate.value, __RollRate.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}BankAngle uses Python identifier BankAngle
    __BankAngle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BankAngle'), 'BankAngle', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLBankAngle', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 172, 6), )

    
    BankAngle = property(__BankAngle.value, __BankAngle.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Heading uses Python identifier Heading
    __Heading = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Heading'), 'Heading', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLHeading', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 173, 6), )

    
    Heading = property(__Heading.value, __Heading.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ClimbAngle uses Python identifier ClimbAngle
    __ClimbAngle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ClimbAngle'), 'ClimbAngle', '__httpwww_amherst_comCEESIMXML_ctCompoundSegment_httpwww_amherst_comCEESIMXMLClimbAngle', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 174, 6), )

    
    ClimbAngle = property(__ClimbAngle.value, __ClimbAngle.set, None, None)

    _ElementMap.update({
        __AltitudeKind.name() : __AltitudeKind,
        __FirstSegmentOnPath.name() : __FirstSegmentOnPath,
        __StartPoint.name() : __StartPoint,
        __EndPoint.name() : __EndPoint,
        __StartRoll.name() : __StartRoll,
        __StartPitch.name() : __StartPitch,
        __StartYaw.name() : __StartYaw,
        __EndRoll.name() : __EndRoll,
        __EndPitch.name() : __EndPitch,
        __EndYaw.name() : __EndYaw,
        __StartSpeed.name() : __StartSpeed,
        __EndSpeed.name() : __EndSpeed,
        __PitchKind.name() : __PitchKind,
        __TurnKind.name() : __TurnKind,
        __LoadFactor.name() : __LoadFactor,
        __RollRate.name() : __RollRate,
        __BankAngle.name() : __BankAngle,
        __Heading.name() : __Heading,
        __ClimbAngle.name() : __ClimbAngle
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctCompoundSegment = ctCompoundSegment
Namespace.addCategoryObject('typeBinding', 'ctCompoundSegment', ctCompoundSegment)


# Complex type {http://www.amherst.com/CEESIM/XML}ctInterceptSegment with content type ELEMENT_ONLY
class ctInterceptSegment (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctInterceptSegment with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctInterceptSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 178, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}InterceptKind uses Python identifier InterceptKind
    __InterceptKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterceptKind'), 'InterceptKind', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLInterceptKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 180, 6), )

    
    InterceptKind = property(__InterceptKind.value, __InterceptKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TargetSutFlag uses Python identifier TargetSutFlag
    __TargetSutFlag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TargetSutFlag'), 'TargetSutFlag', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLTargetSutFlag', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 181, 6), )

    
    TargetSutFlag = property(__TargetSutFlag.value, __TargetSutFlag.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}TargetPlatformNumber uses Python identifier TargetPlatformNumber
    __TargetPlatformNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TargetPlatformNumber'), 'TargetPlatformNumber', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLTargetPlatformNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 182, 6), )

    
    TargetPlatformNumber = property(__TargetPlatformNumber.value, __TargetPlatformNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}InterceptEndAction uses Python identifier InterceptEndAction
    __InterceptEndAction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterceptEndAction'), 'InterceptEndAction', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLInterceptEndAction', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 183, 6), )

    
    InterceptEndAction = property(__InterceptEndAction.value, __InterceptEndAction.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}InterceptRange uses Python identifier InterceptRange
    __InterceptRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterceptRange'), 'InterceptRange', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLInterceptRange', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 184, 6), )

    
    InterceptRange = property(__InterceptRange.value, __InterceptRange.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ConstantSpeed uses Python identifier ConstantSpeed
    __ConstantSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ConstantSpeed'), 'ConstantSpeed', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLConstantSpeed', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 185, 6), )

    
    ConstantSpeed = property(__ConstantSpeed.value, __ConstantSpeed.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}MaximumSpeed uses Python identifier MaximumSpeed
    __MaximumSpeed = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MaximumSpeed'), 'MaximumSpeed', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLMaximumSpeed', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 186, 6), )

    
    MaximumSpeed = property(__MaximumSpeed.value, __MaximumSpeed.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}InterceptDuration uses Python identifier InterceptDuration
    __InterceptDuration = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InterceptDuration'), 'InterceptDuration', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLInterceptDuration', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 187, 6), )

    
    InterceptDuration = property(__InterceptDuration.value, __InterceptDuration.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}LimitDurationFlag uses Python identifier LimitDurationFlag
    __LimitDurationFlag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LimitDurationFlag'), 'LimitDurationFlag', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLLimitDurationFlag', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 188, 6), )

    
    LimitDurationFlag = property(__LimitDurationFlag.value, __LimitDurationFlag.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DurationLimit uses Python identifier DurationLimit
    __DurationLimit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DurationLimit'), 'DurationLimit', '__httpwww_amherst_comCEESIMXML_ctInterceptSegment_httpwww_amherst_comCEESIMXMLDurationLimit', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 189, 6), )

    
    DurationLimit = property(__DurationLimit.value, __DurationLimit.set, None, None)

    _ElementMap.update({
        __InterceptKind.name() : __InterceptKind,
        __TargetSutFlag.name() : __TargetSutFlag,
        __TargetPlatformNumber.name() : __TargetPlatformNumber,
        __InterceptEndAction.name() : __InterceptEndAction,
        __InterceptRange.name() : __InterceptRange,
        __ConstantSpeed.name() : __ConstantSpeed,
        __MaximumSpeed.name() : __MaximumSpeed,
        __InterceptDuration.name() : __InterceptDuration,
        __LimitDurationFlag.name() : __LimitDurationFlag,
        __DurationLimit.name() : __DurationLimit
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctInterceptSegment = ctInterceptSegment
Namespace.addCategoryObject('typeBinding', 'ctInterceptSegment', ctInterceptSegment)




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




ctPlatformScriptEventList._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformScriptEvent'), ctPlatformScriptEvent, scope=ctPlatformScriptEventList, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 44, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 43, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformScriptEventList._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformScriptEvent')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 44, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctPlatformScriptEventList._Automaton = _BuildAutomaton_13()




ctPlatformScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartTime'), stDoubleStartTime, scope=ctPlatformScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 51, 6)))

ctPlatformScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Deactivate'), stBoolDeactivate, scope=ctPlatformScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 52, 6)))

ctPlatformScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Segment'), ctPathSegment, scope=ctPlatformScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 53, 6)))

ctPlatformScriptEvent._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Intercept'), ctInterceptSegment, scope=ctPlatformScriptEvent, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 54, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 51, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartTime')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 51, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 52, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Deactivate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 52, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 53, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Segment')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 53, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 54, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformScriptEvent._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Intercept')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 54, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 51, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 52, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 53, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 54, 6))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 50, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctPlatformScriptEvent._Automaton = _BuildAutomaton_14()




ctPathSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Point'), ctPointSegment, scope=ctPathSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 60, 6)))

ctPathSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Line'), ctLineSegment, scope=ctPathSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 61, 6)))

ctPathSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Arc'), ctArcSegment, scope=ctPathSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 62, 6)))

ctPathSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Compound'), ctCompoundSegment, scope=ctPathSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 63, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 59, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 60, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 61, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 62, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 63, 6))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ctPathSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Point')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 60, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ctPathSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Line')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 61, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ctPathSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Arc')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 62, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ctPathSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Compound')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 63, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctPathSegment._Automaton = _BuildAutomaton_19()




ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind'), stEnumAltitudeKind, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 69, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath'), stBoolFirstSegmentOnPath, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 70, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartPoint'), ctPoint, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 71, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoupledMotionEnable'), stBoolCoupledMotionEnable, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 72, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartRoll'), stDoubleStartRoll, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 73, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartPitch'), stDoubleStartPitch, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 74, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartYaw'), stDoubleStartYaw, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 75, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RollRate'), stDoubleRollRate, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 76, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PitchRate'), stDoublePitchRate, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 77, 6)))

ctPointSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'YawRate'), stDoubleYawRate, scope=ctPointSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 78, 6)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 69, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 69, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 70, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 70, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 71, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 71, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 72, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CoupledMotionEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 72, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 73, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartRoll')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 73, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 74, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartPitch')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 74, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 75, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartYaw')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 75, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 76, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RollRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 76, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 77, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PitchRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 77, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 78, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPointSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'YawRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 78, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 69, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 70, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 71, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 72, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 73, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 74, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 75, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 76, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 77, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 78, 6))
    counters.add(cc_9)
    states = []
    sub_automata = []
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
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 68, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctPointSegment._Automaton = _BuildAutomaton_20()




ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind'), stEnumAltitudeKind, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 84, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath'), stBoolFirstSegmentOnPath, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 85, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartPoint'), ctPoint, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 87, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndPoint'), ctPoint, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 88, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CoupledMotionEnable'), stBoolCoupledMotionEnable, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 89, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartRoll'), stDoubleStartRoll, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 91, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartPitch'), stDoubleStartPitch, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 92, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartYaw'), stDoubleStartYaw, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 93, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndRoll'), stDoubleEndRoll, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 95, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndPitch'), stDoubleEndPitch, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 96, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndYaw'), stDoubleEndYaw, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 97, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RollRate'), stDoubleRollRate, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 99, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PitchRate'), stDoublePitchRate, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 100, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'YawRate'), stDoubleYawRate, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 101, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndRollRate'), stDoubleEndRollRate, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 103, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndPitchRate'), stDoubleEndPitchRate, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 104, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndYawRate'), stDoubleEndYawRate, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 105, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed'), stDoubleStartSpeed, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 107, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed'), stDoubleEndSpeed, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 108, 6)))

ctLineSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PitchKind'), stEnumPitchKind, scope=ctLineSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 109, 6)))

def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 84, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 84, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 85, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 85, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 87, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 87, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 88, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 88, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 89, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CoupledMotionEnable')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 89, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 91, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartRoll')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 91, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 92, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartPitch')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 92, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 93, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartYaw')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 93, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 95, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndRoll')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 95, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 96, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndPitch')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 96, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 97, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndYaw')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 97, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 99, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RollRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 99, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 100, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PitchRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 100, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 101, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'YawRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 101, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 103, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndRollRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 103, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 104, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndPitchRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 104, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 105, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndYawRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 105, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 107, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 107, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 108, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 108, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 109, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctLineSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PitchKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 109, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 84, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 85, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 87, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 88, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 89, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 91, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 92, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 93, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 95, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 96, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 97, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 99, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 100, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 101, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 103, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 104, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 105, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 107, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 108, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 109, 6))
    counters.add(cc_19)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_32())
    sub_automata.append(_BuildAutomaton_33())
    sub_automata.append(_BuildAutomaton_34())
    sub_automata.append(_BuildAutomaton_35())
    sub_automata.append(_BuildAutomaton_36())
    sub_automata.append(_BuildAutomaton_37())
    sub_automata.append(_BuildAutomaton_38())
    sub_automata.append(_BuildAutomaton_39())
    sub_automata.append(_BuildAutomaton_40())
    sub_automata.append(_BuildAutomaton_41())
    sub_automata.append(_BuildAutomaton_42())
    sub_automata.append(_BuildAutomaton_43())
    sub_automata.append(_BuildAutomaton_44())
    sub_automata.append(_BuildAutomaton_45())
    sub_automata.append(_BuildAutomaton_46())
    sub_automata.append(_BuildAutomaton_47())
    sub_automata.append(_BuildAutomaton_48())
    sub_automata.append(_BuildAutomaton_49())
    sub_automata.append(_BuildAutomaton_50())
    sub_automata.append(_BuildAutomaton_51())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 83, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctLineSegment._Automaton = _BuildAutomaton_31()




ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind'), stEnumAltitudeKind, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 115, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath'), stBoolFirstSegmentOnPath, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 116, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartPoint'), ctPoint, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 118, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CenterPoint'), ctPoint, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 119, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndPoint'), ctPoint, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 120, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartRoll'), stDoubleStartRoll, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 122, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartPitch'), stDoubleStartPitch, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 123, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartYaw'), stDoubleStartYaw, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 124, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndRoll'), stDoubleEndRoll, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 126, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndPitch'), stDoubleEndPitch, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 127, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndYaw'), stDoubleEndYaw, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 128, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed'), stDoubleStartSpeed, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 130, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed'), stDoubleEndSpeed, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 131, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PitchKind'), stEnumPitchKind, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 133, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TurnKind'), stEnumTurnKind, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 134, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LoadFactor'), stDoubleLoadFactor, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 136, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RollRate'), stDoubleRollRate, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 138, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BankAngle'), stDoubleBankAngle, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 140, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Heading'), stDoubleHeading, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 141, 6)))

ctArcSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClimbAngle'), stDoubleClimbAngle, scope=ctArcSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 142, 6)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 115, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 115, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 116, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 116, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 118, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 118, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 119, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CenterPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 119, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 120, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 120, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 122, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartRoll')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 122, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 123, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartPitch')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 123, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 124, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartYaw')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 124, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 126, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndRoll')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 126, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 127, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndPitch')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 127, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 128, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndYaw')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 128, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 130, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 130, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 131, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 131, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 133, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PitchKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 133, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 134, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TurnKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 134, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 136, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LoadFactor')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 136, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 138, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RollRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 138, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 140, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BankAngle')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 140, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 141, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Heading')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 141, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 142, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctArcSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClimbAngle')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 142, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 115, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 116, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 118, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 119, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 120, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 122, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 123, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 124, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 126, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 127, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 128, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 130, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 131, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 133, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 134, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 136, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 138, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 140, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 141, 6))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 142, 6))
    counters.add(cc_19)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_53())
    sub_automata.append(_BuildAutomaton_54())
    sub_automata.append(_BuildAutomaton_55())
    sub_automata.append(_BuildAutomaton_56())
    sub_automata.append(_BuildAutomaton_57())
    sub_automata.append(_BuildAutomaton_58())
    sub_automata.append(_BuildAutomaton_59())
    sub_automata.append(_BuildAutomaton_60())
    sub_automata.append(_BuildAutomaton_61())
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
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 114, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctArcSegment._Automaton = _BuildAutomaton_52()




ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind'), stEnumAltitudeKind, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 148, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath'), stBoolFirstSegmentOnPath, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 149, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartPoint'), ctPoint, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 151, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndPoint'), ctPoint, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 152, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartRoll'), stDoubleStartRoll, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 154, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartPitch'), stDoubleStartPitch, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 155, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartYaw'), stDoubleStartYaw, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 156, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndRoll'), stDoubleEndRoll, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 158, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndPitch'), stDoubleEndPitch, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 159, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndYaw'), stDoubleEndYaw, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 160, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed'), stDoubleStartSpeed, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 162, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed'), stDoubleEndSpeed, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 163, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PitchKind'), stEnumPitchKind, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 165, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TurnKind'), stEnumTurnKind, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 166, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LoadFactor'), stDoubleLoadFactor, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 168, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RollRate'), stDoubleRollRate, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 170, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BankAngle'), stDoubleBankAngle, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 172, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Heading'), stDoubleHeading, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 173, 6)))

ctCompoundSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClimbAngle'), stDoubleClimbAngle, scope=ctCompoundSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 174, 6)))

def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 148, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AltitudeKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 148, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 149, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FirstSegmentOnPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 149, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 151, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 151, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 152, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndPoint')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 152, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 154, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartRoll')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 154, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 155, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartPitch')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 155, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 156, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartYaw')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 156, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 158, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndRoll')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 158, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 159, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndPitch')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 159, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 160, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndYaw')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 160, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 162, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'StartSpeed')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 162, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_85 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_85
    del _BuildAutomaton_85
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 163, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndSpeed')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 163, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 165, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PitchKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 165, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 166, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TurnKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 166, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_88 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_88
    del _BuildAutomaton_88
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 168, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LoadFactor')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 168, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 170, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RollRate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 170, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 172, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BankAngle')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 172, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_91 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_91
    del _BuildAutomaton_91
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 173, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Heading')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 173, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 174, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctCompoundSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ClimbAngle')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 174, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 148, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 149, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 151, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 152, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 154, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 155, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 156, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 158, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 159, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 160, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 162, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 163, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 165, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 166, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 168, 6))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 170, 6))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 172, 6))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 173, 6))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 174, 6))
    counters.add(cc_18)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_74())
    sub_automata.append(_BuildAutomaton_75())
    sub_automata.append(_BuildAutomaton_76())
    sub_automata.append(_BuildAutomaton_77())
    sub_automata.append(_BuildAutomaton_78())
    sub_automata.append(_BuildAutomaton_79())
    sub_automata.append(_BuildAutomaton_80())
    sub_automata.append(_BuildAutomaton_81())
    sub_automata.append(_BuildAutomaton_82())
    sub_automata.append(_BuildAutomaton_83())
    sub_automata.append(_BuildAutomaton_84())
    sub_automata.append(_BuildAutomaton_85())
    sub_automata.append(_BuildAutomaton_86())
    sub_automata.append(_BuildAutomaton_87())
    sub_automata.append(_BuildAutomaton_88())
    sub_automata.append(_BuildAutomaton_89())
    sub_automata.append(_BuildAutomaton_90())
    sub_automata.append(_BuildAutomaton_91())
    sub_automata.append(_BuildAutomaton_92())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 147, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctCompoundSegment._Automaton = _BuildAutomaton_73()




ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterceptKind'), stEnumInterceptKind, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 180, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TargetSutFlag'), stBoolTargetSutFlag, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 181, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TargetPlatformNumber'), stIntTargetPlatformNumber, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 182, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterceptEndAction'), stEnumEndActionKind, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 183, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterceptRange'), stDoubleRange, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 184, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ConstantSpeed'), stDoubleSpeed, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 185, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaximumSpeed'), stDoubleSpeed, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 186, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InterceptDuration'), stDoubleDuration, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 187, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LimitDurationFlag'), stBoolLimitDurationFlag, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 188, 6)))

ctInterceptSegment._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DurationLimit'), stDoubleDuration, scope=ctInterceptSegment, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 189, 6)))

def _BuildAutomaton_94 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_94
    del _BuildAutomaton_94
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterceptKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 180, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_95 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_95
    del _BuildAutomaton_95
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 181, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TargetSutFlag')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 181, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 182, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TargetPlatformNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 182, 6))
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
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterceptEndAction')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 183, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_98 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_98
    del _BuildAutomaton_98
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterceptRange')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 184, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_99 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_99
    del _BuildAutomaton_99
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 185, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ConstantSpeed')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 185, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 186, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MaximumSpeed')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 186, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 187, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InterceptDuration')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 187, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_102 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_102
    del _BuildAutomaton_102
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 188, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LimitDurationFlag')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 188, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 189, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctInterceptSegment._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DurationLimit')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 189, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_93 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_93
    del _BuildAutomaton_93
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 181, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 182, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 185, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 186, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 187, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 188, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 189, 6))
    counters.add(cc_6)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_94())
    sub_automata.append(_BuildAutomaton_95())
    sub_automata.append(_BuildAutomaton_96())
    sub_automata.append(_BuildAutomaton_97())
    sub_automata.append(_BuildAutomaton_98())
    sub_automata.append(_BuildAutomaton_99())
    sub_automata.append(_BuildAutomaton_100())
    sub_automata.append(_BuildAutomaton_101())
    sub_automata.append(_BuildAutomaton_102())
    sub_automata.append(_BuildAutomaton_103())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformScriptDataR1-1.xsd', 179, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctInterceptSegment._Automaton = _BuildAutomaton_93()

