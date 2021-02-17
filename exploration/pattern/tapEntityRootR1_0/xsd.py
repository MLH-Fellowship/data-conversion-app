# ./data/ceesim/schema/pattern/tapEntityRootR1_0/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:31:31.763180 by PyXB version 1.2.6 using Python 3.6.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1eba0226-715f-11eb-870f-00155debab14')

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


# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTapEntityMajorRevision
class stTapEntityMajorRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTapEntityMajorRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 36, 2)
    _Documentation = None
stTapEntityMajorRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stTapEntityMajorRevision, value=pyxb.binding.datatypes.int(1))
stTapEntityMajorRevision._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stTapEntityMajorRevision, value=pyxb.binding.datatypes.int(1))
stTapEntityMajorRevision._InitializeFacetMap(stTapEntityMajorRevision._CF_minInclusive,
   stTapEntityMajorRevision._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stTapEntityMajorRevision', stTapEntityMajorRevision)
_module_typeBindings.stTapEntityMajorRevision = stTapEntityMajorRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTapEntityMinorRevision
class stTapEntityMinorRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTapEntityMinorRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 44, 2)
    _Documentation = None
stTapEntityMinorRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stTapEntityMinorRevision, value=pyxb.binding.datatypes.int(0))
stTapEntityMinorRevision._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stTapEntityMinorRevision, value=pyxb.binding.datatypes.int(0))
stTapEntityMinorRevision._InitializeFacetMap(stTapEntityMinorRevision._CF_minInclusive,
   stTapEntityMinorRevision._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stTapEntityMinorRevision', stTapEntityMinorRevision)
_module_typeBindings.stTapEntityMinorRevision = stTapEntityMinorRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringTapFunction
class stStringTapFunction (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringTapFunction')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 78, 2)
    _Documentation = ''
stStringTapFunction._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
stStringTapFunction._InitializeFacetMap(stStringTapFunction._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'stStringTapFunction', stStringTapFunction)
_module_typeBindings.stStringTapFunction = stStringTapFunction

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumTapKind
class stEnumTapKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumTapKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 89, 2)
    _Documentation = ''
stEnumTapKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumTapKind, enum_prefix=None)
stEnumTapKind.Azel = stEnumTapKind._CF_enumeration.addEnumeration(unicode_value='Azel', tag='Azel')
stEnumTapKind.Threed = stEnumTapKind._CF_enumeration.addEnumeration(unicode_value='Threed', tag='Threed')
stEnumTapKind._InitializeFacetMap(stEnumTapKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumTapKind', stEnumTapKind)
_module_typeBindings.stEnumTapKind = stEnumTapKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleTapAngleTol
class stDoubleTapAngleTol (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleTapAngleTol')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 101, 2)
    _Documentation = ''
stDoubleTapAngleTol._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleTapAngleTol, value=pyxb.binding.datatypes.double(0.1))
stDoubleTapAngleTol._InitializeFacetMap(stDoubleTapAngleTol._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleTapAngleTol', stDoubleTapAngleTol)
_module_typeBindings.stDoubleTapAngleTol = stDoubleTapAngleTol

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleTapGainTol
class stDoubleTapGainTol (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleTapGainTol')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 112, 2)
    _Documentation = ''
stDoubleTapGainTol._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleTapGainTol, value=pyxb.binding.datatypes.double(0.1))
stDoubleTapGainTol._InitializeFacetMap(stDoubleTapGainTol._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleTapGainTol', stDoubleTapGainTol)
_module_typeBindings.stDoubleTapGainTol = stDoubleTapGainTol

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleTapPointAngle
class stDoubleTapPointAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleTapPointAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 136, 2)
    _Documentation = ''
stDoubleTapPointAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleTapPointAngle, value=pyxb.binding.datatypes.double(-180.0))
stDoubleTapPointAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleTapPointAngle, value=pyxb.binding.datatypes.double(180.0))
stDoubleTapPointAngle._InitializeFacetMap(stDoubleTapPointAngle._CF_minInclusive,
   stDoubleTapPointAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleTapPointAngle', stDoubleTapPointAngle)
_module_typeBindings.stDoubleTapPointAngle = stDoubleTapPointAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleTapPointGain
class stDoubleTapPointGain (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleTapPointGain')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 148, 2)
    _Documentation = ''
stDoubleTapPointGain._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleTapPointGain, value=pyxb.binding.datatypes.double(-63.75))
stDoubleTapPointGain._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleTapPointGain, value=pyxb.binding.datatypes.double(0.0))
stDoubleTapPointGain._InitializeFacetMap(stDoubleTapPointGain._CF_minInclusive,
   stDoubleTapPointGain._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleTapPointGain', stDoubleTapPointGain)
_module_typeBindings.stDoubleTapPointGain = stDoubleTapPointGain

# Complex type {http://www.amherst.com/CEESIM/XML}ctTransmitAntennaPattern with content type ELEMENT_ONLY
class ctTransmitAntennaPattern (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTransmitAntennaPattern with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTransmitAntennaPattern')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 62, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Header'), 'Header', '__httpwww_amherst_comCEESIMXML_ctTransmitAntennaPattern_httpwww_amherst_comCEESIMXMLHeader', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 64, 6), )

    
    Header = property(__Header.value, __Header.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Pts uses Python identifier Pts
    __Pts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pts'), 'Pts', '__httpwww_amherst_comCEESIMXML_ctTransmitAntennaPattern_httpwww_amherst_comCEESIMXMLPts', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 65, 6), )

    
    Pts = property(__Pts.value, __Pts.set, None, None)

    _ElementMap.update({
        __Header.name() : __Header,
        __Pts.name() : __Pts
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctTransmitAntennaPattern = ctTransmitAntennaPattern
Namespace.addCategoryObject('typeBinding', 'ctTransmitAntennaPattern', ctTransmitAntennaPattern)


# Complex type {http://www.amherst.com/CEESIM/XML}ctTapHeader with content type ELEMENT_ONLY
class ctTapHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTapHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTapHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 69, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_amherst_comCEESIMXML_ctTapHeader_httpwww_amherst_comCEESIMXMLFunction', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 71, 6), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Kind uses Python identifier Kind
    __Kind = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Kind'), 'Kind', '__httpwww_amherst_comCEESIMXML_ctTapHeader_httpwww_amherst_comCEESIMXMLKind', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 72, 6), )

    
    Kind = property(__Kind.value, __Kind.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}AngleTol uses Python identifier AngleTol
    __AngleTol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AngleTol'), 'AngleTol', '__httpwww_amherst_comCEESIMXML_ctTapHeader_httpwww_amherst_comCEESIMXMLAngleTol', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 73, 6), )

    
    AngleTol = property(__AngleTol.value, __AngleTol.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}GainTol uses Python identifier GainTol
    __GainTol = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GainTol'), 'GainTol', '__httpwww_amherst_comCEESIMXML_ctTapHeader_httpwww_amherst_comCEESIMXMLGainTol', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 74, 6), )

    
    GainTol = property(__GainTol.value, __GainTol.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function,
        __Kind.name() : __Kind,
        __AngleTol.name() : __AngleTol,
        __GainTol.name() : __GainTol
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctTapHeader = ctTapHeader
Namespace.addCategoryObject('typeBinding', 'ctTapHeader', ctTapHeader)


# Complex type {http://www.amherst.com/CEESIM/XML}ctTapPoints with content type ELEMENT_ONLY
class ctTapPoints (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTapPoints with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTapPoints')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 123, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Pt uses Python identifier Pt
    __Pt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pt'), 'Pt', '__httpwww_amherst_comCEESIMXML_ctTapPoints_httpwww_amherst_comCEESIMXMLPt', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 125, 6), )

    
    Pt = property(__Pt.value, __Pt.set, None, None)

    _ElementMap.update({
        __Pt.name() : __Pt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctTapPoints = ctTapPoints
Namespace.addCategoryObject('typeBinding', 'ctTapPoints', ctTapPoints)


# Complex type {http://www.amherst.com/CEESIM/XML}ctTapPoint with content type ELEMENT_ONLY
class ctTapPoint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTapPoint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTapPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 129, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Angle uses Python identifier Angle
    __Angle = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Angle'), 'Angle', '__httpwww_amherst_comCEESIMXML_ctTapPoint_httpwww_amherst_comCEESIMXMLAngle', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 131, 6), )

    
    Angle = property(__Angle.value, __Angle.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Gain uses Python identifier Gain
    __Gain = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Gain'), 'Gain', '__httpwww_amherst_comCEESIMXML_ctTapPoint_httpwww_amherst_comCEESIMXMLGain', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 132, 6), )

    
    Gain = property(__Gain.value, __Gain.set, None, None)

    _ElementMap.update({
        __Angle.name() : __Angle,
        __Gain.name() : __Gain
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctTapPoint = ctTapPoint
Namespace.addCategoryObject('typeBinding', 'ctTapPoint', ctTapPoint)


# Complex type {http://www.amherst.com/CEESIM/XML}ctTapEntity with content type ELEMENT_ONLY
class ctTapEntity (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctTapEntity with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctTapEntity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 53, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Tap uses Python identifier Tap
    __Tap = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Tap'), 'Tap', '__httpwww_amherst_comCEESIMXML_ctTapEntity_httpwww_amherst_comCEESIMXMLTap', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 55, 6), )

    
    Tap = property(__Tap.value, __Tap.set, None, None)

    
    # Attribute Major uses Python identifier Major
    __Major = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Major'), 'Major', '__httpwww_amherst_comCEESIMXML_ctTapEntity_Major', _module_typeBindings.stTapEntityMajorRevision, required=True)
    __Major._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 57, 4)
    __Major._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 57, 4)
    
    Major = property(__Major.value, __Major.set, None, None)

    
    # Attribute Minor uses Python identifier Minor
    __Minor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Minor'), 'Minor', '__httpwww_amherst_comCEESIMXML_ctTapEntity_Minor', _module_typeBindings.stTapEntityMinorRevision, required=True)
    __Minor._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 58, 4)
    __Minor._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 58, 4)
    
    Minor = property(__Minor.value, __Minor.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctTapEntity_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 59, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 59, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __Tap.name() : __Tap
    })
    _AttributeMap.update({
        __Major.name() : __Major,
        __Minor.name() : __Minor,
        __PerId.name() : __PerId
    })
_module_typeBindings.ctTapEntity = ctTapEntity
Namespace.addCategoryObject('typeBinding', 'ctTapEntity', ctTapEntity)


TapEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TapEntity'), ctTapEntity, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 51, 2))
Namespace.addCategoryObject('elementBinding', TapEntity.name().localName(), TapEntity)



ctTransmitAntennaPattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Header'), ctTapHeader, scope=ctTransmitAntennaPattern, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 64, 6)))

ctTransmitAntennaPattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pts'), ctTapPoints, scope=ctTransmitAntennaPattern, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 65, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctTransmitAntennaPattern._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Header')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 64, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctTransmitAntennaPattern._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pts')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 65, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_())
    sub_automata.append(_BuildAutomaton_2())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 63, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctTransmitAntennaPattern._Automaton = _BuildAutomaton()




ctTapHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), stStringTapFunction, scope=ctTapHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 71, 6)))

ctTapHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Kind'), stEnumTapKind, scope=ctTapHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 72, 6)))

ctTapHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AngleTol'), stDoubleTapAngleTol, scope=ctTapHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 73, 6)))

ctTapHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GainTol'), stDoubleTapGainTol, scope=ctTapHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 74, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctTapHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 71, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctTapHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Kind')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 72, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 73, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTapHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AngleTol')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 73, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 74, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTapHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GainTol')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 74, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 73, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 74, 6))
    counters.add(cc_1)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 70, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctTapHeader._Automaton = _BuildAutomaton_3()




ctTapPoints._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pt'), ctTapPoint, scope=ctTapPoints, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 125, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 124, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctTapPoints._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pt')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 125, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ctTapPoints._Automaton = _BuildAutomaton_8()




ctTapPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Angle'), stDoubleTapPointAngle, scope=ctTapPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 131, 6)))

ctTapPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Gain'), stDoubleTapPointGain, scope=ctTapPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 132, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctTapPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Angle')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 131, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctTapPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Gain')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 132, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_10())
    sub_automata.append(_BuildAutomaton_11())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 130, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctTapPoint._Automaton = _BuildAutomaton_9()




ctTapEntity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Tap'), ctTransmitAntennaPattern, scope=ctTapEntity, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 55, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctTapEntity._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Tap')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/tapEntityRootR1-0.xsd', 55, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctTapEntity._Automaton = _BuildAutomaton_12()

