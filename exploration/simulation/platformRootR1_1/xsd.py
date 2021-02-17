# ./data/ceesim/schema/simulation/platformRootR1_1/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:32:41.307729 by PyXB version 1.2.6 using Python 3.6.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:48245c9c-715f-11eb-bad6-00155debab14')

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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleActivationTime
class stDoubleActivationTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleActivationTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 57, 2)
    _Documentation = ''
stDoubleActivationTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleActivationTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleActivationTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleActivationTime, value=pyxb.binding.datatypes.double(137438.953471))
stDoubleActivationTime._InitializeFacetMap(stDoubleActivationTime._CF_minInclusive,
   stDoubleActivationTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleActivationTime', stDoubleActivationTime)
_module_typeBindings.stDoubleActivationTime = stDoubleActivationTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSpeedUnits
class stEnumSpeedUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSpeedUnits')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 69, 2)
    _Documentation = ''
stEnumSpeedUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumSpeedUnits, enum_prefix=None)
stEnumSpeedUnits.Ft_Per_Sec = stEnumSpeedUnits._CF_enumeration.addEnumeration(unicode_value='Ft_Per_Sec', tag='Ft_Per_Sec')
stEnumSpeedUnits.Km_Per_Hr = stEnumSpeedUnits._CF_enumeration.addEnumeration(unicode_value='Km_Per_Hr', tag='Km_Per_Hr')
stEnumSpeedUnits.Kt = stEnumSpeedUnits._CF_enumeration.addEnumeration(unicode_value='Kt', tag='Kt')
stEnumSpeedUnits.M_Per_Sec = stEnumSpeedUnits._CF_enumeration.addEnumeration(unicode_value='M_Per_Sec', tag='M_Per_Sec')
stEnumSpeedUnits.Miles_Per_Hour = stEnumSpeedUnits._CF_enumeration.addEnumeration(unicode_value='Miles_Per_Hour', tag='Miles_Per_Hour')
stEnumSpeedUnits._InitializeFacetMap(stEnumSpeedUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumSpeedUnits', stEnumSpeedUnits)
_module_typeBindings.stEnumSpeedUnits = stEnumSpeedUnits

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringPlatformId
class stStringPlatformId (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringPlatformId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 84, 2)
    _Documentation = ''
stStringPlatformId._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringPlatformId._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
stStringPlatformId._InitializeFacetMap(stStringPlatformId._CF_minLength,
   stStringPlatformId._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringPlatformId', stStringPlatformId)
_module_typeBindings.stStringPlatformId = stStringPlatformId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextSymbolKind
class stTextSymbolKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextSymbolKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 96, 2)
    _Documentation = ''
stTextSymbolKind._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextSymbolKind', stTextSymbolKind)
_module_typeBindings.stTextSymbolKind = stTextSymbolKind

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


# Complex type {http://www.amherst.com/CEESIM/XML}ctPlatformData with content type ELEMENT_ONLY
class ctPlatformData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPlatformData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPlatformData')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 39, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformHeader uses Python identifier PlatformHeader
    __PlatformHeader = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformHeader'), 'PlatformHeader', '__httpwww_amherst_comCEESIMXML_ctPlatformData_httpwww_amherst_comCEESIMXMLPlatformHeader', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 41, 6), )

    
    PlatformHeader = property(__PlatformHeader.value, __PlatformHeader.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctPlatformData_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 43, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 43, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __PlatformHeader.name() : __PlatformHeader
    })
    _AttributeMap.update({
        __PerId.name() : __PerId
    })
