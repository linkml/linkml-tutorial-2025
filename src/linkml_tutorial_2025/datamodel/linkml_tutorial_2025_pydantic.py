from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )

    @model_serializer(mode='wrap', when_used='unless-none')
    def treat_empty_lists_as_none(
            self, handler: SerializerFunctionWrapHandler,
            info: SerializationInfo) -> dict[str, Any]:
        if info.exclude_none:
            _instance = self.model_copy()
            for field, field_info in type(_instance).model_fields.items():
                if getattr(_instance, field) == [] and not(
                        field_info.is_required()):
                    setattr(_instance, field, None)
        else:
            _instance = self
        return handler(_instance, info)



class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'linkml_tutorial_2025',
     'default_range': 'string',
     'description': 'This is a demo schema for use in training LinkML Schema '
                    'developers in key LinkML model and build features.',
     'id': 'https://w3id.org/linkml/linkml-tutorial-2025',
     'imports': ['linkml:types'],
     'license': 'MIT',
     'name': 'linkml-tutorial-2025',
     'prefixes': {'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'NCBITaxon': {'prefix_prefix': 'NCBITaxon',
                                'prefix_reference': 'http://purl.obolibrary.org/obo/NCBITaxon_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'PO': {'prefix_prefix': 'PO',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/PO_'},
                  'SIO': {'prefix_prefix': 'SIO',
                          'prefix_reference': 'http://semanticscience.org/resource/SIO_'},
                  'example': {'prefix_prefix': 'example',
                              'prefix_reference': 'https://example.org/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'linkml_tutorial_2025': {'prefix_prefix': 'linkml_tutorial_2025',
                                           'prefix_reference': 'https://w3id.org/linkml/linkml-tutorial-2025/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'src/linkml_tutorial_2025/schema/linkml_tutorial_2025.yaml',
     'title': 'linkml-tutorial-2025'} )

class SampleContainerEnum(str, Enum):
    tube = "tube"
    """
    Sample provided in a tube
    """
    plate = "plate"
    """
    Sample provided in a plate
    """


class PloidyEnum(str, Enum):
    haploid = "haploid"
    diploid = "diploid"
    triploid = "triploid"
    tetraploid = "tetraploid"
    allopolyploid = "allopolyploid"


class NCBITaxonEnum(str):
    pass


class TissueTypeEnum(str):
    pass



class PlantTissueSample(ConfiguredBaseModel):
    """
    Plant tissue sample metadata including collection, taxonomic, and environmental information
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/linkml-tutorial-2025'})

    id: int = Field(default=..., description="""Sample ID (No Edit) - prefilled identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample'], 'slot_uri': 'schema:identifier'} })
    sample_container: SampleContainerEnum = Field(default=..., description="""Select tube or plate""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    plate_location: Optional[str] = Field(default=None, description="""Required if samples provided in a plate. For partial plates, fill by columns. Leave blank if the sample will be shipped in a tube (e.g., B1)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    strain_variety_cultivar: str = Field(default=..., description="""Name or ID of the cultivar, variety, strain, or other similar designation of the primary organism being sampled""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    isolate: Optional[str] = Field(default=None, description="""Isolate or mutant name""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    ncbi_taxonomy_id: NCBITaxonEnum = Field(default=..., description="""Unique identifier from the NCBI taxonomy database""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    ploidy: Optional[PloidyEnum] = Field(default=None, description="""The ploidy level of the genome (e.g. allopolyploid, haploid, diploid, triploid, tetraploid). For terms, select terms listed under class ploidy (PATO:001374) of Phenotypic Quality Ontology (PATO)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample'],
         'exact_mappings': ['PATO:0001374', 'NCIT:C17001', 'SIO:010278'],
         'slot_uri': 'PATO:0001374'} })
    collection_date_time: datetime  = Field(default=..., description="""The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated. All times must be I SO8601 compliant""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    sample_size: str = Field(default=..., description="""The total amount or size (volume (ml), mass (g) or area (m2)) of sample collected. Separate the number and unit by a single space""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    tissue: str = Field(default=..., description="""Detailed description of the organ or type of tissue sampled (e.g. unopened flower buds with 1mm petal visible, 5 mm lateral root tips, 4th leaf fully expanded)""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    tissue_plant_ontology_term: Optional[list[TissueTypeEnum]] = Field(default=[], description="""Plant ontology term corresponding to plant structure sampled. May include multiple terms separated by semicolons. See https://planteome.org""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    depth_meters: Optional[float] = Field(default=None, description="""The vertical distance (in meters) below local surface. For sediment or soil samples depth is measured from sediment or soil surface, respectively. Depth can be reported as an interval for subsurface samples""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    elevation_meters: Optional[float] = Field(default=None, description="""Elevation (in meters) of the sampling site as measured by the vertical distance from mean sea level""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    broad_scale_environmental_context: Optional[str] = Field(default=None, description="""The major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain, to provide the big contextualising environment of where the sampling was done (e.g. in the desert or a rainforest). See https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    local_environmental_context: Optional[str] = Field(default=None, description="""The entity or entities which are in the sample or specimen's local vicinity and which you believe have significant causal influences on your sample or specimen. The terms used here should be countable things (e.g. a rock, a snow crystal, a cave, a hydrothermal vent) of smaller spatial grain than your entry for broad-scale environmental context. See https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })
    environmental_medium: Optional[str] = Field(default=None, description="""The environmental material(s) immediately surrounding the sample or specimen at the time of sampling. These should be mass/volume nouns (e.g. air, water) and not discrete, countable entities (e.g. a tree, a leaf, a table top). See https://github.com/EnvironmentOntology/envo/wiki/Using-ENVO-with-MIxS""", json_schema_extra = { "linkml_meta": {'domain_of': ['PlantTissueSample']} })

    @field_validator('plate_location')
    def pattern_plate_location(cls, v):
        pattern=re.compile(r"^[A-H][1-9][0-2]?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid plate_location format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid plate_location format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('sample_size')
    def pattern_sample_size(cls, v):
        pattern=re.compile(r"^[0-9]+(\.[0-9]+)?\s+(g|ml|m2)$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sample_size format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sample_size format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
PlantTissueSample.model_rebuild()
