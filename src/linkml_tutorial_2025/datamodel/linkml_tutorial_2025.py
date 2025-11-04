# Auto generated from linkml_tutorial_2025.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-11-04T11:56:43
# Schema: linkml-tutorial-2025
#
# id: https://w3id.org/linkml/linkml-tutorial-2025
# description: This is a demo schema for use in training LinkML Schema developers in key LinkML model and build features.
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDateTime

metamodel_version = "1.7.0"
version = None

# Namespaces
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PO = CurieNamespace('PO', 'http://purl.obolibrary.org/obo/PO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/SIO_')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_TUTORIAL_2025 = CurieNamespace('linkml_tutorial_2025', 'https://w3id.org/linkml/linkml-tutorial-2025/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LINKML_TUTORIAL_2025


# Types

# Class references
class PlantTissueSampleId(extended_int):
    pass


@dataclass(repr=False)
class PlantTissueSample(YAMLRoot):
    """
    Plant tissue sample metadata including collection, taxonomic, and environmental information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2025["PlantTissueSample"]
    class_class_curie: ClassVar[str] = "linkml_tutorial_2025:PlantTissueSample"
    class_name: ClassVar[str] = "PlantTissueSample"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2025.PlantTissueSample

    id: Union[int, PlantTissueSampleId] = None
    sample_container: Union[str, "SampleContainerEnum"] = None
    strain_variety_cultivar: str = None
    ncbi_taxonomy_id: Union[str, "NCBITaxonEnum"] = None
    collection_date_time: Union[str, XSDDateTime] = None
    sample_size: str = None
    tissue: str = None
    plate_location: Optional[str] = None
    isolate: Optional[str] = None
    ploidy: Optional[Union[str, "PloidyEnum"]] = None
    tissue_plant_ontology_term: Optional[Union[Union[str, "TissueTypeEnum"], list[Union[str, "TissueTypeEnum"]]]] = empty_list()
    depth_meters: Optional[float] = None
    elevation_meters: Optional[float] = None
    broad_scale_environmental_context: Optional[Union[str, URIorCURIE]] = None
    local_environmental_context: Optional[Union[str, URIorCURIE]] = None
    environmental_medium: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlantTissueSampleId):
            self.id = PlantTissueSampleId(self.id)

        if self._is_empty(self.sample_container):
            self.MissingRequiredField("sample_container")
        if not isinstance(self.sample_container, SampleContainerEnum):
            self.sample_container = SampleContainerEnum(self.sample_container)

        if self._is_empty(self.strain_variety_cultivar):
            self.MissingRequiredField("strain_variety_cultivar")
        if not isinstance(self.strain_variety_cultivar, str):
            self.strain_variety_cultivar = str(self.strain_variety_cultivar)

        if self._is_empty(self.collection_date_time):
            self.MissingRequiredField("collection_date_time")
        if not isinstance(self.collection_date_time, XSDDateTime):
            self.collection_date_time = XSDDateTime(self.collection_date_time)

        if self._is_empty(self.sample_size):
            self.MissingRequiredField("sample_size")
        if not isinstance(self.sample_size, str):
            self.sample_size = str(self.sample_size)

        if self._is_empty(self.tissue):
            self.MissingRequiredField("tissue")
        if not isinstance(self.tissue, str):
            self.tissue = str(self.tissue)

        if self.plate_location is not None and not isinstance(self.plate_location, str):
            self.plate_location = str(self.plate_location)

        if self.isolate is not None and not isinstance(self.isolate, str):
            self.isolate = str(self.isolate)

        if self.ploidy is not None and not isinstance(self.ploidy, PloidyEnum):
            self.ploidy = PloidyEnum(self.ploidy)

        if self.depth_meters is not None and not isinstance(self.depth_meters, float):
            self.depth_meters = float(self.depth_meters)

        if self.elevation_meters is not None and not isinstance(self.elevation_meters, float):
            self.elevation_meters = float(self.elevation_meters)

        if self.broad_scale_environmental_context is not None and not isinstance(self.broad_scale_environmental_context, URIorCURIE):
            self.broad_scale_environmental_context = URIorCURIE(self.broad_scale_environmental_context)

        if self.local_environmental_context is not None and not isinstance(self.local_environmental_context, URIorCURIE):
            self.local_environmental_context = URIorCURIE(self.local_environmental_context)

        if self.environmental_medium is not None and not isinstance(self.environmental_medium, URIorCURIE):
            self.environmental_medium = URIorCURIE(self.environmental_medium)

        super().__post_init__(**kwargs)


# Enumerations
class SampleContainerEnum(EnumDefinitionImpl):

    tube = PermissibleValue(
        text="tube",
        description="Sample provided in a tube")
    plate = PermissibleValue(
        text="plate",
        description="Sample provided in a plate")

    _defn = EnumDefinition(
        name="SampleContainerEnum",
    )

class PloidyEnum(EnumDefinitionImpl):

    haploid = PermissibleValue(
        text="haploid",
        meaning=PATO["0001393"])
    diploid = PermissibleValue(
        text="diploid",
        meaning=PATO["0001394"])
    triploid = PermissibleValue(
        text="triploid",
        meaning=PATO["0001395"])
    tetraploid = PermissibleValue(
        text="tetraploid",
        meaning=PATO["0001396"])
    allopolyploid = PermissibleValue(
        text="allopolyploid",
        meaning=PATO["0001392"])

    _defn = EnumDefinition(
        name="PloidyEnum",
    )

class NCBITaxonEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NCBITaxonEnum",
    )

class TissueTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="TissueTypeEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=LINKML_TUTORIAL_2025.id, domain=None, range=URIRef)

slots.sample_container = Slot(uri=LINKML_TUTORIAL_2025.sample_container, name="sample_container", curie=LINKML_TUTORIAL_2025.curie('sample_container'),
                   model_uri=LINKML_TUTORIAL_2025.sample_container, domain=None, range=Union[str, "SampleContainerEnum"])

slots.plate_location = Slot(uri=LINKML_TUTORIAL_2025.plate_location, name="plate_location", curie=LINKML_TUTORIAL_2025.curie('plate_location'),
                   model_uri=LINKML_TUTORIAL_2025.plate_location, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-H][1-9][0-2]?$'))

slots.strain_variety_cultivar = Slot(uri=LINKML_TUTORIAL_2025.strain_variety_cultivar, name="strain_variety_cultivar", curie=LINKML_TUTORIAL_2025.curie('strain_variety_cultivar'),
                   model_uri=LINKML_TUTORIAL_2025.strain_variety_cultivar, domain=None, range=str)

slots.isolate = Slot(uri=LINKML_TUTORIAL_2025.isolate, name="isolate", curie=LINKML_TUTORIAL_2025.curie('isolate'),
                   model_uri=LINKML_TUTORIAL_2025.isolate, domain=None, range=Optional[str])

slots.ncbi_taxonomy_id = Slot(uri=LINKML_TUTORIAL_2025.ncbi_taxonomy_id, name="ncbi_taxonomy_id", curie=LINKML_TUTORIAL_2025.curie('ncbi_taxonomy_id'),
                   model_uri=LINKML_TUTORIAL_2025.ncbi_taxonomy_id, domain=None, range=Union[str, "NCBITaxonEnum"])

slots.ploidy = Slot(uri=PATO['0001374'], name="ploidy", curie=PATO.curie('0001374'),
                   model_uri=LINKML_TUTORIAL_2025.ploidy, domain=None, range=Optional[Union[str, "PloidyEnum"]])

slots.collection_date_time = Slot(uri=LINKML_TUTORIAL_2025.collection_date_time, name="collection_date_time", curie=LINKML_TUTORIAL_2025.curie('collection_date_time'),
                   model_uri=LINKML_TUTORIAL_2025.collection_date_time, domain=None, range=Union[str, XSDDateTime])

slots.sample_size = Slot(uri=LINKML_TUTORIAL_2025.sample_size, name="sample_size", curie=LINKML_TUTORIAL_2025.curie('sample_size'),
                   model_uri=LINKML_TUTORIAL_2025.sample_size, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]+(\.[0-9]+)?\s+(g|ml|m2)$'))

slots.tissue = Slot(uri=LINKML_TUTORIAL_2025.tissue, name="tissue", curie=LINKML_TUTORIAL_2025.curie('tissue'),
                   model_uri=LINKML_TUTORIAL_2025.tissue, domain=None, range=str)

slots.tissue_plant_ontology_term = Slot(uri=LINKML_TUTORIAL_2025.tissue_plant_ontology_term, name="tissue_plant_ontology_term", curie=LINKML_TUTORIAL_2025.curie('tissue_plant_ontology_term'),
                   model_uri=LINKML_TUTORIAL_2025.tissue_plant_ontology_term, domain=None, range=Optional[Union[Union[str, "TissueTypeEnum"], list[Union[str, "TissueTypeEnum"]]]])

slots.depth_meters = Slot(uri=LINKML_TUTORIAL_2025.depth_meters, name="depth_meters", curie=LINKML_TUTORIAL_2025.curie('depth_meters'),
                   model_uri=LINKML_TUTORIAL_2025.depth_meters, domain=None, range=Optional[float])

slots.elevation_meters = Slot(uri=LINKML_TUTORIAL_2025.elevation_meters, name="elevation_meters", curie=LINKML_TUTORIAL_2025.curie('elevation_meters'),
                   model_uri=LINKML_TUTORIAL_2025.elevation_meters, domain=None, range=Optional[float])

slots.broad_scale_environmental_context = Slot(uri=LINKML_TUTORIAL_2025.broad_scale_environmental_context, name="broad_scale_environmental_context", curie=LINKML_TUTORIAL_2025.curie('broad_scale_environmental_context'),
                   model_uri=LINKML_TUTORIAL_2025.broad_scale_environmental_context, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.local_environmental_context = Slot(uri=LINKML_TUTORIAL_2025.local_environmental_context, name="local_environmental_context", curie=LINKML_TUTORIAL_2025.curie('local_environmental_context'),
                   model_uri=LINKML_TUTORIAL_2025.local_environmental_context, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.environmental_medium = Slot(uri=LINKML_TUTORIAL_2025.environmental_medium, name="environmental_medium", curie=LINKML_TUTORIAL_2025.curie('environmental_medium'),
                   model_uri=LINKML_TUTORIAL_2025.environmental_medium, domain=None, range=Optional[Union[str, URIorCURIE]])
