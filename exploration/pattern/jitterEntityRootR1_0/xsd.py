# ./data/ceesim/schema/pattern/jitterEntityRootR1_0/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:31:26.640858 by PyXB version 1.2.6 using Python 3.6.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1ba81a28-715f-11eb-b254-00155debab14')

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


# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stJitterEntityMajorRevision
class stJitterEntityMajorRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stJitterEntityMajorRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 38, 2)
    _Documentation = None
stJitterEntityMajorRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stJitterEntityMajorRevision, value=pyxb.binding.datatypes.int(1))
stJitterEntityMajorRevision._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stJitterEntityMajorRevision, value=pyxb.binding.datatypes.int(1))
stJitterEntityMajorRevision._InitializeFacetMap(stJitterEntityMajorRevision._CF_minInclusive,
   stJitterEntityMajorRevision._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stJitterEntityMajorRevision', stJitterEntityMajorRevision)
_module_typeBindings.stJitterEntityMajorRevision = stJitterEntityMajorRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stJitterEntityMinorRevision
class stJitterEntityMinorRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stJitterEntityMinorRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 46, 2)
    _Documentation = None
stJitterEntityMinorRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stJitterEntityMinorRevision, value=pyxb.binding.datatypes.int(0))
stJitterEntityMinorRevision._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stJitterEntityMinorRevision, value=pyxb.binding.datatypes.int(0))
stJitterEntityMinorRevision._InitializeFacetMap(stJitterEntityMinorRevision._CF_minInclusive,
   stJitterEntityMinorRevision._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stJitterEntityMinorRevision', stJitterEntityMinorRevision)
_module_typeBindings.stJitterEntityMinorRevision = stJitterEntityMinorRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntIndexNumber
class stIntIndexNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntIndexNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 63, 2)
    _Documentation = ''
stIntIndexNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntIndexNumber, value=pyxb.binding.datatypes.int(1))
stIntIndexNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntIndexNumber, value=pyxb.binding.datatypes.int(65536))
stIntIndexNumber._InitializeFacetMap(stIntIndexNumber._CF_minInclusive,
   stIntIndexNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntIndexNumber', stIntIndexNumber)
_module_typeBindings.stIntIndexNumber = stIntIndexNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringFunction
class stStringFunction (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringFunction')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 57, 2)
    _Documentation = ''
stStringFunction._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
stStringFunction._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringFunction._InitializeFacetMap(stStringFunction._CF_minLength,
   stStringFunction._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringFunction', stStringFunction)
_module_typeBindings.stStringFunction = stStringFunction

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleValue
class stDoubleValue (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleValue')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 76, 2)
    _Documentation = ''
stDoubleValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleValue, value=pyxb.binding.datatypes.double(-1.0))
stDoubleValue._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleValue, value=pyxb.binding.datatypes.double(1.0))
stDoubleValue._InitializeFacetMap(stDoubleValue._CF_minInclusive,
   stDoubleValue._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleValue', stDoubleValue)
_module_typeBindings.stDoubleValue = stDoubleValue

# Complex type {http://www.amherst.com/CEESIM/XML}ctPatternPoints with content type ELEMENT_ONLY
class ctPatternPoints (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPatternPoints with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPatternPoints')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 57, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Pt uses Python identifier Pt
    __Pt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pt'), 'Pt', '__httpwww_amherst_comCEESIMXML_ctPatternPoints_httpwww_amherst_comCEESIMXMLPt', True, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 59, 6), )

    
    Pt = property(__Pt.value, __Pt.set, None, None)

    _ElementMap.update({
        __Pt.name() : __Pt
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPatternPoints = ctPatternPoints
Namespace.addCategoryObject('typeBinding', 'ctPatternPoints', ctPatternPoints)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPatternData with content type ELEMENT_ONLY
class ctPatternData (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPatternData with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPatternData')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 39, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Header'), 'Header', '__httpwww_amherst_comCEESIMXML_ctPatternData_httpwww_amherst_comCEESIMXMLHeader', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 41, 6), )

    
    Header = property(__Header.value, __Header.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Pts uses Python identifier Pts
    __Pts = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Pts'), 'Pts', '__httpwww_amherst_comCEESIMXML_ctPatternData_httpwww_amherst_comCEESIMXMLPts', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 42, 6), )

    
    Pts = property(__Pts.value, __Pts.set, None, None)

    _ElementMap.update({
        __Header.name() : __Header,
        __Pts.name() : __Pts
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPatternData = ctPatternData
Namespace.addCategoryObject('typeBinding', 'ctPatternData', ctPatternData)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPatternHeader with content type ELEMENT_ONLY
class ctPatternHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPatternHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPatternHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 51, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_amherst_comCEESIMXML_ctPatternHeader_httpwww_amherst_comCEESIMXMLFunction', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 53, 6), )

    
    Function = property(__Function.value, __Function.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPatternHeader = ctPatternHeader
Namespace.addCategoryObject('typeBinding', 'ctPatternHeader', ctPatternHeader)


# Complex type {http://www.amherst.com/CEESIM/XML}ctPatternPoint with content type ELEMENT_ONLY
class ctPatternPoint (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctPatternPoint with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctPatternPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 69, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Index uses Python identifier Index
    __Index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Index'), 'Index', '__httpwww_amherst_comCEESIMXML_ctPatternPoint_httpwww_amherst_comCEESIMXMLIndex', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 71, 6), )

    
    Index = property(__Index.value, __Index.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Value'), 'Value', '__httpwww_amherst_comCEESIMXML_ctPatternPoint_httpwww_amherst_comCEESIMXMLValue', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 72, 6), )

    
    Value = property(__Value.value, __Value.set, None, None)

    _ElementMap.update({
        __Index.name() : __Index,
        __Value.name() : __Value
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctPatternPoint = ctPatternPoint
Namespace.addCategoryObject('typeBinding', 'ctPatternPoint', ctPatternPoint)


# Complex type {http://www.amherst.com/CEESIM/XML}ctJitterEntity with content type ELEMENT_ONLY
class ctJitterEntity (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctJitterEntity with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctJitterEntity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 77, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Jitter uses Python identifier Jitter
    __Jitter = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Jitter'), 'Jitter', '__httpwww_amherst_comCEESIMXML_ctJitterEntity_httpwww_amherst_comCEESIMXMLJitter', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 79, 6), )

    
    Jitter = property(__Jitter.value, __Jitter.set, None, None)

    
    # Attribute Major uses Python identifier Major
    __Major = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Major'), 'Major', '__httpwww_amherst_comCEESIMXML_ctJitterEntity_Major', _module_typeBindings.stJitterEntityMajorRevision, required=True)
    __Major._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 81, 4)
    __Major._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 81, 4)
    
    Major = property(__Major.value, __Major.set, None, None)

    
    # Attribute Minor uses Python identifier Minor
    __Minor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Minor'), 'Minor', '__httpwww_amherst_comCEESIMXML_ctJitterEntity_Minor', _module_typeBindings.stJitterEntityMinorRevision, required=True)
    __Minor._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 82, 4)
    __Minor._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 82, 4)
    
    Minor = property(__Minor.value, __Minor.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctJitterEntity_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 83, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 83, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __Jitter.name() : __Jitter
    })
    _AttributeMap.update({
        __Major.name() : __Major,
        __Minor.name() : __Minor,
        __PerId.name() : __PerId
    })
_module_typeBindings.ctJitterEntity = ctJitterEntity
Namespace.addCategoryObject('typeBinding', 'ctJitterEntity', ctJitterEntity)


JitterEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'JitterEntity'), ctJitterEntity, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 75, 2))
Namespace.addCategoryObject('elementBinding', JitterEntity.name().localName(), JitterEntity)



ctPatternPoints._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pt'), ctPatternPoint, scope=ctPatternPoints, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 59, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=65536, max=65536, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 58, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctPatternPoints._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pt')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 59, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctPatternPoints._Automaton = _BuildAutomaton()




ctPatternData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Header'), ctPatternHeader, scope=ctPatternData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 41, 6)))

ctPatternData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Pts'), ctPatternPoints, scope=ctPatternData, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 42, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPatternData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Header')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 41, 6))
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
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPatternData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Pts')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 42, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 40, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctPatternData._Automaton = _BuildAutomaton_()




ctPatternHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), stStringFunction, scope=ctPatternHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 53, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPatternHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 53, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctPatternHeader._Automaton = _BuildAutomaton_4()




ctPatternPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Index'), stIntIndexNumber, scope=ctPatternPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 71, 6)))

ctPatternPoint._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Value'), stDoubleValue, scope=ctPatternPoint, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 72, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ctPatternPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Index')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 71, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctPatternPoint._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Value')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/patternDataR1-0.xsd', 72, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctPatternPoint._Automaton = _BuildAutomaton_5()




ctJitterEntity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Jitter'), ctPatternData, scope=ctJitterEntity, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 79, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctJitterEntity._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Jitter')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/jitterEntityRootR1-0.xsd', 79, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctJitterEntity._Automaton = _BuildAutomaton_6()