_module_typeBindings.ctPlatformData = ctPlatformData
Namespace.addCategoryObject('typeBinding', 'ctPlatformData', ctPlatformData)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPlatformHeader with content type ELEMENT_ONLY
class ctPlatformHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPlatformHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPlatformHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 46, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}UserPlatformNumber uses Python identifier UserPlatformNumber
    __UserPlatformNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UserPlatformNumber'), 'UserPlatformNumber', '__httpwww_amherst_comCEESIMXML_ctPlatformHeader_httpwww_amherst_comCEESIMXMLUserPlatformNumber', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 48, 6), )

    
    UserPlatformNumber = property(__UserPlatformNumber.value, __UserPlatformNumber.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}PlatformId uses Python identifier PlatformId
    __PlatformId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PlatformId'), 'PlatformId', '__httpwww_amherst_comCEESIMXML_ctPlatformHeader_httpwww_amherst_comCEESIMXMLPlatformId', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 49, 6), )

    
    PlatformId = property(__PlatformId.value, __PlatformId.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SymbolKind uses Python identifier SymbolKind
    __SymbolKind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SymbolKind'), 'SymbolKind', '__httpwww_amherst_comCEESIMXML_ctPlatformHeader_httpwww_amherst_comCEESIMXMLSymbolKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 50, 6), )

    
    SymbolKind = property(__SymbolKind.value, __SymbolKind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ActivationTime uses Python identifier ActivationTime
    __ActivationTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ActivationTime'), 'ActivationTime', '__httpwww_amherst_comCEESIMXML_ctPlatformHeader_httpwww_amherst_comCEESIMXMLActivationTime', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 51, 6), )

    
    ActivationTime = property(__ActivationTime.value, __ActivationTime.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SpeedUnits uses Python identifier SpeedUnits
    __SpeedUnits = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SpeedUnits'), 'SpeedUnits', '__httpwww_amherst_comCEESIMXML_ctPlatformHeader_httpwww_amherst_comCEESIMXMLSpeedUnits', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 52, 6), )

    
    SpeedUnits = property(__SpeedUnits.value, __SpeedUnits.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}LastUpdateDate uses Python identifier LastUpdateDate
    __LastUpdateDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LastUpdateDate'), 'LastUpdateDate', '__httpwww_amherst_comCEESIMXML_ctPlatformHeader_httpwww_amherst_comCEESIMXMLLastUpdateDate', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 53, 6), )

    
    LastUpdateDate = property(__LastUpdateDate.value, __LastUpdateDate.set, None, None)

    _ElementMap.update({
        __UserPlatformNumber.name() : __UserPlatformNumber,
        __PlatformId.name() : __PlatformId,
        __SymbolKind.name() : __SymbolKind,
        __ActivationTime.name() : __ActivationTime,
        __SpeedUnits.name() : __SpeedUnits,
        __LastUpdateDate.name() : __LastUpdateDate
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPlatformHeader = ctPlatformHeader
Namespace.addCategoryObject('typeBinding', 'ctPlatformHeader', ctPlatformHeader)


Platform = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Platform'), ctPlatformData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformRootR1-1.xsd', 38, 2))
Namespace.addCategoryObject('elementBinding', Platform.name().localName(), Platform)



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




ctPlatformData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformHeader'), ctPlatformHeader, scope=ctPlatformData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 41, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPlatformData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformHeader')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 41, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctPlatformData._Automaton = _BuildAutomaton_13()




ctPlatformHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UserPlatformNumber'), stIntUserPlatformNumber, scope=ctPlatformHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 48, 6)))

ctPlatformHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PlatformId'), stStringPlatformId, scope=ctPlatformHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 49, 6)))

ctPlatformHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SymbolKind'), stTextSymbolKind, scope=ctPlatformHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 50, 6)))

ctPlatformHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ActivationTime'), stDoubleActivationTime, scope=ctPlatformHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 51, 6)))

ctPlatformHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SpeedUnits'), stEnumSpeedUnits, scope=ctPlatformHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 52, 6)))

ctPlatformHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LastUpdateDate'), stDateModificationDate, scope=ctPlatformHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 53, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPlatformHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UserPlatformNumber')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 48, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPlatformHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PlatformId')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 49, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 50, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SymbolKind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 50, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 51, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ActivationTime')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 51, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 52, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SpeedUnits')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 52, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 53, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPlatformHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LastUpdateDate')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 53, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 50, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 51, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 52, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 53, 6))
    counters.add(cc_3)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_15())
    sub_automata.append(_BuildAutomaton_16())
    sub_automata.append(_BuildAutomaton_17())
    sub_automata.append(_BuildAutomaton_18())
    sub_automata.append(_BuildAutomaton_19())
    sub_automata.append(_BuildAutomaton_20())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/platformDataR1-1.xsd', 47, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctPlatformHeader._Automaton = _BuildAutomaton_14()

