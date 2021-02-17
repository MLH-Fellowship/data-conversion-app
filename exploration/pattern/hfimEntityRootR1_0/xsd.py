# ./data/ceesim/schema/pattern/hfimEntityRootR1_0/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:31:24.786022 by PyXB version 1.2.6 using Python 3.6.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1a8c26f2-715f-11eb-b80d-00155debab14')

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


# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stHfimEntityMajorRevision
class stHfimEntityMajorRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stHfimEntityMajorRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 38, 2)
    _Documentation = None
stHfimEntityMajorRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stHfimEntityMajorRevision, value=pyxb.binding.datatypes.int(1))
stHfimEntityMajorRevision._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stHfimEntityMajorRevision, value=pyxb.binding.datatypes.int(1))
stHfimEntityMajorRevision._InitializeFacetMap(stHfimEntityMajorRevision._CF_minInclusive,
   stHfimEntityMajorRevision._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stHfimEntityMajorRevision', stHfimEntityMajorRevision)
_module_typeBindings.stHfimEntityMajorRevision = stHfimEntityMajorRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stHfimEntityMinorRevision
class stHfimEntityMinorRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stHfimEntityMinorRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 46, 2)
    _Documentation = None
stHfimEntityMinorRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stHfimEntityMinorRevision, value=pyxb.binding.datatypes.int(0))
stHfimEntityMinorRevision._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stHfimEntityMinorRevision, value=pyxb.binding.datatypes.int(0))
stHfimEntityMinorRevision._InitializeFacetMap(stHfimEntityMinorRevision._CF_minInclusive,
   stHfimEntityMinorRevision._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stHfimEntityMinorRevision', stHfimEntityMinorRevision)
_module_typeBindings.stHfimEntityMinorRevision = stHfimEntityMinorRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringHfimFunction
class stStringHfimFunction (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringHfimFunction')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 88, 2)
    _Documentation = ''
stStringHfimFunction._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
stStringHfimFunction._InitializeFacetMap(stStringHfimFunction._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'stStringHfimFunction', stStringHfimFunction)
_module_typeBindings.stStringHfimFunction = stStringHfimFunction

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringHfimComment
class stStringHfimComment (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringHfimComment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 99, 2)
    _Documentation = ''
stStringHfimComment._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringHfimComment._InitializeFacetMap(stStringHfimComment._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'stStringHfimComment', stStringHfimComment)
_module_typeBindings.stStringHfimComment = stStringHfimComment

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntDownloadDataLength
class stIntDownloadDataLength (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntDownloadDataLength')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 110, 2)
    _Documentation = ''
stIntDownloadDataLength._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntDownloadDataLength, value=pyxb.binding.datatypes.int(0))
stIntDownloadDataLength._InitializeFacetMap(stIntDownloadDataLength._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntDownloadDataLength', stIntDownloadDataLength)
_module_typeBindings.stIntDownloadDataLength = stIntDownloadDataLength

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntEditorDataLength
class stIntEditorDataLength (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntEditorDataLength')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 121, 2)
    _Documentation = ''
stIntEditorDataLength._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntEditorDataLength, value=pyxb.binding.datatypes.int(0))
stIntEditorDataLength._InitializeFacetMap(stIntEditorDataLength._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntEditorDataLength', stIntEditorDataLength)
_module_typeBindings.stIntEditorDataLength = stIntEditorDataLength

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumAmplitudeAxisScaleKind
class stEnumAmplitudeAxisScaleKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumAmplitudeAxisScaleKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 132, 2)
    _Documentation = ''
stEnumAmplitudeAxisScaleKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumAmplitudeAxisScaleKind, enum_prefix=None)
stEnumAmplitudeAxisScaleKind.Linear = stEnumAmplitudeAxisScaleKind._CF_enumeration.addEnumeration(unicode_value='Linear', tag='Linear')
stEnumAmplitudeAxisScaleKind.Logarithmic = stEnumAmplitudeAxisScaleKind._CF_enumeration.addEnumeration(unicode_value='Logarithmic', tag='Logarithmic')
stEnumAmplitudeAxisScaleKind._InitializeFacetMap(stEnumAmplitudeAxisScaleKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumAmplitudeAxisScaleKind', stEnumAmplitudeAxisScaleKind)
_module_typeBindings.stEnumAmplitudeAxisScaleKind = stEnumAmplitudeAxisScaleKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSamplePeriod
class stDoubleSamplePeriod (pyxb.binding.datatypes.double, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSamplePeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 144, 2)
    _Documentation = ''
stDoubleSamplePeriod._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stDoubleSamplePeriod, enum_prefix=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000001562500', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000006250000', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000025000000', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000100000000', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000000781250', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000003125000', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000012500000', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000050000000', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000200000000', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000000390625', tag=None)
stDoubleSamplePeriod._CF_enumeration.addEnumeration(unicode_value='0.00000000078125', tag=None)
stDoubleSamplePeriod._InitializeFacetMap(stDoubleSamplePeriod._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stDoubleSamplePeriod', stDoubleSamplePeriod)
_module_typeBindings.stDoubleSamplePeriod = stDoubleSamplePeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumViewModeKind
class stEnumViewModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumViewModeKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 165, 2)
    _Documentation = ''
stEnumViewModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumViewModeKind, enum_prefix=None)
stEnumViewModeKind.Frequency_Amplitude = stEnumViewModeKind._CF_enumeration.addEnumeration(unicode_value='Frequency_Amplitude', tag='Frequency_Amplitude')
stEnumViewModeKind.Phase_Amplitude = stEnumViewModeKind._CF_enumeration.addEnumeration(unicode_value='Phase_Amplitude', tag='Phase_Amplitude')
stEnumViewModeKind.Iphase_Qphase = stEnumViewModeKind._CF_enumeration.addEnumeration(unicode_value='Iphase_Qphase', tag='Iphase_Qphase')
stEnumViewModeKind.Amop = stEnumViewModeKind._CF_enumeration.addEnumeration(unicode_value='Amop', tag='Amop')
stEnumViewModeKind._InitializeFacetMap(stEnumViewModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumViewModeKind', stEnumViewModeKind)
_module_typeBindings.stEnumViewModeKind = stEnumViewModeKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stUnsignedLongCrc
class stUnsignedLongCrc (pyxb.binding.datatypes.unsignedLong):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stUnsignedLongCrc')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 179, 2)
    _Documentation = ''
stUnsignedLongCrc._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stUnsignedLongCrc, value=pyxb.binding.datatypes.unsignedLong(0))
stUnsignedLongCrc._InitializeFacetMap(stUnsignedLongCrc._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'stUnsignedLongCrc', stUnsignedLongCrc)
_module_typeBindings.stUnsignedLongCrc = stUnsignedLongCrc

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntVersion
class stIntVersion (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntVersion')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 190, 2)
    _Documentation = ''
stIntVersion._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntVersion, value=pyxb.binding.datatypes.int(0))
stIntVersion._InitializeFacetMap(stIntVersion._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntVersion', stIntVersion)
_module_typeBindings.stIntVersion = stIntVersion

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntRevision
class stIntRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 201, 2)
    _Documentation = ''
stIntRevision._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntRevision, value=pyxb.binding.datatypes.int(0))
stIntRevision._InitializeFacetMap(stIntRevision._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntRevision', stIntRevision)
_module_typeBindings.stIntRevision = stIntRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumFilterPathKind
class stEnumFilterPathKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumFilterPathKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 212, 2)
    _Documentation = ''
stEnumFilterPathKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumFilterPathKind, enum_prefix=None)
stEnumFilterPathKind.Non_Filtered_Path = stEnumFilterPathKind._CF_enumeration.addEnumeration(unicode_value='Non_Filtered_Path', tag='Non_Filtered_Path')
stEnumFilterPathKind.Filtered_Path = stEnumFilterPathKind._CF_enumeration.addEnumeration(unicode_value='Filtered_Path', tag='Filtered_Path')
stEnumFilterPathKind._InitializeFacetMap(stEnumFilterPathKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumFilterPathKind', stEnumFilterPathKind)
_module_typeBindings.stEnumFilterPathKind = stEnumFilterPathKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumUpsamplingStateKind
class stEnumUpsamplingStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumUpsamplingStateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 224, 2)
    _Documentation = ''
stEnumUpsamplingStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumUpsamplingStateKind, enum_prefix=None)
stEnumUpsamplingStateKind.Disabled = stEnumUpsamplingStateKind._CF_enumeration.addEnumeration(unicode_value='Disabled', tag='Disabled')
stEnumUpsamplingStateKind.Enabled = stEnumUpsamplingStateKind._CF_enumeration.addEnumeration(unicode_value='Enabled', tag='Enabled')
stEnumUpsamplingStateKind._InitializeFacetMap(stEnumUpsamplingStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumUpsamplingStateKind', stEnumUpsamplingStateKind)
_module_typeBindings.stEnumUpsamplingStateKind = stEnumUpsamplingStateKind

# Complex type {http://www.amherst.com/CEESIM/XML}ctHfimPattern with content type ELEMENT_ONLY
class ctHfimPattern (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctHfimPattern with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctHfimPattern')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 64, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Header'), 'Header', '__httpwww_amherst_comCEESIMXML_ctHfimPattern_httpwww_amherst_comCEESIMXMLHeader', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 66, 6), )

    
    Header = property(__Header.value, __Header.set, None, None)

    _ElementMap.update({
        __Header.name() : __Header
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctHfimPattern = ctHfimPattern
Namespace.addCategoryObject('typeBinding', 'ctHfimPattern', ctHfimPattern)


# Complex type {http://www.amherst.com/CEESIM/XML}ctHfimHeader with content type ELEMENT_ONLY
class ctHfimHeader (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctHfimHeader with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctHfimHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Function uses Python identifier Function
    __Function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Function'), 'Function', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLFunction', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 72, 6), )

    
    Function = property(__Function.value, __Function.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLComment', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 73, 6), )

    
    Comment = property(__Comment.value, __Comment.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}DownloadDataLength uses Python identifier DownloadDataLength
    __DownloadDataLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DownloadDataLength'), 'DownloadDataLength', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLDownloadDataLength', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 74, 6), )

    
    DownloadDataLength = property(__DownloadDataLength.value, __DownloadDataLength.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}EditorDataLength uses Python identifier EditorDataLength
    __EditorDataLength = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EditorDataLength'), 'EditorDataLength', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLEditorDataLength', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 75, 6), )

    
    EditorDataLength = property(__EditorDataLength.value, __EditorDataLength.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}AmplitudeAxisScale uses Python identifier AmplitudeAxisScale
    __AmplitudeAxisScale = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AmplitudeAxisScale'), 'AmplitudeAxisScale', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLAmplitudeAxisScale', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 76, 6), )

    
    AmplitudeAxisScale = property(__AmplitudeAxisScale.value, __AmplitudeAxisScale.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}SamplePeriod uses Python identifier SamplePeriod
    __SamplePeriod = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SamplePeriod'), 'SamplePeriod', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLSamplePeriod', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 77, 6), )

    
    SamplePeriod = property(__SamplePeriod.value, __SamplePeriod.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ViewMode uses Python identifier ViewMode
    __ViewMode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ViewMode'), 'ViewMode', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLViewMode', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 78, 6), )

    
    ViewMode = property(__ViewMode.value, __ViewMode.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}ICrc uses Python identifier ICrc
    __ICrc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ICrc'), 'ICrc', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLICrc', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 79, 6), )

    
    ICrc = property(__ICrc.value, __ICrc.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}QCrc uses Python identifier QCrc
    __QCrc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'QCrc'), 'QCrc', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLQCrc', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 80, 6), )

    
    QCrc = property(__QCrc.value, __QCrc.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Version uses Python identifier Version
    __Version = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Version'), 'Version', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLVersion', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 81, 6), )

    
    Version = property(__Version.value, __Version.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}Revision uses Python identifier Revision
    __Revision = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Revision'), 'Revision', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLRevision', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 82, 6), )

    
    Revision = property(__Revision.value, __Revision.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}FilterPath uses Python identifier FilterPath
    __FilterPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FilterPath'), 'FilterPath', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLFilterPath', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 83, 6), )

    
    FilterPath = property(__FilterPath.value, __FilterPath.set, None, None)

    
    # Element {http://www.amherst.com/CEESIM/XML}UpsamplingState uses Python identifier UpsamplingState
    __UpsamplingState = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UpsamplingState'), 'UpsamplingState', '__httpwww_amherst_comCEESIMXML_ctHfimHeader_httpwww_amherst_comCEESIMXMLUpsamplingState', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 84, 6), )

    
    UpsamplingState = property(__UpsamplingState.value, __UpsamplingState.set, None, None)

    _ElementMap.update({
        __Function.name() : __Function,
        __Comment.name() : __Comment,
        __DownloadDataLength.name() : __DownloadDataLength,
        __EditorDataLength.name() : __EditorDataLength,
        __AmplitudeAxisScale.name() : __AmplitudeAxisScale,
        __SamplePeriod.name() : __SamplePeriod,
        __ViewMode.name() : __ViewMode,
        __ICrc.name() : __ICrc,
        __QCrc.name() : __QCrc,
        __Version.name() : __Version,
        __Revision.name() : __Revision,
        __FilterPath.name() : __FilterPath,
        __UpsamplingState.name() : __UpsamplingState
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ctHfimHeader = ctHfimHeader
Namespace.addCategoryObject('typeBinding', 'ctHfimHeader', ctHfimHeader)


# Complex type {http://www.amherst.com/CEESIM/XML}ctHfimEntity with content type ELEMENT_ONLY
class ctHfimEntity (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.amherst.com/CEESIM/XML}ctHfimEntity with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ctHfimEntity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 55, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.amherst.com/CEESIM/XML}Hfim uses Python identifier Hfim
    __Hfim = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Hfim'), 'Hfim', '__httpwww_amherst_comCEESIMXML_ctHfimEntity_httpwww_amherst_comCEESIMXMLHfim', False, pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 57, 6), )

    
    Hfim = property(__Hfim.value, __Hfim.set, None, None)

    
    # Attribute Major uses Python identifier Major
    __Major = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Major'), 'Major', '__httpwww_amherst_comCEESIMXML_ctHfimEntity_Major', _module_typeBindings.stHfimEntityMajorRevision, required=True)
    __Major._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 59, 4)
    __Major._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 59, 4)
    
    Major = property(__Major.value, __Major.set, None, None)

    
    # Attribute Minor uses Python identifier Minor
    __Minor = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Minor'), 'Minor', '__httpwww_amherst_comCEESIMXML_ctHfimEntity_Minor', _module_typeBindings.stHfimEntityMinorRevision, required=True)
    __Minor._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 60, 4)
    __Minor._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 60, 4)
    
    Minor = property(__Minor.value, __Minor.set, None, None)

    
    # Attribute PerId uses Python identifier PerId
    __PerId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PerId'), 'PerId', '__httpwww_amherst_comCEESIMXML_ctHfimEntity_PerId', pyxb.binding.datatypes.string, unicode_default='')
    __PerId._DeclarationLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 61, 4)
    __PerId._UseLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 61, 4)
    
    PerId = property(__PerId.value, __PerId.set, None, None)

    _ElementMap.update({
        __Hfim.name() : __Hfim
    })
    _AttributeMap.update({
        __Major.name() : __Major,
        __Minor.name() : __Minor,
        __PerId.name() : __PerId
    })
