# ./data/ceesim/schema/simulation/commonSimpleTypesR1_0/xsd.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:a4350b0d114ff7faaa29729d5e9d9f9b6b49754c
# Generated 2021-02-17 12:31:36.952657 by PyXB version 1.2.6 using Python 3.6.9.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:217dc09c-715f-11eb-89be-00155debab14')

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


# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntDwellTimePulses
class stIntDwellTimePulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntDwellTimePulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 42, 2)
    _Documentation = ''
stIntDwellTimePulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntDwellTimePulses, value=pyxb.binding.datatypes.int(0))
stIntDwellTimePulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntDwellTimePulses, value=pyxb.binding.datatypes.int(2147483647))
stIntDwellTimePulses._InitializeFacetMap(stIntDwellTimePulses._CF_minInclusive,
   stIntDwellTimePulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntDwellTimePulses', stIntDwellTimePulses)
_module_typeBindings.stIntDwellTimePulses = stIntDwellTimePulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSwitchDwellTimePulses
class stIntSwitchDwellTimePulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSwitchDwellTimePulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 54, 2)
    _Documentation = ''
stIntSwitchDwellTimePulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntSwitchDwellTimePulses, value=pyxb.binding.datatypes.int(0))
stIntSwitchDwellTimePulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntSwitchDwellTimePulses, value=pyxb.binding.datatypes.int(2147483647))
stIntSwitchDwellTimePulses._InitializeFacetMap(stIntSwitchDwellTimePulses._CF_minInclusive,
   stIntSwitchDwellTimePulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntSwitchDwellTimePulses', stIntSwitchDwellTimePulses)
_module_typeBindings.stIntSwitchDwellTimePulses = stIntSwitchDwellTimePulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntBeamDwellTimePulses
class stIntBeamDwellTimePulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntBeamDwellTimePulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 66, 2)
    _Documentation = ''
stIntBeamDwellTimePulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntBeamDwellTimePulses, value=pyxb.binding.datatypes.int(0))
stIntBeamDwellTimePulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntBeamDwellTimePulses, value=pyxb.binding.datatypes.int(2147483647))
stIntBeamDwellTimePulses._InitializeFacetMap(stIntBeamDwellTimePulses._CF_minInclusive,
   stIntBeamDwellTimePulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntBeamDwellTimePulses', stIntBeamDwellTimePulses)
_module_typeBindings.stIntBeamDwellTimePulses = stIntBeamDwellTimePulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSubmodeId
class stIntSubmodeId (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSubmodeId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 78, 2)
    _Documentation = ''
stIntSubmodeId._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntSubmodeId, value=pyxb.binding.datatypes.int(0))
stIntSubmodeId._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntSubmodeId, value=pyxb.binding.datatypes.int(2147483647))
stIntSubmodeId._InitializeFacetMap(stIntSubmodeId._CF_minInclusive,
   stIntSubmodeId._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntSubmodeId', stIntSubmodeId)
_module_typeBindings.stIntSubmodeId = stIntSubmodeId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntEventNumber
class stIntEventNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntEventNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 90, 2)
    _Documentation = ''
stIntEventNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntEventNumber, value=pyxb.binding.datatypes.int(1))
stIntEventNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntEventNumber, value=pyxb.binding.datatypes.int(2147483647))
stIntEventNumber._InitializeFacetMap(stIntEventNumber._CF_minInclusive,
   stIntEventNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntEventNumber', stIntEventNumber)
_module_typeBindings.stIntEventNumber = stIntEventNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntInterruptGeneratorDurationPulses
class stIntInterruptGeneratorDurationPulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntInterruptGeneratorDurationPulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 102, 2)
    _Documentation = ''
stIntInterruptGeneratorDurationPulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntInterruptGeneratorDurationPulses, value=pyxb.binding.datatypes.int(0))
stIntInterruptGeneratorDurationPulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntInterruptGeneratorDurationPulses, value=pyxb.binding.datatypes.int(268435455))
stIntInterruptGeneratorDurationPulses._InitializeFacetMap(stIntInterruptGeneratorDurationPulses._CF_minInclusive,
   stIntInterruptGeneratorDurationPulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntInterruptGeneratorDurationPulses', stIntInterruptGeneratorDurationPulses)
_module_typeBindings.stIntInterruptGeneratorDurationPulses = stIntInterruptGeneratorDurationPulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntInterruptGeneratorRevisitPulses
class stIntInterruptGeneratorRevisitPulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntInterruptGeneratorRevisitPulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 114, 2)
    _Documentation = ''
stIntInterruptGeneratorRevisitPulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntInterruptGeneratorRevisitPulses, value=pyxb.binding.datatypes.int(0))
stIntInterruptGeneratorRevisitPulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntInterruptGeneratorRevisitPulses, value=pyxb.binding.datatypes.int(268435455))
stIntInterruptGeneratorRevisitPulses._InitializeFacetMap(stIntInterruptGeneratorRevisitPulses._CF_minInclusive,
   stIntInterruptGeneratorRevisitPulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntInterruptGeneratorRevisitPulses', stIntInterruptGeneratorRevisitPulses)
_module_typeBindings.stIntInterruptGeneratorRevisitPulses = stIntInterruptGeneratorRevisitPulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntInterruptGeneratorStartTimePulses
class stIntInterruptGeneratorStartTimePulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntInterruptGeneratorStartTimePulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 126, 2)
    _Documentation = ''
stIntInterruptGeneratorStartTimePulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntInterruptGeneratorStartTimePulses, value=pyxb.binding.datatypes.int(0))
stIntInterruptGeneratorStartTimePulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntInterruptGeneratorStartTimePulses, value=pyxb.binding.datatypes.int(268435455))
stIntInterruptGeneratorStartTimePulses._InitializeFacetMap(stIntInterruptGeneratorStartTimePulses._CF_minInclusive,
   stIntInterruptGeneratorStartTimePulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntInterruptGeneratorStartTimePulses', stIntInterruptGeneratorStartTimePulses)
_module_typeBindings.stIntInterruptGeneratorStartTimePulses = stIntInterruptGeneratorStartTimePulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntVirtualNumber
class stIntVirtualNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntVirtualNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 138, 2)
    _Documentation = ''
stIntVirtualNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntVirtualNumber, value=pyxb.binding.datatypes.int(0))
stIntVirtualNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntVirtualNumber, value=pyxb.binding.datatypes.int(65535))
stIntVirtualNumber._InitializeFacetMap(stIntVirtualNumber._CF_minInclusive,
   stIntVirtualNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntVirtualNumber', stIntVirtualNumber)
_module_typeBindings.stIntVirtualNumber = stIntVirtualNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntDwellVariationPulses
class stIntDwellVariationPulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntDwellVariationPulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 150, 2)
    _Documentation = ''
stIntDwellVariationPulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntDwellVariationPulses, value=pyxb.binding.datatypes.int(0))
stIntDwellVariationPulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntDwellVariationPulses, value=pyxb.binding.datatypes.int(65535))
stIntDwellVariationPulses._InitializeFacetMap(stIntDwellVariationPulses._CF_minInclusive,
   stIntDwellVariationPulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntDwellVariationPulses', stIntDwellVariationPulses)
_module_typeBindings.stIntDwellVariationPulses = stIntDwellVariationPulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSiteId
class stIntSiteId (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSiteId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 162, 2)
    _Documentation = ''
stIntSiteId._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntSiteId, value=pyxb.binding.datatypes.int(0))
stIntSiteId._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntSiteId, value=pyxb.binding.datatypes.int(8192))
stIntSiteId._InitializeFacetMap(stIntSiteId._CF_minInclusive,
   stIntSiteId._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntSiteId', stIntSiteId)
_module_typeBindings.stIntSiteId = stIntSiteId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntExternalModeId
class stIntExternalModeId (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntExternalModeId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 174, 2)
    _Documentation = ''
stIntExternalModeId._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntExternalModeId, value=pyxb.binding.datatypes.int(0))
stIntExternalModeId._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntExternalModeId, value=pyxb.binding.datatypes.int(8192))
stIntExternalModeId._InitializeFacetMap(stIntExternalModeId._CF_minInclusive,
   stIntExternalModeId._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntExternalModeId', stIntExternalModeId)
_module_typeBindings.stIntExternalModeId = stIntExternalModeId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSubmodeGeneratorNumber
class stIntSubmodeGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSubmodeGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 186, 2)
    _Documentation = ''
stIntSubmodeGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntSubmodeGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntSubmodeGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntSubmodeGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntSubmodeGeneratorNumber._InitializeFacetMap(stIntSubmodeGeneratorNumber._CF_minInclusive,
   stIntSubmodeGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntSubmodeGeneratorNumber', stIntSubmodeGeneratorNumber)
_module_typeBindings.stIntSubmodeGeneratorNumber = stIntSubmodeGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntMasterGeneratorNumber
class stIntMasterGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntMasterGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 198, 2)
    _Documentation = ''
stIntMasterGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntMasterGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntMasterGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntMasterGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntMasterGeneratorNumber._InitializeFacetMap(stIntMasterGeneratorNumber._CF_minInclusive,
   stIntMasterGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntMasterGeneratorNumber', stIntMasterGeneratorNumber)
_module_typeBindings.stIntMasterGeneratorNumber = stIntMasterGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntAzMasterGeneratorNumber
class stIntAzMasterGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntAzMasterGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 210, 2)
    _Documentation = ''
stIntAzMasterGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntAzMasterGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntAzMasterGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntAzMasterGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntAzMasterGeneratorNumber._InitializeFacetMap(stIntAzMasterGeneratorNumber._CF_minInclusive,
   stIntAzMasterGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntAzMasterGeneratorNumber', stIntAzMasterGeneratorNumber)
_module_typeBindings.stIntAzMasterGeneratorNumber = stIntAzMasterGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntElMasterGeneratorNumber
class stIntElMasterGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntElMasterGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 222, 2)
    _Documentation = ''
stIntElMasterGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntElMasterGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntElMasterGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntElMasterGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntElMasterGeneratorNumber._InitializeFacetMap(stIntElMasterGeneratorNumber._CF_minInclusive,
   stIntElMasterGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntElMasterGeneratorNumber', stIntElMasterGeneratorNumber)
_module_typeBindings.stIntElMasterGeneratorNumber = stIntElMasterGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSynchronizedGeneratorNumber
class stIntSynchronizedGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSynchronizedGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 234, 2)
    _Documentation = ''
stIntSynchronizedGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntSynchronizedGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntSynchronizedGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntSynchronizedGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntSynchronizedGeneratorNumber._InitializeFacetMap(stIntSynchronizedGeneratorNumber._CF_minInclusive,
   stIntSynchronizedGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntSynchronizedGeneratorNumber', stIntSynchronizedGeneratorNumber)
_module_typeBindings.stIntSynchronizedGeneratorNumber = stIntSynchronizedGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntGeneratorNumber
class stIntGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 246, 2)
    _Documentation = ''
stIntGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntGeneratorNumber._InitializeFacetMap(stIntGeneratorNumber._CF_minInclusive,
   stIntGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntGeneratorNumber', stIntGeneratorNumber)
_module_typeBindings.stIntGeneratorNumber = stIntGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntScriptGeneratorNumber
class stIntScriptGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntScriptGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 258, 2)
    _Documentation = ''
stIntScriptGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntScriptGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntScriptGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntScriptGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntScriptGeneratorNumber._InitializeFacetMap(stIntScriptGeneratorNumber._CF_minInclusive,
   stIntScriptGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntScriptGeneratorNumber', stIntScriptGeneratorNumber)
_module_typeBindings.stIntScriptGeneratorNumber = stIntScriptGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntInterruptGeneratorNumber
class stIntInterruptGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntInterruptGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 270, 2)
    _Documentation = ''
stIntInterruptGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntInterruptGeneratorNumber, value=pyxb.binding.datatypes.int(1))
stIntInterruptGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntInterruptGeneratorNumber, value=pyxb.binding.datatypes.int(32))
stIntInterruptGeneratorNumber._InitializeFacetMap(stIntInterruptGeneratorNumber._CF_minInclusive,
   stIntInterruptGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntInterruptGeneratorNumber', stIntInterruptGeneratorNumber)
_module_typeBindings.stIntInterruptGeneratorNumber = stIntInterruptGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntAzTrackPlatformNumber
class stIntAzTrackPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntAzTrackPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 282, 2)
    _Documentation = ''
stIntAzTrackPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntAzTrackPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntAzTrackPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntAzTrackPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntAzTrackPlatformNumber._InitializeFacetMap(stIntAzTrackPlatformNumber._CF_minInclusive,
   stIntAzTrackPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntAzTrackPlatformNumber', stIntAzTrackPlatformNumber)
_module_typeBindings.stIntAzTrackPlatformNumber = stIntAzTrackPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntElTrackPlatformNumber
class stIntElTrackPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntElTrackPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 294, 2)
    _Documentation = ''
stIntElTrackPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntElTrackPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntElTrackPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntElTrackPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntElTrackPlatformNumber._InitializeFacetMap(stIntElTrackPlatformNumber._CF_minInclusive,
   stIntElTrackPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntElTrackPlatformNumber', stIntElTrackPlatformNumber)
_module_typeBindings.stIntElTrackPlatformNumber = stIntElTrackPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntUserEmitterNumber
class stIntUserEmitterNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntUserEmitterNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 306, 2)
    _Documentation = ''
stIntUserEmitterNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntUserEmitterNumber, value=pyxb.binding.datatypes.int(1))
stIntUserEmitterNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntUserEmitterNumber, value=pyxb.binding.datatypes.int(32767))
stIntUserEmitterNumber._InitializeFacetMap(stIntUserEmitterNumber._CF_minInclusive,
   stIntUserEmitterNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntUserEmitterNumber', stIntUserEmitterNumber)
_module_typeBindings.stIntUserEmitterNumber = stIntUserEmitterNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntUserPlatformNumber
class stIntUserPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntUserPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 318, 2)
    _Documentation = ''
stIntUserPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntUserPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntUserPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntUserPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntUserPlatformNumber._InitializeFacetMap(stIntUserPlatformNumber._CF_minInclusive,
   stIntUserPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntUserPlatformNumber', stIntUserPlatformNumber)
_module_typeBindings.stIntUserPlatformNumber = stIntUserPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSutPlatformNumber
class stIntSutPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSutPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 330, 2)
    _Documentation = ''
stIntSutPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntSutPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntSutPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntSutPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntSutPlatformNumber._InitializeFacetMap(stIntSutPlatformNumber._CF_minInclusive,
   stIntSutPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntSutPlatformNumber', stIntSutPlatformNumber)
_module_typeBindings.stIntSutPlatformNumber = stIntSutPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntLowerEmitterNumber
class stIntLowerEmitterNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntLowerEmitterNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 342, 2)
    _Documentation = ''
stIntLowerEmitterNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntLowerEmitterNumber, value=pyxb.binding.datatypes.int(1))
stIntLowerEmitterNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntLowerEmitterNumber, value=pyxb.binding.datatypes.int(32767))
stIntLowerEmitterNumber._InitializeFacetMap(stIntLowerEmitterNumber._CF_minInclusive,
   stIntLowerEmitterNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntLowerEmitterNumber', stIntLowerEmitterNumber)
_module_typeBindings.stIntLowerEmitterNumber = stIntLowerEmitterNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntUpperEmitterNumber
class stIntUpperEmitterNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntUpperEmitterNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 354, 2)
    _Documentation = ''
stIntUpperEmitterNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntUpperEmitterNumber, value=pyxb.binding.datatypes.int(1))
stIntUpperEmitterNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntUpperEmitterNumber, value=pyxb.binding.datatypes.int(32767))
stIntUpperEmitterNumber._InitializeFacetMap(stIntUpperEmitterNumber._CF_minInclusive,
   stIntUpperEmitterNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntUpperEmitterNumber', stIntUpperEmitterNumber)
_module_typeBindings.stIntUpperEmitterNumber = stIntUpperEmitterNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntTrackPlatformNumber
class stIntTrackPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntTrackPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 366, 2)
    _Documentation = ''
stIntTrackPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntTrackPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntTrackPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntTrackPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntTrackPlatformNumber._InitializeFacetMap(stIntTrackPlatformNumber._CF_minInclusive,
   stIntTrackPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntTrackPlatformNumber', stIntTrackPlatformNumber)
_module_typeBindings.stIntTrackPlatformNumber = stIntTrackPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntBarTrackPlatformNumber
class stIntBarTrackPlatformNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntBarTrackPlatformNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 378, 2)
    _Documentation = ''
stIntBarTrackPlatformNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntBarTrackPlatformNumber, value=pyxb.binding.datatypes.int(1))
stIntBarTrackPlatformNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntBarTrackPlatformNumber, value=pyxb.binding.datatypes.int(32767))
stIntBarTrackPlatformNumber._InitializeFacetMap(stIntBarTrackPlatformNumber._CF_minInclusive,
   stIntBarTrackPlatformNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntBarTrackPlatformNumber', stIntBarTrackPlatformNumber)
_module_typeBindings.stIntBarTrackPlatformNumber = stIntBarTrackPlatformNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntGpOrPoolNumber
class stIntGpOrPoolNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntGpOrPoolNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 390, 2)
    _Documentation = ''
stIntGpOrPoolNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntGpOrPoolNumber, value=pyxb.binding.datatypes.int(1))
stIntGpOrPoolNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntGpOrPoolNumber, value=pyxb.binding.datatypes.int(64))
stIntGpOrPoolNumber._InitializeFacetMap(stIntGpOrPoolNumber._CF_minInclusive,
   stIntGpOrPoolNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntGpOrPoolNumber', stIntGpOrPoolNumber)
_module_typeBindings.stIntGpOrPoolNumber = stIntGpOrPoolNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntChannelNumber
class stIntChannelNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntChannelNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 402, 2)
    _Documentation = ''
stIntChannelNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntChannelNumber, value=pyxb.binding.datatypes.int(1))
stIntChannelNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntChannelNumber, value=pyxb.binding.datatypes.int(64))
stIntChannelNumber._InitializeFacetMap(stIntChannelNumber._CF_minInclusive,
   stIntChannelNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntChannelNumber', stIntChannelNumber)
_module_typeBindings.stIntChannelNumber = stIntChannelNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntPoolNumber
class stIntPoolNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntPoolNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 414, 2)
    _Documentation = ''
stIntPoolNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntPoolNumber, value=pyxb.binding.datatypes.int(1))
stIntPoolNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntPoolNumber, value=pyxb.binding.datatypes.int(64))
stIntPoolNumber._InitializeFacetMap(stIntPoolNumber._CF_minInclusive,
   stIntPoolNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntPoolNumber', stIntPoolNumber)
_module_typeBindings.stIntPoolNumber = stIntPoolNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntTestPointChannelNumber
class stIntTestPointChannelNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntTestPointChannelNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 426, 2)
    _Documentation = ''
stIntTestPointChannelNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntTestPointChannelNumber, value=pyxb.binding.datatypes.int(1))
stIntTestPointChannelNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntTestPointChannelNumber, value=pyxb.binding.datatypes.int(8))
stIntTestPointChannelNumber._InitializeFacetMap(stIntTestPointChannelNumber._CF_minInclusive,
   stIntTestPointChannelNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntTestPointChannelNumber', stIntTestPointChannelNumber)
_module_typeBindings.stIntTestPointChannelNumber = stIntTestPointChannelNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSegmentNumber
class stIntSegmentNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSegmentNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 438, 2)
    _Documentation = ''
stIntSegmentNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntSegmentNumber, value=pyxb.binding.datatypes.int(1))
stIntSegmentNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntSegmentNumber, value=pyxb.binding.datatypes.int(8192))
stIntSegmentNumber._InitializeFacetMap(stIntSegmentNumber._CF_minInclusive,
   stIntSegmentNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntSegmentNumber', stIntSegmentNumber)
_module_typeBindings.stIntSegmentNumber = stIntSegmentNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntNormalLinkSegment
class stIntNormalLinkSegment (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntNormalLinkSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 450, 2)
    _Documentation = ''
stIntNormalLinkSegment._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntNormalLinkSegment, value=pyxb.binding.datatypes.int(1))
stIntNormalLinkSegment._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntNormalLinkSegment, value=pyxb.binding.datatypes.int(8192))
stIntNormalLinkSegment._InitializeFacetMap(stIntNormalLinkSegment._CF_minInclusive,
   stIntNormalLinkSegment._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntNormalLinkSegment', stIntNormalLinkSegment)
_module_typeBindings.stIntNormalLinkSegment = stIntNormalLinkSegment

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntExternalLinkSegment
class stIntExternalLinkSegment (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntExternalLinkSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 462, 2)
    _Documentation = ''
stIntExternalLinkSegment._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntExternalLinkSegment, value=pyxb.binding.datatypes.int(1))
stIntExternalLinkSegment._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntExternalLinkSegment, value=pyxb.binding.datatypes.int(8192))
stIntExternalLinkSegment._InitializeFacetMap(stIntExternalLinkSegment._CF_minInclusive,
   stIntExternalLinkSegment._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntExternalLinkSegment', stIntExternalLinkSegment)
_module_typeBindings.stIntExternalLinkSegment = stIntExternalLinkSegment

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntAssociatedFrequencySegment
class stIntAssociatedFrequencySegment (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntAssociatedFrequencySegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 474, 2)
    _Documentation = ''
stIntAssociatedFrequencySegment._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntAssociatedFrequencySegment, value=pyxb.binding.datatypes.int(1))
stIntAssociatedFrequencySegment._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntAssociatedFrequencySegment, value=pyxb.binding.datatypes.int(8192))
stIntAssociatedFrequencySegment._InitializeFacetMap(stIntAssociatedFrequencySegment._CF_minInclusive,
   stIntAssociatedFrequencySegment._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntAssociatedFrequencySegment', stIntAssociatedFrequencySegment)
_module_typeBindings.stIntAssociatedFrequencySegment = stIntAssociatedFrequencySegment

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntAssociatedPulseSegment
class stIntAssociatedPulseSegment (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntAssociatedPulseSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 486, 2)
    _Documentation = ''
stIntAssociatedPulseSegment._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntAssociatedPulseSegment, value=pyxb.binding.datatypes.int(1))
stIntAssociatedPulseSegment._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntAssociatedPulseSegment, value=pyxb.binding.datatypes.int(8192))
stIntAssociatedPulseSegment._InitializeFacetMap(stIntAssociatedPulseSegment._CF_minInclusive,
   stIntAssociatedPulseSegment._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntAssociatedPulseSegment', stIntAssociatedPulseSegment)
_module_typeBindings.stIntAssociatedPulseSegment = stIntAssociatedPulseSegment

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntPlatformTrackNumber
class stIntPlatformTrackNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntPlatformTrackNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 498, 2)
    _Documentation = ''
stIntPlatformTrackNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntPlatformTrackNumber, value=pyxb.binding.datatypes.int(1))
stIntPlatformTrackNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntPlatformTrackNumber, value=pyxb.binding.datatypes.int(32767))
stIntPlatformTrackNumber._InitializeFacetMap(stIntPlatformTrackNumber._CF_minInclusive,
   stIntPlatformTrackNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntPlatformTrackNumber', stIntPlatformTrackNumber)
_module_typeBindings.stIntPlatformTrackNumber = stIntPlatformTrackNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntNumberOfElevationLevels
class stIntNumberOfElevationLevels (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntNumberOfElevationLevels')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 510, 2)
    _Documentation = ''
stIntNumberOfElevationLevels._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntNumberOfElevationLevels, value=pyxb.binding.datatypes.int(1))
stIntNumberOfElevationLevels._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntNumberOfElevationLevels, value=pyxb.binding.datatypes.int(999))
stIntNumberOfElevationLevels._InitializeFacetMap(stIntNumberOfElevationLevels._CF_minInclusive,
   stIntNumberOfElevationLevels._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntNumberOfElevationLevels', stIntNumberOfElevationLevels)
_module_typeBindings.stIntNumberOfElevationLevels = stIntNumberOfElevationLevels

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntNumberOfBars
class stIntNumberOfBars (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntNumberOfBars')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 522, 2)
    _Documentation = ''
stIntNumberOfBars._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntNumberOfBars, value=pyxb.binding.datatypes.int(2))
stIntNumberOfBars._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntNumberOfBars, value=pyxb.binding.datatypes.int(100))
stIntNumberOfBars._InitializeFacetMap(stIntNumberOfBars._CF_minInclusive,
   stIntNumberOfBars._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntNumberOfBars', stIntNumberOfBars)
_module_typeBindings.stIntNumberOfBars = stIntNumberOfBars

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntDelayTimeModPeriodPulses
class stIntDelayTimeModPeriodPulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntDelayTimeModPeriodPulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 534, 2)
    _Documentation = ''
stIntDelayTimeModPeriodPulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntDelayTimeModPeriodPulses, value=pyxb.binding.datatypes.int(2))
stIntDelayTimeModPeriodPulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntDelayTimeModPeriodPulses, value=pyxb.binding.datatypes.int(268435455))
stIntDelayTimeModPeriodPulses._InitializeFacetMap(stIntDelayTimeModPeriodPulses._CF_minInclusive,
   stIntDelayTimeModPeriodPulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntDelayTimeModPeriodPulses', stIntDelayTimeModPeriodPulses)
_module_typeBindings.stIntDelayTimeModPeriodPulses = stIntDelayTimeModPeriodPulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntModPeriodPulses
class stIntModPeriodPulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntModPeriodPulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 546, 2)
    _Documentation = ''
stIntModPeriodPulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntModPeriodPulses, value=pyxb.binding.datatypes.int(2))
stIntModPeriodPulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntModPeriodPulses, value=pyxb.binding.datatypes.int(268435455))
stIntModPeriodPulses._InitializeFacetMap(stIntModPeriodPulses._CF_minInclusive,
   stIntModPeriodPulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntModPeriodPulses', stIntModPeriodPulses)
_module_typeBindings.stIntModPeriodPulses = stIntModPeriodPulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntInterpulseModulationPeriodPulses
class stIntInterpulseModulationPeriodPulses (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntInterpulseModulationPeriodPulses')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 558, 2)
    _Documentation = ''
stIntInterpulseModulationPeriodPulses._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntInterpulseModulationPeriodPulses, value=pyxb.binding.datatypes.int(2))
stIntInterpulseModulationPeriodPulses._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntInterpulseModulationPeriodPulses, value=pyxb.binding.datatypes.int(268435455))
stIntInterpulseModulationPeriodPulses._InitializeFacetMap(stIntInterpulseModulationPeriodPulses._CF_minInclusive,
   stIntInterpulseModulationPeriodPulses._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntInterpulseModulationPeriodPulses', stIntInterpulseModulationPeriodPulses)
_module_typeBindings.stIntInterpulseModulationPeriodPulses = stIntInterpulseModulationPeriodPulses

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntNumberOfRevolutions
class stIntNumberOfRevolutions (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntNumberOfRevolutions')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 570, 2)
    _Documentation = ''
stIntNumberOfRevolutions._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntNumberOfRevolutions, value=pyxb.binding.datatypes.int(2))
stIntNumberOfRevolutions._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntNumberOfRevolutions, value=pyxb.binding.datatypes.int(32))
stIntNumberOfRevolutions._InitializeFacetMap(stIntNumberOfRevolutions._CF_minInclusive,
   stIntNumberOfRevolutions._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntNumberOfRevolutions', stIntNumberOfRevolutions)
_module_typeBindings.stIntNumberOfRevolutions = stIntNumberOfRevolutions

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntScenarioRevision
class stIntScenarioRevision (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntScenarioRevision')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 582, 2)
    _Documentation = ''
stIntScenarioRevision._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stIntScenarioRevision', stIntScenarioRevision)
_module_typeBindings.stIntScenarioRevision = stIntScenarioRevision

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntSoftwareReleaseOfLastHeaderEdit
class stIntSoftwareReleaseOfLastHeaderEdit (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntSoftwareReleaseOfLastHeaderEdit')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 591, 2)
    _Documentation = ''
stIntSoftwareReleaseOfLastHeaderEdit._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stIntSoftwareReleaseOfLastHeaderEdit', stIntSoftwareReleaseOfLastHeaderEdit)
_module_typeBindings.stIntSoftwareReleaseOfLastHeaderEdit = stIntSoftwareReleaseOfLastHeaderEdit

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntDisplayServer
class stIntDisplayServer (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntDisplayServer')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 600, 2)
    _Documentation = ''
stIntDisplayServer._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stIntDisplayServer', stIntDisplayServer)
_module_typeBindings.stIntDisplayServer = stIntDisplayServer

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntDisplayId
class stIntDisplayId (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntDisplayId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 609, 2)
    _Documentation = ''
stIntDisplayId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stIntDisplayId', stIntDisplayId)
_module_typeBindings.stIntDisplayId = stIntDisplayId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntLowerGeneratorNumber
class stIntLowerGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntLowerGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 618, 2)
    _Documentation = ''
stIntLowerGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntLowerGeneratorNumber, value=pyxb.binding.datatypes.int(0))
stIntLowerGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntLowerGeneratorNumber, value=pyxb.binding.datatypes.int(2047))
stIntLowerGeneratorNumber._InitializeFacetMap(stIntLowerGeneratorNumber._CF_minInclusive,
   stIntLowerGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntLowerGeneratorNumber', stIntLowerGeneratorNumber)
_module_typeBindings.stIntLowerGeneratorNumber = stIntLowerGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntUpperGeneratorNumber
class stIntUpperGeneratorNumber (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntUpperGeneratorNumber')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 630, 2)
    _Documentation = ''
stIntUpperGeneratorNumber._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntUpperGeneratorNumber, value=pyxb.binding.datatypes.int(0))
stIntUpperGeneratorNumber._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntUpperGeneratorNumber, value=pyxb.binding.datatypes.int(2047))
stIntUpperGeneratorNumber._InitializeFacetMap(stIntUpperGeneratorNumber._CF_minInclusive,
   stIntUpperGeneratorNumber._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntUpperGeneratorNumber', stIntUpperGeneratorNumber)
_module_typeBindings.stIntUpperGeneratorNumber = stIntUpperGeneratorNumber

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stIntNavIfRtAddress
class stIntNavIfRtAddress (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stIntNavIfRtAddress')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 642, 2)
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 654, 2)
    _Documentation = ''
stIntNavIfRtSubAddress._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stIntNavIfRtSubAddress, value=pyxb.binding.datatypes.int(0))
stIntNavIfRtSubAddress._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stIntNavIfRtSubAddress, value=pyxb.binding.datatypes.int(31))
stIntNavIfRtSubAddress._InitializeFacetMap(stIntNavIfRtSubAddress._CF_minInclusive,
   stIntNavIfRtSubAddress._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stIntNavIfRtSubAddress', stIntNavIfRtSubAddress)
_module_typeBindings.stIntNavIfRtSubAddress = stIntNavIfRtSubAddress

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSecJitterLimit
class stDoubleSecJitterLimit (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSecJitterLimit')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 666, 2)
    _Documentation = ''
stDoubleSecJitterLimit._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSecJitterLimit, value=pyxb.binding.datatypes.double(2.3283e-16))
stDoubleSecJitterLimit._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSecJitterLimit, value=pyxb.binding.datatypes.double(9.9996948e-07))
stDoubleSecJitterLimit._InitializeFacetMap(stDoubleSecJitterLimit._CF_minInclusive,
   stDoubleSecJitterLimit._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSecJitterLimit', stDoubleSecJitterLimit)
_module_typeBindings.stDoubleSecJitterLimit = stDoubleSecJitterLimit

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSecModAmp
class stDoubleSecModAmp (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSecModAmp')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 678, 2)
    _Documentation = ''
stDoubleSecModAmp._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSecModAmp, value=pyxb.binding.datatypes.double(2.3283e-16))
stDoubleSecModAmp._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSecModAmp, value=pyxb.binding.datatypes.double(9.9996948e-07))
stDoubleSecModAmp._InitializeFacetMap(stDoubleSecModAmp._CF_minInclusive,
   stDoubleSecModAmp._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSecModAmp', stDoubleSecModAmp)
_module_typeBindings.stDoubleSecModAmp = stDoubleSecModAmp

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSecDtJitterLimit
class stDoubleSecDtJitterLimit (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSecDtJitterLimit')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 690, 2)
    _Documentation = ''
stDoubleSecDtJitterLimit._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSecDtJitterLimit, value=pyxb.binding.datatypes.double(2.3283e-16))
stDoubleSecDtJitterLimit._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSecDtJitterLimit, value=pyxb.binding.datatypes.double(9.9996948196e-07))
stDoubleSecDtJitterLimit._InitializeFacetMap(stDoubleSecDtJitterLimit._CF_minInclusive,
   stDoubleSecDtJitterLimit._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSecDtJitterLimit', stDoubleSecDtJitterLimit)
_module_typeBindings.stDoubleSecDtJitterLimit = stDoubleSecDtJitterLimit

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSecDtModAmp
class stDoubleSecDtModAmp (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSecDtModAmp')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 702, 2)
    _Documentation = ''
stDoubleSecDtModAmp._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSecDtModAmp, value=pyxb.binding.datatypes.double(2.3283e-16))
stDoubleSecDtModAmp._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSecDtModAmp, value=pyxb.binding.datatypes.double(9.9996948196e-07))
stDoubleSecDtModAmp._InitializeFacetMap(stDoubleSecDtModAmp._CF_minInclusive,
   stDoubleSecDtModAmp._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSecDtModAmp', stDoubleSecDtModAmp)
_module_typeBindings.stDoubleSecDtModAmp = stDoubleSecDtModAmp

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePriCrystalValue
class stDoublePriCrystalValue (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePriCrystalValue')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 714, 2)
    _Documentation = ''
stDoublePriCrystalValue._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePriCrystalValue, value=pyxb.binding.datatypes.double(2.3283e-16))
stDoublePriCrystalValue._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePriCrystalValue, value=pyxb.binding.datatypes.double(0.00051199998474121))
stDoublePriCrystalValue._InitializeFacetMap(stDoublePriCrystalValue._CF_minInclusive,
   stDoublePriCrystalValue._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePriCrystalValue', stDoublePriCrystalValue)
_module_typeBindings.stDoublePriCrystalValue = stDoublePriCrystalValue

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleRasterFlybackTime
class stDoubleRasterFlybackTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleRasterFlybackTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 726, 2)
    _Documentation = ''
stDoubleRasterFlybackTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleRasterFlybackTime, value=pyxb.binding.datatypes.double(1e-06))
stDoubleRasterFlybackTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleRasterFlybackTime, value=pyxb.binding.datatypes.double(120.0))
stDoubleRasterFlybackTime._InitializeFacetMap(stDoubleRasterFlybackTime._CF_minInclusive,
   stDoubleRasterFlybackTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleRasterFlybackTime', stDoubleRasterFlybackTime)
_module_typeBindings.stDoubleRasterFlybackTime = stDoubleRasterFlybackTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePalmerRate
class stDoublePalmerRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePalmerRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 738, 2)
    _Documentation = ''
stDoublePalmerRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePalmerRate, value=pyxb.binding.datatypes.double(0.0002328))
stDoublePalmerRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePalmerRate, value=pyxb.binding.datatypes.double(31250.0))
stDoublePalmerRate._InitializeFacetMap(stDoublePalmerRate._CF_minInclusive,
   stDoublePalmerRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePalmerRate', stDoublePalmerRate)
_module_typeBindings.stDoublePalmerRate = stDoublePalmerRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePolarizationModRate
class stDoublePolarizationModRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePolarizationModRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 750, 2)
    _Documentation = ''
stDoublePolarizationModRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePolarizationModRate, value=pyxb.binding.datatypes.double(0.0002328))
stDoublePolarizationModRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePolarizationModRate, value=pyxb.binding.datatypes.double(31250.0))
stDoublePolarizationModRate._InitializeFacetMap(stDoublePolarizationModRate._CF_minInclusive,
   stDoublePolarizationModRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePolarizationModRate', stDoublePolarizationModRate)
_module_typeBindings.stDoublePolarizationModRate = stDoublePolarizationModRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleConicalModRate
class stDoubleConicalModRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleConicalModRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 762, 2)
    _Documentation = ''
stDoubleConicalModRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleConicalModRate, value=pyxb.binding.datatypes.double(0.0002328))
stDoubleConicalModRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleConicalModRate, value=pyxb.binding.datatypes.double(31250.0))
stDoubleConicalModRate._InitializeFacetMap(stDoubleConicalModRate._CF_minInclusive,
   stDoubleConicalModRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleConicalModRate', stDoubleConicalModRate)
_module_typeBindings.stDoubleConicalModRate = stDoubleConicalModRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSpiralModulationRate
class stDoubleSpiralModulationRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSpiralModulationRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 774, 2)
    _Documentation = ''
stDoubleSpiralModulationRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSpiralModulationRate, value=pyxb.binding.datatypes.double(0.0002328))
stDoubleSpiralModulationRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSpiralModulationRate, value=pyxb.binding.datatypes.double(31250.0))
stDoubleSpiralModulationRate._InitializeFacetMap(stDoubleSpiralModulationRate._CF_minInclusive,
   stDoubleSpiralModulationRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSpiralModulationRate', stDoubleSpiralModulationRate)
_module_typeBindings.stDoubleSpiralModulationRate = stDoubleSpiralModulationRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElScanPeriod
class stDoubleElScanPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElScanPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 786, 2)
    _Documentation = ''
stDoubleElScanPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElScanPeriod, value=pyxb.binding.datatypes.double(0.000256))
stDoubleElScanPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElScanPeriod, value=pyxb.binding.datatypes.double(1073.741824))
stDoubleElScanPeriod._InitializeFacetMap(stDoubleElScanPeriod._CF_minInclusive,
   stDoubleElScanPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElScanPeriod', stDoubleElScanPeriod)
_module_typeBindings.stDoubleElScanPeriod = stDoubleElScanPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleHelicalScanPeriod
class stDoubleHelicalScanPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleHelicalScanPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 798, 2)
    _Documentation = ''
stDoubleHelicalScanPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleHelicalScanPeriod, value=pyxb.binding.datatypes.double(0.000256))
stDoubleHelicalScanPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleHelicalScanPeriod, value=pyxb.binding.datatypes.double(1073.741824))
stDoubleHelicalScanPeriod._InitializeFacetMap(stDoubleHelicalScanPeriod._CF_minInclusive,
   stDoubleHelicalScanPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleHelicalScanPeriod', stDoubleHelicalScanPeriod)
_module_typeBindings.stDoubleHelicalScanPeriod = stDoubleHelicalScanPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzScanPeriod
class stDoubleAzScanPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzScanPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 810, 2)
    _Documentation = ''
stDoubleAzScanPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzScanPeriod, value=pyxb.binding.datatypes.double(0.000511984375))
stDoubleAzScanPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzScanPeriod, value=pyxb.binding.datatypes.double(2147.418112))
stDoubleAzScanPeriod._InitializeFacetMap(stDoubleAzScanPeriod._CF_minInclusive,
   stDoubleAzScanPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzScanPeriod', stDoubleAzScanPeriod)
_module_typeBindings.stDoubleAzScanPeriod = stDoubleAzScanPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePulseWidth
class stDoublePulseWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePulseWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 822, 2)
    _Documentation = ''
stDoublePulseWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePulseWidth, value=pyxb.binding.datatypes.double(3.90625e-09))
stDoublePulseWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePulseWidth, value=pyxb.binding.datatypes.double(0.13107199609375))
stDoublePulseWidth._InitializeFacetMap(stDoublePulseWidth._CF_minInclusive,
   stDoublePulseWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePulseWidth', stDoublePulseWidth)
_module_typeBindings.stDoublePulseWidth = stDoublePulseWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleJitterLimitPulse
class stDoubleJitterLimitPulse (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleJitterLimitPulse')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 834, 2)
    _Documentation = ''
stDoubleJitterLimitPulse._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleJitterLimitPulse, value=pyxb.binding.datatypes.double(3.90625e-09))
stDoubleJitterLimitPulse._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleJitterLimitPulse, value=pyxb.binding.datatypes.double(0.06553599609375))
stDoubleJitterLimitPulse._InitializeFacetMap(stDoubleJitterLimitPulse._CF_minInclusive,
   stDoubleJitterLimitPulse._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleJitterLimitPulse', stDoubleJitterLimitPulse)
_module_typeBindings.stDoubleJitterLimitPulse = stDoubleJitterLimitPulse

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStaggerModDwellTime
class stDoubleStaggerModDwellTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStaggerModDwellTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 846, 2)
    _Documentation = ''
stDoubleStaggerModDwellTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStaggerModDwellTime, value=pyxb.binding.datatypes.double(3.91e-09))
stDoubleStaggerModDwellTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStaggerModDwellTime, value=pyxb.binding.datatypes.double(0.131071996))
stDoubleStaggerModDwellTime._InitializeFacetMap(stDoubleStaggerModDwellTime._CF_minInclusive,
   stDoubleStaggerModDwellTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStaggerModDwellTime', stDoubleStaggerModDwellTime)
_module_typeBindings.stDoubleStaggerModDwellTime = stDoubleStaggerModDwellTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleHfimSize
class stDoubleHfimSize (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleHfimSize')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 858, 2)
    _Documentation = ''
stDoubleHfimSize._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleHfimSize, value=pyxb.binding.datatypes.double(2e-08))
stDoubleHfimSize._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleHfimSize, value=pyxb.binding.datatypes.double(0.065535))
stDoubleHfimSize._InitializeFacetMap(stDoubleHfimSize._CF_minInclusive,
   stDoubleHfimSize._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleHfimSize', stDoubleHfimSize)
_module_typeBindings.stDoubleHfimSize = stDoubleHfimSize

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElSectorWidth
class stDoubleElSectorWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElSectorWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 870, 2)
    _Documentation = ''
stDoubleElSectorWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElSectorWidth, value=pyxb.binding.datatypes.double(0.02197))
stDoubleElSectorWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElSectorWidth, value=pyxb.binding.datatypes.double(180.0))
stDoubleElSectorWidth._InitializeFacetMap(stDoubleElSectorWidth._CF_minInclusive,
   stDoubleElSectorWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElSectorWidth', stDoubleElSectorWidth)
_module_typeBindings.stDoubleElSectorWidth = stDoubleElSectorWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleHelicalSectorWidth
class stDoubleHelicalSectorWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleHelicalSectorWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 882, 2)
    _Documentation = ''
stDoubleHelicalSectorWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleHelicalSectorWidth, value=pyxb.binding.datatypes.double(0.02197))
stDoubleHelicalSectorWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleHelicalSectorWidth, value=pyxb.binding.datatypes.double(180.0))
stDoubleHelicalSectorWidth._InitializeFacetMap(stDoubleHelicalSectorWidth._CF_minInclusive,
   stDoubleHelicalSectorWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleHelicalSectorWidth', stDoubleHelicalSectorWidth)
_module_typeBindings.stDoubleHelicalSectorWidth = stDoubleHelicalSectorWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzSectorWidth
class stDoubleAzSectorWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzSectorWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 894, 2)
    _Documentation = ''
stDoubleAzSectorWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzSectorWidth, value=pyxb.binding.datatypes.double(0.02197))
stDoubleAzSectorWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzSectorWidth, value=pyxb.binding.datatypes.double(359.978))
stDoubleAzSectorWidth._InitializeFacetMap(stDoubleAzSectorWidth._CF_minInclusive,
   stDoubleAzSectorWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzSectorWidth', stDoubleAzSectorWidth)
_module_typeBindings.stDoubleAzSectorWidth = stDoubleAzSectorWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBarWidth
class stDoubleBarWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBarWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 906, 2)
    _Documentation = ''
stDoubleBarWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBarWidth, value=pyxb.binding.datatypes.double(0.02197))
stDoubleBarWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBarWidth, value=pyxb.binding.datatypes.double(359.978))
stDoubleBarWidth._InitializeFacetMap(stDoubleBarWidth._CF_minInclusive,
   stDoubleBarWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBarWidth', stDoubleBarWidth)
_module_typeBindings.stDoubleBarWidth = stDoubleBarWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleCoverageAngle
class stDoubleCoverageAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleCoverageAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 918, 2)
    _Documentation = ''
stDoubleCoverageAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleCoverageAngle, value=pyxb.binding.datatypes.double(0.02197))
stDoubleCoverageAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleCoverageAngle, value=pyxb.binding.datatypes.double(359.978))
stDoubleCoverageAngle._InitializeFacetMap(stDoubleCoverageAngle._CF_minInclusive,
   stDoubleCoverageAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleCoverageAngle', stDoubleCoverageAngle)
_module_typeBindings.stDoubleCoverageAngle = stDoubleCoverageAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstPri
class stDoubleBurstPri (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstPri')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 930, 2)
    _Documentation = ''
stDoubleBurstPri._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstPri, value=pyxb.binding.datatypes.double(1.5625e-08))
stDoubleBurstPri._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstPri, value=pyxb.binding.datatypes.double(0.001024))
stDoubleBurstPri._InitializeFacetMap(stDoubleBurstPri._CF_minInclusive,
   stDoubleBurstPri._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstPri', stDoubleBurstPri)
_module_typeBindings.stDoubleBurstPri = stDoubleBurstPri

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstModBasePri
class stDoubleBurstModBasePri (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstModBasePri')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 942, 2)
    _Documentation = ''
stDoubleBurstModBasePri._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstModBasePri, value=pyxb.binding.datatypes.double(1.5625e-08))
stDoubleBurstModBasePri._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstModBasePri, value=pyxb.binding.datatypes.double(0.001024))
stDoubleBurstModBasePri._InitializeFacetMap(stDoubleBurstModBasePri._CF_minInclusive,
   stDoubleBurstModBasePri._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstModBasePri', stDoubleBurstModBasePri)
_module_typeBindings.stDoubleBurstModBasePri = stDoubleBurstModBasePri

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstPulseWidth
class stDoubleBurstPulseWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstPulseWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 954, 2)
    _Documentation = ''
stDoubleBurstPulseWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstPulseWidth, value=pyxb.binding.datatypes.double(7.8125e-09))
stDoubleBurstPulseWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstPulseWidth, value=pyxb.binding.datatypes.double(0.000512))
stDoubleBurstPulseWidth._InitializeFacetMap(stDoubleBurstPulseWidth._CF_minInclusive,
   stDoubleBurstPulseWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstPulseWidth', stDoubleBurstPulseWidth)
_module_typeBindings.stDoubleBurstPulseWidth = stDoubleBurstPulseWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstModPulseWidth
class stDoubleBurstModPulseWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstModPulseWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 966, 2)
    _Documentation = ''
stDoubleBurstModPulseWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstModPulseWidth, value=pyxb.binding.datatypes.double(7.8125e-09))
stDoubleBurstModPulseWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstModPulseWidth, value=pyxb.binding.datatypes.double(0.000512))
stDoubleBurstModPulseWidth._InitializeFacetMap(stDoubleBurstModPulseWidth._CF_minInclusive,
   stDoubleBurstModPulseWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstModPulseWidth', stDoubleBurstModPulseWidth)
_module_typeBindings.stDoubleBurstModPulseWidth = stDoubleBurstModPulseWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAmplitudeCellSize
class stDoubleAmplitudeCellSize (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAmplitudeCellSize')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 978, 2)
    _Documentation = ''
stDoubleAmplitudeCellSize._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAmplitudeCellSize, value=pyxb.binding.datatypes.double(7.8125e-09))
stDoubleAmplitudeCellSize._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAmplitudeCellSize, value=pyxb.binding.datatypes.double(0.131072))
stDoubleAmplitudeCellSize._InitializeFacetMap(stDoubleAmplitudeCellSize._CF_minInclusive,
   stDoubleAmplitudeCellSize._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAmplitudeCellSize', stDoubleAmplitudeCellSize)
_module_typeBindings.stDoubleAmplitudeCellSize = stDoubleAmplitudeCellSize

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleFrequencyCellSize
class stDoubleFrequencyCellSize (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleFrequencyCellSize')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 990, 2)
    _Documentation = ''
stDoubleFrequencyCellSize._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleFrequencyCellSize, value=pyxb.binding.datatypes.double(7.8125e-09))
stDoubleFrequencyCellSize._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleFrequencyCellSize, value=pyxb.binding.datatypes.double(0.131072))
stDoubleFrequencyCellSize._InitializeFacetMap(stDoubleFrequencyCellSize._CF_minInclusive,
   stDoubleFrequencyCellSize._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleFrequencyCellSize', stDoubleFrequencyCellSize)
_module_typeBindings.stDoubleFrequencyCellSize = stDoubleFrequencyCellSize

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePhaseCellSize
class stDoublePhaseCellSize (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePhaseCellSize')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1002, 2)
    _Documentation = ''
stDoublePhaseCellSize._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePhaseCellSize, value=pyxb.binding.datatypes.double(7.8125e-09))
stDoublePhaseCellSize._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePhaseCellSize, value=pyxb.binding.datatypes.double(0.131072))
stDoublePhaseCellSize._InitializeFacetMap(stDoublePhaseCellSize._CF_minInclusive,
   stDoublePhaseCellSize._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePhaseCellSize', stDoublePhaseCellSize)
_module_typeBindings.stDoublePhaseCellSize = stDoublePhaseCellSize

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLinearFreqDuration
class stDoubleLinearFreqDuration (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLinearFreqDuration')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1014, 2)
    _Documentation = ''
stDoubleLinearFreqDuration._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLinearFreqDuration, value=pyxb.binding.datatypes.double(7.8125e-09))
stDoubleLinearFreqDuration._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLinearFreqDuration, value=pyxb.binding.datatypes.double(0.131072))
stDoubleLinearFreqDuration._InitializeFacetMap(stDoubleLinearFreqDuration._CF_minInclusive,
   stDoubleLinearFreqDuration._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLinearFreqDuration', stDoubleLinearFreqDuration)
_module_typeBindings.stDoubleLinearFreqDuration = stDoubleLinearFreqDuration

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstModDeviation
class stDoubleBurstModDeviation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstModDeviation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1026, 2)
    _Documentation = ''
stDoubleBurstModDeviation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstModDeviation, value=pyxb.binding.datatypes.double(1.5625e-08))
stDoubleBurstModDeviation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstModDeviation, value=pyxb.binding.datatypes.double(0.001023984375))
stDoubleBurstModDeviation._InitializeFacetMap(stDoubleBurstModDeviation._CF_minInclusive,
   stDoubleBurstModDeviation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstModDeviation', stDoubleBurstModDeviation)
_module_typeBindings.stDoubleBurstModDeviation = stDoubleBurstModDeviation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstDwell
class stDoubleBurstDwell (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstDwell')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1038, 2)
    _Documentation = ''
stDoubleBurstDwell._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstDwell, value=pyxb.binding.datatypes.double(1.5625e-08))
stDoubleBurstDwell._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstDwell, value=pyxb.binding.datatypes.double(0.1310719921875))
stDoubleBurstDwell._InitializeFacetMap(stDoubleBurstDwell._CF_minInclusive,
   stDoubleBurstDwell._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstDwell', stDoubleBurstDwell)
_module_typeBindings.stDoubleBurstDwell = stDoubleBurstDwell

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstModDwell
class stDoubleBurstModDwell (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstModDwell')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1050, 2)
    _Documentation = ''
stDoubleBurstModDwell._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstModDwell, value=pyxb.binding.datatypes.double(1.5625e-08))
stDoubleBurstModDwell._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstModDwell, value=pyxb.binding.datatypes.double(0.1310719921875))
stDoubleBurstModDwell._InitializeFacetMap(stDoubleBurstModDwell._CF_minInclusive,
   stDoubleBurstModDwell._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstModDwell', stDoubleBurstModDwell)
_module_typeBindings.stDoubleBurstModDwell = stDoubleBurstModDwell

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStaggerModDwellTimeSinglePulse
class stDoubleStaggerModDwellTimeSinglePulse (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStaggerModDwellTimeSinglePulse')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1062, 2)
    _Documentation = ''
stDoubleStaggerModDwellTimeSinglePulse._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStaggerModDwellTimeSinglePulse, value=pyxb.binding.datatypes.double(1.5625e-08))
stDoubleStaggerModDwellTimeSinglePulse._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStaggerModDwellTimeSinglePulse, value=pyxb.binding.datatypes.double(0.1310719921875))
stDoubleStaggerModDwellTimeSinglePulse._InitializeFacetMap(stDoubleStaggerModDwellTimeSinglePulse._CF_minInclusive,
   stDoubleStaggerModDwellTimeSinglePulse._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStaggerModDwellTimeSinglePulse', stDoubleStaggerModDwellTimeSinglePulse)
_module_typeBindings.stDoubleStaggerModDwellTimeSinglePulse = stDoubleStaggerModDwellTimeSinglePulse

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstPulseDuration
class stDoubleBurstPulseDuration (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstPulseDuration')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1074, 2)
    _Documentation = ''
stDoubleBurstPulseDuration._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstPulseDuration, value=pyxb.binding.datatypes.double(1.5625e-08))
stDoubleBurstPulseDuration._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstPulseDuration, value=pyxb.binding.datatypes.double(0.1310719921875))
stDoubleBurstPulseDuration._InitializeFacetMap(stDoubleBurstPulseDuration._CF_minInclusive,
   stDoubleBurstPulseDuration._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstPulseDuration', stDoubleBurstPulseDuration)
_module_typeBindings.stDoubleBurstPulseDuration = stDoubleBurstPulseDuration

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBarScanRate
class stDoubleBarScanRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBarScanRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1086, 2)
    _Documentation = ''
stDoubleBarScanRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBarScanRate, value=pyxb.binding.datatypes.double(0.1676))
stDoubleBarScanRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBarScanRate, value=pyxb.binding.datatypes.double(703125.0))
stDoubleBarScanRate._InitializeFacetMap(stDoubleBarScanRate._CF_minInclusive,
   stDoubleBarScanRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBarScanRate', stDoubleBarScanRate)
_module_typeBindings.stDoubleBarScanRate = stDoubleBarScanRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSwitchDelayTime
class stDoubleSwitchDelayTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSwitchDelayTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1098, 2)
    _Documentation = ''
stDoubleSwitchDelayTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSwitchDelayTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleSwitchDelayTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSwitchDelayTime, value=pyxb.binding.datatypes.double(0.001))
stDoubleSwitchDelayTime._InitializeFacetMap(stDoubleSwitchDelayTime._CF_minInclusive,
   stDoubleSwitchDelayTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSwitchDelayTime', stDoubleSwitchDelayTime)
_module_typeBindings.stDoubleSwitchDelayTime = stDoubleSwitchDelayTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDwellVariation
class stDoubleDwellVariation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDwellVariation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1110, 2)
    _Documentation = ''
stDoubleDwellVariation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDwellVariation, value=pyxb.binding.datatypes.double(0.0))
stDoubleDwellVariation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDwellVariation, value=pyxb.binding.datatypes.double(0.065535))
stDoubleDwellVariation._InitializeFacetMap(stDoubleDwellVariation._CF_minInclusive,
   stDoubleDwellVariation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDwellVariation', stDoubleDwellVariation)
_module_typeBindings.stDoubleDwellVariation = stDoubleDwellVariation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzFlybackTime
class stDoubleAzFlybackTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzFlybackTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1122, 2)
    _Documentation = ''
stDoubleAzFlybackTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzFlybackTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleAzFlybackTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzFlybackTime, value=pyxb.binding.datatypes.double(120.0))
stDoubleAzFlybackTime._InitializeFacetMap(stDoubleAzFlybackTime._CF_minInclusive,
   stDoubleAzFlybackTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzFlybackTime', stDoubleAzFlybackTime)
_module_typeBindings.stDoubleAzFlybackTime = stDoubleAzFlybackTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElFlybackTime
class stDoubleElFlybackTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElFlybackTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1134, 2)
    _Documentation = ''
stDoubleElFlybackTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElFlybackTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleElFlybackTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElFlybackTime, value=pyxb.binding.datatypes.double(120.0))
stDoubleElFlybackTime._InitializeFacetMap(stDoubleElFlybackTime._CF_minInclusive,
   stDoubleElFlybackTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElFlybackTime', stDoubleElFlybackTime)
_module_typeBindings.stDoubleElFlybackTime = stDoubleElFlybackTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleFlybackTime
class stDoubleFlybackTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleFlybackTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1146, 2)
    _Documentation = ''
stDoubleFlybackTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleFlybackTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleFlybackTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleFlybackTime, value=pyxb.binding.datatypes.double(120.0))
stDoubleFlybackTime._InitializeFacetMap(stDoubleFlybackTime._CF_minInclusive,
   stDoubleFlybackTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleFlybackTime', stDoubleFlybackTime)
_module_typeBindings.stDoubleFlybackTime = stDoubleFlybackTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleTransmitAttenuation
class stDoubleTransmitAttenuation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleTransmitAttenuation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1158, 2)
    _Documentation = ''
stDoubleTransmitAttenuation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleTransmitAttenuation, value=pyxb.binding.datatypes.double(0.0))
stDoubleTransmitAttenuation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleTransmitAttenuation, value=pyxb.binding.datatypes.double(127.75))
stDoubleTransmitAttenuation._InitializeFacetMap(stDoubleTransmitAttenuation._CF_minInclusive,
   stDoubleTransmitAttenuation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleTransmitAttenuation', stDoubleTransmitAttenuation)
_module_typeBindings.stDoubleTransmitAttenuation = stDoubleTransmitAttenuation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleHighRange
class stDoubleHighRange (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleHighRange')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1170, 2)
    _Documentation = ''
stDoubleHighRange._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleHighRange, value=pyxb.binding.datatypes.double(0.0))
stDoubleHighRange._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleHighRange, value=pyxb.binding.datatypes.double(14724656.0))
stDoubleHighRange._InitializeFacetMap(stDoubleHighRange._CF_minInclusive,
   stDoubleHighRange._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleHighRange', stDoubleHighRange)
_module_typeBindings.stDoubleHighRange = stDoubleHighRange

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleFrequencyOffset
class stDoubleFrequencyOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleFrequencyOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1182, 2)
    _Documentation = ''
stDoubleFrequencyOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleFrequencyOffset, value=pyxb.binding.datatypes.double(-16000000000.0))
stDoubleFrequencyOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleFrequencyOffset, value=pyxb.binding.datatypes.double(16000000000.0))
stDoubleFrequencyOffset._InitializeFacetMap(stDoubleFrequencyOffset._CF_minInclusive,
   stDoubleFrequencyOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleFrequencyOffset', stDoubleFrequencyOffset)
_module_typeBindings.stDoubleFrequencyOffset = stDoubleFrequencyOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleNoiseBandwidth
class stDoubleNoiseBandwidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleNoiseBandwidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1194, 2)
    _Documentation = ''
stDoubleNoiseBandwidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleNoiseBandwidth, value=pyxb.binding.datatypes.double(0.0))
stDoubleNoiseBandwidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleNoiseBandwidth, value=pyxb.binding.datatypes.double(2000000000.0))
stDoubleNoiseBandwidth._InitializeFacetMap(stDoubleNoiseBandwidth._CF_minInclusive,
   stDoubleNoiseBandwidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleNoiseBandwidth', stDoubleNoiseBandwidth)
_module_typeBindings.stDoubleNoiseBandwidth = stDoubleNoiseBandwidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDwellTime
class stDoubleDwellTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDwellTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1206, 2)
    _Documentation = ''
stDoubleDwellTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDwellTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleDwellTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDwellTime, value=pyxb.binding.datatypes.double(2147.483647))
stDoubleDwellTime._InitializeFacetMap(stDoubleDwellTime._CF_minInclusive,
   stDoubleDwellTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDwellTime', stDoubleDwellTime)
_module_typeBindings.stDoubleDwellTime = stDoubleDwellTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleInterruptGeneratorDuration
class stDoubleInterruptGeneratorDuration (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleInterruptGeneratorDuration')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1218, 2)
    _Documentation = ''
stDoubleInterruptGeneratorDuration._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleInterruptGeneratorDuration, value=pyxb.binding.datatypes.double(0.0))
stDoubleInterruptGeneratorDuration._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleInterruptGeneratorDuration, value=pyxb.binding.datatypes.double(2147.483647996))
stDoubleInterruptGeneratorDuration._InitializeFacetMap(stDoubleInterruptGeneratorDuration._CF_minInclusive,
   stDoubleInterruptGeneratorDuration._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleInterruptGeneratorDuration', stDoubleInterruptGeneratorDuration)
_module_typeBindings.stDoubleInterruptGeneratorDuration = stDoubleInterruptGeneratorDuration

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleInterruptGeneratorRevisit
class stDoubleInterruptGeneratorRevisit (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleInterruptGeneratorRevisit')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1230, 2)
    _Documentation = ''
stDoubleInterruptGeneratorRevisit._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleInterruptGeneratorRevisit, value=pyxb.binding.datatypes.double(0.0))
stDoubleInterruptGeneratorRevisit._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleInterruptGeneratorRevisit, value=pyxb.binding.datatypes.double(2147.483647996))
stDoubleInterruptGeneratorRevisit._InitializeFacetMap(stDoubleInterruptGeneratorRevisit._CF_minInclusive,
   stDoubleInterruptGeneratorRevisit._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleInterruptGeneratorRevisit', stDoubleInterruptGeneratorRevisit)
_module_typeBindings.stDoubleInterruptGeneratorRevisit = stDoubleInterruptGeneratorRevisit

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleInterruptGeneratorStartTime
class stDoubleInterruptGeneratorStartTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleInterruptGeneratorStartTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1242, 2)
    _Documentation = ''
stDoubleInterruptGeneratorStartTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleInterruptGeneratorStartTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleInterruptGeneratorStartTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleInterruptGeneratorStartTime, value=pyxb.binding.datatypes.double(2147.483647996))
stDoubleInterruptGeneratorStartTime._InitializeFacetMap(stDoubleInterruptGeneratorStartTime._CF_minInclusive,
   stDoubleInterruptGeneratorStartTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleInterruptGeneratorStartTime', stDoubleInterruptGeneratorStartTime)
_module_typeBindings.stDoubleInterruptGeneratorStartTime = stDoubleInterruptGeneratorStartTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAttenuation
class stDoubleAttenuation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAttenuation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1254, 2)
    _Documentation = ''
stDoubleAttenuation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAttenuation, value=pyxb.binding.datatypes.double(0.0))
stDoubleAttenuation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAttenuation, value=pyxb.binding.datatypes.double(31.5))
stDoubleAttenuation._InitializeFacetMap(stDoubleAttenuation._CF_minInclusive,
   stDoubleAttenuation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAttenuation', stDoubleAttenuation)
_module_typeBindings.stDoubleAttenuation = stDoubleAttenuation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleModAmpFrequency
class stDoubleModAmpFrequency (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleModAmpFrequency')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1266, 2)
    _Documentation = ''
stDoubleModAmpFrequency._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleModAmpFrequency, value=pyxb.binding.datatypes.double(0.0))
stDoubleModAmpFrequency._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleModAmpFrequency, value=pyxb.binding.datatypes.double(32000000000.0))
stDoubleModAmpFrequency._InitializeFacetMap(stDoubleModAmpFrequency._CF_minInclusive,
   stDoubleModAmpFrequency._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleModAmpFrequency', stDoubleModAmpFrequency)
_module_typeBindings.stDoubleModAmpFrequency = stDoubleModAmpFrequency

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDelayTimeModAmp
class stDoubleDelayTimeModAmp (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDelayTimeModAmp')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1278, 2)
    _Documentation = ''
stDoubleDelayTimeModAmp._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDelayTimeModAmp, value=pyxb.binding.datatypes.double(0.0))
stDoubleDelayTimeModAmp._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDelayTimeModAmp, value=pyxb.binding.datatypes.double(0.032))
stDoubleDelayTimeModAmp._InitializeFacetMap(stDoubleDelayTimeModAmp._CF_minInclusive,
   stDoubleDelayTimeModAmp._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDelayTimeModAmp', stDoubleDelayTimeModAmp)
_module_typeBindings.stDoubleDelayTimeModAmp = stDoubleDelayTimeModAmp

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzInitialBeamOffset
class stDoubleAzInitialBeamOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzInitialBeamOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1290, 2)
    _Documentation = ''
stDoubleAzInitialBeamOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzInitialBeamOffset, value=pyxb.binding.datatypes.double(0.0))
stDoubleAzInitialBeamOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzInitialBeamOffset, value=pyxb.binding.datatypes.double(359.978))
stDoubleAzInitialBeamOffset._InitializeFacetMap(stDoubleAzInitialBeamOffset._CF_minInclusive,
   stDoubleAzInitialBeamOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzInitialBeamOffset', stDoubleAzInitialBeamOffset)
_module_typeBindings.stDoubleAzInitialBeamOffset = stDoubleAzInitialBeamOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleInitialBeamOffset
class stDoubleInitialBeamOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleInitialBeamOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1302, 2)
    _Documentation = ''
stDoubleInitialBeamOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleInitialBeamOffset, value=pyxb.binding.datatypes.double(0.0))
stDoubleInitialBeamOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleInitialBeamOffset, value=pyxb.binding.datatypes.double(359.978))
stDoubleInitialBeamOffset._InitializeFacetMap(stDoubleInitialBeamOffset._CF_minInclusive,
   stDoubleInitialBeamOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleInitialBeamOffset', stDoubleInitialBeamOffset)
_module_typeBindings.stDoubleInitialBeamOffset = stDoubleInitialBeamOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePalmerInitialOffset
class stDoublePalmerInitialOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePalmerInitialOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1314, 2)
    _Documentation = ''
stDoublePalmerInitialOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePalmerInitialOffset, value=pyxb.binding.datatypes.double(0.0))
stDoublePalmerInitialOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePalmerInitialOffset, value=pyxb.binding.datatypes.double(359.978))
stDoublePalmerInitialOffset._InitializeFacetMap(stDoublePalmerInitialOffset._CF_minInclusive,
   stDoublePalmerInitialOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePalmerInitialOffset', stDoublePalmerInitialOffset)
_module_typeBindings.stDoublePalmerInitialOffset = stDoublePalmerInitialOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzBeamwidth
class stDoubleAzBeamwidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzBeamwidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1326, 2)
    _Documentation = ''
stDoubleAzBeamwidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzBeamwidth, value=pyxb.binding.datatypes.double(0.0))
stDoubleAzBeamwidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzBeamwidth, value=pyxb.binding.datatypes.double(360.0))
stDoubleAzBeamwidth._InitializeFacetMap(stDoubleAzBeamwidth._CF_minInclusive,
   stDoubleAzBeamwidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzBeamwidth', stDoubleAzBeamwidth)
_module_typeBindings.stDoubleAzBeamwidth = stDoubleAzBeamwidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerAz
class stDoubleLowerAz (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerAz')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1338, 2)
    _Documentation = ''
stDoubleLowerAz._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerAz, value=pyxb.binding.datatypes.double(0.0))
stDoubleLowerAz._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerAz, value=pyxb.binding.datatypes.double(360.0))
stDoubleLowerAz._InitializeFacetMap(stDoubleLowerAz._CF_minInclusive,
   stDoubleLowerAz._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerAz', stDoubleLowerAz)
_module_typeBindings.stDoubleLowerAz = stDoubleLowerAz

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperAz
class stDoubleUpperAz (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperAz')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1350, 2)
    _Documentation = ''
stDoubleUpperAz._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperAz, value=pyxb.binding.datatypes.double(0.0))
stDoubleUpperAz._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperAz, value=pyxb.binding.datatypes.double(360.0))
stDoubleUpperAz._InitializeFacetMap(stDoubleUpperAz._CF_minInclusive,
   stDoubleUpperAz._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperAz', stDoubleUpperAz)
_module_typeBindings.stDoubleUpperAz = stDoubleUpperAz

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDelayTimeJitterLimit
class stDoubleDelayTimeJitterLimit (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDelayTimeJitterLimit')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1362, 2)
    _Documentation = ''
stDoubleDelayTimeJitterLimit._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDelayTimeJitterLimit, value=pyxb.binding.datatypes.double(0.0))
stDoubleDelayTimeJitterLimit._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDelayTimeJitterLimit, value=pyxb.binding.datatypes.double(0.499998))
stDoubleDelayTimeJitterLimit._InitializeFacetMap(stDoubleDelayTimeJitterLimit._CF_minInclusive,
   stDoubleDelayTimeJitterLimit._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDelayTimeJitterLimit', stDoubleDelayTimeJitterLimit)
_module_typeBindings.stDoubleDelayTimeJitterLimit = stDoubleDelayTimeJitterLimit

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleJitterLimitPri
class stDoubleJitterLimitPri (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleJitterLimitPri')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1374, 2)
    _Documentation = ''
stDoubleJitterLimitPri._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleJitterLimitPri, value=pyxb.binding.datatypes.double(0.0))
stDoubleJitterLimitPri._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleJitterLimitPri, value=pyxb.binding.datatypes.double(0.499998))
stDoubleJitterLimitPri._InitializeFacetMap(stDoubleJitterLimitPri._CF_minInclusive,
   stDoubleJitterLimitPri._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleJitterLimitPri', stDoubleJitterLimitPri)
_module_typeBindings.stDoubleJitterLimitPri = stDoubleJitterLimitPri

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleClockedPriJitterExcursion
class stDoubleClockedPriJitterExcursion (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleClockedPriJitterExcursion')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1386, 2)
    _Documentation = ''
stDoubleClockedPriJitterExcursion._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleClockedPriJitterExcursion, value=pyxb.binding.datatypes.double(0.0))
stDoubleClockedPriJitterExcursion._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleClockedPriJitterExcursion, value=pyxb.binding.datatypes.double(0.499998))
stDoubleClockedPriJitterExcursion._InitializeFacetMap(stDoubleClockedPriJitterExcursion._CF_minInclusive,
   stDoubleClockedPriJitterExcursion._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleClockedPriJitterExcursion', stDoubleClockedPriJitterExcursion)
_module_typeBindings.stDoubleClockedPriJitterExcursion = stDoubleClockedPriJitterExcursion

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAgilityLimit
class stDoubleAgilityLimit (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAgilityLimit')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1398, 2)
    _Documentation = ''
stDoubleAgilityLimit._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAgilityLimit, value=pyxb.binding.datatypes.double(0.0))
stDoubleAgilityLimit._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAgilityLimit, value=pyxb.binding.datatypes.double(65499940000.0))
stDoubleAgilityLimit._InitializeFacetMap(stDoubleAgilityLimit._CF_minInclusive,
   stDoubleAgilityLimit._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAgilityLimit', stDoubleAgilityLimit)
_module_typeBindings.stDoubleAgilityLimit = stDoubleAgilityLimit

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleModAmpPri
class stDoubleModAmpPri (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleModAmpPri')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1410, 2)
    _Documentation = ''
stDoubleModAmpPri._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleModAmpPri, value=pyxb.binding.datatypes.double(0.0))
stDoubleModAmpPri._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleModAmpPri, value=pyxb.binding.datatypes.double(0.06553599999999976))
stDoubleModAmpPri._InitializeFacetMap(stDoubleModAmpPri._CF_minInclusive,
   stDoubleModAmpPri._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleModAmpPri', stDoubleModAmpPri)
_module_typeBindings.stDoubleModAmpPri = stDoubleModAmpPri

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleInterpulseModulationPeakDeviation
class stDoubleInterpulseModulationPeakDeviation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleInterpulseModulationPeakDeviation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1422, 2)
    _Documentation = ''
stDoubleInterpulseModulationPeakDeviation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleInterpulseModulationPeakDeviation, value=pyxb.binding.datatypes.double(0.0))
stDoubleInterpulseModulationPeakDeviation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleInterpulseModulationPeakDeviation, value=pyxb.binding.datatypes.double(0.06553599999999977))
stDoubleInterpulseModulationPeakDeviation._InitializeFacetMap(stDoubleInterpulseModulationPeakDeviation._CF_minInclusive,
   stDoubleInterpulseModulationPeakDeviation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleInterpulseModulationPeakDeviation', stDoubleInterpulseModulationPeakDeviation)
_module_typeBindings.stDoubleInterpulseModulationPeakDeviation = stDoubleInterpulseModulationPeakDeviation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleFrequency
class stDoubleFrequency (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleFrequency')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1434, 2)
    _Documentation = ''
stDoubleFrequency._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleFrequency, value=pyxb.binding.datatypes.double(0.0))
stDoubleFrequency._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleFrequency, value=pyxb.binding.datatypes.double(65535000000.0))
stDoubleFrequency._InitializeFacetMap(stDoubleFrequency._CF_minInclusive,
   stDoubleFrequency._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleFrequency', stDoubleFrequency)
_module_typeBindings.stDoubleFrequency = stDoubleFrequency

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBarTransitRate
class stDoubleBarTransitRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBarTransitRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1446, 2)
    _Documentation = ''
stDoubleBarTransitRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBarTransitRate, value=pyxb.binding.datatypes.double(0.0))
stDoubleBarTransitRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBarTransitRate, value=pyxb.binding.datatypes.double(703125.0))
stDoubleBarTransitRate._InitializeFacetMap(stDoubleBarTransitRate._CF_minInclusive,
   stDoubleBarTransitRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBarTransitRate', stDoubleBarTransitRate)
_module_typeBindings.stDoubleBarTransitRate = stDoubleBarTransitRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEventTime
class stDoubleEventTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEventTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1458, 2)
    _Documentation = ''
stDoubleEventTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEventTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleEventTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEventTime, value=pyxb.binding.datatypes.double(137438.953471))
stDoubleEventTime._InitializeFacetMap(stDoubleEventTime._CF_minInclusive,
   stDoubleEventTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEventTime', stDoubleEventTime)
_module_typeBindings.stDoubleEventTime = stDoubleEventTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartTime
class stDoubleStartTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1470, 2)
    _Documentation = ''
stDoubleStartTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleStartTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartTime, value=pyxb.binding.datatypes.double(86400.0))
stDoubleStartTime._InitializeFacetMap(stDoubleStartTime._CF_minInclusive,
   stDoubleStartTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartTime', stDoubleStartTime)
_module_typeBindings.stDoubleStartTime = stDoubleStartTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePalmerSquintAngle
class stDoublePalmerSquintAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePalmerSquintAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1482, 2)
    _Documentation = ''
stDoublePalmerSquintAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePalmerSquintAngle, value=pyxb.binding.datatypes.double(0.0))
stDoublePalmerSquintAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePalmerSquintAngle, value=pyxb.binding.datatypes.double(90.0))
stDoublePalmerSquintAngle._InitializeFacetMap(stDoublePalmerSquintAngle._CF_minInclusive,
   stDoublePalmerSquintAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePalmerSquintAngle', stDoublePalmerSquintAngle)
_module_typeBindings.stDoublePalmerSquintAngle = stDoublePalmerSquintAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSquintAngle
class stDoubleSquintAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSquintAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1494, 2)
    _Documentation = ''
stDoubleSquintAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSquintAngle, value=pyxb.binding.datatypes.double(0.0))
stDoubleSquintAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSquintAngle, value=pyxb.binding.datatypes.double(90.0))
stDoubleSquintAngle._InitializeFacetMap(stDoubleSquintAngle._CF_minInclusive,
   stDoubleSquintAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSquintAngle', stDoubleSquintAngle)
_module_typeBindings.stDoubleSquintAngle = stDoubleSquintAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleVhPolRatio
class stDoubleVhPolRatio (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleVhPolRatio')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1506, 2)
    _Documentation = ''
stDoubleVhPolRatio._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleVhPolRatio, value=pyxb.binding.datatypes.double(0.0))
stDoubleVhPolRatio._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleVhPolRatio, value=pyxb.binding.datatypes.double(90.0))
stDoubleVhPolRatio._InitializeFacetMap(stDoubleVhPolRatio._CF_minInclusive,
   stDoubleVhPolRatio._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleVhPolRatio', stDoubleVhPolRatio)
_module_typeBindings.stDoubleVhPolRatio = stDoubleVhPolRatio

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBankAngle
class stDoubleBankAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBankAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1518, 2)
    _Documentation = ''
stDoubleBankAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBankAngle, value=pyxb.binding.datatypes.double(-90.0))
stDoubleBankAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBankAngle, value=pyxb.binding.datatypes.double(90.0))
stDoubleBankAngle._InitializeFacetMap(stDoubleBankAngle._CF_minInclusive,
   stDoubleBankAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBankAngle', stDoubleBankAngle)
_module_typeBindings.stDoubleBankAngle = stDoubleBankAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleNorthLatitude
class stDoubleNorthLatitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleNorthLatitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1530, 2)
    _Documentation = ''
stDoubleNorthLatitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleNorthLatitude, value=pyxb.binding.datatypes.double(0.0))
stDoubleNorthLatitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleNorthLatitude, value=pyxb.binding.datatypes.double(90.0))
stDoubleNorthLatitude._InitializeFacetMap(stDoubleNorthLatitude._CF_minInclusive,
   stDoubleNorthLatitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleNorthLatitude', stDoubleNorthLatitude)
_module_typeBindings.stDoubleNorthLatitude = stDoubleNorthLatitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSouthLatitude
class stDoubleSouthLatitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSouthLatitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1542, 2)
    _Documentation = ''
stDoubleSouthLatitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSouthLatitude, value=pyxb.binding.datatypes.double(0.0))
stDoubleSouthLatitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSouthLatitude, value=pyxb.binding.datatypes.double(90.0))
stDoubleSouthLatitude._InitializeFacetMap(stDoubleSouthLatitude._CF_minInclusive,
   stDoubleSouthLatitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSouthLatitude', stDoubleSouthLatitude)
_module_typeBindings.stDoubleSouthLatitude = stDoubleSouthLatitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElBeamwidth
class stDoubleElBeamwidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElBeamwidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1554, 2)
    _Documentation = ''
stDoubleElBeamwidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElBeamwidth, value=pyxb.binding.datatypes.double(0.0))
stDoubleElBeamwidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElBeamwidth, value=pyxb.binding.datatypes.double(180.0))
stDoubleElBeamwidth._InitializeFacetMap(stDoubleElBeamwidth._CF_minInclusive,
   stDoubleElBeamwidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElBeamwidth', stDoubleElBeamwidth)
_module_typeBindings.stDoubleElBeamwidth = stDoubleElBeamwidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElInitialBeamOffset
class stDoubleElInitialBeamOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElInitialBeamOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1566, 2)
    _Documentation = ''
stDoubleElInitialBeamOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElInitialBeamOffset, value=pyxb.binding.datatypes.double(0.0))
stDoubleElInitialBeamOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElInitialBeamOffset, value=pyxb.binding.datatypes.double(180.0))
stDoubleElInitialBeamOffset._InitializeFacetMap(stDoubleElInitialBeamOffset._CF_minInclusive,
   stDoubleElInitialBeamOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElInitialBeamOffset', stDoubleElInitialBeamOffset)
_module_typeBindings.stDoubleElInitialBeamOffset = stDoubleElInitialBeamOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleWestLongitude
class stDoubleWestLongitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleWestLongitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1578, 2)
    _Documentation = ''
stDoubleWestLongitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleWestLongitude, value=pyxb.binding.datatypes.double(0.0))
stDoubleWestLongitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleWestLongitude, value=pyxb.binding.datatypes.double(180.0))
stDoubleWestLongitude._InitializeFacetMap(stDoubleWestLongitude._CF_minInclusive,
   stDoubleWestLongitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleWestLongitude', stDoubleWestLongitude)
_module_typeBindings.stDoubleWestLongitude = stDoubleWestLongitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEastLongitude
class stDoubleEastLongitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEastLongitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1590, 2)
    _Documentation = ''
stDoubleEastLongitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEastLongitude, value=pyxb.binding.datatypes.double(0.0))
stDoubleEastLongitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEastLongitude, value=pyxb.binding.datatypes.double(180.0))
stDoubleEastLongitude._InitializeFacetMap(stDoubleEastLongitude._CF_minInclusive,
   stDoubleEastLongitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEastLongitude', stDoubleEastLongitude)
_module_typeBindings.stDoubleEastLongitude = stDoubleEastLongitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleClockedPriJitterVariance
class stDoubleClockedPriJitterVariance (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleClockedPriJitterVariance')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1602, 2)
    _Documentation = ''
stDoubleClockedPriJitterVariance._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleClockedPriJitterVariance, value=pyxb.binding.datatypes.double(0.0))
stDoubleClockedPriJitterVariance._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleClockedPriJitterVariance, value=pyxb.binding.datatypes.double(99.99))
stDoubleClockedPriJitterVariance._InitializeFacetMap(stDoubleClockedPriJitterVariance._CF_minInclusive,
   stDoubleClockedPriJitterVariance._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleClockedPriJitterVariance', stDoubleClockedPriJitterVariance)
_module_typeBindings.stDoubleClockedPriJitterVariance = stDoubleClockedPriJitterVariance

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleInterpulseModPriPercentage
class stDoubleInterpulseModPriPercentage (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleInterpulseModPriPercentage')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1614, 2)
    _Documentation = ''
stDoubleInterpulseModPriPercentage._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleInterpulseModPriPercentage, value=pyxb.binding.datatypes.double(0.0))
stDoubleInterpulseModPriPercentage._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleInterpulseModPriPercentage, value=pyxb.binding.datatypes.double(99.99))
stDoubleInterpulseModPriPercentage._InitializeFacetMap(stDoubleInterpulseModPriPercentage._CF_minInclusive,
   stDoubleInterpulseModPriPercentage._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleInterpulseModPriPercentage', stDoubleInterpulseModPriPercentage)
_module_typeBindings.stDoubleInterpulseModPriPercentage = stDoubleInterpulseModPriPercentage

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleMissingPulseFactor
class stDoubleMissingPulseFactor (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleMissingPulseFactor')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1626, 2)
    _Documentation = ''
stDoubleMissingPulseFactor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleMissingPulseFactor, value=pyxb.binding.datatypes.double(0.0))
stDoubleMissingPulseFactor._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleMissingPulseFactor, value=pyxb.binding.datatypes.double(99.99847))
stDoubleMissingPulseFactor._InitializeFacetMap(stDoubleMissingPulseFactor._CF_minInclusive,
   stDoubleMissingPulseFactor._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleMissingPulseFactor', stDoubleMissingPulseFactor)
_module_typeBindings.stDoubleMissingPulseFactor = stDoubleMissingPulseFactor

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDelayTime
class stDoubleDelayTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDelayTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1638, 2)
    _Documentation = ''
stDoubleDelayTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDelayTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleDelayTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDelayTime, value=pyxb.binding.datatypes.double(0.999999))
stDoubleDelayTime._InitializeFacetMap(stDoubleDelayTime._CF_minInclusive,
   stDoubleDelayTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDelayTime', stDoubleDelayTime)
_module_typeBindings.stDoubleDelayTime = stDoubleDelayTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePri
class stDoublePri (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePri')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1650, 2)
    _Documentation = ''
stDoublePri._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePri, value=pyxb.binding.datatypes.double(0.0))
stDoublePri._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePri, value=pyxb.binding.datatypes.double(0.999999))
stDoublePri._InitializeFacetMap(stDoublePri._CF_minInclusive,
   stDoublePri._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePri', stDoublePri)
_module_typeBindings.stDoublePri = stDoublePri

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBurstModPeriod
class stDoubleBurstModPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBurstModPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1662, 2)
    _Documentation = ''
stDoubleBurstModPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBurstModPeriod, value=pyxb.binding.datatypes.double(1e-06))
stDoubleBurstModPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBurstModPeriod, value=pyxb.binding.datatypes.double(0.131071992))
stDoubleBurstModPeriod._InitializeFacetMap(stDoubleBurstModPeriod._CF_minInclusive,
   stDoubleBurstModPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBurstModPeriod', stDoubleBurstModPeriod)
_module_typeBindings.stDoubleBurstModPeriod = stDoubleBurstModPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleFreqChannelization
class stDoubleFreqChannelization (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleFreqChannelization')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1674, 2)
    _Documentation = ''
stDoubleFreqChannelization._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleFreqChannelization, value=pyxb.binding.datatypes.double(1.0))
stDoubleFreqChannelization._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleFreqChannelization, value=pyxb.binding.datatypes.double(511937500.0))
stDoubleFreqChannelization._InitializeFacetMap(stDoubleFreqChannelization._CF_minInclusive,
   stDoubleFreqChannelization._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleFreqChannelization', stDoubleFreqChannelization)
_module_typeBindings.stDoubleFreqChannelization = stDoubleFreqChannelization

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDelayTimeModPeriod
class stDoubleDelayTimeModPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDelayTimeModPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1686, 2)
    _Documentation = ''
stDoubleDelayTimeModPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDelayTimeModPeriod, value=pyxb.binding.datatypes.double(0.0001))
stDoubleDelayTimeModPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDelayTimeModPeriod, value=pyxb.binding.datatypes.double(268.435456))
stDoubleDelayTimeModPeriod._InitializeFacetMap(stDoubleDelayTimeModPeriod._CF_minInclusive,
   stDoubleDelayTimeModPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDelayTimeModPeriod', stDoubleDelayTimeModPeriod)
_module_typeBindings.stDoubleDelayTimeModPeriod = stDoubleDelayTimeModPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSecDtModPeriod
class stDoubleSecDtModPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSecDtModPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1698, 2)
    _Documentation = ''
stDoubleSecDtModPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSecDtModPeriod, value=pyxb.binding.datatypes.double(0.0001))
stDoubleSecDtModPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSecDtModPeriod, value=pyxb.binding.datatypes.double(268.435456))
stDoubleSecDtModPeriod._InitializeFacetMap(stDoubleSecDtModPeriod._CF_minInclusive,
   stDoubleSecDtModPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSecDtModPeriod', stDoubleSecDtModPeriod)
_module_typeBindings.stDoubleSecDtModPeriod = stDoubleSecDtModPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleSecModPeriod
class stDoubleSecModPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleSecModPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1710, 2)
    _Documentation = ''
stDoubleSecModPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleSecModPeriod, value=pyxb.binding.datatypes.double(0.0001))
stDoubleSecModPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleSecModPeriod, value=pyxb.binding.datatypes.double(268.435456))
stDoubleSecModPeriod._InitializeFacetMap(stDoubleSecModPeriod._CF_minInclusive,
   stDoubleSecModPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleSecModPeriod', stDoubleSecModPeriod)
_module_typeBindings.stDoubleSecModPeriod = stDoubleSecModPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleModPeriod
class stDoubleModPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleModPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1722, 2)
    _Documentation = ''
stDoubleModPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleModPeriod, value=pyxb.binding.datatypes.double(0.0001))
stDoubleModPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleModPeriod, value=pyxb.binding.datatypes.double(268.435456))
stDoubleModPeriod._InitializeFacetMap(stDoubleModPeriod._CF_minInclusive,
   stDoubleModPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleModPeriod', stDoubleModPeriod)
_module_typeBindings.stDoubleModPeriod = stDoubleModPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleInterpulseModulationPeriod
class stDoubleInterpulseModulationPeriod (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleInterpulseModulationPeriod')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1734, 2)
    _Documentation = ''
stDoubleInterpulseModulationPeriod._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleInterpulseModulationPeriod, value=pyxb.binding.datatypes.double(0.0001))
stDoubleInterpulseModulationPeriod._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleInterpulseModulationPeriod, value=pyxb.binding.datatypes.double(268.435456))
stDoubleInterpulseModulationPeriod._InitializeFacetMap(stDoubleInterpulseModulationPeriod._CF_minInclusive,
   stDoubleInterpulseModulationPeriod._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleInterpulseModulationPeriod', stDoubleInterpulseModulationPeriod)
_module_typeBindings.stDoubleInterpulseModulationPeriod = stDoubleInterpulseModulationPeriod

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleFrequencyDeviation
class stDoubleFrequencyDeviation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleFrequencyDeviation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1746, 2)
    _Documentation = ''
stDoubleFrequencyDeviation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleFrequencyDeviation, value=pyxb.binding.datatypes.double(-1000000000.0))
stDoubleFrequencyDeviation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleFrequencyDeviation, value=pyxb.binding.datatypes.double(1000000000.0))
stDoubleFrequencyDeviation._InitializeFacetMap(stDoubleFrequencyDeviation._CF_minInclusive,
   stDoubleFrequencyDeviation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleFrequencyDeviation', stDoubleFrequencyDeviation)
_module_typeBindings.stDoubleFrequencyDeviation = stDoubleFrequencyDeviation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLinearFreqDeviation
class stDoubleLinearFreqDeviation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLinearFreqDeviation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1758, 2)
    _Documentation = ''
stDoubleLinearFreqDeviation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLinearFreqDeviation, value=pyxb.binding.datatypes.double(-1000000000.0))
stDoubleLinearFreqDeviation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLinearFreqDeviation, value=pyxb.binding.datatypes.double(1000000000.0))
stDoubleLinearFreqDeviation._InitializeFacetMap(stDoubleLinearFreqDeviation._CF_minInclusive,
   stDoubleLinearFreqDeviation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLinearFreqDeviation', stDoubleLinearFreqDeviation)
_module_typeBindings.stDoubleLinearFreqDeviation = stDoubleLinearFreqDeviation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzTrackOffset
class stDoubleAzTrackOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzTrackOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1770, 2)
    _Documentation = ''
stDoubleAzTrackOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzTrackOffset, value=pyxb.binding.datatypes.double(-180.0))
stDoubleAzTrackOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzTrackOffset, value=pyxb.binding.datatypes.double(180.0))
stDoubleAzTrackOffset._InitializeFacetMap(stDoubleAzTrackOffset._CF_minInclusive,
   stDoubleAzTrackOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzTrackOffset', stDoubleAzTrackOffset)
_module_typeBindings.stDoubleAzTrackOffset = stDoubleAzTrackOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElPointAngle
class stDoubleElPointAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElPointAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1782, 2)
    _Documentation = ''
stDoubleElPointAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElPointAngle, value=pyxb.binding.datatypes.double(-180.0))
stDoubleElPointAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElPointAngle, value=pyxb.binding.datatypes.double(180.0))
stDoubleElPointAngle._InitializeFacetMap(stDoubleElPointAngle._CF_minInclusive,
   stDoubleElPointAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElPointAngle', stDoubleElPointAngle)
_module_typeBindings.stDoubleElPointAngle = stDoubleElPointAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElMasterOffset
class stDoubleElMasterOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElMasterOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1794, 2)
    _Documentation = ''
stDoubleElMasterOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElMasterOffset, value=pyxb.binding.datatypes.double(-180.0))
stDoubleElMasterOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElMasterOffset, value=pyxb.binding.datatypes.double(180.0))
stDoubleElMasterOffset._InitializeFacetMap(stDoubleElMasterOffset._CF_minInclusive,
   stDoubleElMasterOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElMasterOffset', stDoubleElMasterOffset)
_module_typeBindings.stDoubleElMasterOffset = stDoubleElMasterOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleVhPhaseDelta
class stDoubleVhPhaseDelta (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleVhPhaseDelta')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1806, 2)
    _Documentation = ''
stDoubleVhPhaseDelta._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleVhPhaseDelta, value=pyxb.binding.datatypes.double(-180.0))
stDoubleVhPhaseDelta._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleVhPhaseDelta, value=pyxb.binding.datatypes.double(180.0))
stDoubleVhPhaseDelta._InitializeFacetMap(stDoubleVhPhaseDelta._CF_minInclusive,
   stDoubleVhPhaseDelta._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleVhPhaseDelta', stDoubleVhPhaseDelta)
_module_typeBindings.stDoubleVhPhaseDelta = stDoubleVhPhaseDelta

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzReferencePoint
class stDoubleAzReferencePoint (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzReferencePoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1818, 2)
    _Documentation = ''
stDoubleAzReferencePoint._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzReferencePoint, value=pyxb.binding.datatypes.double(-180.0))
stDoubleAzReferencePoint._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzReferencePoint, value=pyxb.binding.datatypes.double(180.0))
stDoubleAzReferencePoint._InitializeFacetMap(stDoubleAzReferencePoint._CF_minInclusive,
   stDoubleAzReferencePoint._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzReferencePoint', stDoubleAzReferencePoint)
_module_typeBindings.stDoubleAzReferencePoint = stDoubleAzReferencePoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElPlatformTrackRefOffset
class stDoubleElPlatformTrackRefOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElPlatformTrackRefOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1830, 2)
    _Documentation = ''
stDoubleElPlatformTrackRefOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElPlatformTrackRefOffset, value=pyxb.binding.datatypes.double(-180.0))
stDoubleElPlatformTrackRefOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElPlatformTrackRefOffset, value=pyxb.binding.datatypes.double(180.0))
stDoubleElPlatformTrackRefOffset._InitializeFacetMap(stDoubleElPlatformTrackRefOffset._CF_minInclusive,
   stDoubleElPlatformTrackRefOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElPlatformTrackRefOffset', stDoubleElPlatformTrackRefOffset)
_module_typeBindings.stDoubleElPlatformTrackRefOffset = stDoubleElPlatformTrackRefOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElSutTrackRefOffset
class stDoubleElSutTrackRefOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElSutTrackRefOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1842, 2)
    _Documentation = ''
stDoubleElSutTrackRefOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElSutTrackRefOffset, value=pyxb.binding.datatypes.double(-180.0))
stDoubleElSutTrackRefOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElSutTrackRefOffset, value=pyxb.binding.datatypes.double(180.0))
stDoubleElSutTrackRefOffset._InitializeFacetMap(stDoubleElSutTrackRefOffset._CF_minInclusive,
   stDoubleElSutTrackRefOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElSutTrackRefOffset', stDoubleElSutTrackRefOffset)
_module_typeBindings.stDoubleElSutTrackRefOffset = stDoubleElSutTrackRefOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBeamElPointAngle
class stDoubleBeamElPointAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBeamElPointAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1854, 2)
    _Documentation = ''
stDoubleBeamElPointAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBeamElPointAngle, value=pyxb.binding.datatypes.double(-180.0))
stDoubleBeamElPointAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBeamElPointAngle, value=pyxb.binding.datatypes.double(180.0))
stDoubleBeamElPointAngle._InitializeFacetMap(stDoubleBeamElPointAngle._CF_minInclusive,
   stDoubleBeamElPointAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBeamElPointAngle', stDoubleBeamElPointAngle)
_module_typeBindings.stDoubleBeamElPointAngle = stDoubleBeamElPointAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBeamAzTrackOffset
class stDoubleBeamAzTrackOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBeamAzTrackOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1866, 2)
    _Documentation = ''
stDoubleBeamAzTrackOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBeamAzTrackOffset, value=pyxb.binding.datatypes.double(-180.0))
stDoubleBeamAzTrackOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBeamAzTrackOffset, value=pyxb.binding.datatypes.double(180.0))
stDoubleBeamAzTrackOffset._InitializeFacetMap(stDoubleBeamAzTrackOffset._CF_minInclusive,
   stDoubleBeamAzTrackOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBeamAzTrackOffset', stDoubleBeamAzTrackOffset)
_module_typeBindings.stDoubleBeamAzTrackOffset = stDoubleBeamAzTrackOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElStartAngle
class stDoubleElStartAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElStartAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1878, 2)
    _Documentation = ''
stDoubleElStartAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElStartAngle, value=pyxb.binding.datatypes.double(-180.0))
stDoubleElStartAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElStartAngle, value=pyxb.binding.datatypes.double(180.0))
stDoubleElStartAngle._InitializeFacetMap(stDoubleElStartAngle._CF_minInclusive,
   stDoubleElStartAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElStartAngle', stDoubleElStartAngle)
_module_typeBindings.stDoubleElStartAngle = stDoubleElStartAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBarElPointAngle
class stDoubleBarElPointAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBarElPointAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1890, 2)
    _Documentation = ''
stDoubleBarElPointAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBarElPointAngle, value=pyxb.binding.datatypes.double(-180.0))
stDoubleBarElPointAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBarElPointAngle, value=pyxb.binding.datatypes.double(180.0))
stDoubleBarElPointAngle._InitializeFacetMap(stDoubleBarElPointAngle._CF_minInclusive,
   stDoubleBarElPointAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBarElPointAngle', stDoubleBarElPointAngle)
_module_typeBindings.stDoubleBarElPointAngle = stDoubleBarElPointAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBarAzTrackOffset
class stDoubleBarAzTrackOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBarAzTrackOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1902, 2)
    _Documentation = ''
stDoubleBarAzTrackOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBarAzTrackOffset, value=pyxb.binding.datatypes.double(-180.0))
stDoubleBarAzTrackOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBarAzTrackOffset, value=pyxb.binding.datatypes.double(180.0))
stDoubleBarAzTrackOffset._InitializeFacetMap(stDoubleBarAzTrackOffset._CF_minInclusive,
   stDoubleBarAzTrackOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBarAzTrackOffset', stDoubleBarAzTrackOffset)
_module_typeBindings.stDoubleBarAzTrackOffset = stDoubleBarAzTrackOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBarOffset
class stDoubleBarOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBarOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1914, 2)
    _Documentation = ''
stDoubleBarOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBarOffset, value=pyxb.binding.datatypes.double(-180.0))
stDoubleBarOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBarOffset, value=pyxb.binding.datatypes.double(180.0))
stDoubleBarOffset._InitializeFacetMap(stDoubleBarOffset._CF_minInclusive,
   stDoubleBarOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBarOffset', stDoubleBarOffset)
_module_typeBindings.stDoubleBarOffset = stDoubleBarOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartRoll
class stDoubleStartRoll (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartRoll')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1926, 2)
    _Documentation = ''
stDoubleStartRoll._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartRoll, value=pyxb.binding.datatypes.double(-180.0))
stDoubleStartRoll._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartRoll, value=pyxb.binding.datatypes.double(180.0))
stDoubleStartRoll._InitializeFacetMap(stDoubleStartRoll._CF_minInclusive,
   stDoubleStartRoll._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartRoll', stDoubleStartRoll)
_module_typeBindings.stDoubleStartRoll = stDoubleStartRoll

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartPitch
class stDoubleStartPitch (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartPitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1938, 2)
    _Documentation = ''
stDoubleStartPitch._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartPitch, value=pyxb.binding.datatypes.double(-180.0))
stDoubleStartPitch._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartPitch, value=pyxb.binding.datatypes.double(180.0))
stDoubleStartPitch._InitializeFacetMap(stDoubleStartPitch._CF_minInclusive,
   stDoubleStartPitch._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartPitch', stDoubleStartPitch)
_module_typeBindings.stDoubleStartPitch = stDoubleStartPitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartYaw
class stDoubleStartYaw (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartYaw')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1950, 2)
    _Documentation = ''
stDoubleStartYaw._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartYaw, value=pyxb.binding.datatypes.double(-180.0))
stDoubleStartYaw._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartYaw, value=pyxb.binding.datatypes.double(180.0))
stDoubleStartYaw._InitializeFacetMap(stDoubleStartYaw._CF_minInclusive,
   stDoubleStartYaw._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartYaw', stDoubleStartYaw)
_module_typeBindings.stDoubleStartYaw = stDoubleStartYaw

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndRoll
class stDoubleEndRoll (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndRoll')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1962, 2)
    _Documentation = ''
stDoubleEndRoll._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndRoll, value=pyxb.binding.datatypes.double(-180.0))
stDoubleEndRoll._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndRoll, value=pyxb.binding.datatypes.double(180.0))
stDoubleEndRoll._InitializeFacetMap(stDoubleEndRoll._CF_minInclusive,
   stDoubleEndRoll._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndRoll', stDoubleEndRoll)
_module_typeBindings.stDoubleEndRoll = stDoubleEndRoll

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndPitch
class stDoubleEndPitch (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndPitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1974, 2)
    _Documentation = ''
stDoubleEndPitch._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndPitch, value=pyxb.binding.datatypes.double(-180.0))
stDoubleEndPitch._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndPitch, value=pyxb.binding.datatypes.double(180.0))
stDoubleEndPitch._InitializeFacetMap(stDoubleEndPitch._CF_minInclusive,
   stDoubleEndPitch._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndPitch', stDoubleEndPitch)
_module_typeBindings.stDoubleEndPitch = stDoubleEndPitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndYaw
class stDoubleEndYaw (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndYaw')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1986, 2)
    _Documentation = ''
stDoubleEndYaw._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndYaw, value=pyxb.binding.datatypes.double(-180.0))
stDoubleEndYaw._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndYaw, value=pyxb.binding.datatypes.double(180.0))
stDoubleEndYaw._InitializeFacetMap(stDoubleEndYaw._CF_minInclusive,
   stDoubleEndYaw._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndYaw', stDoubleEndYaw)
_module_typeBindings.stDoubleEndYaw = stDoubleEndYaw

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleHeading
class stDoubleHeading (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleHeading')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 1998, 2)
    _Documentation = ''
stDoubleHeading._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleHeading, value=pyxb.binding.datatypes.double(-180.0))
stDoubleHeading._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleHeading, value=pyxb.binding.datatypes.double(180.0))
stDoubleHeading._InitializeFacetMap(stDoubleHeading._CF_minInclusive,
   stDoubleHeading._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleHeading', stDoubleHeading)
_module_typeBindings.stDoubleHeading = stDoubleHeading

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLongitude
class stDoubleLongitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLongitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2010, 2)
    _Documentation = ''
stDoubleLongitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLongitude, value=pyxb.binding.datatypes.double(-180.0))
stDoubleLongitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLongitude, value=pyxb.binding.datatypes.double(180.0))
stDoubleLongitude._InitializeFacetMap(stDoubleLongitude._CF_minInclusive,
   stDoubleLongitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLongitude', stDoubleLongitude)
_module_typeBindings.stDoubleLongitude = stDoubleLongitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleGeopoliticalCenterLongitude
class stDoubleGeopoliticalCenterLongitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleGeopoliticalCenterLongitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2022, 2)
    _Documentation = ''
stDoubleGeopoliticalCenterLongitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleGeopoliticalCenterLongitude, value=pyxb.binding.datatypes.double(-180.0))
stDoubleGeopoliticalCenterLongitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleGeopoliticalCenterLongitude, value=pyxb.binding.datatypes.double(180.0))
stDoubleGeopoliticalCenterLongitude._InitializeFacetMap(stDoubleGeopoliticalCenterLongitude._CF_minInclusive,
   stDoubleGeopoliticalCenterLongitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleGeopoliticalCenterLongitude', stDoubleGeopoliticalCenterLongitude)
_module_typeBindings.stDoubleGeopoliticalCenterLongitude = stDoubleGeopoliticalCenterLongitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleErp
class stDoubleErp (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleErp')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2034, 2)
    _Documentation = ''
stDoubleErp._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleErp, value=pyxb.binding.datatypes.double(-255.75))
stDoubleErp._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleErp, value=pyxb.binding.datatypes.double(255.75))
stDoubleErp._InitializeFacetMap(stDoubleErp._CF_minInclusive,
   stDoubleErp._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleErp', stDoubleErp)
_module_typeBindings.stDoubleErp = stDoubleErp

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzPointAngle
class stDoubleAzPointAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzPointAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2046, 2)
    _Documentation = ''
stDoubleAzPointAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzPointAngle, value=pyxb.binding.datatypes.double(-359.978))
stDoubleAzPointAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzPointAngle, value=pyxb.binding.datatypes.double(359.978))
stDoubleAzPointAngle._InitializeFacetMap(stDoubleAzPointAngle._CF_minInclusive,
   stDoubleAzPointAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzPointAngle', stDoubleAzPointAngle)
_module_typeBindings.stDoubleAzPointAngle = stDoubleAzPointAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzMasterOffset
class stDoubleAzMasterOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzMasterOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2058, 2)
    _Documentation = ''
stDoubleAzMasterOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzMasterOffset, value=pyxb.binding.datatypes.double(-359.978))
stDoubleAzMasterOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzMasterOffset, value=pyxb.binding.datatypes.double(359.978))
stDoubleAzMasterOffset._InitializeFacetMap(stDoubleAzMasterOffset._CF_minInclusive,
   stDoubleAzMasterOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzMasterOffset', stDoubleAzMasterOffset)
_module_typeBindings.stDoubleAzMasterOffset = stDoubleAzMasterOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzPlatformTrackRefOffset
class stDoubleAzPlatformTrackRefOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzPlatformTrackRefOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2070, 2)
    _Documentation = ''
stDoubleAzPlatformTrackRefOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzPlatformTrackRefOffset, value=pyxb.binding.datatypes.double(-359.978))
stDoubleAzPlatformTrackRefOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzPlatformTrackRefOffset, value=pyxb.binding.datatypes.double(359.978))
stDoubleAzPlatformTrackRefOffset._InitializeFacetMap(stDoubleAzPlatformTrackRefOffset._CF_minInclusive,
   stDoubleAzPlatformTrackRefOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzPlatformTrackRefOffset', stDoubleAzPlatformTrackRefOffset)
_module_typeBindings.stDoubleAzPlatformTrackRefOffset = stDoubleAzPlatformTrackRefOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzSutTrackRefOffset
class stDoubleAzSutTrackRefOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzSutTrackRefOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2082, 2)
    _Documentation = ''
stDoubleAzSutTrackRefOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzSutTrackRefOffset, value=pyxb.binding.datatypes.double(-359.978))
stDoubleAzSutTrackRefOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzSutTrackRefOffset, value=pyxb.binding.datatypes.double(359.978))
stDoubleAzSutTrackRefOffset._InitializeFacetMap(stDoubleAzSutTrackRefOffset._CF_minInclusive,
   stDoubleAzSutTrackRefOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzSutTrackRefOffset', stDoubleAzSutTrackRefOffset)
_module_typeBindings.stDoubleAzSutTrackRefOffset = stDoubleAzSutTrackRefOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBeamAzPointAngle
class stDoubleBeamAzPointAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBeamAzPointAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2094, 2)
    _Documentation = ''
stDoubleBeamAzPointAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBeamAzPointAngle, value=pyxb.binding.datatypes.double(-359.978))
stDoubleBeamAzPointAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBeamAzPointAngle, value=pyxb.binding.datatypes.double(359.978))
stDoubleBeamAzPointAngle._InitializeFacetMap(stDoubleBeamAzPointAngle._CF_minInclusive,
   stDoubleBeamAzPointAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBeamAzPointAngle', stDoubleBeamAzPointAngle)
_module_typeBindings.stDoubleBeamAzPointAngle = stDoubleBeamAzPointAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzStartAngle
class stDoubleAzStartAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzStartAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2106, 2)
    _Documentation = ''
stDoubleAzStartAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzStartAngle, value=pyxb.binding.datatypes.double(-359.978))
stDoubleAzStartAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzStartAngle, value=pyxb.binding.datatypes.double(359.978))
stDoubleAzStartAngle._InitializeFacetMap(stDoubleAzStartAngle._CF_minInclusive,
   stDoubleAzStartAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzStartAngle', stDoubleAzStartAngle)
_module_typeBindings.stDoubleAzStartAngle = stDoubleAzStartAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBarAzPointAngle
class stDoubleBarAzPointAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBarAzPointAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2118, 2)
    _Documentation = ''
stDoubleBarAzPointAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBarAzPointAngle, value=pyxb.binding.datatypes.double(-359.978))
stDoubleBarAzPointAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBarAzPointAngle, value=pyxb.binding.datatypes.double(359.978))
stDoubleBarAzPointAngle._InitializeFacetMap(stDoubleBarAzPointAngle._CF_minInclusive,
   stDoubleBarAzPointAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBarAzPointAngle', stDoubleBarAzPointAngle)
_module_typeBindings.stDoubleBarAzPointAngle = stDoubleBarAzPointAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAzSidelobeRatio
class stDoubleAzSidelobeRatio (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAzSidelobeRatio')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2130, 2)
    _Documentation = ''
stDoubleAzSidelobeRatio._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAzSidelobeRatio, value=pyxb.binding.datatypes.double(-63.75))
stDoubleAzSidelobeRatio._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAzSidelobeRatio, value=pyxb.binding.datatypes.double(0.0))
stDoubleAzSidelobeRatio._InitializeFacetMap(stDoubleAzSidelobeRatio._CF_minInclusive,
   stDoubleAzSidelobeRatio._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAzSidelobeRatio', stDoubleAzSidelobeRatio)
_module_typeBindings.stDoubleAzSidelobeRatio = stDoubleAzSidelobeRatio

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElSidelobeRatio
class stDoubleElSidelobeRatio (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElSidelobeRatio')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2142, 2)
    _Documentation = ''
stDoubleElSidelobeRatio._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElSidelobeRatio, value=pyxb.binding.datatypes.double(-63.75))
stDoubleElSidelobeRatio._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElSidelobeRatio, value=pyxb.binding.datatypes.double(0.0))
stDoubleElSidelobeRatio._InitializeFacetMap(stDoubleElSidelobeRatio._CF_minInclusive,
   stDoubleElSidelobeRatio._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElSidelobeRatio', stDoubleElSidelobeRatio)
_module_typeBindings.stDoubleElSidelobeRatio = stDoubleElSidelobeRatio

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElTrackOffset
class stDoubleElTrackOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElTrackOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2154, 2)
    _Documentation = ''
stDoubleElTrackOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElTrackOffset, value=pyxb.binding.datatypes.double(-90.0))
stDoubleElTrackOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElTrackOffset, value=pyxb.binding.datatypes.double(90.0))
stDoubleElTrackOffset._InitializeFacetMap(stDoubleElTrackOffset._CF_minInclusive,
   stDoubleElTrackOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElTrackOffset', stDoubleElTrackOffset)
_module_typeBindings.stDoubleElTrackOffset = stDoubleElTrackOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleElReferencePoint
class stDoubleElReferencePoint (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleElReferencePoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2166, 2)
    _Documentation = ''
stDoubleElReferencePoint._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleElReferencePoint, value=pyxb.binding.datatypes.double(-90.0))
stDoubleElReferencePoint._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleElReferencePoint, value=pyxb.binding.datatypes.double(90.0))
stDoubleElReferencePoint._InitializeFacetMap(stDoubleElReferencePoint._CF_minInclusive,
   stDoubleElReferencePoint._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleElReferencePoint', stDoubleElReferencePoint)
_module_typeBindings.stDoubleElReferencePoint = stDoubleElReferencePoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBeamElTrackOffset
class stDoubleBeamElTrackOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBeamElTrackOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2178, 2)
    _Documentation = ''
stDoubleBeamElTrackOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBeamElTrackOffset, value=pyxb.binding.datatypes.double(-90.0))
stDoubleBeamElTrackOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBeamElTrackOffset, value=pyxb.binding.datatypes.double(90.0))
stDoubleBeamElTrackOffset._InitializeFacetMap(stDoubleBeamElTrackOffset._CF_minInclusive,
   stDoubleBeamElTrackOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBeamElTrackOffset', stDoubleBeamElTrackOffset)
_module_typeBindings.stDoubleBeamElTrackOffset = stDoubleBeamElTrackOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleBarElTrackOffset
class stDoubleBarElTrackOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleBarElTrackOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2190, 2)
    _Documentation = ''
stDoubleBarElTrackOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleBarElTrackOffset, value=pyxb.binding.datatypes.double(-90.0))
stDoubleBarElTrackOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleBarElTrackOffset, value=pyxb.binding.datatypes.double(90.0))
stDoubleBarElTrackOffset._InitializeFacetMap(stDoubleBarElTrackOffset._CF_minInclusive,
   stDoubleBarElTrackOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleBarElTrackOffset', stDoubleBarElTrackOffset)
_module_typeBindings.stDoubleBarElTrackOffset = stDoubleBarElTrackOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleClimbAngle
class stDoubleClimbAngle (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleClimbAngle')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2202, 2)
    _Documentation = ''
stDoubleClimbAngle._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleClimbAngle, value=pyxb.binding.datatypes.double(-90.0))
stDoubleClimbAngle._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleClimbAngle, value=pyxb.binding.datatypes.double(90.0))
stDoubleClimbAngle._InitializeFacetMap(stDoubleClimbAngle._CF_minInclusive,
   stDoubleClimbAngle._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleClimbAngle', stDoubleClimbAngle)
_module_typeBindings.stDoubleClimbAngle = stDoubleClimbAngle

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerElevation
class stDoubleLowerElevation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerElevation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2214, 2)
    _Documentation = ''
stDoubleLowerElevation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerElevation, value=pyxb.binding.datatypes.double(-90.0))
stDoubleLowerElevation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerElevation, value=pyxb.binding.datatypes.double(90.0))
stDoubleLowerElevation._InitializeFacetMap(stDoubleLowerElevation._CF_minInclusive,
   stDoubleLowerElevation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerElevation', stDoubleLowerElevation)
_module_typeBindings.stDoubleLowerElevation = stDoubleLowerElevation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperElevation
class stDoubleUpperElevation (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperElevation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2226, 2)
    _Documentation = ''
stDoubleUpperElevation._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperElevation, value=pyxb.binding.datatypes.double(-90.0))
stDoubleUpperElevation._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperElevation, value=pyxb.binding.datatypes.double(90.0))
stDoubleUpperElevation._InitializeFacetMap(stDoubleUpperElevation._CF_minInclusive,
   stDoubleUpperElevation._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperElevation', stDoubleUpperElevation)
_module_typeBindings.stDoubleUpperElevation = stDoubleUpperElevation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleGeopoliticalCenterLatitude
class stDoubleGeopoliticalCenterLatitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleGeopoliticalCenterLatitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2238, 2)
    _Documentation = ''
stDoubleGeopoliticalCenterLatitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleGeopoliticalCenterLatitude, value=pyxb.binding.datatypes.double(-90.0))
stDoubleGeopoliticalCenterLatitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleGeopoliticalCenterLatitude, value=pyxb.binding.datatypes.double(90.0))
stDoubleGeopoliticalCenterLatitude._InitializeFacetMap(stDoubleGeopoliticalCenterLatitude._CF_minInclusive,
   stDoubleGeopoliticalCenterLatitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleGeopoliticalCenterLatitude', stDoubleGeopoliticalCenterLatitude)
_module_typeBindings.stDoubleGeopoliticalCenterLatitude = stDoubleGeopoliticalCenterLatitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLatitude
class stDoubleLatitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLatitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2250, 2)
    _Documentation = ''
stDoubleLatitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLatitude, value=pyxb.binding.datatypes.double(-90.0))
stDoubleLatitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLatitude, value=pyxb.binding.datatypes.double(90.0))
stDoubleLatitude._InitializeFacetMap(stDoubleLatitude._CF_minInclusive,
   stDoubleLatitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLatitude', stDoubleLatitude)
_module_typeBindings.stDoubleLatitude = stDoubleLatitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleXOffset
class stDoubleXOffset (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleXOffset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2262, 2)
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2274, 2)
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2286, 2)
    _Documentation = ''
stDoubleZOffset._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleZOffset, value=pyxb.binding.datatypes.double(-999999.999))
stDoubleZOffset._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleZOffset, value=pyxb.binding.datatypes.double(999999.999))
stDoubleZOffset._InitializeFacetMap(stDoubleZOffset._CF_minInclusive,
   stDoubleZOffset._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleZOffset', stDoubleZOffset)
_module_typeBindings.stDoubleZOffset = stDoubleZOffset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDwellDurationScript
class stDoubleDwellDurationScript (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDwellDurationScript')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2298, 2)
    _Documentation = ''
stDoubleDwellDurationScript._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDwellDurationScript, value=pyxb.binding.datatypes.double(1e-06))
stDoubleDwellDurationScript._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDwellDurationScript, value=pyxb.binding.datatypes.double(137438.953471))
stDoubleDwellDurationScript._InitializeFacetMap(stDoubleDwellDurationScript._CF_minInclusive,
   stDoubleDwellDurationScript._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDwellDurationScript', stDoubleDwellDurationScript)
_module_typeBindings.stDoubleDwellDurationScript = stDoubleDwellDurationScript

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDisplayIntensity
class stDoubleDisplayIntensity (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDisplayIntensity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2310, 2)
    _Documentation = ''
stDoubleDisplayIntensity._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDisplayIntensity, value=pyxb.binding.datatypes.double(0.01))
stDoubleDisplayIntensity._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDisplayIntensity, value=pyxb.binding.datatypes.double(1.0))
stDoubleDisplayIntensity._InitializeFacetMap(stDoubleDisplayIntensity._CF_minInclusive,
   stDoubleDisplayIntensity._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDisplayIntensity', stDoubleDisplayIntensity)
_module_typeBindings.stDoubleDisplayIntensity = stDoubleDisplayIntensity

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEarthRadiusFactor
class stDoubleEarthRadiusFactor (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEarthRadiusFactor')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2322, 2)
    _Documentation = ''
stDoubleEarthRadiusFactor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEarthRadiusFactor, value=pyxb.binding.datatypes.double(0.1))
stDoubleEarthRadiusFactor._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEarthRadiusFactor, value=pyxb.binding.datatypes.double(1000.0))
stDoubleEarthRadiusFactor._InitializeFacetMap(stDoubleEarthRadiusFactor._CF_minInclusive,
   stDoubleEarthRadiusFactor._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEarthRadiusFactor', stDoubleEarthRadiusFactor)
_module_typeBindings.stDoubleEarthRadiusFactor = stDoubleEarthRadiusFactor

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDisplayScale
class stDoubleDisplayScale (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDisplayScale')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2334, 2)
    _Documentation = ''
stDoubleDisplayScale._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDisplayScale, value=pyxb.binding.datatypes.double(0.01))
stDoubleDisplayScale._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDisplayScale, value=pyxb.binding.datatypes.double(8.0))
stDoubleDisplayScale._InitializeFacetMap(stDoubleDisplayScale._CF_minInclusive,
   stDoubleDisplayScale._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDisplayScale', stDoubleDisplayScale)
_module_typeBindings.stDoubleDisplayScale = stDoubleDisplayScale

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleScale
class stDoubleScale (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleScale')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2346, 2)
    _Documentation = ''
stDoubleScale._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleScale, value=pyxb.binding.datatypes.double(0.0))
stDoubleScale._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleScale, value=pyxb.binding.datatypes.double(1.0))
stDoubleScale._InitializeFacetMap(stDoubleScale._CF_minInclusive,
   stDoubleScale._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleScale', stDoubleScale)
_module_typeBindings.stDoubleScale = stDoubleScale

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleIntensity
class stDoubleIntensity (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleIntensity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2358, 2)
    _Documentation = ''
stDoubleIntensity._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleIntensity, value=pyxb.binding.datatypes.double(0.0))
stDoubleIntensity._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleIntensity, value=pyxb.binding.datatypes.double(1.0))
stDoubleIntensity._InitializeFacetMap(stDoubleIntensity._CF_minInclusive,
   stDoubleIntensity._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleIntensity', stDoubleIntensity)
_module_typeBindings.stDoubleIntensity = stDoubleIntensity

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLoadFactor
class stDoubleLoadFactor (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLoadFactor')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2370, 2)
    _Documentation = ''
stDoubleLoadFactor._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLoadFactor, value=pyxb.binding.datatypes.double(0.0))
stDoubleLoadFactor._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLoadFactor, value=pyxb.binding.datatypes.double(100.0))
stDoubleLoadFactor._InitializeFacetMap(stDoubleLoadFactor._CF_minInclusive,
   stDoubleLoadFactor._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLoadFactor', stDoubleLoadFactor)
_module_typeBindings.stDoubleLoadFactor = stDoubleLoadFactor

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleStartSpeed
class stDoubleStartSpeed (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleStartSpeed')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2382, 2)
    _Documentation = ''
stDoubleStartSpeed._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleStartSpeed, value=pyxb.binding.datatypes.double(0.0))
stDoubleStartSpeed._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleStartSpeed, value=pyxb.binding.datatypes.double(2777.77777777778))
stDoubleStartSpeed._InitializeFacetMap(stDoubleStartSpeed._CF_minInclusive,
   stDoubleStartSpeed._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleStartSpeed', stDoubleStartSpeed)
_module_typeBindings.stDoubleStartSpeed = stDoubleStartSpeed

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndSpeed
class stDoubleEndSpeed (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndSpeed')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2394, 2)
    _Documentation = ''
stDoubleEndSpeed._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndSpeed, value=pyxb.binding.datatypes.double(0.0))
stDoubleEndSpeed._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndSpeed, value=pyxb.binding.datatypes.double(2777.77777777778))
stDoubleEndSpeed._InitializeFacetMap(stDoubleEndSpeed._CF_minInclusive,
   stDoubleEndSpeed._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndSpeed', stDoubleEndSpeed)
_module_typeBindings.stDoubleEndSpeed = stDoubleEndSpeed

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDuctingHeight
class stDoubleDuctingHeight (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDuctingHeight')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2406, 2)
    _Documentation = ''
stDoubleDuctingHeight._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDuctingHeight, value=pyxb.binding.datatypes.double(0.0))
stDoubleDuctingHeight._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDuctingHeight, value=pyxb.binding.datatypes.double(1000000.0))
stDoubleDuctingHeight._InitializeFacetMap(stDoubleDuctingHeight._CF_minInclusive,
   stDoubleDuctingHeight._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDuctingHeight', stDoubleDuctingHeight)
_module_typeBindings.stDoubleDuctingHeight = stDoubleDuctingHeight

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerFrequency
class stDoubleLowerFrequency (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerFrequency')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2418, 2)
    _Documentation = ''
stDoubleLowerFrequency._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerFrequency, value=pyxb.binding.datatypes.double(0.0))
stDoubleLowerFrequency._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerFrequency, value=pyxb.binding.datatypes.double(131071000000.0))
stDoubleLowerFrequency._InitializeFacetMap(stDoubleLowerFrequency._CF_minInclusive,
   stDoubleLowerFrequency._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerFrequency', stDoubleLowerFrequency)
_module_typeBindings.stDoubleLowerFrequency = stDoubleLowerFrequency

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperFrequency
class stDoubleUpperFrequency (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperFrequency')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2430, 2)
    _Documentation = ''
stDoubleUpperFrequency._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperFrequency, value=pyxb.binding.datatypes.double(0.0))
stDoubleUpperFrequency._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperFrequency, value=pyxb.binding.datatypes.double(131071000000.0))
stDoubleUpperFrequency._InitializeFacetMap(stDoubleUpperFrequency._CF_minInclusive,
   stDoubleUpperFrequency._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperFrequency', stDoubleUpperFrequency)
_module_typeBindings.stDoubleUpperFrequency = stDoubleUpperFrequency

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerPulseWidth
class stDoubleLowerPulseWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerPulseWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2442, 2)
    _Documentation = ''
stDoubleLowerPulseWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerPulseWidth, value=pyxb.binding.datatypes.double(0.0))
stDoubleLowerPulseWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerPulseWidth, value=pyxb.binding.datatypes.double(0.131071))
stDoubleLowerPulseWidth._InitializeFacetMap(stDoubleLowerPulseWidth._CF_minInclusive,
   stDoubleLowerPulseWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerPulseWidth', stDoubleLowerPulseWidth)
_module_typeBindings.stDoubleLowerPulseWidth = stDoubleLowerPulseWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperPulseWidth
class stDoubleUpperPulseWidth (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperPulseWidth')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2454, 2)
    _Documentation = ''
stDoubleUpperPulseWidth._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperPulseWidth, value=pyxb.binding.datatypes.double(0.0))
stDoubleUpperPulseWidth._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperPulseWidth, value=pyxb.binding.datatypes.double(0.131071))
stDoubleUpperPulseWidth._InitializeFacetMap(stDoubleUpperPulseWidth._CF_minInclusive,
   stDoubleUpperPulseWidth._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperPulseWidth', stDoubleUpperPulseWidth)
_module_typeBindings.stDoubleUpperPulseWidth = stDoubleUpperPulseWidth

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleActivationTime
class stDoubleActivationTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleActivationTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2466, 2)
    _Documentation = ''
stDoubleActivationTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleActivationTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleActivationTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleActivationTime, value=pyxb.binding.datatypes.double(137438.953471))
stDoubleActivationTime._InitializeFacetMap(stDoubleActivationTime._CF_minInclusive,
   stDoubleActivationTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleActivationTime', stDoubleActivationTime)
_module_typeBindings.stDoubleActivationTime = stDoubleActivationTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerTime
class stDoubleLowerTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2478, 2)
    _Documentation = ''
stDoubleLowerTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleLowerTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerTime, value=pyxb.binding.datatypes.double(137438.0))
stDoubleLowerTime._InitializeFacetMap(stDoubleLowerTime._CF_minInclusive,
   stDoubleLowerTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerTime', stDoubleLowerTime)
_module_typeBindings.stDoubleLowerTime = stDoubleLowerTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperTime
class stDoubleUpperTime (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperTime')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2490, 2)
    _Documentation = ''
stDoubleUpperTime._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperTime, value=pyxb.binding.datatypes.double(0.0))
stDoubleUpperTime._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperTime, value=pyxb.binding.datatypes.double(137438.0))
stDoubleUpperTime._InitializeFacetMap(stDoubleUpperTime._CF_minInclusive,
   stDoubleUpperTime._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperTime', stDoubleUpperTime)
_module_typeBindings.stDoubleUpperTime = stDoubleUpperTime

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleDuctingRefractivity
class stDoubleDuctingRefractivity (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleDuctingRefractivity')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2502, 2)
    _Documentation = ''
stDoubleDuctingRefractivity._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleDuctingRefractivity, value=pyxb.binding.datatypes.double(0.0))
stDoubleDuctingRefractivity._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleDuctingRefractivity, value=pyxb.binding.datatypes.double(32.0))
stDoubleDuctingRefractivity._InitializeFacetMap(stDoubleDuctingRefractivity._CF_minInclusive,
   stDoubleDuctingRefractivity._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleDuctingRefractivity', stDoubleDuctingRefractivity)
_module_typeBindings.stDoubleDuctingRefractivity = stDoubleDuctingRefractivity

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleRollRate
class stDoubleRollRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleRollRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2514, 2)
    _Documentation = ''
stDoubleRollRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleRollRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleRollRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleRollRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleRollRate._InitializeFacetMap(stDoubleRollRate._CF_minInclusive,
   stDoubleRollRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleRollRate', stDoubleRollRate)
_module_typeBindings.stDoubleRollRate = stDoubleRollRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoublePitchRate
class stDoublePitchRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoublePitchRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2526, 2)
    _Documentation = ''
stDoublePitchRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoublePitchRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoublePitchRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoublePitchRate, value=pyxb.binding.datatypes.double(1000.0))
stDoublePitchRate._InitializeFacetMap(stDoublePitchRate._CF_minInclusive,
   stDoublePitchRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoublePitchRate', stDoublePitchRate)
_module_typeBindings.stDoublePitchRate = stDoublePitchRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleYawRate
class stDoubleYawRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleYawRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2538, 2)
    _Documentation = ''
stDoubleYawRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleYawRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleYawRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleYawRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleYawRate._InitializeFacetMap(stDoubleYawRate._CF_minInclusive,
   stDoubleYawRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleYawRate', stDoubleYawRate)
_module_typeBindings.stDoubleYawRate = stDoubleYawRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndRollRate
class stDoubleEndRollRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndRollRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2550, 2)
    _Documentation = ''
stDoubleEndRollRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndRollRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleEndRollRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndRollRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleEndRollRate._InitializeFacetMap(stDoubleEndRollRate._CF_minInclusive,
   stDoubleEndRollRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndRollRate', stDoubleEndRollRate)
_module_typeBindings.stDoubleEndRollRate = stDoubleEndRollRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndPitchRate
class stDoubleEndPitchRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndPitchRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2562, 2)
    _Documentation = ''
stDoubleEndPitchRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndPitchRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleEndPitchRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndPitchRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleEndPitchRate._InitializeFacetMap(stDoubleEndPitchRate._CF_minInclusive,
   stDoubleEndPitchRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndPitchRate', stDoubleEndPitchRate)
_module_typeBindings.stDoubleEndPitchRate = stDoubleEndPitchRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleEndYawRate
class stDoubleEndYawRate (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleEndYawRate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2574, 2)
    _Documentation = ''
stDoubleEndYawRate._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleEndYawRate, value=pyxb.binding.datatypes.double(-1000.0))
stDoubleEndYawRate._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleEndYawRate, value=pyxb.binding.datatypes.double(1000.0))
stDoubleEndYawRate._InitializeFacetMap(stDoubleEndYawRate._CF_minInclusive,
   stDoubleEndYawRate._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleEndYawRate', stDoubleEndYawRate)
_module_typeBindings.stDoubleEndYawRate = stDoubleEndYawRate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleZ
class stDoubleZ (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleZ')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2586, 2)
    _Documentation = ''
stDoubleZ._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleZ, value=pyxb.binding.datatypes.double(-1000000.0))
stDoubleZ._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleZ, value=pyxb.binding.datatypes.double(1000000.0))
stDoubleZ._InitializeFacetMap(stDoubleZ._CF_minInclusive,
   stDoubleZ._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleZ', stDoubleZ)
_module_typeBindings.stDoubleZ = stDoubleZ

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleAltitude
class stDoubleAltitude (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleAltitude')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2598, 2)
    _Documentation = ''
stDoubleAltitude._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleAltitude, value=pyxb.binding.datatypes.double(-1000000.0))
stDoubleAltitude._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleAltitude, value=pyxb.binding.datatypes.double(1000000.0))
stDoubleAltitude._InitializeFacetMap(stDoubleAltitude._CF_minInclusive,
   stDoubleAltitude._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleAltitude', stDoubleAltitude)
_module_typeBindings.stDoubleAltitude = stDoubleAltitude

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleVelocityVectorDuration
class stDoubleVelocityVectorDuration (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleVelocityVectorDuration')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2610, 2)
    _Documentation = ''
stDoubleVelocityVectorDuration._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleVelocityVectorDuration, value=pyxb.binding.datatypes.double(0.0))
stDoubleVelocityVectorDuration._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleVelocityVectorDuration, value=pyxb.binding.datatypes.double(600.0))
stDoubleVelocityVectorDuration._InitializeFacetMap(stDoubleVelocityVectorDuration._CF_minInclusive,
   stDoubleVelocityVectorDuration._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleVelocityVectorDuration', stDoubleVelocityVectorDuration)
_module_typeBindings.stDoubleVelocityVectorDuration = stDoubleVelocityVectorDuration

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleX
class stDoubleX (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleX')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2622, 2)
    _Documentation = ''
stDoubleX._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleX, value=pyxb.binding.datatypes.double(-2000000.0))
stDoubleX._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleX, value=pyxb.binding.datatypes.double(2000000.0))
stDoubleX._InitializeFacetMap(stDoubleX._CF_minInclusive,
   stDoubleX._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleX', stDoubleX)
_module_typeBindings.stDoubleX = stDoubleX

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleY
class stDoubleY (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleY')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2634, 2)
    _Documentation = ''
stDoubleY._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleY, value=pyxb.binding.datatypes.double(-2000000.0))
stDoubleY._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleY, value=pyxb.binding.datatypes.double(2000000.0))
stDoubleY._InitializeFacetMap(stDoubleY._CF_minInclusive,
   stDoubleY._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleY', stDoubleY)
_module_typeBindings.stDoubleY = stDoubleY

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleLowerPower
class stDoubleLowerPower (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleLowerPower')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2646, 2)
    _Documentation = ''
stDoubleLowerPower._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleLowerPower, value=pyxb.binding.datatypes.double(-256.0))
stDoubleLowerPower._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleLowerPower, value=pyxb.binding.datatypes.double(255.75))
stDoubleLowerPower._InitializeFacetMap(stDoubleLowerPower._CF_minInclusive,
   stDoubleLowerPower._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleLowerPower', stDoubleLowerPower)
_module_typeBindings.stDoubleLowerPower = stDoubleLowerPower

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDoubleUpperPower
class stDoubleUpperPower (pyxb.binding.datatypes.double):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDoubleUpperPower')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2658, 2)
    _Documentation = ''
stDoubleUpperPower._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=stDoubleUpperPower, value=pyxb.binding.datatypes.double(-256.0))
stDoubleUpperPower._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=stDoubleUpperPower, value=pyxb.binding.datatypes.double(255.75))
stDoubleUpperPower._InitializeFacetMap(stDoubleUpperPower._CF_minInclusive,
   stDoubleUpperPower._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', 'stDoubleUpperPower', stDoubleUpperPower)
_module_typeBindings.stDoubleUpperPower = stDoubleUpperPower

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumAntennaModelKind
class stEnumAntennaModelKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumAntennaModelKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2670, 2)
    _Documentation = ''
stEnumAntennaModelKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumAntennaModelKind, enum_prefix=None)
stEnumAntennaModelKind.Elliptical = stEnumAntennaModelKind._CF_enumeration.addEnumeration(unicode_value='Elliptical', tag='Elliptical')
stEnumAntennaModelKind.Rectangular = stEnumAntennaModelKind._CF_enumeration.addEnumeration(unicode_value='Rectangular', tag='Rectangular')
stEnumAntennaModelKind._InitializeFacetMap(stEnumAntennaModelKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumAntennaModelKind', stEnumAntennaModelKind)
_module_typeBindings.stEnumAntennaModelKind = stEnumAntennaModelKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumRasterOrientation
class stEnumRasterOrientation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumRasterOrientation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2682, 2)
    _Documentation = ''
stEnumRasterOrientation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumRasterOrientation, enum_prefix=None)
stEnumRasterOrientation.Azimuth = stEnumRasterOrientation._CF_enumeration.addEnumeration(unicode_value='Azimuth', tag='Azimuth')
stEnumRasterOrientation.Elevation = stEnumRasterOrientation._CF_enumeration.addEnumeration(unicode_value='Elevation', tag='Elevation')
stEnumRasterOrientation._InitializeFacetMap(stEnumRasterOrientation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumRasterOrientation', stEnumRasterOrientation)
_module_typeBindings.stEnumRasterOrientation = stEnumRasterOrientation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumInitialBarDirection
class stEnumInitialBarDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumInitialBarDirection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2694, 2)
    _Documentation = ''
stEnumInitialBarDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumInitialBarDirection, enum_prefix=None)
stEnumInitialBarDirection.Clockwise = stEnumInitialBarDirection._CF_enumeration.addEnumeration(unicode_value='Clockwise', tag='Clockwise')
stEnumInitialBarDirection.Counter_Clockwise = stEnumInitialBarDirection._CF_enumeration.addEnumeration(unicode_value='Counter_Clockwise', tag='Counter_Clockwise')
stEnumInitialBarDirection.Up = stEnumInitialBarDirection._CF_enumeration.addEnumeration(unicode_value='Up', tag='Up')
stEnumInitialBarDirection.Down = stEnumInitialBarDirection._CF_enumeration.addEnumeration(unicode_value='Down', tag='Down')
stEnumInitialBarDirection._InitializeFacetMap(stEnumInitialBarDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumInitialBarDirection', stEnumInitialBarDirection)
_module_typeBindings.stEnumInitialBarDirection = stEnumInitialBarDirection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumInterbarDirection
class stEnumInterbarDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumInterbarDirection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2708, 2)
    _Documentation = ''
stEnumInterbarDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumInterbarDirection, enum_prefix=None)
stEnumInterbarDirection.Clockwise = stEnumInterbarDirection._CF_enumeration.addEnumeration(unicode_value='Clockwise', tag='Clockwise')
stEnumInterbarDirection.Counter_Clockwise = stEnumInterbarDirection._CF_enumeration.addEnumeration(unicode_value='Counter_Clockwise', tag='Counter_Clockwise')
stEnumInterbarDirection.Up = stEnumInterbarDirection._CF_enumeration.addEnumeration(unicode_value='Up', tag='Up')
stEnumInterbarDirection.Down = stEnumInterbarDirection._CF_enumeration.addEnumeration(unicode_value='Down', tag='Down')
stEnumInterbarDirection._InitializeFacetMap(stEnumInterbarDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumInterbarDirection', stEnumInterbarDirection)
_module_typeBindings.stEnumInterbarDirection = stEnumInterbarDirection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumAzScanDirection
class stEnumAzScanDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumAzScanDirection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2722, 2)
    _Documentation = ''
stEnumAzScanDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumAzScanDirection, enum_prefix=None)
stEnumAzScanDirection.Clockwise = stEnumAzScanDirection._CF_enumeration.addEnumeration(unicode_value='Clockwise', tag='Clockwise')
stEnumAzScanDirection.Counter_Clockwise = stEnumAzScanDirection._CF_enumeration.addEnumeration(unicode_value='Counter_Clockwise', tag='Counter_Clockwise')
stEnumAzScanDirection._InitializeFacetMap(stEnumAzScanDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumAzScanDirection', stEnumAzScanDirection)
_module_typeBindings.stEnumAzScanDirection = stEnumAzScanDirection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumBeamListOrder
class stEnumBeamListOrder (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumBeamListOrder')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2734, 2)
    _Documentation = ''
stEnumBeamListOrder._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumBeamListOrder, enum_prefix=None)
stEnumBeamListOrder.Random = stEnumBeamListOrder._CF_enumeration.addEnumeration(unicode_value='Random', tag='Random')
stEnumBeamListOrder.Sequential = stEnumBeamListOrder._CF_enumeration.addEnumeration(unicode_value='Sequential', tag='Sequential')
stEnumBeamListOrder._InitializeFacetMap(stEnumBeamListOrder._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumBeamListOrder', stEnumBeamListOrder)
_module_typeBindings.stEnumBeamListOrder = stEnumBeamListOrder

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumBiQuadPhaseMode
class stEnumBiQuadPhaseMode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumBiQuadPhaseMode')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2746, 2)
    _Documentation = ''
stEnumBiQuadPhaseMode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumBiQuadPhaseMode, enum_prefix=None)
stEnumBiQuadPhaseMode.None_ = stEnumBiQuadPhaseMode._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
stEnumBiQuadPhaseMode.Bi_Phase = stEnumBiQuadPhaseMode._CF_enumeration.addEnumeration(unicode_value='Bi_Phase', tag='Bi_Phase')
stEnumBiQuadPhaseMode.Quad_Phase = stEnumBiQuadPhaseMode._CF_enumeration.addEnumeration(unicode_value='Quad_Phase', tag='Quad_Phase')
stEnumBiQuadPhaseMode.Bi_And_Quad_Phase = stEnumBiQuadPhaseMode._CF_enumeration.addEnumeration(unicode_value='Bi_And_Quad_Phase', tag='Bi_And_Quad_Phase')
stEnumBiQuadPhaseMode._InitializeFacetMap(stEnumBiQuadPhaseMode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumBiQuadPhaseMode', stEnumBiQuadPhaseMode)
_module_typeBindings.stEnumBiQuadPhaseMode = stEnumBiQuadPhaseMode

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDirectionKind
class stEnumDirectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDirectionKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2760, 2)
    _Documentation = ''
stEnumDirectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDirectionKind, enum_prefix=None)
stEnumDirectionKind.Pointing_Angle = stEnumDirectionKind._CF_enumeration.addEnumeration(unicode_value='Pointing_Angle', tag='Pointing_Angle')
stEnumDirectionKind.Tracking = stEnumDirectionKind._CF_enumeration.addEnumeration(unicode_value='Tracking', tag='Tracking')
stEnumDirectionKind.Sut_Tracking = stEnumDirectionKind._CF_enumeration.addEnumeration(unicode_value='Sut_Tracking', tag='Sut_Tracking')
stEnumDirectionKind._InitializeFacetMap(stEnumDirectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDirectionKind', stEnumDirectionKind)
_module_typeBindings.stEnumDirectionKind = stEnumDirectionKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumBeamDirectionKind
class stEnumBeamDirectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumBeamDirectionKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2773, 2)
    _Documentation = ''
stEnumBeamDirectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumBeamDirectionKind, enum_prefix=None)
stEnumBeamDirectionKind.Pointing_Angle = stEnumBeamDirectionKind._CF_enumeration.addEnumeration(unicode_value='Pointing_Angle', tag='Pointing_Angle')
stEnumBeamDirectionKind.Tracking = stEnumBeamDirectionKind._CF_enumeration.addEnumeration(unicode_value='Tracking', tag='Tracking')
stEnumBeamDirectionKind.Sut_Tracking = stEnumBeamDirectionKind._CF_enumeration.addEnumeration(unicode_value='Sut_Tracking', tag='Sut_Tracking')
stEnumBeamDirectionKind._InitializeFacetMap(stEnumBeamDirectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumBeamDirectionKind', stEnumBeamDirectionKind)
_module_typeBindings.stEnumBeamDirectionKind = stEnumBeamDirectionKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumBarDirectionKind
class stEnumBarDirectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumBarDirectionKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2786, 2)
    _Documentation = ''
stEnumBarDirectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumBarDirectionKind, enum_prefix=None)
stEnumBarDirectionKind.Pointing_Angle = stEnumBarDirectionKind._CF_enumeration.addEnumeration(unicode_value='Pointing_Angle', tag='Pointing_Angle')
stEnumBarDirectionKind.Tracking = stEnumBarDirectionKind._CF_enumeration.addEnumeration(unicode_value='Tracking', tag='Tracking')
stEnumBarDirectionKind.Sut_Tracking = stEnumBarDirectionKind._CF_enumeration.addEnumeration(unicode_value='Sut_Tracking', tag='Sut_Tracking')
stEnumBarDirectionKind._InitializeFacetMap(stEnumBarDirectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumBarDirectionKind', stEnumBarDirectionKind)
_module_typeBindings.stEnumBarDirectionKind = stEnumBarDirectionKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumElScanDirection
class stEnumElScanDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumElScanDirection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2799, 2)
    _Documentation = ''
stEnumElScanDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumElScanDirection, enum_prefix=None)
stEnumElScanDirection.Up = stEnumElScanDirection._CF_enumeration.addEnumeration(unicode_value='Up', tag='Up')
stEnumElScanDirection.Down = stEnumElScanDirection._CF_enumeration.addEnumeration(unicode_value='Down', tag='Down')
stEnumElScanDirection._InitializeFacetMap(stEnumElScanDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumElScanDirection', stEnumElScanDirection)
_module_typeBindings.stEnumElScanDirection = stEnumElScanDirection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumGeneratorKind
class stEnumGeneratorKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumGeneratorKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2812, 2)
    _Documentation = ''
stEnumGeneratorKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumGeneratorKind, enum_prefix=None)
stEnumGeneratorKind.Independent = stEnumGeneratorKind._CF_enumeration.addEnumeration(unicode_value='Independent', tag='Independent')
stEnumGeneratorKind.Synchronized = stEnumGeneratorKind._CF_enumeration.addEnumeration(unicode_value='Synchronized', tag='Synchronized')
stEnumGeneratorKind.Interrupt = stEnumGeneratorKind._CF_enumeration.addEnumeration(unicode_value='Interrupt', tag='Interrupt')
stEnumGeneratorKind._InitializeFacetMap(stEnumGeneratorKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumGeneratorKind', stEnumGeneratorKind)
_module_typeBindings.stEnumGeneratorKind = stEnumGeneratorKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumHfimSamplePeriodKind
class stEnumHfimSamplePeriodKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumHfimSamplePeriodKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2825, 2)
    _Documentation = ''
stEnumHfimSamplePeriodKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumHfimSamplePeriodKind, enum_prefix=None)
stEnumHfimSamplePeriodKind.Period_15_625_Nanosec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_15_625_Nanosec', tag='Period_15_625_Nanosec')
stEnumHfimSamplePeriodKind.Period_62_5_Nanosec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_62_5_Nanosec', tag='Period_62_5_Nanosec')
stEnumHfimSamplePeriodKind.Period_250_Nanosec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_250_Nanosec', tag='Period_250_Nanosec')
stEnumHfimSamplePeriodKind.Period_1_Usec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_1_Usec', tag='Period_1_Usec')
stEnumHfimSamplePeriodKind.Period_7_813_Nanosec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_7_813_Nanosec', tag='Period_7_813_Nanosec')
stEnumHfimSamplePeriodKind.Period_31_25_Nanosec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_31_25_Nanosec', tag='Period_31_25_Nanosec')
stEnumHfimSamplePeriodKind.Period_125_Nanosec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_125_Nanosec', tag='Period_125_Nanosec')
stEnumHfimSamplePeriodKind.Period_500_Nanosec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_500_Nanosec', tag='Period_500_Nanosec')
stEnumHfimSamplePeriodKind.Period_2_Usec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_2_Usec', tag='Period_2_Usec')
stEnumHfimSamplePeriodKind.Period_3_90625_Nanosec = stEnumHfimSamplePeriodKind._CF_enumeration.addEnumeration(unicode_value='Period_3_90625_Nanosec', tag='Period_3_90625_Nanosec')
stEnumHfimSamplePeriodKind._InitializeFacetMap(stEnumHfimSamplePeriodKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumHfimSamplePeriodKind', stEnumHfimSamplePeriodKind)
_module_typeBindings.stEnumHfimSamplePeriodKind = stEnumHfimSamplePeriodKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumInterpulseModulationKind
class stEnumInterpulseModulationKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumInterpulseModulationKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2845, 2)
    _Documentation = ''
stEnumInterpulseModulationKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumInterpulseModulationKind, enum_prefix=None)
stEnumInterpulseModulationKind.Constant_Duty_Cycle = stEnumInterpulseModulationKind._CF_enumeration.addEnumeration(unicode_value='Constant_Duty_Cycle', tag='Constant_Duty_Cycle')
stEnumInterpulseModulationKind.Pulse_Width_Jitter = stEnumInterpulseModulationKind._CF_enumeration.addEnumeration(unicode_value='Pulse_Width_Jitter', tag='Pulse_Width_Jitter')
stEnumInterpulseModulationKind.Periodic_Modulation = stEnumInterpulseModulationKind._CF_enumeration.addEnumeration(unicode_value='Periodic_Modulation', tag='Periodic_Modulation')
stEnumInterpulseModulationKind._InitializeFacetMap(stEnumInterpulseModulationKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumInterpulseModulationKind', stEnumInterpulseModulationKind)
_module_typeBindings.stEnumInterpulseModulationKind = stEnumInterpulseModulationKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPowerLevelKind
class stEnumPowerLevelKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPowerLevelKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2858, 2)
    _Documentation = ''
stEnumPowerLevelKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPowerLevelKind, enum_prefix=None)
stEnumPowerLevelKind.Low_Power = stEnumPowerLevelKind._CF_enumeration.addEnumeration(unicode_value='Low_Power', tag='Low_Power')
stEnumPowerLevelKind.High_Power = stEnumPowerLevelKind._CF_enumeration.addEnumeration(unicode_value='High_Power', tag='High_Power')
stEnumPowerLevelKind._InitializeFacetMap(stEnumPowerLevelKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPowerLevelKind', stEnumPowerLevelKind)
_module_typeBindings.stEnumPowerLevelKind = stEnumPowerLevelKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPhaseShiftKind
class stEnumPhaseShiftKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPhaseShiftKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2870, 2)
    _Documentation = ''
stEnumPhaseShiftKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPhaseShiftKind, enum_prefix=None)
stEnumPhaseShiftKind.Of_0 = stEnumPhaseShiftKind._CF_enumeration.addEnumeration(unicode_value='Of_0', tag='Of_0')
stEnumPhaseShiftKind.Of_90 = stEnumPhaseShiftKind._CF_enumeration.addEnumeration(unicode_value='Of_90', tag='Of_90')
stEnumPhaseShiftKind.Of_180 = stEnumPhaseShiftKind._CF_enumeration.addEnumeration(unicode_value='Of_180', tag='Of_180')
stEnumPhaseShiftKind.Of_270 = stEnumPhaseShiftKind._CF_enumeration.addEnumeration(unicode_value='Of_270', tag='Of_270')
stEnumPhaseShiftKind._InitializeFacetMap(stEnumPhaseShiftKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPhaseShiftKind', stEnumPhaseShiftKind)
_module_typeBindings.stEnumPhaseShiftKind = stEnumPhaseShiftKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPolarizationModelKind
class stEnumPolarizationModelKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPolarizationModelKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2884, 2)
    _Documentation = ''
stEnumPolarizationModelKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPolarizationModelKind, enum_prefix=None)
stEnumPolarizationModelKind.None_ = stEnumPolarizationModelKind._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
stEnumPolarizationModelKind.Uniform_Polarization = stEnumPolarizationModelKind._CF_enumeration.addEnumeration(unicode_value='Uniform_Polarization', tag='Uniform_Polarization')
stEnumPolarizationModelKind.Az_El_Polarization = stEnumPolarizationModelKind._CF_enumeration.addEnumeration(unicode_value='Az_El_Polarization', tag='Az_El_Polarization')
stEnumPolarizationModelKind._InitializeFacetMap(stEnumPolarizationModelKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPolarizationModelKind', stEnumPolarizationModelKind)
_module_typeBindings.stEnumPolarizationModelKind = stEnumPolarizationModelKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPolarizationKind
class stEnumPolarizationKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPolarizationKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2897, 2)
    _Documentation = ''
stEnumPolarizationKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPolarizationKind, enum_prefix=None)
stEnumPolarizationKind.PolNone = stEnumPolarizationKind._CF_enumeration.addEnumeration(unicode_value='PolNone', tag='PolNone')
stEnumPolarizationKind.Horizontal = stEnumPolarizationKind._CF_enumeration.addEnumeration(unicode_value='Horizontal', tag='Horizontal')
stEnumPolarizationKind.Vertical = stEnumPolarizationKind._CF_enumeration.addEnumeration(unicode_value='Vertical', tag='Vertical')
stEnumPolarizationKind.Right_Slant = stEnumPolarizationKind._CF_enumeration.addEnumeration(unicode_value='Right_Slant', tag='Right_Slant')
stEnumPolarizationKind.Left_Slant = stEnumPolarizationKind._CF_enumeration.addEnumeration(unicode_value='Left_Slant', tag='Left_Slant')
stEnumPolarizationKind.RH_Circular = stEnumPolarizationKind._CF_enumeration.addEnumeration(unicode_value='RH_Circular', tag='RH_Circular')
stEnumPolarizationKind.LH_Circular = stEnumPolarizationKind._CF_enumeration.addEnumeration(unicode_value='LH_Circular', tag='LH_Circular')
stEnumPolarizationKind.Elliptical = stEnumPolarizationKind._CF_enumeration.addEnumeration(unicode_value='Elliptical', tag='Elliptical')
stEnumPolarizationKind._InitializeFacetMap(stEnumPolarizationKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPolarizationKind', stEnumPolarizationKind)
_module_typeBindings.stEnumPolarizationKind = stEnumPolarizationKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumFrequencySource
class stEnumFrequencySource (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumFrequencySource')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2915, 2)
    _Documentation = ''
stEnumFrequencySource._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumFrequencySource, enum_prefix=None)
stEnumFrequencySource.Primary = stEnumFrequencySource._CF_enumeration.addEnumeration(unicode_value='Primary', tag='Primary')
stEnumFrequencySource.Secondary = stEnumFrequencySource._CF_enumeration.addEnumeration(unicode_value='Secondary', tag='Secondary')
stEnumFrequencySource._InitializeFacetMap(stEnumFrequencySource._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumFrequencySource', stEnumFrequencySource)
_module_typeBindings.stEnumFrequencySource = stEnumFrequencySource

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPriority
class stEnumPriority (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPriority')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2927, 2)
    _Documentation = ''
stEnumPriority._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPriority, enum_prefix=None)
stEnumPriority.None_ = stEnumPriority._CF_enumeration.addEnumeration(unicode_value='None', tag='None_')
stEnumPriority.Digital = stEnumPriority._CF_enumeration.addEnumeration(unicode_value='Digital', tag='Digital')
stEnumPriority.Digital_Rf_Interrupt = stEnumPriority._CF_enumeration.addEnumeration(unicode_value='Digital_Rf_Interrupt', tag='Digital_Rf_Interrupt')
stEnumPriority._InitializeFacetMap(stEnumPriority._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPriority', stEnumPriority)
_module_typeBindings.stEnumPriority = stEnumPriority

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPulseGroupKind
class stEnumPulseGroupKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPulseGroupKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2940, 2)
    _Documentation = ''
stEnumPulseGroupKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPulseGroupKind, enum_prefix=None)
stEnumPulseGroupKind.Stable = stEnumPulseGroupKind._CF_enumeration.addEnumeration(unicode_value='Stable', tag='Stable')
stEnumPulseGroupKind.Modulation = stEnumPulseGroupKind._CF_enumeration.addEnumeration(unicode_value='Modulation', tag='Modulation')
stEnumPulseGroupKind.Stagger = stEnumPulseGroupKind._CF_enumeration.addEnumeration(unicode_value='Stagger', tag='Stagger')
stEnumPulseGroupKind._InitializeFacetMap(stEnumPulseGroupKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPulseGroupKind', stEnumPulseGroupKind)
_module_typeBindings.stEnumPulseGroupKind = stEnumPulseGroupKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDwellKind
class stEnumDwellKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDwellKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2953, 2)
    _Documentation = ''
stEnumDwellKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDwellKind, enum_prefix=None)
stEnumDwellKind.Pulse_Based = stEnumDwellKind._CF_enumeration.addEnumeration(unicode_value='Pulse_Based', tag='Pulse_Based')
stEnumDwellKind.Time_Based = stEnumDwellKind._CF_enumeration.addEnumeration(unicode_value='Time_Based', tag='Time_Based')
stEnumDwellKind._InitializeFacetMap(stEnumDwellKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDwellKind', stEnumDwellKind)
_module_typeBindings.stEnumDwellKind = stEnumDwellKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDelayTimeModPeriodKind
class stEnumDelayTimeModPeriodKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDelayTimeModPeriodKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2965, 2)
    _Documentation = ''
stEnumDelayTimeModPeriodKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDelayTimeModPeriodKind, enum_prefix=None)
stEnumDelayTimeModPeriodKind.Pulse_Based = stEnumDelayTimeModPeriodKind._CF_enumeration.addEnumeration(unicode_value='Pulse_Based', tag='Pulse_Based')
stEnumDelayTimeModPeriodKind.Time_Based = stEnumDelayTimeModPeriodKind._CF_enumeration.addEnumeration(unicode_value='Time_Based', tag='Time_Based')
stEnumDelayTimeModPeriodKind._InitializeFacetMap(stEnumDelayTimeModPeriodKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDelayTimeModPeriodKind', stEnumDelayTimeModPeriodKind)
_module_typeBindings.stEnumDelayTimeModPeriodKind = stEnumDelayTimeModPeriodKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumModPeriodKind
class stEnumModPeriodKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumModPeriodKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2977, 2)
    _Documentation = ''
stEnumModPeriodKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumModPeriodKind, enum_prefix=None)
stEnumModPeriodKind.Pulse_Based = stEnumModPeriodKind._CF_enumeration.addEnumeration(unicode_value='Pulse_Based', tag='Pulse_Based')
stEnumModPeriodKind.Time_Based = stEnumModPeriodKind._CF_enumeration.addEnumeration(unicode_value='Time_Based', tag='Time_Based')
stEnumModPeriodKind._InitializeFacetMap(stEnumModPeriodKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumModPeriodKind', stEnumModPeriodKind)
_module_typeBindings.stEnumModPeriodKind = stEnumModPeriodKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumInterruptGeneratorKind
class stEnumInterruptGeneratorKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumInterruptGeneratorKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 2989, 2)
    _Documentation = ''
stEnumInterruptGeneratorKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumInterruptGeneratorKind, enum_prefix=None)
stEnumInterruptGeneratorKind.Pulse_Based = stEnumInterruptGeneratorKind._CF_enumeration.addEnumeration(unicode_value='Pulse_Based', tag='Pulse_Based')
stEnumInterruptGeneratorKind.Time_Based = stEnumInterruptGeneratorKind._CF_enumeration.addEnumeration(unicode_value='Time_Based', tag='Time_Based')
stEnumInterruptGeneratorKind._InitializeFacetMap(stEnumInterruptGeneratorKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumInterruptGeneratorKind', stEnumInterruptGeneratorKind)
_module_typeBindings.stEnumInterruptGeneratorKind = stEnumInterruptGeneratorKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSwitchDelayKind
class stEnumSwitchDelayKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSwitchDelayKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3001, 2)
    _Documentation = ''
stEnumSwitchDelayKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumSwitchDelayKind, enum_prefix=None)
stEnumSwitchDelayKind.Pulse_Based = stEnumSwitchDelayKind._CF_enumeration.addEnumeration(unicode_value='Pulse_Based', tag='Pulse_Based')
stEnumSwitchDelayKind.Time_Based = stEnumSwitchDelayKind._CF_enumeration.addEnumeration(unicode_value='Time_Based', tag='Time_Based')
stEnumSwitchDelayKind._InitializeFacetMap(stEnumSwitchDelayKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumSwitchDelayKind', stEnumSwitchDelayKind)
_module_typeBindings.stEnumSwitchDelayKind = stEnumSwitchDelayKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumBeamDwellKind
class stEnumBeamDwellKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumBeamDwellKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3013, 2)
    _Documentation = ''
stEnumBeamDwellKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumBeamDwellKind, enum_prefix=None)
stEnumBeamDwellKind.Pulse_Based = stEnumBeamDwellKind._CF_enumeration.addEnumeration(unicode_value='Pulse_Based', tag='Pulse_Based')
stEnumBeamDwellKind.Time_Based = stEnumBeamDwellKind._CF_enumeration.addEnumeration(unicode_value='Time_Based', tag='Time_Based')
stEnumBeamDwellKind._InitializeFacetMap(stEnumBeamDwellKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumBeamDwellKind', stEnumBeamDwellKind)
_module_typeBindings.stEnumBeamDwellKind = stEnumBeamDwellKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumInterpulseModulationPeriodKind
class stEnumInterpulseModulationPeriodKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumInterpulseModulationPeriodKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3025, 2)
    _Documentation = ''
stEnumInterpulseModulationPeriodKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumInterpulseModulationPeriodKind, enum_prefix=None)
stEnumInterpulseModulationPeriodKind.Pulse_Based = stEnumInterpulseModulationPeriodKind._CF_enumeration.addEnumeration(unicode_value='Pulse_Based', tag='Pulse_Based')
stEnumInterpulseModulationPeriodKind.Time_Based = stEnumInterpulseModulationPeriodKind._CF_enumeration.addEnumeration(unicode_value='Time_Based', tag='Time_Based')
stEnumInterpulseModulationPeriodKind._InitializeFacetMap(stEnumInterpulseModulationPeriodKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumInterpulseModulationPeriodKind', stEnumInterpulseModulationPeriodKind)
_module_typeBindings.stEnumInterpulseModulationPeriodKind = stEnumInterpulseModulationPeriodKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumAzScanKind
class stEnumAzScanKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumAzScanKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3037, 2)
    _Documentation = ''
stEnumAzScanKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumAzScanKind, enum_prefix=None)
stEnumAzScanKind.Circular = stEnumAzScanKind._CF_enumeration.addEnumeration(unicode_value='Circular', tag='Circular')
stEnumAzScanKind.Omni = stEnumAzScanKind._CF_enumeration.addEnumeration(unicode_value='Omni', tag='Omni')
stEnumAzScanKind.Sector = stEnumAzScanKind._CF_enumeration.addEnumeration(unicode_value='Sector', tag='Sector')
stEnumAzScanKind.Steady = stEnumAzScanKind._CF_enumeration.addEnumeration(unicode_value='Steady', tag='Steady')
stEnumAzScanKind.Synchronized = stEnumAzScanKind._CF_enumeration.addEnumeration(unicode_value='Synchronized', tag='Synchronized')
stEnumAzScanKind._InitializeFacetMap(stEnumAzScanKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumAzScanKind', stEnumAzScanKind)
_module_typeBindings.stEnumAzScanKind = stEnumAzScanKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumElScanKind
class stEnumElScanKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumElScanKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3052, 2)
    _Documentation = ''
stEnumElScanKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumElScanKind, enum_prefix=None)
stEnumElScanKind.Circular = stEnumElScanKind._CF_enumeration.addEnumeration(unicode_value='Circular', tag='Circular')
stEnumElScanKind.Omni = stEnumElScanKind._CF_enumeration.addEnumeration(unicode_value='Omni', tag='Omni')
stEnumElScanKind.Sector = stEnumElScanKind._CF_enumeration.addEnumeration(unicode_value='Sector', tag='Sector')
stEnumElScanKind.Steady = stEnumElScanKind._CF_enumeration.addEnumeration(unicode_value='Steady', tag='Steady')
stEnumElScanKind.Synchronized = stEnumElScanKind._CF_enumeration.addEnumeration(unicode_value='Synchronized', tag='Synchronized')
stEnumElScanKind._InitializeFacetMap(stEnumElScanKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumElScanKind', stEnumElScanKind)
_module_typeBindings.stEnumElScanKind = stEnumElScanKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumScanMotion
class stEnumScanMotion (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumScanMotion')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3067, 2)
    _Documentation = ''
stEnumScanMotion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumScanMotion, enum_prefix=None)
stEnumScanMotion.Bidirectional = stEnumScanMotion._CF_enumeration.addEnumeration(unicode_value='Bidirectional', tag='Bidirectional')
stEnumScanMotion.Unidirectional = stEnumScanMotion._CF_enumeration.addEnumeration(unicode_value='Unidirectional', tag='Unidirectional')
stEnumScanMotion.Unidirectional_Flyback = stEnumScanMotion._CF_enumeration.addEnumeration(unicode_value='Unidirectional_Flyback', tag='Unidirectional_Flyback')
stEnumScanMotion._InitializeFacetMap(stEnumScanMotion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumScanMotion', stEnumScanMotion)
_module_typeBindings.stEnumScanMotion = stEnumScanMotion

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumAzScanMotion
class stEnumAzScanMotion (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumAzScanMotion')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3080, 2)
    _Documentation = ''
stEnumAzScanMotion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumAzScanMotion, enum_prefix=None)
stEnumAzScanMotion.Bidirectional = stEnumAzScanMotion._CF_enumeration.addEnumeration(unicode_value='Bidirectional', tag='Bidirectional')
stEnumAzScanMotion.Unidirectional = stEnumAzScanMotion._CF_enumeration.addEnumeration(unicode_value='Unidirectional', tag='Unidirectional')
stEnumAzScanMotion.Unidirectional_Flyback = stEnumAzScanMotion._CF_enumeration.addEnumeration(unicode_value='Unidirectional_Flyback', tag='Unidirectional_Flyback')
stEnumAzScanMotion._InitializeFacetMap(stEnumAzScanMotion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumAzScanMotion', stEnumAzScanMotion)
_module_typeBindings.stEnumAzScanMotion = stEnumAzScanMotion

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumElScanMotion
class stEnumElScanMotion (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumElScanMotion')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3093, 2)
    _Documentation = ''
stEnumElScanMotion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumElScanMotion, enum_prefix=None)
stEnumElScanMotion.Bidirectional = stEnumElScanMotion._CF_enumeration.addEnumeration(unicode_value='Bidirectional', tag='Bidirectional')
stEnumElScanMotion.Unidirectional = stEnumElScanMotion._CF_enumeration.addEnumeration(unicode_value='Unidirectional', tag='Unidirectional')
stEnumElScanMotion.Unidirectional_Flyback = stEnumElScanMotion._CF_enumeration.addEnumeration(unicode_value='Unidirectional_Flyback', tag='Unidirectional_Flyback')
stEnumElScanMotion._InitializeFacetMap(stEnumElScanMotion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumElScanMotion', stEnumElScanMotion)
_module_typeBindings.stEnumElScanMotion = stEnumElScanMotion

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumBarScanMotion
class stEnumBarScanMotion (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumBarScanMotion')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3106, 2)
    _Documentation = ''
stEnumBarScanMotion._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumBarScanMotion, enum_prefix=None)
stEnumBarScanMotion.Bidirectional = stEnumBarScanMotion._CF_enumeration.addEnumeration(unicode_value='Bidirectional', tag='Bidirectional')
stEnumBarScanMotion.Unidirectional = stEnumBarScanMotion._CF_enumeration.addEnumeration(unicode_value='Unidirectional', tag='Unidirectional')
stEnumBarScanMotion.Unidirectional_Flyback = stEnumBarScanMotion._CF_enumeration.addEnumeration(unicode_value='Unidirectional_Flyback', tag='Unidirectional_Flyback')
stEnumBarScanMotion._InitializeFacetMap(stEnumBarScanMotion._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumBarScanMotion', stEnumBarScanMotion)
_module_typeBindings.stEnumBarScanMotion = stEnumBarScanMotion

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSpiralDirection
class stEnumSpiralDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSpiralDirection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3119, 2)
    _Documentation = ''
stEnumSpiralDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumSpiralDirection, enum_prefix=None)
stEnumSpiralDirection.Inward = stEnumSpiralDirection._CF_enumeration.addEnumeration(unicode_value='Inward', tag='Inward')
stEnumSpiralDirection.Outward = stEnumSpiralDirection._CF_enumeration.addEnumeration(unicode_value='Outward', tag='Outward')
stEnumSpiralDirection._InitializeFacetMap(stEnumSpiralDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumSpiralDirection', stEnumSpiralDirection)
_module_typeBindings.stEnumSpiralDirection = stEnumSpiralDirection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumTriggerType
class stEnumTriggerType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumTriggerType')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3131, 2)
    _Documentation = ''
stEnumTriggerType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumTriggerType, enum_prefix=None)
stEnumTriggerType.Bar = stEnumTriggerType._CF_enumeration.addEnumeration(unicode_value='Bar', tag='Bar')
stEnumTriggerType.Raster = stEnumTriggerType._CF_enumeration.addEnumeration(unicode_value='Raster', tag='Raster')
stEnumTriggerType._InitializeFacetMap(stEnumTriggerType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumTriggerType', stEnumTriggerType)
_module_typeBindings.stEnumTriggerType = stEnumTriggerType

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumAltitudeKind
class stEnumAltitudeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumAltitudeKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3143, 2)
    _Documentation = ''
stEnumAltitudeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumAltitudeKind, enum_prefix=None)
stEnumAltitudeKind.Km_Above_Sea_Level = stEnumAltitudeKind._CF_enumeration.addEnumeration(unicode_value='Km_Above_Sea_Level', tag='Km_Above_Sea_Level')
stEnumAltitudeKind.Km_Above_Terrain = stEnumAltitudeKind._CF_enumeration.addEnumeration(unicode_value='Km_Above_Terrain', tag='Km_Above_Terrain')
stEnumAltitudeKind._InitializeFacetMap(stEnumAltitudeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumAltitudeKind', stEnumAltitudeKind)
_module_typeBindings.stEnumAltitudeKind = stEnumAltitudeKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPitchKind
class stEnumPitchKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPitchKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3155, 2)
    _Documentation = ''
stEnumPitchKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPitchKind, enum_prefix=None)
stEnumPitchKind.Absolute = stEnumPitchKind._CF_enumeration.addEnumeration(unicode_value='Absolute', tag='Absolute')
stEnumPitchKind.Relative = stEnumPitchKind._CF_enumeration.addEnumeration(unicode_value='Relative', tag='Relative')
stEnumPitchKind._InitializeFacetMap(stEnumPitchKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPitchKind', stEnumPitchKind)
_module_typeBindings.stEnumPitchKind = stEnumPitchKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPulseContendedStateKind
class stEnumPulseContendedStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPulseContendedStateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3167, 2)
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3180, 2)
    _Documentation = ''
stEnumPulseInhibitStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumPulseInhibitStateKind, enum_prefix=None)
stEnumPulseInhibitStateKind.Ignore = stEnumPulseInhibitStateKind._CF_enumeration.addEnumeration(unicode_value='Ignore', tag='Ignore')
stEnumPulseInhibitStateKind.Store_Only_Pulses_Inhibited = stEnumPulseInhibitStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Pulses_Inhibited', tag='Store_Only_Pulses_Inhibited')
stEnumPulseInhibitStateKind.Store_Only_Pulses_Not_Inhibited = stEnumPulseInhibitStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Pulses_Not_Inhibited', tag='Store_Only_Pulses_Not_Inhibited')
stEnumPulseInhibitStateKind._InitializeFacetMap(stEnumPulseInhibitStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumPulseInhibitStateKind', stEnumPulseInhibitStateKind)
_module_typeBindings.stEnumPulseInhibitStateKind = stEnumPulseInhibitStateKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumExternalGatingStateKind
class stEnumExternalGatingStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumExternalGatingStateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3193, 2)
    _Documentation = ''
stEnumExternalGatingStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumExternalGatingStateKind, enum_prefix=None)
stEnumExternalGatingStateKind.Ignore = stEnumExternalGatingStateKind._CF_enumeration.addEnumeration(unicode_value='Ignore', tag='Ignore')
stEnumExternalGatingStateKind.Store_Only_Gated_Pulses = stEnumExternalGatingStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Gated_Pulses', tag='Store_Only_Gated_Pulses')
stEnumExternalGatingStateKind._InitializeFacetMap(stEnumExternalGatingStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumExternalGatingStateKind', stEnumExternalGatingStateKind)
_module_typeBindings.stEnumExternalGatingStateKind = stEnumExternalGatingStateKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDgsVideoStateKind
class stEnumDgsVideoStateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDgsVideoStateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3205, 2)
    _Documentation = ''
stEnumDgsVideoStateKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDgsVideoStateKind, enum_prefix=None)
stEnumDgsVideoStateKind.Ignore = stEnumDgsVideoStateKind._CF_enumeration.addEnumeration(unicode_value='Ignore', tag='Ignore')
stEnumDgsVideoStateKind.Store_Only_Video_Enabled_Pulses = stEnumDgsVideoStateKind._CF_enumeration.addEnumeration(unicode_value='Store_Only_Video_Enabled_Pulses', tag='Store_Only_Video_Enabled_Pulses')
stEnumDgsVideoStateKind._InitializeFacetMap(stEnumDgsVideoStateKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDgsVideoStateKind', stEnumDgsVideoStateKind)
_module_typeBindings.stEnumDgsVideoStateKind = stEnumDgsVideoStateKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumPdwKind
class stEnumPdwKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumPdwKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3217, 2)
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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDistanceUnits
class stEnumDistanceUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDistanceUnits')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3233, 2)
    _Documentation = ''
stEnumDistanceUnits._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDistanceUnits, enum_prefix=None)
stEnumDistanceUnits.Kilometers = stEnumDistanceUnits._CF_enumeration.addEnumeration(unicode_value='Kilometers', tag='Kilometers')
stEnumDistanceUnits.Nautical_Miles = stEnumDistanceUnits._CF_enumeration.addEnumeration(unicode_value='Nautical_Miles', tag='Nautical_Miles')
stEnumDistanceUnits._InitializeFacetMap(stEnumDistanceUnits._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDistanceUnits', stEnumDistanceUnits)
_module_typeBindings.stEnumDistanceUnits = stEnumDistanceUnits

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumEnvironmentKind
class stEnumEnvironmentKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumEnvironmentKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3245, 2)
    _Documentation = ''
stEnumEnvironmentKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumEnvironmentKind, enum_prefix=None)
stEnumEnvironmentKind.Round = stEnumEnvironmentKind._CF_enumeration.addEnumeration(unicode_value='Round', tag='Round')
stEnumEnvironmentKind.Flat = stEnumEnvironmentKind._CF_enumeration.addEnumeration(unicode_value='Flat', tag='Flat')
stEnumEnvironmentKind._InitializeFacetMap(stEnumEnvironmentKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumEnvironmentKind', stEnumEnvironmentKind)
_module_typeBindings.stEnumEnvironmentKind = stEnumEnvironmentKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumRainfallRateKind
class stEnumRainfallRateKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumRainfallRateKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3257, 2)
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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSituationDisplayModeKind
class stEnumSituationDisplayModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSituationDisplayModeKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3273, 2)
    _Documentation = ''
stEnumSituationDisplayModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumSituationDisplayModeKind, enum_prefix=None)
stEnumSituationDisplayModeKind.Rectangular = stEnumSituationDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Rectangular', tag='Rectangular')
stEnumSituationDisplayModeKind.Polar = stEnumSituationDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Polar', tag='Polar')
stEnumSituationDisplayModeKind._InitializeFacetMap(stEnumSituationDisplayModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumSituationDisplayModeKind', stEnumSituationDisplayModeKind)
_module_typeBindings.stEnumSituationDisplayModeKind = stEnumSituationDisplayModeKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumGuiDisplayModeKind
class stEnumGuiDisplayModeKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumGuiDisplayModeKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3285, 2)
    _Documentation = ''
stEnumGuiDisplayModeKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumGuiDisplayModeKind, enum_prefix=None)
stEnumGuiDisplayModeKind.Plan_View = stEnumGuiDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Plan_View', tag='Plan_View')
stEnumGuiDisplayModeKind.Threed_View = stEnumGuiDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Threed_View', tag='Threed_View')
stEnumGuiDisplayModeKind.Polar_View = stEnumGuiDisplayModeKind._CF_enumeration.addEnumeration(unicode_value='Polar_View', tag='Polar_View')
stEnumGuiDisplayModeKind._InitializeFacetMap(stEnumGuiDisplayModeKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumGuiDisplayModeKind', stEnumGuiDisplayModeKind)
_module_typeBindings.stEnumGuiDisplayModeKind = stEnumGuiDisplayModeKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDisplayGridKind
class stEnumDisplayGridKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDisplayGridKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3298, 2)
    _Documentation = ''
stEnumDisplayGridKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDisplayGridKind, enum_prefix=None)
stEnumDisplayGridKind.Decimal = stEnumDisplayGridKind._CF_enumeration.addEnumeration(unicode_value='Decimal', tag='Decimal')
stEnumDisplayGridKind.Deg_Min_Sec = stEnumDisplayGridKind._CF_enumeration.addEnumeration(unicode_value='Deg_Min_Sec', tag='Deg_Min_Sec')
stEnumDisplayGridKind._InitializeFacetMap(stEnumDisplayGridKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDisplayGridKind', stEnumDisplayGridKind)
_module_typeBindings.stEnumDisplayGridKind = stEnumDisplayGridKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSituationDisplayCenterKind
class stEnumSituationDisplayCenterKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSituationDisplayCenterKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3310, 2)
    _Documentation = ''
stEnumSituationDisplayCenterKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumSituationDisplayCenterKind, enum_prefix=None)
stEnumSituationDisplayCenterKind.On_Sut = stEnumSituationDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='On_Sut', tag='On_Sut')
stEnumSituationDisplayCenterKind.At_Point = stEnumSituationDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='At_Point', tag='At_Point')
stEnumSituationDisplayCenterKind._InitializeFacetMap(stEnumSituationDisplayCenterKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumSituationDisplayCenterKind', stEnumSituationDisplayCenterKind)
_module_typeBindings.stEnumSituationDisplayCenterKind = stEnumSituationDisplayCenterKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDisplayCenterKind
class stEnumDisplayCenterKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDisplayCenterKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3322, 2)
    _Documentation = ''
stEnumDisplayCenterKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDisplayCenterKind, enum_prefix=None)
stEnumDisplayCenterKind.On_Sut = stEnumDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='On_Sut', tag='On_Sut')
stEnumDisplayCenterKind.On_Platform = stEnumDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='On_Platform', tag='On_Platform')
stEnumDisplayCenterKind.At_Fixed_Point = stEnumDisplayCenterKind._CF_enumeration.addEnumeration(unicode_value='At_Fixed_Point', tag='At_Fixed_Point')
stEnumDisplayCenterKind._InitializeFacetMap(stEnumDisplayCenterKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDisplayCenterKind', stEnumDisplayCenterKind)
_module_typeBindings.stEnumDisplayCenterKind = stEnumDisplayCenterKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSpeedUnits
class stEnumSpeedUnits (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSpeedUnits')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3335, 2)
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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumTurnKind
class stEnumTurnKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumTurnKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3350, 2)
    _Documentation = ''
stEnumTurnKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumTurnKind, enum_prefix=None)
stEnumTurnKind.Load_Factor = stEnumTurnKind._CF_enumeration.addEnumeration(unicode_value='Load_Factor', tag='Load_Factor')
stEnumTurnKind.Radius = stEnumTurnKind._CF_enumeration.addEnumeration(unicode_value='Radius', tag='Radius')
stEnumTurnKind._InitializeFacetMap(stEnumTurnKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumTurnKind', stEnumTurnKind)
_module_typeBindings.stEnumTurnKind = stEnumTurnKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumTerrainDtedKind
class stEnumTerrainDtedKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumTerrainDtedKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3362, 2)
    _Documentation = ''
stEnumTerrainDtedKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumTerrainDtedKind, enum_prefix=None)
stEnumTerrainDtedKind.Level_0 = stEnumTerrainDtedKind._CF_enumeration.addEnumeration(unicode_value='Level_0', tag='Level_0')
stEnumTerrainDtedKind.Level_1 = stEnumTerrainDtedKind._CF_enumeration.addEnumeration(unicode_value='Level_1', tag='Level_1')
stEnumTerrainDtedKind.Ceesim_Elv = stEnumTerrainDtedKind._CF_enumeration.addEnumeration(unicode_value='Ceesim_Elv', tag='Ceesim_Elv')
stEnumTerrainDtedKind._InitializeFacetMap(stEnumTerrainDtedKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumTerrainDtedKind', stEnumTerrainDtedKind)
_module_typeBindings.stEnumTerrainDtedKind = stEnumTerrainDtedKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNorthSouthDirectionKind
class stEnumNorthSouthDirectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNorthSouthDirectionKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3375, 2)
    _Documentation = ''
stEnumNorthSouthDirectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNorthSouthDirectionKind, enum_prefix=None)
stEnumNorthSouthDirectionKind.North = stEnumNorthSouthDirectionKind._CF_enumeration.addEnumeration(unicode_value='North', tag='North')
stEnumNorthSouthDirectionKind.South = stEnumNorthSouthDirectionKind._CF_enumeration.addEnumeration(unicode_value='South', tag='South')
stEnumNorthSouthDirectionKind._InitializeFacetMap(stEnumNorthSouthDirectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNorthSouthDirectionKind', stEnumNorthSouthDirectionKind)
_module_typeBindings.stEnumNorthSouthDirectionKind = stEnumNorthSouthDirectionKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumEastWestDirectionKind
class stEnumEastWestDirectionKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumEastWestDirectionKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3387, 2)
    _Documentation = ''
stEnumEastWestDirectionKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumEastWestDirectionKind, enum_prefix=None)
stEnumEastWestDirectionKind.East = stEnumEastWestDirectionKind._CF_enumeration.addEnumeration(unicode_value='East', tag='East')
stEnumEastWestDirectionKind.West = stEnumEastWestDirectionKind._CF_enumeration.addEnumeration(unicode_value='West', tag='West')
stEnumEastWestDirectionKind._InitializeFacetMap(stEnumEastWestDirectionKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumEastWestDirectionKind', stEnumEastWestDirectionKind)
_module_typeBindings.stEnumEastWestDirectionKind = stEnumEastWestDirectionKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumDuctingBoundaryKind
class stEnumDuctingBoundaryKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumDuctingBoundaryKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3399, 2)
    _Documentation = ''
stEnumDuctingBoundaryKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumDuctingBoundaryKind, enum_prefix=None)
stEnumDuctingBoundaryKind.Independent_Of_Surface_Type = stEnumDuctingBoundaryKind._CF_enumeration.addEnumeration(unicode_value='Independent_Of_Surface_Type', tag='Independent_Of_Surface_Type')
stEnumDuctingBoundaryKind.Land_Sea_Boundaries = stEnumDuctingBoundaryKind._CF_enumeration.addEnumeration(unicode_value='Land_Sea_Boundaries', tag='Land_Sea_Boundaries')
stEnumDuctingBoundaryKind._InitializeFacetMap(stEnumDuctingBoundaryKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumDuctingBoundaryKind', stEnumDuctingBoundaryKind)
_module_typeBindings.stEnumDuctingBoundaryKind = stEnumDuctingBoundaryKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumSurfaceKind
class stEnumSurfaceKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumSurfaceKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3411, 2)
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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumEventType
class stEnumEventType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumEventType')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3431, 2)
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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNavIfPhysicalIfKind
class stEnumNavIfPhysicalIfKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNavIfPhysicalIfKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3448, 2)
    _Documentation = ''
stEnumNavIfPhysicalIfKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNavIfPhysicalIfKind, enum_prefix=None)
stEnumNavIfPhysicalIfKind.Nav_1553b = stEnumNavIfPhysicalIfKind._CF_enumeration.addEnumeration(unicode_value='Nav_1553b', tag='Nav_1553b')
stEnumNavIfPhysicalIfKind.Nav_Ethernet = stEnumNavIfPhysicalIfKind._CF_enumeration.addEnumeration(unicode_value='Nav_Ethernet', tag='Nav_Ethernet')
stEnumNavIfPhysicalIfKind.Nav_Rm = stEnumNavIfPhysicalIfKind._CF_enumeration.addEnumeration(unicode_value='Nav_Rm', tag='Nav_Rm')
stEnumNavIfPhysicalIfKind._InitializeFacetMap(stEnumNavIfPhysicalIfKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNavIfPhysicalIfKind', stEnumNavIfPhysicalIfKind)
_module_typeBindings.stEnumNavIfPhysicalIfKind = stEnumNavIfPhysicalIfKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNavIf1553BusKind
class stEnumNavIf1553BusKind (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNavIf1553BusKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3461, 2)
    _Documentation = ''
stEnumNavIf1553BusKind._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNavIf1553BusKind, enum_prefix=None)
stEnumNavIf1553BusKind.Bus_A = stEnumNavIf1553BusKind._CF_enumeration.addEnumeration(unicode_value='Bus_A', tag='Bus_A')
stEnumNavIf1553BusKind.Bus_B = stEnumNavIf1553BusKind._CF_enumeration.addEnumeration(unicode_value='Bus_B', tag='Bus_B')
stEnumNavIf1553BusKind._InitializeFacetMap(stEnumNavIf1553BusKind._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNavIf1553BusKind', stEnumNavIf1553BusKind)
_module_typeBindings.stEnumNavIf1553BusKind = stEnumNavIf1553BusKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNavIfUpdateInterval
class stEnumNavIfUpdateInterval (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNavIfUpdateInterval')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3473, 2)
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

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stEnumNavIfTransferDirection
class stEnumNavIfTransferDirection (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stEnumNavIfTransferDirection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3491, 2)
    _Documentation = ''
stEnumNavIfTransferDirection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=stEnumNavIfTransferDirection, enum_prefix=None)
stEnumNavIfTransferDirection.Receive = stEnumNavIfTransferDirection._CF_enumeration.addEnumeration(unicode_value='Receive', tag='Receive')
stEnumNavIfTransferDirection.Transmit = stEnumNavIfTransferDirection._CF_enumeration.addEnumeration(unicode_value='Transmit', tag='Transmit')
stEnumNavIfTransferDirection._InitializeFacetMap(stEnumNavIfTransferDirection._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'stEnumNavIfTransferDirection', stEnumNavIfTransferDirection)
_module_typeBindings.stEnumNavIfTransferDirection = stEnumNavIfTransferDirection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringPlatformId
class stStringPlatformId (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringPlatformId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3503, 2)
    _Documentation = ''
stStringPlatformId._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringPlatformId._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12))
stStringPlatformId._InitializeFacetMap(stStringPlatformId._CF_minLength,
   stStringPlatformId._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringPlatformId', stStringPlatformId)
_module_typeBindings.stStringPlatformId = stStringPlatformId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringSegmentName
class stStringSegmentName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringSegmentName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3515, 2)
    _Documentation = ''
stStringSegmentName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stStringSegmentName', stStringSegmentName)
_module_typeBindings.stStringSegmentName = stStringSegmentName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringDelayTimeJitterDstrbKind
class stStringDelayTimeJitterDstrbKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringDelayTimeJitterDstrbKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3524, 2)
    _Documentation = ''
stStringDelayTimeJitterDstrbKind._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringDelayTimeJitterDstrbKind._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringDelayTimeJitterDstrbKind._InitializeFacetMap(stStringDelayTimeJitterDstrbKind._CF_minLength,
   stStringDelayTimeJitterDstrbKind._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringDelayTimeJitterDstrbKind', stStringDelayTimeJitterDstrbKind)
_module_typeBindings.stStringDelayTimeJitterDstrbKind = stStringDelayTimeJitterDstrbKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringSecDtJitterDstrbKind
class stStringSecDtJitterDstrbKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringSecDtJitterDstrbKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3536, 2)
    _Documentation = ''
stStringSecDtJitterDstrbKind._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringSecDtJitterDstrbKind._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringSecDtJitterDstrbKind._InitializeFacetMap(stStringSecDtJitterDstrbKind._CF_minLength,
   stStringSecDtJitterDstrbKind._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringSecDtJitterDstrbKind', stStringSecDtJitterDstrbKind)
_module_typeBindings.stStringSecDtJitterDstrbKind = stStringSecDtJitterDstrbKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringJitterDstrbKind
class stStringJitterDstrbKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringJitterDstrbKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3548, 2)
    _Documentation = ''
stStringJitterDstrbKind._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringJitterDstrbKind._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringJitterDstrbKind._InitializeFacetMap(stStringJitterDstrbKind._CF_minLength,
   stStringJitterDstrbKind._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringJitterDstrbKind', stStringJitterDstrbKind)
_module_typeBindings.stStringJitterDstrbKind = stStringJitterDstrbKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringSecJitterDstrbKind
class stStringSecJitterDstrbKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringSecJitterDstrbKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3560, 2)
    _Documentation = ''
stStringSecJitterDstrbKind._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringSecJitterDstrbKind._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringSecJitterDstrbKind._InitializeFacetMap(stStringSecJitterDstrbKind._CF_minLength,
   stStringSecJitterDstrbKind._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringSecJitterDstrbKind', stStringSecJitterDstrbKind)
_module_typeBindings.stStringSecJitterDstrbKind = stStringSecJitterDstrbKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringAgilityPatternName
class stStringAgilityPatternName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringAgilityPatternName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3572, 2)
    _Documentation = ''
stStringAgilityPatternName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringAgilityPatternName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringAgilityPatternName._InitializeFacetMap(stStringAgilityPatternName._CF_minLength,
   stStringAgilityPatternName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringAgilityPatternName', stStringAgilityPatternName)
_module_typeBindings.stStringAgilityPatternName = stStringAgilityPatternName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringJitterDstrbName
class stStringJitterDstrbName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringJitterDstrbName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3584, 2)
    _Documentation = ''
stStringJitterDstrbName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringJitterDstrbName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringJitterDstrbName._InitializeFacetMap(stStringJitterDstrbName._CF_minLength,
   stStringJitterDstrbName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringJitterDstrbName', stStringJitterDstrbName)
_module_typeBindings.stStringJitterDstrbName = stStringJitterDstrbName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringCommentScenarioHeader
class stStringCommentScenarioHeader (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringCommentScenarioHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3596, 2)
    _Documentation = ''
stStringCommentScenarioHeader._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringCommentScenarioHeader._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30))
stStringCommentScenarioHeader._InitializeFacetMap(stStringCommentScenarioHeader._CF_minLength,
   stStringCommentScenarioHeader._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringCommentScenarioHeader', stStringCommentScenarioHeader)
_module_typeBindings.stStringCommentScenarioHeader = stStringCommentScenarioHeader

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringModeComment
class stStringModeComment (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringModeComment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3608, 2)
    _Documentation = ''
stStringModeComment._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringModeComment._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(250))
stStringModeComment._InitializeFacetMap(stStringModeComment._CF_minLength,
   stStringModeComment._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringModeComment', stStringModeComment)
_module_typeBindings.stStringModeComment = stStringModeComment

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringGeneratorComment
class stStringGeneratorComment (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringGeneratorComment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3620, 2)
    _Documentation = ''
stStringGeneratorComment._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stStringGeneratorComment', stStringGeneratorComment)
_module_typeBindings.stStringGeneratorComment = stStringGeneratorComment

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringGeneratorName
class stStringGeneratorName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringGeneratorName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3629, 2)
    _Documentation = ''
stStringGeneratorName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringGeneratorName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(250))
stStringGeneratorName._InitializeFacetMap(stStringGeneratorName._CF_minLength,
   stStringGeneratorName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringGeneratorName', stStringGeneratorName)
_module_typeBindings.stStringGeneratorName = stStringGeneratorName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringModeName
class stStringModeName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringModeName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3641, 2)
    _Documentation = ''
stStringModeName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
stStringModeName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(22))
stStringModeName._InitializeFacetMap(stStringModeName._CF_minLength,
   stStringModeName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringModeName', stStringModeName)
_module_typeBindings.stStringModeName = stStringModeName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringEmitterId
class stStringEmitterId (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringEmitterId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3653, 2)
    _Documentation = ''
stStringEmitterId._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringEmitterId._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(5))
stStringEmitterId._InitializeFacetMap(stStringEmitterId._CF_minLength,
   stStringEmitterId._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringEmitterId', stStringEmitterId)
_module_typeBindings.stStringEmitterId = stStringEmitterId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringEmitterName
class stStringEmitterName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringEmitterName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3665, 2)
    _Documentation = ''
stStringEmitterName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringEmitterName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(22))
stStringEmitterName._InitializeFacetMap(stStringEmitterName._CF_minLength,
   stStringEmitterName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringEmitterName', stStringEmitterName)
_module_typeBindings.stStringEmitterName = stStringEmitterName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringModeNameScript
class stStringModeNameScript (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringModeNameScript')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3677, 2)
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3689, 2)
    _Documentation = ''
stStringRangeModeName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringRangeModeName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(22))
stStringRangeModeName._InitializeFacetMap(stStringRangeModeName._CF_minLength,
   stStringRangeModeName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringRangeModeName', stStringRangeModeName)
_module_typeBindings.stStringRangeModeName = stStringRangeModeName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringSubmodeName
class stStringSubmodeName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringSubmodeName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3701, 2)
    _Documentation = ''
stStringSubmodeName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringSubmodeName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(22))
stStringSubmodeName._InitializeFacetMap(stStringSubmodeName._CF_minLength,
   stStringSubmodeName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringSubmodeName', stStringSubmodeName)
_module_typeBindings.stStringSubmodeName = stStringSubmodeName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringEmitterLibraryName
class stStringEmitterLibraryName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringEmitterLibraryName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3713, 2)
    _Documentation = ''
stStringEmitterLibraryName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringEmitterLibraryName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
stStringEmitterLibraryName._InitializeFacetMap(stStringEmitterLibraryName._CF_minLength,
   stStringEmitterLibraryName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringEmitterLibraryName', stStringEmitterLibraryName)
_module_typeBindings.stStringEmitterLibraryName = stStringEmitterLibraryName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringDuctingFileName
class stStringDuctingFileName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringDuctingFileName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3725, 2)
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
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3737, 2)
    _Documentation = ''
