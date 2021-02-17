# ./data/ceesim/schema/pattern/complexPriEntityRootR1_0/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:31:22.964163 by PyXB version 1.2.6 using Python 3.6.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1974a9a6-715f-11eb-b10b-00155debab14')

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


# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stComplexPriPatternEntityMajorRevision
class stComplexPriPatternEntityMajorRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stComplexPriPatternEntityMajorRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 39, 2)
    _Documentation = None
stComplexPriPatternEntityMajorRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stComplexPriPatternEntityMajorRevision, value=pyxb.binding.datatypes.int(1))
stComplexPriPatternEntityMajorRevision._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stComplexPriPatternEntityMajorRevision, value=pyxb.binding.datatypes.int(1))
stComplexPriPatternEntityMajorRevision._InitializeFacetMap(stComplexPriPatternEntityMajorRevision._CF_minInclusive,
   stComplexPriPatternEntityMajorRevision._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stComplexPriPatternEntityMajorRevision', stComplexPriPatternEntityMajorRevision)
_module_typeBindings.stComplexPriPatternEntityMajorRevision = stComplexPriPatternEntityMajorRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stComplexPriPatternEntityMinorRevision
class stComplexPriPatternEntityMinorRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stComplexPriPatternEntityMinorRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 47, 2)
    _Documentation = None
stComplexPriPatternEntityMinorRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stComplexPriPatternEntityMinorRevision, value=pyxb.binding.datatypes.int(0))
stComplexPriPatternEntityMinorRevision._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stComplexPriPatternEntityMinorRevision, value=pyxb.binding.datatypes.int(0))
stComplexPriPatternEntityMinorRevision._InitializeFacetMap(stComplexPriPatternEntityMinorRevision._CF_minInclusive,
   stComplexPriPatternEntityMinorRevision._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stComplexPriPatternEntityMinorRevision', stComplexPriPatternEntityMinorRevision)
_module_typeBindings.stComplexPriPatternEntityMinorRevision = stComplexPriPatternEntityMinorRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleMultiplierValue
class stDoubleMultiplierValue (pyxb.binding.datatypes.double, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleMultiplierValue')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 97, 2)
    _Documentation = ''
stDoubleMultiplierValue._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stDoubleMultiplierValue, enum_prefix=None)
stDoubleMultiplierValue._CF_enumeration.addEnumeration(unicode_value='0.5', tag=None)
stDoubleMultiplierValue._CF_enumeration.addEnumeration(unicode_value='1.0', tag=None)
stDoubleMultiplierValue._CF_enumeration.addEnumeration(unicode_value='2.0', tag=None)
stDoubleMultiplierValue._CF_enumeration.addEnumeration(unicode_value='4.0', tag=None)
stDoubleMultiplierValue._InitializeFacetMap(stDoubleMultiplierValue._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stDoubleMultiplierValue', stDoubleMultiplierValue)
_module_typeBindings.stDoubleMultiplierValue = stDoubleMultiplierValue

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleValue
class stDoubleValue (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleValue')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 111, 2)
    _Documentation = ''
stDoubleValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleValue, value=pyxb.binding.datatypes.double(1e-06))
stDoubleValue._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleValue, value=pyxb.binding.datatypes.double(0.999999))
stDoubleValue._InitializeFacetMap(stDoubleValue._CF_minInclusive,
   stDoubleValue._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleValue', stDoubleValue)
_module_typeBindings.stDoubleValue = stDoubleValue

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntIndexNumber
class stIntIndexNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntIndexNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 123, 2)
    _Documentation = ''
stIntIndexNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntIndexNumber, value=pyxb.binding.datatypes.int(1))
stIntIndexNumber._InitializeFacetMap(stIntIndexNumber._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntIndexNumber', stIntIndexNumber)
_module_typeBindings.stIntIndexNumber = stIntIndexNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringFunction
class stStringFunction (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringFunction')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 134, 2)
    _Documentation = ''
stStringFunction._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
stStringFunction._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringFunction._InitializeFacetMap(stStringFunction._CF_minLength,
   stStringFunction._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringFunction', stStringFunction)
_module_typeBindings.stStringFunction = stStringFunction

# Complex type {http://www.amherst.com/CEESIM/XML}ctComplexPriPattern with content type ELEMENT_ONLY
class ctComplexPriPattern (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctComplexPriPattern with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctComplexPriPattern')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 65, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Header'), 'Header', '__httpwww_amherst_comCEESIMXML_ctComplexPriPattern_httpwww_amherst_comCEESIMXMLHeader', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 67, 6), )

    
    Header = property(__Header.value, __Header.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Pts uses Python identifier Pts
    __Pts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pts'), 'Pts', '__httpwww_amherst_comCEESIMXML_ctComplexPriPattern_httpwww_amherst_comCEESIMXMLPts', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 68, 6), )

    
    Pts = property(__Pts.value, __Pts.set, None, None)

    _ElementMap.update({
        __Header.name() : __Header,
        __Pts.name() : __Pts
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctComplexPriPattern = ctComplexPriPattern
Namespace.addCategoryObject('typeBinding', 'ctComplexPriPattern', ctComplexPriPattern)


# Complex type {http://www.amherst.com/CEESIM/XML}ctComplexPriPatternHeader with content type ELEMENT_ONLY
class ctComplexPriPatternHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctComplexPriPatternHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctComplexPriPatternHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 77, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_amherst_comCEESIMXML_ctComplexPriPatternHeader_httpwww_amherst_comCEESIMXMLFunction', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 79, 6), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Multiplier uses Python identifier Multiplier
    __Multiplier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Multiplier'), 'Multiplier', '__httpwww_amherst_comCEESIMXML_ctComplexPriPatternHeader_httpwww_amherst_comCEESIMXMLMultiplier', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 80, 6), )

    
    Multiplier = property(__Multiplier.value, __Multiplier.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function,
        __Multiplier.name() : __Multiplier
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctComplexPriPatternHeader = ctComplexPriPatternHeader
Namespace.addCategoryObject('typeBinding', 'ctComplexPriPatternHeader', ctComplexPriPatternHeader)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPts with content type ELEMENT_ONLY
class ctPts (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPts with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPts')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 84, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Pt uses Python identifier Pt
    __Pt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pt'), 'Pt', '__httpwww_amherst_comCEESIMXML_ctPts_httpwww_amherst_comCEESIMXMLPt', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 86, 6), )

    
    Pt = property(__Pt.value, __Pt.set, None, None)

    _ElementMap.update({
        __Pt.name() : __Pt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPts = ctPts
Namespace.addCategoryObject('typeBinding', 'ctPts', ctPts)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPt with content type ELEMENT_ONLY
class ctPt (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPt with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPt')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 90, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Index uses Python identifier Index
    __Index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Index'), 'Index', '__httpwww_amherst_comCEESIMXML_ctPt_httpwww_amherst_comCEESIMXMLIndex', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 92, 6), )

    
    Index = property(__Index.value, __Index.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httpwww_amherst_comCEESIMXML_ctPt_httpwww_amherst_comCEESIMXMLValue', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 93, 6), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Index.name() : __Index,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPt = ctPt
Namespace.addCategoryObject('typeBinding', 'ctPt', ctPt)


# Complex type {http://www.amherst.com/CEESIM/XML}ctComplexPriPatternEntity with content type ELEMENT_ONLY
class ctComplexPriPatternEntity (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctComplexPriPatternEntity with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctComplexPriPatternEntity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 56, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}ComplexPriPattern uses Python identifier ComplexPriPattern
    __ComplexPriPattern = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ComplexPriPattern'), 'ComplexPriPattern', '__httpwww_amherst_comCEESIMXML_ctComplexPriPatternEntity_httpwww_amherst_comCEESIMXMLComplexPriPattern', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 58, 6), )

    
    ComplexPriPattern = property(__ComplexPriPattern.value, __ComplexPriPattern.set, None, None)

    
    # Attribute Major uses Python identifier Major
    __Major = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Major'), 'Major', '__httpwww_amherst_comCEESIMXML_ctComplexPriPatternEntity_Major', _module_typeBindings.stComplexPriPatternEntityMajorRevision, required=True)
    __Major._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 60, 4)
    __Major._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 60, 4)
    
    Major = property(__Major.value, __Major.set, None, None)

    
    # Attribute Minor uses Python identifier Minor
    __Minor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Minor'), 'Minor', '__httpwww_amherst_comCEESIMXML_ctComplexPriPatternEntity_Minor', _module_typeBindings.stComplexPriPatternEntityMinorRevision, required=True)
    __Minor._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 61, 4)
    __Minor._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 61, 4)
    
    Minor = property(__Minor.value, __Minor.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctComplexPriPatternEntity_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 62, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 62, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __ComplexPriPattern.name() : __ComplexPriPattern
    })
    _AttributeMap.update({
        __Major.name() : __Major,
        __Minor.name() : __Minor,
        __PerId.name() : __PerId
    })
_module_typeBindings.ctComplexPriPatternEntity = ctComplexPriPatternEntity
Namespace.addCategoryObject('typeBinding', 'ctComplexPriPatternEntity', ctComplexPriPatternEntity)


ComplexPriPatternEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComplexPriPatternEntity'), ctComplexPriPatternEntity, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 54, 2))
Namespace.addCategoryObject('elementBinding', ComplexPriPatternEntity.name().localName(), ComplexPriPatternEntity)



ctComplexPriPattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Header'), ctComplexPriPatternHeader, scope=ctComplexPriPattern, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 67, 6)))

ctComplexPriPattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pts'), ctPts, scope=ctComplexPriPattern, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 68, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctComplexPriPattern._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Header')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 67, 6))
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
    symbol = pyxb.binding.content.ElementUse(ctComplexPriPattern._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pts')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 68, 6))
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
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 66, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctComplexPriPattern._Automaton = _BuildAutomaton()




ctComplexPriPatternHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), stStringFunction, scope=ctComplexPriPatternHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 79, 6)))

ctComplexPriPatternHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Multiplier'), stDoubleMultiplierValue, scope=ctComplexPriPatternHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 80, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctComplexPriPatternHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 79, 6))
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
    symbol = pyxb.binding.content.ElementUse(ctComplexPriPatternHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Multiplier')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 80, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 78, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctComplexPriPatternHeader._Automaton = _BuildAutomaton_3()




ctPts._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pt'), ctPt, scope=ctPts, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 86, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPts._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pt')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 86, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctPts._Automaton = _BuildAutomaton_6()




ctPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Index'), stIntIndexNumber, scope=ctPt, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 92, 6)))

ctPt._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), stDoubleValue, scope=ctPt, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 93, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ctPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Index')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 92, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPt._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 93, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctPt._Automaton = _BuildAutomaton_7()




ctComplexPriPatternEntity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ComplexPriPattern'), ctComplexPriPattern, scope=ctComplexPriPatternEntity, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 58, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctComplexPriPatternEntity._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ComplexPriPattern')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/complexPriEntityRootR1-0.xsd', 58, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctComplexPriPatternEntity._Automaton = _BuildAutomaton_8()