_module_typeBindings.ctHfimEntity = ctHfimEntity
Namespace.addCategoryObject('typeBinding', 'ctHfimEntity', ctHfimEntity)


HfimEntity = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'HfimEntity'), ctHfimEntity, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 53, 2))
Namespace.addCategoryObject('elementBinding', HfimEntity.name().localName(), HfimEntity)



ctHfimPattern._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Header'), ctHfimHeader, scope=ctHfimPattern, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 66, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctHfimPattern._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Header')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 66, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctHfimPattern._Automaton = _BuildAutomaton()




ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Function'), stStringHfimFunction, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 72, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), stStringHfimComment, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 73, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DownloadDataLength'), stIntDownloadDataLength, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 74, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EditorDataLength'), stIntEditorDataLength, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 75, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AmplitudeAxisScale'), stEnumAmplitudeAxisScaleKind, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 76, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SamplePeriod'), stDoubleSamplePeriod, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 77, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ViewMode'), stEnumViewModeKind, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 78, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ICrc'), stUnsignedLongCrc, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 79, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'QCrc'), stUnsignedLongCrc, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 80, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Version'), stIntVersion, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 81, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Revision'), stIntRevision, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 82, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FilterPath'), stEnumFilterPathKind, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 83, 6)))

ctHfimHeader._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UpsamplingState'), stEnumUpsamplingStateKind, scope=ctHfimHeader, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 84, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Function')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 72, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 73, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 73, 6))
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
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DownloadDataLength')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 74, 6))
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
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EditorDataLength')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 75, 6))
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
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AmplitudeAxisScale')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 76, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SamplePeriod')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 77, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ViewMode')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 78, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 79, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ICrc')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 79, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 80, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'QCrc')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 80, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 81, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Version')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 81, 6))
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
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Revision')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 82, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=st_0)

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 83, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FilterPath')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 83, 6))
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
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 84, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ctHfimHeader._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UpsamplingState')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 84, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=st_0)

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 73, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 79, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 80, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 81, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 83, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 84, 6))
    counters.add(cc_5)
    states = []
    sub_automata = []
    sub_automata.append(_BuildAutomaton_2())
    sub_automata.append(_BuildAutomaton_3())
    sub_automata.append(_BuildAutomaton_4())
    sub_automata.append(_BuildAutomaton_5())
    sub_automata.append(_BuildAutomaton_6())
    sub_automata.append(_BuildAutomaton_7())
    sub_automata.append(_BuildAutomaton_8())
    sub_automata.append(_BuildAutomaton_9())
    sub_automata.append(_BuildAutomaton_10())
    sub_automata.append(_BuildAutomaton_11())
    sub_automata.append(_BuildAutomaton_12())
    sub_automata.append(_BuildAutomaton_13())
    sub_automata.append(_BuildAutomaton_14())
    final_update = set()
    symbol = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 71, 4)
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=True)
    st_0._set_subAutomata(*sub_automata)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctHfimHeader._Automaton = _BuildAutomaton_()




ctHfimEntity._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Hfim'), ctHfimPattern, scope=ctHfimEntity, location=pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 57, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ctHfimEntity._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Hfim')), pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/pattern/hfimEntityRootR1-0.xsd', 57, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ctHfimEntity._Automaton = _BuildAutomaton_15()