stStringDxFileName._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(0))
stStringDxFileName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(255))
stStringDxFileName._InitializeFacetMap(stStringDxFileName._CF_minLength,
   stStringDxFileName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringDxFileName', stStringDxFileName)
_module_typeBindings.stStringDxFileName = stStringDxFileName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stStringComplexPriEntryId
class stStringComplexPriEntryId (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stStringComplexPriEntryId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3749, 2)
    _Documentation = ''
stStringComplexPriEntryId._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
stStringComplexPriEntryId._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40))
stStringComplexPriEntryId._InitializeFacetMap(stStringComplexPriEntryId._CF_minLength,
   stStringComplexPriEntryId._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'stStringComplexPriEntryId', stStringComplexPriEntryId)
_module_typeBindings.stStringComplexPriEntryId = stStringComplexPriEntryId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextCommentHeader
class stTextCommentHeader (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextCommentHeader')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3761, 2)
    _Documentation = ''
stTextCommentHeader._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextCommentHeader', stTextCommentHeader)
_module_typeBindings.stTextCommentHeader = stTextCommentHeader

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextAzElPatternName
class stTextAzElPatternName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextAzElPatternName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3770, 2)
    _Documentation = ''
stTextAzElPatternName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextAzElPatternName', stTextAzElPatternName)
_module_typeBindings.stTextAzElPatternName = stTextAzElPatternName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextHfimSampleName
class stTextHfimSampleName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextHfimSampleName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3779, 2)
    _Documentation = ''
stTextHfimSampleName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextHfimSampleName', stTextHfimSampleName)
_module_typeBindings.stTextHfimSampleName = stTextHfimSampleName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextSymbolKind
class stTextSymbolKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextSymbolKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3788, 2)
    _Documentation = ''
stTextSymbolKind._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextSymbolKind', stTextSymbolKind)
_module_typeBindings.stTextSymbolKind = stTextSymbolKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextScenarioElementLibraryName
class stTextScenarioElementLibraryName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextScenarioElementLibraryName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3797, 2)
    _Documentation = ''
stTextScenarioElementLibraryName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextScenarioElementLibraryName', stTextScenarioElementLibraryName)
_module_typeBindings.stTextScenarioElementLibraryName = stTextScenarioElementLibraryName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextGeotiffPath
class stTextGeotiffPath (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextGeotiffPath')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3806, 2)
    _Documentation = ''
stTextGeotiffPath._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextGeotiffPath', stTextGeotiffPath)
_module_typeBindings.stTextGeotiffPath = stTextGeotiffPath

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextAzScanShape
class stTextAzScanShape (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextAzScanShape')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3815, 2)
    _Documentation = ''
stTextAzScanShape._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextAzScanShape', stTextAzScanShape)
_module_typeBindings.stTextAzScanShape = stTextAzScanShape

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextElScanShape
class stTextElScanShape (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextElScanShape')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3824, 2)
    _Documentation = ''
stTextElScanShape._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextElScanShape', stTextElScanShape)
_module_typeBindings.stTextElScanShape = stTextElScanShape

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextDelayTimeModPatternKind
class stTextDelayTimeModPatternKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextDelayTimeModPatternKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3833, 2)
    _Documentation = ''
stTextDelayTimeModPatternKind._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextDelayTimeModPatternKind', stTextDelayTimeModPatternKind)
_module_typeBindings.stTextDelayTimeModPatternKind = stTextDelayTimeModPatternKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextSecDtModPatternKind
class stTextSecDtModPatternKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextSecDtModPatternKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3842, 2)
    _Documentation = ''
stTextSecDtModPatternKind._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextSecDtModPatternKind', stTextSecDtModPatternKind)
_module_typeBindings.stTextSecDtModPatternKind = stTextSecDtModPatternKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextSecModPatternKind
class stTextSecModPatternKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextSecModPatternKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3851, 2)
    _Documentation = ''
stTextSecModPatternKind._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextSecModPatternKind', stTextSecModPatternKind)
_module_typeBindings.stTextSecModPatternKind = stTextSecModPatternKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextModPatternKind
class stTextModPatternKind (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextModPatternKind')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3860, 2)
    _Documentation = ''
stTextModPatternKind._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextModPatternKind', stTextModPatternKind)
_module_typeBindings.stTextModPatternKind = stTextModPatternKind

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextInterpulseModulationPatternName
class stTextInterpulseModulationPatternName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextInterpulseModulationPatternName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3869, 2)
    _Documentation = ''
stTextInterpulseModulationPatternName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextInterpulseModulationPatternName', stTextInterpulseModulationPatternName)
_module_typeBindings.stTextInterpulseModulationPatternName = stTextInterpulseModulationPatternName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextPerId
class stTextPerId (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextPerId')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3878, 2)
    _Documentation = ''
stTextPerId._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextPerId', stTextPerId)
_module_typeBindings.stTextPerId = stTextPerId

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stTextBurstModPatternName
class stTextBurstModPatternName (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stTextBurstModPatternName')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3887, 2)
    _Documentation = ''
stTextBurstModPatternName._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stTextBurstModPatternName', stTextBurstModPatternName)
_module_typeBindings.stTextBurstModPatternName = stTextBurstModPatternName

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAgilityResolutionSwitch
class stBoolAgilityResolutionSwitch (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAgilityResolutionSwitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3896, 2)
    _Documentation = ''
stBoolAgilityResolutionSwitch._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAgilityResolutionSwitch', stBoolAgilityResolutionSwitch)
_module_typeBindings.stBoolAgilityResolutionSwitch = stBoolAgilityResolutionSwitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAgilityStatus
class stBoolAgilityStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAgilityStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3905, 2)
    _Documentation = ''
stBoolAgilityStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAgilityStatus', stBoolAgilityStatus)
_module_typeBindings.stBoolAgilityStatus = stBoolAgilityStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAntennaRotation
class stBoolAntennaRotation (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAntennaRotation')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3914, 2)
    _Documentation = ''
stBoolAntennaRotation._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAntennaRotation', stBoolAntennaRotation)
_module_typeBindings.stBoolAntennaRotation = stBoolAntennaRotation

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAtmosphericAbsorptionAttenuationEnable
class stBoolAtmosphericAbsorptionAttenuationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAtmosphericAbsorptionAttenuationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3923, 2)
    _Documentation = ''
stBoolAtmosphericAbsorptionAttenuationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAtmosphericAbsorptionAttenuationEnable', stBoolAtmosphericAbsorptionAttenuationEnable)
_module_typeBindings.stBoolAtmosphericAbsorptionAttenuationEnable = stBoolAtmosphericAbsorptionAttenuationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzExitCondition
class stBoolAzExitCondition (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzExitCondition')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3932, 2)
    _Documentation = ''
stBoolAzExitCondition._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzExitCondition', stBoolAzExitCondition)
_module_typeBindings.stBoolAzExitCondition = stBoolAzExitCondition

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzimuthFrequencyTrigger
class stBoolAzimuthFrequencyTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzimuthFrequencyTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3941, 2)
    _Documentation = ''
stBoolAzimuthFrequencyTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzimuthFrequencyTrigger', stBoolAzimuthFrequencyTrigger)
_module_typeBindings.stBoolAzimuthFrequencyTrigger = stBoolAzimuthFrequencyTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzimuthPriTrigger
class stBoolAzimuthPriTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzimuthPriTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3950, 2)
    _Documentation = ''
stBoolAzimuthPriTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzimuthPriTrigger', stBoolAzimuthPriTrigger)
_module_typeBindings.stBoolAzimuthPriTrigger = stBoolAzimuthPriTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzimuthPulseTrigger
class stBoolAzimuthPulseTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzimuthPulseTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3959, 2)
    _Documentation = ''
stBoolAzimuthPulseTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzimuthPulseTrigger', stBoolAzimuthPulseTrigger)
_module_typeBindings.stBoolAzimuthPulseTrigger = stBoolAzimuthPulseTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzimuthTestPoint
class stBoolAzimuthTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzimuthTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3968, 2)
    _Documentation = ''
stBoolAzimuthTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzimuthTestPoint', stBoolAzimuthTestPoint)
_module_typeBindings.stBoolAzimuthTestPoint = stBoolAzimuthTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzPeriodSynchronization
class stBoolAzPeriodSynchronization (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzPeriodSynchronization')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3977, 2)
    _Documentation = ''
stBoolAzPeriodSynchronization._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzPeriodSynchronization', stBoolAzPeriodSynchronization)
_module_typeBindings.stBoolAzPeriodSynchronization = stBoolAzPeriodSynchronization

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzScanReset
class stBoolAzScanReset (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzScanReset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3986, 2)
    _Documentation = ''
stBoolAzScanReset._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzScanReset', stBoolAzScanReset)
_module_typeBindings.stBoolAzScanReset = stBoolAzScanReset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzSutTrackingSwitch
class stBoolAzSutTrackingSwitch (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzSutTrackingSwitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 3995, 2)
    _Documentation = ''
stBoolAzSutTrackingSwitch._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzSutTrackingSwitch', stBoolAzSutTrackingSwitch)
_module_typeBindings.stBoolAzSutTrackingSwitch = stBoolAzSutTrackingSwitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolAzTrackingSwitch
class stBoolAzTrackingSwitch (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolAzTrackingSwitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4004, 2)
    _Documentation = ''
stBoolAzTrackingSwitch._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolAzTrackingSwitch', stBoolAzTrackingSwitch)
_module_typeBindings.stBoolAzTrackingSwitch = stBoolAzTrackingSwitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBarFrequencyTrigger
class stBoolBarFrequencyTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBarFrequencyTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4013, 2)
    _Documentation = ''
stBoolBarFrequencyTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBarFrequencyTrigger', stBoolBarFrequencyTrigger)
_module_typeBindings.stBoolBarFrequencyTrigger = stBoolBarFrequencyTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBarPriTrigger
class stBoolBarPriTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBarPriTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4022, 2)
    _Documentation = ''
stBoolBarPriTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBarPriTrigger', stBoolBarPriTrigger)
_module_typeBindings.stBoolBarPriTrigger = stBoolBarPriTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBarPulseTrigger
class stBoolBarPulseTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBarPulseTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4031, 2)
    _Documentation = ''
stBoolBarPulseTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBarPulseTrigger', stBoolBarPulseTrigger)
_module_typeBindings.stBoolBarPulseTrigger = stBoolBarPulseTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBarScanTrigger
class stBoolBarScanTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBarScanTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4040, 2)
    _Documentation = ''
stBoolBarScanTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBarScanTrigger', stBoolBarScanTrigger)
_module_typeBindings.stBoolBarScanTrigger = stBoolBarScanTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBeamAzimuthTestPoint
class stBoolBeamAzimuthTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBeamAzimuthTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4049, 2)
    _Documentation = ''
stBoolBeamAzimuthTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBeamAzimuthTestPoint', stBoolBeamAzimuthTestPoint)
_module_typeBindings.stBoolBeamAzimuthTestPoint = stBoolBeamAzimuthTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBeamBlankingList
class stBoolBeamBlankingList (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBeamBlankingList')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4058, 2)
    _Documentation = ''
stBoolBeamBlankingList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBeamBlankingList', stBoolBeamBlankingList)
_module_typeBindings.stBoolBeamBlankingList = stBoolBeamBlankingList

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBeamDwellStatus
class stBoolBeamDwellStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBeamDwellStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4067, 2)
    _Documentation = ''
stBoolBeamDwellStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBeamDwellStatus', stBoolBeamDwellStatus)
_module_typeBindings.stBoolBeamDwellStatus = stBoolBeamDwellStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBeamElevationTestPoint
class stBoolBeamElevationTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBeamElevationTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4076, 2)
    _Documentation = ''
stBoolBeamElevationTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBeamElevationTestPoint', stBoolBeamElevationTestPoint)
_module_typeBindings.stBoolBeamElevationTestPoint = stBoolBeamElevationTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBeamFrequencyTrigger
class stBoolBeamFrequencyTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBeamFrequencyTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4085, 2)
    _Documentation = ''
stBoolBeamFrequencyTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBeamFrequencyTrigger', stBoolBeamFrequencyTrigger)
_module_typeBindings.stBoolBeamFrequencyTrigger = stBoolBeamFrequencyTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBeamPriTrigger
class stBoolBeamPriTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBeamPriTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4094, 2)
    _Documentation = ''
stBoolBeamPriTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBeamPriTrigger', stBoolBeamPriTrigger)
_module_typeBindings.stBoolBeamPriTrigger = stBoolBeamPriTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBeamPulseTrigger
class stBoolBeamPulseTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBeamPulseTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4103, 2)
    _Documentation = ''
stBoolBeamPulseTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBeamPulseTrigger', stBoolBeamPulseTrigger)
_module_typeBindings.stBoolBeamPulseTrigger = stBoolBeamPulseTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolBidirectionReturnOnSameBar
class stBoolBidirectionReturnOnSameBar (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolBidirectionReturnOnSameBar')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4112, 2)
    _Documentation = ''
stBoolBidirectionReturnOnSameBar._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolBidirectionReturnOnSameBar', stBoolBidirectionReturnOnSameBar)
_module_typeBindings.stBoolBidirectionReturnOnSameBar = stBoolBidirectionReturnOnSameBar

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolChangeTracking
class stBoolChangeTracking (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolChangeTracking')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4121, 2)
    _Documentation = ''
stBoolChangeTracking._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolChangeTracking', stBoolChangeTracking)
_module_typeBindings.stBoolChangeTracking = stBoolChangeTracking

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolChannelAudioTestPoint
class stBoolChannelAudioTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolChannelAudioTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4130, 2)
    _Documentation = ''
stBoolChannelAudioTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolChannelAudioTestPoint', stBoolChannelAudioTestPoint)
_module_typeBindings.stBoolChannelAudioTestPoint = stBoolChannelAudioTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolChannelVideoTestPoint
class stBoolChannelVideoTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolChannelVideoTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4139, 2)
    _Documentation = ''
stBoolChannelVideoTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolChannelVideoTestPoint', stBoolChannelVideoTestPoint)
_module_typeBindings.stBoolChannelVideoTestPoint = stBoolChannelVideoTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolCircularBufferCollection
class stBoolCircularBufferCollection (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolCircularBufferCollection')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4148, 2)
    _Documentation = ''
stBoolCircularBufferCollection._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolCircularBufferCollection', stBoolCircularBufferCollection)
_module_typeBindings.stBoolCircularBufferCollection = stBoolCircularBufferCollection

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolClockedPriJitterState
class stBoolClockedPriJitterState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolClockedPriJitterState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4157, 2)
    _Documentation = ''
stBoolClockedPriJitterState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolClockedPriJitterState', stBoolClockedPriJitterState)
_module_typeBindings.stBoolClockedPriJitterState = stBoolClockedPriJitterState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolComplexPriState
class stBoolComplexPriState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolComplexPriState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4166, 2)
    _Documentation = ''
stBoolComplexPriState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolComplexPriState', stBoolComplexPriState)
_module_typeBindings.stBoolComplexPriState = stBoolComplexPriState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolCoupledAxisMotionModel
class stBoolCoupledAxisMotionModel (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolCoupledAxisMotionModel')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4175, 2)
    _Documentation = ''
stBoolCoupledAxisMotionModel._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolCoupledAxisMotionModel', stBoolCoupledAxisMotionModel)
_module_typeBindings.stBoolCoupledAxisMotionModel = stBoolCoupledAxisMotionModel

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolCoupledMotionEnable
class stBoolCoupledMotionEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolCoupledMotionEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4184, 2)
    _Documentation = ''
stBoolCoupledMotionEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolCoupledMotionEnable', stBoolCoupledMotionEnable)
_module_typeBindings.stBoolCoupledMotionEnable = stBoolCoupledMotionEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolCwInterruptEnable
class stBoolCwInterruptEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolCwInterruptEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4193, 2)
    _Documentation = ''
stBoolCwInterruptEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolCwInterruptEnable', stBoolCwInterruptEnable)
_module_typeBindings.stBoolCwInterruptEnable = stBoolCwInterruptEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDataRecordingEnable
class stBoolDataRecordingEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDataRecordingEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4202, 2)
    _Documentation = ''
stBoolDataRecordingEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDataRecordingEnable', stBoolDataRecordingEnable)
_module_typeBindings.stBoolDataRecordingEnable = stBoolDataRecordingEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDeactivate
class stBoolDeactivate (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDeactivate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4211, 2)
    _Documentation = ''
stBoolDeactivate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDeactivate', stBoolDeactivate)
_module_typeBindings.stBoolDeactivate = stBoolDeactivate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDedicatedChannelStatus
class stBoolDedicatedChannelStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDedicatedChannelStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4220, 2)
    _Documentation = ''
stBoolDedicatedChannelStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDedicatedChannelStatus', stBoolDedicatedChannelStatus)
_module_typeBindings.stBoolDedicatedChannelStatus = stBoolDedicatedChannelStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDelayTimeJitterResSwitch
class stBoolDelayTimeJitterResSwitch (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDelayTimeJitterResSwitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4229, 2)
    _Documentation = ''
stBoolDelayTimeJitterResSwitch._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDelayTimeJitterResSwitch', stBoolDelayTimeJitterResSwitch)
_module_typeBindings.stBoolDelayTimeJitterResSwitch = stBoolDelayTimeJitterResSwitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDelayTimeJitterStatus
class stBoolDelayTimeJitterStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDelayTimeJitterStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4238, 2)
    _Documentation = ''
stBoolDelayTimeJitterStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDelayTimeJitterStatus', stBoolDelayTimeJitterStatus)
_module_typeBindings.stBoolDelayTimeJitterStatus = stBoolDelayTimeJitterStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDelayTimeModPeriodSync
class stBoolDelayTimeModPeriodSync (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDelayTimeModPeriodSync')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4247, 2)
    _Documentation = ''
stBoolDelayTimeModPeriodSync._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDelayTimeModPeriodSync', stBoolDelayTimeModPeriodSync)
_module_typeBindings.stBoolDelayTimeModPeriodSync = stBoolDelayTimeModPeriodSync

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDelayTimeModStatus
class stBoolDelayTimeModStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDelayTimeModStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4256, 2)
    _Documentation = ''
stBoolDelayTimeModStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDelayTimeModStatus', stBoolDelayTimeModStatus)
_module_typeBindings.stBoolDelayTimeModStatus = stBoolDelayTimeModStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDigitalVideoTestPoint
class stBoolDigitalVideoTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDigitalVideoTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4265, 2)
    _Documentation = ''
stBoolDigitalVideoTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDigitalVideoTestPoint', stBoolDigitalVideoTestPoint)
_module_typeBindings.stBoolDigitalVideoTestPoint = stBoolDigitalVideoTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDiscreteAmplitudeState
class stBoolDiscreteAmplitudeState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDiscreteAmplitudeState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4274, 2)
    _Documentation = ''
stBoolDiscreteAmplitudeState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDiscreteAmplitudeState', stBoolDiscreteAmplitudeState)
_module_typeBindings.stBoolDiscreteAmplitudeState = stBoolDiscreteAmplitudeState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDiscreteFrequencyState
class stBoolDiscreteFrequencyState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDiscreteFrequencyState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4283, 2)
    _Documentation = ''
stBoolDiscreteFrequencyState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDiscreteFrequencyState', stBoolDiscreteFrequencyState)
_module_typeBindings.stBoolDiscreteFrequencyState = stBoolDiscreteFrequencyState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDiscretePhaseShiftState
class stBoolDiscretePhaseShiftState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDiscretePhaseShiftState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4292, 2)
    _Documentation = ''
stBoolDiscretePhaseShiftState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDiscretePhaseShiftState', stBoolDiscretePhaseShiftState)
_module_typeBindings.stBoolDiscretePhaseShiftState = stBoolDiscretePhaseShiftState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayGeopolitical
class stBoolDisplayGeopolitical (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayGeopolitical')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4301, 2)
    _Documentation = ''
stBoolDisplayGeopolitical._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayGeopolitical', stBoolDisplayGeopolitical)
_module_typeBindings.stBoolDisplayGeopolitical = stBoolDisplayGeopolitical

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayGrids
class stBoolDisplayGrids (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayGrids')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4310, 2)
    _Documentation = ''
stBoolDisplayGrids._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayGrids', stBoolDisplayGrids)
_module_typeBindings.stBoolDisplayGrids = stBoolDisplayGrids

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayHud
class stBoolDisplayHud (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayHud')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4319, 2)
    _Documentation = ''
stBoolDisplayHud._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayHud', stBoolDisplayHud)
_module_typeBindings.stBoolDisplayHud = stBoolDisplayHud

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayInactivePlatforms
class stBoolDisplayInactivePlatforms (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayInactivePlatforms')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4328, 2)
    _Documentation = ''
stBoolDisplayInactivePlatforms._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayInactivePlatforms', stBoolDisplayInactivePlatforms)
_module_typeBindings.stBoolDisplayInactivePlatforms = stBoolDisplayInactivePlatforms

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayBarriers
class stBoolDisplayBarriers (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayBarriers')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4337, 2)
    _Documentation = ''
stBoolDisplayBarriers._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayBarriers', stBoolDisplayBarriers)
_module_typeBindings.stBoolDisplayBarriers = stBoolDisplayBarriers

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayCanals
class stBoolDisplayCanals (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayCanals')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4346, 2)
    _Documentation = ''
stBoolDisplayCanals._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayCanals', stBoolDisplayCanals)
_module_typeBindings.stBoolDisplayCanals = stBoolDisplayCanals

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayCoastline
class stBoolDisplayCoastline (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayCoastline')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4355, 2)
    _Documentation = ''
stBoolDisplayCoastline._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayCoastline', stBoolDisplayCoastline)
_module_typeBindings.stBoolDisplayCoastline = stBoolDisplayCoastline

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayDepthLines
class stBoolDisplayDepthLines (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayDepthLines')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4364, 2)
    _Documentation = ''
stBoolDisplayDepthLines._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayDepthLines', stBoolDisplayDepthLines)
_module_typeBindings.stBoolDisplayDepthLines = stBoolDisplayDepthLines

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayLandforms
class stBoolDisplayLandforms (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayLandforms')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4373, 2)
    _Documentation = ''
stBoolDisplayLandforms._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayLandforms', stBoolDisplayLandforms)
_module_typeBindings.stBoolDisplayLandforms = stBoolDisplayLandforms

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPipelines
class stBoolDisplayPipelines (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPipelines')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4382, 2)
    _Documentation = ''
stBoolDisplayPipelines._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPipelines', stBoolDisplayPipelines)
_module_typeBindings.stBoolDisplayPipelines = stBoolDisplayPipelines

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPoliticalLines
class stBoolDisplayPoliticalLines (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPoliticalLines')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4391, 2)
    _Documentation = ''
stBoolDisplayPoliticalLines._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPoliticalLines', stBoolDisplayPoliticalLines)
_module_typeBindings.stBoolDisplayPoliticalLines = stBoolDisplayPoliticalLines

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayRailroads
class stBoolDisplayRailroads (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayRailroads')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4400, 2)
    _Documentation = ''
stBoolDisplayRailroads._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayRailroads', stBoolDisplayRailroads)
_module_typeBindings.stBoolDisplayRailroads = stBoolDisplayRailroads

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayRoads
class stBoolDisplayRoads (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayRoads')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4409, 2)
    _Documentation = ''
stBoolDisplayRoads._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayRoads', stBoolDisplayRoads)
_module_typeBindings.stBoolDisplayRoads = stBoolDisplayRoads

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayStructures
class stBoolDisplayStructures (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayStructures')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4418, 2)
    _Documentation = ''
stBoolDisplayStructures._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayStructures', stBoolDisplayStructures)
_module_typeBindings.stBoolDisplayStructures = stBoolDisplayStructures

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayTrails
class stBoolDisplayTrails (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayTrails')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4427, 2)
    _Documentation = ''
stBoolDisplayTrails._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayTrails', stBoolDisplayTrails)
_module_typeBindings.stBoolDisplayTrails = stBoolDisplayTrails

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayUtilities
class stBoolDisplayUtilities (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayUtilities')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4436, 2)
    _Documentation = ''
stBoolDisplayUtilities._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayUtilities', stBoolDisplayUtilities)
_module_typeBindings.stBoolDisplayUtilities = stBoolDisplayUtilities

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayWaterways
class stBoolDisplayWaterways (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayWaterways')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4445, 2)
    _Documentation = ''
stBoolDisplayWaterways._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayWaterways', stBoolDisplayWaterways)
_module_typeBindings.stBoolDisplayWaterways = stBoolDisplayWaterways

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPath
class stBoolDisplayPath (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPath')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4454, 2)
    _Documentation = ''
stBoolDisplayPath._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPath', stBoolDisplayPath)
_module_typeBindings.stBoolDisplayPath = stBoolDisplayPath

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPathHistory
class stBoolDisplayPathHistory (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPathHistory')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4463, 2)
    _Documentation = ''
stBoolDisplayPathHistory._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPathHistory', stBoolDisplayPathHistory)
_module_typeBindings.stBoolDisplayPathHistory = stBoolDisplayPathHistory

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPlatform
class stBoolDisplayPlatform (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPlatform')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4472, 2)
    _Documentation = ''
stBoolDisplayPlatform._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPlatform', stBoolDisplayPlatform)
_module_typeBindings.stBoolDisplayPlatform = stBoolDisplayPlatform

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayPlatformDetails
class stBoolDisplayPlatformDetails (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayPlatformDetails')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4481, 2)
    _Documentation = ''
stBoolDisplayPlatformDetails._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayPlatformDetails', stBoolDisplayPlatformDetails)
_module_typeBindings.stBoolDisplayPlatformDetails = stBoolDisplayPlatformDetails

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayProjectedPath
class stBoolDisplayProjectedPath (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayProjectedPath')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4490, 2)
    _Documentation = ''
stBoolDisplayProjectedPath._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayProjectedPath', stBoolDisplayProjectedPath)
_module_typeBindings.stBoolDisplayProjectedPath = stBoolDisplayProjectedPath

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayRoughness
class stBoolDisplayRoughness (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayRoughness')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4499, 2)
    _Documentation = ''
stBoolDisplayRoughness._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayRoughness', stBoolDisplayRoughness)
_module_typeBindings.stBoolDisplayRoughness = stBoolDisplayRoughness

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayRoughnessLegend
class stBoolDisplayRoughnessLegend (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayRoughnessLegend')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4508, 2)
    _Documentation = ''
stBoolDisplayRoughnessLegend._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayRoughnessLegend', stBoolDisplayRoughnessLegend)
_module_typeBindings.stBoolDisplayRoughnessLegend = stBoolDisplayRoughnessLegend

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplaySymbol
class stBoolDisplaySymbol (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplaySymbol')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4517, 2)
    _Documentation = ''
stBoolDisplaySymbol._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplaySymbol', stBoolDisplaySymbol)
_module_typeBindings.stBoolDisplaySymbol = stBoolDisplaySymbol

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplaySymbolLegend
class stBoolDisplaySymbolLegend (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplaySymbolLegend')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4526, 2)
    _Documentation = ''
stBoolDisplaySymbolLegend._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplaySymbolLegend', stBoolDisplaySymbolLegend)
_module_typeBindings.stBoolDisplaySymbolLegend = stBoolDisplaySymbolLegend

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayTerrain
class stBoolDisplayTerrain (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayTerrain')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4535, 2)
    _Documentation = ''
stBoolDisplayTerrain._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayTerrain', stBoolDisplayTerrain)
_module_typeBindings.stBoolDisplayTerrain = stBoolDisplayTerrain

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayTerrainLegend
class stBoolDisplayTerrainLegend (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayTerrainLegend')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4544, 2)
    _Documentation = ''
stBoolDisplayTerrainLegend._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayTerrainLegend', stBoolDisplayTerrainLegend)
_module_typeBindings.stBoolDisplayTerrainLegend = stBoolDisplayTerrainLegend

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayVisibility
class stBoolDisplayVisibility (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayVisibility')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4553, 2)
    _Documentation = ''
stBoolDisplayVisibility._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayVisibility', stBoolDisplayVisibility)
_module_typeBindings.stBoolDisplayVisibility = stBoolDisplayVisibility

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDisplayVmapLegend
class stBoolDisplayVmapLegend (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDisplayVmapLegend')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4562, 2)
    _Documentation = ''
stBoolDisplayVmapLegend._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDisplayVmapLegend', stBoolDisplayVmapLegend)
_module_typeBindings.stBoolDisplayVmapLegend = stBoolDisplayVmapLegend

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDpmBoardCollectionEnable
class stBoolDpmBoardCollectionEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDpmBoardCollectionEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4571, 2)
    _Documentation = ''
stBoolDpmBoardCollectionEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDpmBoardCollectionEnable', stBoolDpmBoardCollectionEnable)
_module_typeBindings.stBoolDpmBoardCollectionEnable = stBoolDpmBoardCollectionEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDuctingEnable
class stBoolDuctingEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDuctingEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4580, 2)
    _Documentation = ''
stBoolDuctingEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDuctingEnable', stBoolDuctingEnable)
_module_typeBindings.stBoolDuctingEnable = stBoolDuctingEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDwellFrequencyTrigger
class stBoolDwellFrequencyTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDwellFrequencyTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4589, 2)
    _Documentation = ''
stBoolDwellFrequencyTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDwellFrequencyTrigger', stBoolDwellFrequencyTrigger)
_module_typeBindings.stBoolDwellFrequencyTrigger = stBoolDwellFrequencyTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDwellPriTrigger
class stBoolDwellPriTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDwellPriTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4598, 2)
    _Documentation = ''
stBoolDwellPriTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDwellPriTrigger', stBoolDwellPriTrigger)
_module_typeBindings.stBoolDwellPriTrigger = stBoolDwellPriTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDwellPulseTrigger
class stBoolDwellPulseTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDwellPulseTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4607, 2)
    _Documentation = ''
stBoolDwellPulseTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDwellPulseTrigger', stBoolDwellPulseTrigger)
_module_typeBindings.stBoolDwellPulseTrigger = stBoolDwellPulseTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolDwellStatus
class stBoolDwellStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolDwellStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4616, 2)
    _Documentation = ''
stBoolDwellStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolDwellStatus', stBoolDwellStatus)
_module_typeBindings.stBoolDwellStatus = stBoolDwellStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolEarSequenceTriggerState
class stBoolEarSequenceTriggerState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolEarSequenceTriggerState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4625, 2)
    _Documentation = ''
stBoolEarSequenceTriggerState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolEarSequenceTriggerState', stBoolEarSequenceTriggerState)
_module_typeBindings.stBoolEarSequenceTriggerState = stBoolEarSequenceTriggerState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElevationFrequencyTrigger
class stBoolElevationFrequencyTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElevationFrequencyTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4634, 2)
    _Documentation = ''
stBoolElevationFrequencyTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElevationFrequencyTrigger', stBoolElevationFrequencyTrigger)
_module_typeBindings.stBoolElevationFrequencyTrigger = stBoolElevationFrequencyTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElevationPriTrigger
class stBoolElevationPriTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElevationPriTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4643, 2)
    _Documentation = ''
stBoolElevationPriTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElevationPriTrigger', stBoolElevationPriTrigger)
_module_typeBindings.stBoolElevationPriTrigger = stBoolElevationPriTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElevationPulseTrigger
class stBoolElevationPulseTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElevationPulseTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4652, 2)
    _Documentation = ''
stBoolElevationPulseTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElevationPulseTrigger', stBoolElevationPulseTrigger)
_module_typeBindings.stBoolElevationPulseTrigger = stBoolElevationPulseTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElevationTestPoint
class stBoolElevationTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElevationTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4661, 2)
    _Documentation = ''
stBoolElevationTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElevationTestPoint', stBoolElevationTestPoint)
_module_typeBindings.stBoolElevationTestPoint = stBoolElevationTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElExitCondition
class stBoolElExitCondition (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElExitCondition')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4670, 2)
    _Documentation = ''
stBoolElExitCondition._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElExitCondition', stBoolElExitCondition)
_module_typeBindings.stBoolElExitCondition = stBoolElExitCondition

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolEllipticalAxisScaling
class stBoolEllipticalAxisScaling (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolEllipticalAxisScaling')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4679, 2)
    _Documentation = ''
stBoolEllipticalAxisScaling._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolEllipticalAxisScaling', stBoolEllipticalAxisScaling)
_module_typeBindings.stBoolEllipticalAxisScaling = stBoolEllipticalAxisScaling

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElPeriodSynchronization
class stBoolElPeriodSynchronization (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElPeriodSynchronization')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4688, 2)
    _Documentation = ''
stBoolElPeriodSynchronization._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElPeriodSynchronization', stBoolElPeriodSynchronization)
_module_typeBindings.stBoolElPeriodSynchronization = stBoolElPeriodSynchronization

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElScanReset
class stBoolElScanReset (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElScanReset')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4697, 2)
    _Documentation = ''
stBoolElScanReset._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElScanReset', stBoolElScanReset)
_module_typeBindings.stBoolElScanReset = stBoolElScanReset

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElSutTrackingSwitch
class stBoolElSutTrackingSwitch (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElSutTrackingSwitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4706, 2)
    _Documentation = ''
stBoolElSutTrackingSwitch._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElSutTrackingSwitch', stBoolElSutTrackingSwitch)
_module_typeBindings.stBoolElSutTrackingSwitch = stBoolElSutTrackingSwitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolElTrackingSwitch
class stBoolElTrackingSwitch (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolElTrackingSwitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4715, 2)
    _Documentation = ''
stBoolElTrackingSwitch._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolElTrackingSwitch', stBoolElTrackingSwitch)
_module_typeBindings.stBoolElTrackingSwitch = stBoolElTrackingSwitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolScenarioElementLibraryEnable
class stBoolScenarioElementLibraryEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolScenarioElementLibraryEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4724, 2)
    _Documentation = ''
stBoolScenarioElementLibraryEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolScenarioElementLibraryEnable', stBoolScenarioElementLibraryEnable)
_module_typeBindings.stBoolScenarioElementLibraryEnable = stBoolScenarioElementLibraryEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolEmitterLibraryEnable
class stBoolEmitterLibraryEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolEmitterLibraryEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4733, 2)
    _Documentation = ''
stBoolEmitterLibraryEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolEmitterLibraryEnable', stBoolEmitterLibraryEnable)
_module_typeBindings.stBoolEmitterLibraryEnable = stBoolEmitterLibraryEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolEndOfRasterTriggerStatus
class stBoolEndOfRasterTriggerStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolEndOfRasterTriggerStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4742, 2)
    _Documentation = ''
stBoolEndOfRasterTriggerStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolEndOfRasterTriggerStatus', stBoolEndOfRasterTriggerStatus)
_module_typeBindings.stBoolEndOfRasterTriggerStatus = stBoolEndOfRasterTriggerStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolExternalSutFlag
class stBoolExternalSutFlag (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolExternalSutFlag')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4751, 2)
    _Documentation = ''
stBoolExternalSutFlag._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolExternalSutFlag', stBoolExternalSutFlag)
_module_typeBindings.stBoolExternalSutFlag = stBoolExternalSutFlag

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolFirstSegmentOnPath
class stBoolFirstSegmentOnPath (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolFirstSegmentOnPath')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4760, 2)
    _Documentation = ''
stBoolFirstSegmentOnPath._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolFirstSegmentOnPath', stBoolFirstSegmentOnPath)
_module_typeBindings.stBoolFirstSegmentOnPath = stBoolFirstSegmentOnPath

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolFrequencyAttenuationEnable
class stBoolFrequencyAttenuationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolFrequencyAttenuationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4769, 2)
    _Documentation = ''
stBoolFrequencyAttenuationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolFrequencyAttenuationEnable', stBoolFrequencyAttenuationEnable)
_module_typeBindings.stBoolFrequencyAttenuationEnable = stBoolFrequencyAttenuationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolFrequencyDopplerShiftEnable
class stBoolFrequencyDopplerShiftEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolFrequencyDopplerShiftEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4778, 2)
    _Documentation = ''
stBoolFrequencyDopplerShiftEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolFrequencyDopplerShiftEnable', stBoolFrequencyDopplerShiftEnable)
_module_typeBindings.stBoolFrequencyDopplerShiftEnable = stBoolFrequencyDopplerShiftEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolFrequencyTrigger
class stBoolFrequencyTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolFrequencyTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4787, 2)
    _Documentation = ''
stBoolFrequencyTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolFrequencyTrigger', stBoolFrequencyTrigger)
_module_typeBindings.stBoolFrequencyTrigger = stBoolFrequencyTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolGeneratorEventDefined
class stBoolGeneratorEventDefined (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolGeneratorEventDefined')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4796, 2)
    _Documentation = ''
stBoolGeneratorEventDefined._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolGeneratorEventDefined', stBoolGeneratorEventDefined)
_module_typeBindings.stBoolGeneratorEventDefined = stBoolGeneratorEventDefined

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolGeneratorTriggerState
class stBoolGeneratorTriggerState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolGeneratorTriggerState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4805, 2)
    _Documentation = ''
stBoolGeneratorTriggerState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolGeneratorTriggerState', stBoolGeneratorTriggerState)
_module_typeBindings.stBoolGeneratorTriggerState = stBoolGeneratorTriggerState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolGeotiffEnable
class stBoolGeotiffEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolGeotiffEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4814, 2)
    _Documentation = ''
stBoolGeotiffEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolGeotiffEnable', stBoolGeotiffEnable)
_module_typeBindings.stBoolGeotiffEnable = stBoolGeotiffEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolGpAssigned
class stBoolGpAssigned (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolGpAssigned')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4823, 2)
    _Documentation = ''
stBoolGpAssigned._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolGpAssigned', stBoolGpAssigned)
_module_typeBindings.stBoolGpAssigned = stBoolGpAssigned

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolGpPooled
class stBoolGpPooled (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolGpPooled')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4832, 2)
    _Documentation = ''
stBoolGpPooled._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolGpPooled', stBoolGpPooled)
_module_typeBindings.stBoolGpPooled = stBoolGpPooled

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolHfimState
class stBoolHfimState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolHfimState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4841, 2)
    _Documentation = ''
stBoolHfimState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolHfimState', stBoolHfimState)
_module_typeBindings.stBoolHfimState = stBoolHfimState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolHorizonMaskingEnable
class stBoolHorizonMaskingEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolHorizonMaskingEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4850, 2)
    _Documentation = ''
stBoolHorizonMaskingEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolHorizonMaskingEnable', stBoolHorizonMaskingEnable)
_module_typeBindings.stBoolHorizonMaskingEnable = stBoolHorizonMaskingEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterbarBlankingStatus
class stBoolInterbarBlankingStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterbarBlankingStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4859, 2)
    _Documentation = ''
stBoolInterbarBlankingStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterbarBlankingStatus', stBoolInterbarBlankingStatus)
_module_typeBindings.stBoolInterbarBlankingStatus = stBoolInterbarBlankingStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterbarFrequencyTrigger
class stBoolInterbarFrequencyTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterbarFrequencyTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4868, 2)
    _Documentation = ''
stBoolInterbarFrequencyTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterbarFrequencyTrigger', stBoolInterbarFrequencyTrigger)
_module_typeBindings.stBoolInterbarFrequencyTrigger = stBoolInterbarFrequencyTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterbarPriTrigger
class stBoolInterbarPriTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterbarPriTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4877, 2)
    _Documentation = ''
stBoolInterbarPriTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterbarPriTrigger', stBoolInterbarPriTrigger)
_module_typeBindings.stBoolInterbarPriTrigger = stBoolInterbarPriTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterbarPulseTrigger
class stBoolInterbarPulseTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterbarPulseTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4886, 2)
    _Documentation = ''
stBoolInterbarPulseTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterbarPulseTrigger', stBoolInterbarPulseTrigger)
_module_typeBindings.stBoolInterbarPulseTrigger = stBoolInterbarPulseTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterbarScanTrigger
class stBoolInterbarScanTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterbarScanTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4895, 2)
    _Documentation = ''
stBoolInterbarScanTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterbarScanTrigger', stBoolInterbarScanTrigger)
_module_typeBindings.stBoolInterbarScanTrigger = stBoolInterbarScanTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterpulseModulationPriSync
class stBoolInterpulseModulationPriSync (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterpulseModulationPriSync')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4904, 2)
    _Documentation = ''
stBoolInterpulseModulationPriSync._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterpulseModulationPriSync', stBoolInterpulseModulationPriSync)
_module_typeBindings.stBoolInterpulseModulationPriSync = stBoolInterpulseModulationPriSync

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterpulseModulationStatus
class stBoolInterpulseModulationStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterpulseModulationStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4913, 2)
    _Documentation = ''
stBoolInterpulseModulationStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterpulseModulationStatus', stBoolInterpulseModulationStatus)
_module_typeBindings.stBoolInterpulseModulationStatus = stBoolInterpulseModulationStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterruptActive
class stBoolInterruptActive (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterruptActive')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4922, 2)
    _Documentation = ''
stBoolInterruptActive._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterruptActive', stBoolInterruptActive)
_module_typeBindings.stBoolInterruptActive = stBoolInterruptActive

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInterruptGeneratorInterruptActive
class stBoolInterruptGeneratorInterruptActive (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInterruptGeneratorInterruptActive')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4931, 2)
    _Documentation = ''
stBoolInterruptGeneratorInterruptActive._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInterruptGeneratorInterruptActive', stBoolInterruptGeneratorInterruptActive)
_module_typeBindings.stBoolInterruptGeneratorInterruptActive = stBoolInterruptGeneratorInterruptActive

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolIntrapulseModulationStatus
class stBoolIntrapulseModulationStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolIntrapulseModulationStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4940, 2)
    _Documentation = ''
stBoolIntrapulseModulationStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolIntrapulseModulationStatus', stBoolIntrapulseModulationStatus)
_module_typeBindings.stBoolIntrapulseModulationStatus = stBoolIntrapulseModulationStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolInvalidPdwsFlag
class stBoolInvalidPdwsFlag (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolInvalidPdwsFlag')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4949, 2)
    _Documentation = ''
stBoolInvalidPdwsFlag._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolInvalidPdwsFlag', stBoolInvalidPdwsFlag)
_module_typeBindings.stBoolInvalidPdwsFlag = stBoolInvalidPdwsFlag

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolJammerStatus
class stBoolJammerStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolJammerStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4958, 2)
    _Documentation = ''
stBoolJammerStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolJammerStatus', stBoolJammerStatus)
_module_typeBindings.stBoolJammerStatus = stBoolJammerStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolJitterResSwitch
class stBoolJitterResSwitch (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolJitterResSwitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4967, 2)
    _Documentation = ''
stBoolJitterResSwitch._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolJitterResSwitch', stBoolJitterResSwitch)
_module_typeBindings.stBoolJitterResSwitch = stBoolJitterResSwitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolJitterStatus
class stBoolJitterStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolJitterStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4976, 2)
    _Documentation = ''
stBoolJitterStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolJitterStatus', stBoolJitterStatus)
_module_typeBindings.stBoolJitterStatus = stBoolJitterStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolLinearFreqResetFlag
class stBoolLinearFreqResetFlag (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolLinearFreqResetFlag')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4985, 2)
    _Documentation = ''
stBoolLinearFreqResetFlag._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolLinearFreqResetFlag', stBoolLinearFreqResetFlag)
_module_typeBindings.stBoolLinearFreqResetFlag = stBoolLinearFreqResetFlag

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolLinearFrequencyState
class stBoolLinearFrequencyState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolLinearFrequencyState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 4994, 2)
    _Documentation = ''
stBoolLinearFrequencyState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolLinearFrequencyState', stBoolLinearFrequencyState)
_module_typeBindings.stBoolLinearFrequencyState = stBoolLinearFrequencyState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolVmapEnable
class stBoolVmapEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolVmapEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5003, 2)
    _Documentation = ''
stBoolVmapEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolVmapEnable', stBoolVmapEnable)
_module_typeBindings.stBoolVmapEnable = stBoolVmapEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolModeProtectionSwitch
class stBoolModeProtectionSwitch (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolModeProtectionSwitch')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5012, 2)
    _Documentation = ''
stBoolModeProtectionSwitch._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolModeProtectionSwitch', stBoolModeProtectionSwitch)
_module_typeBindings.stBoolModeProtectionSwitch = stBoolModeProtectionSwitch

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolModPeriodSync
class stBoolModPeriodSync (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolModPeriodSync')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5021, 2)
    _Documentation = ''
stBoolModPeriodSync._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolModPeriodSync', stBoolModPeriodSync)
_module_typeBindings.stBoolModPeriodSync = stBoolModPeriodSync

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolModStatus
class stBoolModStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolModStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5030, 2)
    _Documentation = ''
stBoolModStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolModStatus', stBoolModStatus)
_module_typeBindings.stBoolModStatus = stBoolModStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolMultipathEnable
class stBoolMultipathEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolMultipathEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5039, 2)
    _Documentation = ''
stBoolMultipathEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolMultipathEnable', stBoolMultipathEnable)
_module_typeBindings.stBoolMultipathEnable = stBoolMultipathEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolNavIfEnable
class stBoolNavIfEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolNavIfEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5048, 2)
    _Documentation = ''
stBoolNavIfEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolNavIfEnable', stBoolNavIfEnable)
_module_typeBindings.stBoolNavIfEnable = stBoolNavIfEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolNoiseBandwidthState
class stBoolNoiseBandwidthState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolNoiseBandwidthState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5057, 2)
    _Documentation = ''
stBoolNoiseBandwidthState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolNoiseBandwidthState', stBoolNoiseBandwidthState)
_module_typeBindings.stBoolNoiseBandwidthState = stBoolNoiseBandwidthState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOldTrackDataValid
class stBoolOldTrackDataValid (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOldTrackDataValid')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5066, 2)
    _Documentation = ''
stBoolOldTrackDataValid._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOldTrackDataValid', stBoolOldTrackDataValid)
_module_typeBindings.stBoolOldTrackDataValid = stBoolOldTrackDataValid

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOldTrackIsSut
class stBoolOldTrackIsSut (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOldTrackIsSut')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5075, 2)
    _Documentation = ''
stBoolOldTrackIsSut._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOldTrackIsSut', stBoolOldTrackIsSut)
_module_typeBindings.stBoolOldTrackIsSut = stBoolOldTrackIsSut

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOverrideInterruptGenerators
class stBoolOverrideInterruptGenerators (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOverrideInterruptGenerators')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5084, 2)
    _Documentation = ''
stBoolOverrideInterruptGenerators._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOverrideInterruptGenerators', stBoolOverrideInterruptGenerators)
_module_typeBindings.stBoolOverrideInterruptGenerators = stBoolOverrideInterruptGenerators

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOverrideScanInterrupts
class stBoolOverrideScanInterrupts (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOverrideScanInterrupts')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5093, 2)
    _Documentation = ''
stBoolOverrideScanInterrupts._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOverrideScanInterrupts', stBoolOverrideScanInterrupts)
_module_typeBindings.stBoolOverrideScanInterrupts = stBoolOverrideScanInterrupts

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolOverrideTrack
class stBoolOverrideTrack (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolOverrideTrack')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5102, 2)
    _Documentation = ''
stBoolOverrideTrack._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolOverrideTrack', stBoolOverrideTrack)
_module_typeBindings.stBoolOverrideTrack = stBoolOverrideTrack

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPalmerExitCondition
class stBoolPalmerExitCondition (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPalmerExitCondition')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5111, 2)
    _Documentation = ''
stBoolPalmerExitCondition._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPalmerExitCondition', stBoolPalmerExitCondition)
_module_typeBindings.stBoolPalmerExitCondition = stBoolPalmerExitCondition

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPalmerFrequencyTrigger
class stBoolPalmerFrequencyTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPalmerFrequencyTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5120, 2)
    _Documentation = ''
stBoolPalmerFrequencyTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPalmerFrequencyTrigger', stBoolPalmerFrequencyTrigger)
_module_typeBindings.stBoolPalmerFrequencyTrigger = stBoolPalmerFrequencyTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPalmerPriTrigger
class stBoolPalmerPriTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPalmerPriTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5129, 2)
    _Documentation = ''
stBoolPalmerPriTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPalmerPriTrigger', stBoolPalmerPriTrigger)
_module_typeBindings.stBoolPalmerPriTrigger = stBoolPalmerPriTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPalmerPulseTrigger
class stBoolPalmerPulseTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPalmerPulseTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5138, 2)
    _Documentation = ''
stBoolPalmerPulseTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPalmerPulseTrigger', stBoolPalmerPulseTrigger)
_module_typeBindings.stBoolPalmerPulseTrigger = stBoolPalmerPulseTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPalmerStatus
class stBoolPalmerStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPalmerStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5147, 2)
    _Documentation = ''
stBoolPalmerStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPalmerStatus', stBoolPalmerStatus)
_module_typeBindings.stBoolPalmerStatus = stBoolPalmerStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPgpDefaultMode
class stBoolPgpDefaultMode (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPgpDefaultMode')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5156, 2)
    _Documentation = ''
stBoolPgpDefaultMode._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPgpDefaultMode', stBoolPgpDefaultMode)
_module_typeBindings.stBoolPgpDefaultMode = stBoolPgpDefaultMode

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPgpDropTrackMode
class stBoolPgpDropTrackMode (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPgpDropTrackMode')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5165, 2)
    _Documentation = ''
stBoolPgpDropTrackMode._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPgpDropTrackMode', stBoolPgpDropTrackMode)
_module_typeBindings.stBoolPgpDropTrackMode = stBoolPgpDropTrackMode

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPooledStatus
class stBoolPooledStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPooledStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5174, 2)
    _Documentation = ''
stBoolPooledStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPooledStatus', stBoolPooledStatus)
_module_typeBindings.stBoolPooledStatus = stBoolPooledStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPriTestPoint
class stBoolPriTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPriTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5183, 2)
    _Documentation = ''
stBoolPriTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPriTestPoint', stBoolPriTestPoint)
_module_typeBindings.stBoolPriTestPoint = stBoolPriTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPriTestPoint2
class stBoolPriTestPoint2 (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPriTestPoint2')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5192, 2)
    _Documentation = ''
stBoolPriTestPoint2._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPriTestPoint2', stBoolPriTestPoint2)
_module_typeBindings.stBoolPriTestPoint2 = stBoolPriTestPoint2

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPriTestPoint3
class stBoolPriTestPoint3 (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPriTestPoint3')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5201, 2)
    _Documentation = ''
stBoolPriTestPoint3._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPriTestPoint3', stBoolPriTestPoint3)
_module_typeBindings.stBoolPriTestPoint3 = stBoolPriTestPoint3

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPriTestPoint4
class stBoolPriTestPoint4 (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPriTestPoint4')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5210, 2)
    _Documentation = ''
stBoolPriTestPoint4._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPriTestPoint4', stBoolPriTestPoint4)
_module_typeBindings.stBoolPriTestPoint4 = stBoolPriTestPoint4

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPriTrigger
class stBoolPriTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPriTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5219, 2)
    _Documentation = ''
stBoolPriTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPriTrigger', stBoolPriTrigger)
_module_typeBindings.stBoolPriTrigger = stBoolPriTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPulseGroupState
class stBoolPulseGroupState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPulseGroupState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5228, 2)
    _Documentation = ''
stBoolPulseGroupState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPulseGroupState', stBoolPulseGroupState)
_module_typeBindings.stBoolPulseGroupState = stBoolPulseGroupState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPulseInvisibleState
class stBoolPulseInvisibleState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPulseInvisibleState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5237, 2)
    _Documentation = ''
stBoolPulseInvisibleState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPulseInvisibleState', stBoolPulseInvisibleState)
_module_typeBindings.stBoolPulseInvisibleState = stBoolPulseInvisibleState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPulseTrigger
class stBoolPulseTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPulseTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5246, 2)
    _Documentation = ''
stBoolPulseTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPulseTrigger', stBoolPulseTrigger)
_module_typeBindings.stBoolPulseTrigger = stBoolPulseTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolPulseTruncationEnable
class stBoolPulseTruncationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolPulseTruncationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5255, 2)
    _Documentation = ''
stBoolPulseTruncationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolPulseTruncationEnable', stBoolPulseTruncationEnable)
_module_typeBindings.stBoolPulseTruncationEnable = stBoolPulseTruncationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRadiationEnable
class stBoolRadiationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRadiationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5264, 2)
    _Documentation = ''
stBoolRadiationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRadiationEnable', stBoolRadiationEnable)
_module_typeBindings.stBoolRadiationEnable = stBoolRadiationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRadiationState
class stBoolRadiationState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRadiationState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5273, 2)
    _Documentation = ''
stBoolRadiationState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRadiationState', stBoolRadiationState)
_module_typeBindings.stBoolRadiationState = stBoolRadiationState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRangeAndPriDopplerShiftEnable
class stBoolRangeAndPriDopplerShiftEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRangeAndPriDopplerShiftEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5282, 2)
    _Documentation = ''
stBoolRangeAndPriDopplerShiftEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRangeAndPriDopplerShiftEnable', stBoolRangeAndPriDopplerShiftEnable)
_module_typeBindings.stBoolRangeAndPriDopplerShiftEnable = stBoolRangeAndPriDopplerShiftEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRangeAttenuationEnable
class stBoolRangeAttenuationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRangeAttenuationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5291, 2)
    _Documentation = ''
stBoolRangeAttenuationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRangeAttenuationEnable', stBoolRangeAttenuationEnable)
_module_typeBindings.stBoolRangeAttenuationEnable = stBoolRangeAttenuationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRangeRadiationState
class stBoolRangeRadiationState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRangeRadiationState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5300, 2)
    _Documentation = ''
stBoolRangeRadiationState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRangeRadiationState', stBoolRangeRadiationState)
_module_typeBindings.stBoolRangeRadiationState = stBoolRangeRadiationState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRangeResyncOnModeChangeState
class stBoolRangeResyncOnModeChangeState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRangeResyncOnModeChangeState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5309, 2)
    _Documentation = ''
stBoolRangeResyncOnModeChangeState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRangeResyncOnModeChangeState', stBoolRangeResyncOnModeChangeState)
_module_typeBindings.stBoolRangeResyncOnModeChangeState = stBoolRangeResyncOnModeChangeState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRasterFlybackStatus
class stBoolRasterFlybackStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRasterFlybackStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5318, 2)
    _Documentation = ''
stBoolRasterFlybackStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRasterFlybackStatus', stBoolRasterFlybackStatus)
_module_typeBindings.stBoolRasterFlybackStatus = stBoolRasterFlybackStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordEmitterEventsEnable
class stBoolRecordEmitterEventsEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordEmitterEventsEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5327, 2)
    _Documentation = ''
stBoolRecordEmitterEventsEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordEmitterEventsEnable', stBoolRecordEmitterEventsEnable)
_module_typeBindings.stBoolRecordEmitterEventsEnable = stBoolRecordEmitterEventsEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordEmitterStatusEnable
class stBoolRecordEmitterStatusEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordEmitterStatusEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5336, 2)
    _Documentation = ''
stBoolRecordEmitterStatusEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordEmitterStatusEnable', stBoolRecordEmitterStatusEnable)
_module_typeBindings.stBoolRecordEmitterStatusEnable = stBoolRecordEmitterStatusEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordPlatformEventsEnable
class stBoolRecordPlatformEventsEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordPlatformEventsEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5345, 2)
    _Documentation = ''
stBoolRecordPlatformEventsEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordPlatformEventsEnable', stBoolRecordPlatformEventsEnable)
_module_typeBindings.stBoolRecordPlatformEventsEnable = stBoolRecordPlatformEventsEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordPlatformStatusEnable
class stBoolRecordPlatformStatusEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordPlatformStatusEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5354, 2)
    _Documentation = ''
stBoolRecordPlatformStatusEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordPlatformStatusEnable', stBoolRecordPlatformStatusEnable)
_module_typeBindings.stBoolRecordPlatformStatusEnable = stBoolRecordPlatformStatusEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRecordPulseCountsEnable
class stBoolRecordPulseCountsEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRecordPulseCountsEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5363, 2)
    _Documentation = ''
stBoolRecordPulseCountsEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRecordPulseCountsEnable', stBoolRecordPulseCountsEnable)
_module_typeBindings.stBoolRecordPulseCountsEnable = stBoolRecordPulseCountsEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolResyncOnModeChangeState
class stBoolResyncOnModeChangeState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolResyncOnModeChangeState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5372, 2)
    _Documentation = ''
stBoolResyncOnModeChangeState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolResyncOnModeChangeState', stBoolResyncOnModeChangeState)
_module_typeBindings.stBoolResyncOnModeChangeState = stBoolResyncOnModeChangeState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRfBlanking
class stBoolRfBlanking (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRfBlanking')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5381, 2)
    _Documentation = ''
stBoolRfBlanking._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRfBlanking', stBoolRfBlanking)
_module_typeBindings.stBoolRfBlanking = stBoolRfBlanking

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRfBlankingVideoTestPoint
class stBoolRfBlankingVideoTestPoint (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRfBlankingVideoTestPoint')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5390, 2)
    _Documentation = ''
stBoolRfBlankingVideoTestPoint._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRfBlankingVideoTestPoint', stBoolRfBlankingVideoTestPoint)
_module_typeBindings.stBoolRfBlankingVideoTestPoint = stBoolRfBlankingVideoTestPoint

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolRoughnessEnable
class stBoolRoughnessEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolRoughnessEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5399, 2)
    _Documentation = ''
stBoolRoughnessEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolRoughnessEnable', stBoolRoughnessEnable)
_module_typeBindings.stBoolRoughnessEnable = stBoolRoughnessEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolScanBlanking
class stBoolScanBlanking (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolScanBlanking')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5408, 2)
    _Documentation = ''
stBoolScanBlanking._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolScanBlanking', stBoolScanBlanking)
_module_typeBindings.stBoolScanBlanking = stBoolScanBlanking

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolScanTrigger
class stBoolScanTrigger (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolScanTrigger')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5417, 2)
    _Documentation = ''
stBoolScanTrigger._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolScanTrigger', stBoolScanTrigger)
_module_typeBindings.stBoolScanTrigger = stBoolScanTrigger

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolScenarioIsAnElementLibrary
class stBoolScenarioIsAnElementLibrary (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolScenarioIsAnElementLibrary')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5426, 2)
    _Documentation = ''
stBoolScenarioIsAnElementLibrary._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolScenarioIsAnElementLibrary', stBoolScenarioIsAnElementLibrary)
_module_typeBindings.stBoolScenarioIsAnElementLibrary = stBoolScenarioIsAnElementLibrary

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSecDtJitterStatus
class stBoolSecDtJitterStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSecDtJitterStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5435, 2)
    _Documentation = ''
stBoolSecDtJitterStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSecDtJitterStatus', stBoolSecDtJitterStatus)
_module_typeBindings.stBoolSecDtJitterStatus = stBoolSecDtJitterStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSecDtModStatus
class stBoolSecDtModStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSecDtModStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5444, 2)
    _Documentation = ''
stBoolSecDtModStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSecDtModStatus', stBoolSecDtModStatus)
_module_typeBindings.stBoolSecDtModStatus = stBoolSecDtModStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSecJitterStatus
class stBoolSecJitterStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSecJitterStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5453, 2)
    _Documentation = ''
stBoolSecJitterStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSecJitterStatus', stBoolSecJitterStatus)
_module_typeBindings.stBoolSecJitterStatus = stBoolSecJitterStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSecModStatus
class stBoolSecModStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSecModStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5462, 2)
    _Documentation = ''
stBoolSecModStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSecModStatus', stBoolSecModStatus)
_module_typeBindings.stBoolSecModStatus = stBoolSecModStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSensitivityOverride
class stBoolSensitivityOverride (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSensitivityOverride')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5471, 2)
    _Documentation = ''
stBoolSensitivityOverride._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSensitivityOverride', stBoolSensitivityOverride)
_module_typeBindings.stBoolSensitivityOverride = stBoolSensitivityOverride

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSensitivityThresholdEnable
class stBoolSensitivityThresholdEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSensitivityThresholdEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5480, 2)
    _Documentation = ''
stBoolSensitivityThresholdEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSensitivityThresholdEnable', stBoolSensitivityThresholdEnable)
_module_typeBindings.stBoolSensitivityThresholdEnable = stBoolSensitivityThresholdEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSlowRiseTimeStatus
class stBoolSlowRiseTimeStatus (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSlowRiseTimeStatus')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5489, 2)
    _Documentation = ''
stBoolSlowRiseTimeStatus._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSlowRiseTimeStatus', stBoolSlowRiseTimeStatus)
_module_typeBindings.stBoolSlowRiseTimeStatus = stBoolSlowRiseTimeStatus

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSutEmitterEarthReflectionEnable
class stBoolSutEmitterEarthReflectionEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSutEmitterEarthReflectionEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5498, 2)
    _Documentation = ''
stBoolSutEmitterEarthReflectionEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSutEmitterEarthReflectionEnable', stBoolSutEmitterEarthReflectionEnable)
_module_typeBindings.stBoolSutEmitterEarthReflectionEnable = stBoolSutEmitterEarthReflectionEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolSwitchDelayState
class stBoolSwitchDelayState (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolSwitchDelayState')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5507, 2)
    _Documentation = ''
stBoolSwitchDelayState._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolSwitchDelayState', stBoolSwitchDelayState)
_module_typeBindings.stBoolSwitchDelayState = stBoolSwitchDelayState

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolTerminalSegment
class stBoolTerminalSegment (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolTerminalSegment')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5516, 2)
    _Documentation = ''
stBoolTerminalSegment._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolTerminalSegment', stBoolTerminalSegment)
_module_typeBindings.stBoolTerminalSegment = stBoolTerminalSegment

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolTerrainEnable
class stBoolTerrainEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolTerrainEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5525, 2)
    _Documentation = ''
stBoolTerrainEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolTerrainEnable', stBoolTerrainEnable)
_module_typeBindings.stBoolTerrainEnable = stBoolTerrainEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolTerrainMaskingAttenuationEnable
class stBoolTerrainMaskingAttenuationEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolTerrainMaskingAttenuationEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5534, 2)
    _Documentation = ''
stBoolTerrainMaskingAttenuationEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolTerrainMaskingAttenuationEnable', stBoolTerrainMaskingAttenuationEnable)
_module_typeBindings.stBoolTerrainMaskingAttenuationEnable = stBoolTerrainMaskingAttenuationEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stBoolWaveSplashEnable
class stBoolWaveSplashEnable (pyxb.binding.datatypes.boolean):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stBoolWaveSplashEnable')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5543, 2)
    _Documentation = ''
stBoolWaveSplashEnable._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stBoolWaveSplashEnable', stBoolWaveSplashEnable)
_module_typeBindings.stBoolWaveSplashEnable = stBoolWaveSplashEnable

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDateCreationDate
class stDateCreationDate (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDateCreationDate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5552, 2)
    _Documentation = ''
stDateCreationDate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stDateCreationDate', stDateCreationDate)
_module_typeBindings.stDateCreationDate = stDateCreationDate

# Atomic simple type: {http://www.amherst.com/CEESIM/XML}stDateModificationDate
class stDateModificationDate (pyxb.binding.datatypes.dateTime):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'stDateModificationDate')
    _XSDLocation = pyxb.utils.utility.Location('/mnt/d/Repositories/data-translation/data/ceesim/schema/simulation/commonSimpleTypesR1-0.xsd', 5561, 2)
    _Documentation = ''
stDateModificationDate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'stDateModificationDate', stDateModificationDate)
_module_typeBindings.stDateModificationDate = stDateModificationDate
