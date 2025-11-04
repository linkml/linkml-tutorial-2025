<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# LinkML Tutorial 2025

This repository demonstrates LinkML schema development for modeling plant tissue sample metadata. It serves as a training resource for learning key LinkML features including data modeling, validation, and artifact generation.

## About This Project

This project implements a **PlantTissueSample** schema that captures comprehensive metadata for plant tissue samples, including:

- **Sample identification and container information** (tubes, plates, well locations)
- **Taxonomic classification** using NCBI Taxonomy IDs
- **Biological characteristics** (ploidy levels, tissue types, cultivar/strain information)
- **Collection metadata** (timestamps, sample sizes, tissue descriptions)
- **Environmental context** using ENVO (Environment Ontology) terms
- **Geospatial information** (depth, elevation)
- **Plant anatomy** using Plant Ontology (PO) terms

## Key LinkML Features Demonstrated

This tutorial showcases important LinkML modeling patterns:

### 1. **Ontology Integration**
- Uses standard biomedical ontologies (ENVO, PO, PATO, NCBITaxon)
- Demonstrates semantic mappings with `meaning`, `exact_mappings`, and `slot_uri`
- Shows `reachable_from` for dynamic enumeration from ontology hierarchies

### 2. **Data Validation**
- Required vs. optional fields
- Enumerated values with controlled vocabularies
- Pattern constraints (e.g., plate well positions: `^[A-H][1-9][0-2]?$`)
- Type ranges (string, integer, float, datetime, uriorcurie)
- Multivalued slots for multiple ontology term annotations

### 3. **Schema Components**
- **Classes**: PlantTissueSample with identifier and metadata slots
- **Enumerations**: SampleContainerEnum, PloidyEnum with PATO mappings
- **Dynamic Enumerations**: NCBITaxonEnum and TissueTypeEnum using `reachable_from`
- **Slots**: Field definitions with descriptions, constraints, and semantic annotations

## Learning Objectives

By exploring this repository, you will learn how to:

1. **Define LinkML schemas** with classes, slots, and enumerations
2. **Integrate ontologies** for semantic interoperability
3. **Add validation constraints** (required fields, patterns, ranges)
4. **Generate artifacts** (Python classes, Pydantic models, JSON Schema)
5. **Create test data** (valid and invalid examples)
6. **Validate data** using linkml-validate
7. **Document schemas** with auto-generated documentation

## Documentation Website

[https://linkml.github.io/linkml-tutorial-2025](https://linkml.github.io/linkml-tutorial-2025)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [src/](src/) - source files (edit these)
  * [linkml_tutorial_2025](src/linkml_tutorial_2025)
    * [schema/](src/linkml_tutorial_2025/schema) -- LinkML schema
      (edit this)
    * [datamodel/](src/linkml_tutorial_2025/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Getting Started

### Prerequisites
- Python 3.9+
- [just](https://github.com/casey/just/) command runner
- [uv](https://docs.astral.sh/uv/) package manager

### Quick Start

```bash
# Clone the repository
git clone https://github.com/linkml/linkml-tutorial-2025.git
cd linkml-tutorial-2025

# Install dependencies
uv sync

# Run tests
just test

# Validate example data
uv run linkml-validate -s src/linkml_tutorial_2025/schema/linkml_tutorial_2025.yaml \
  -C PlantTissueSample tests/data/valid/PlantTissueSample-001.yaml

# Generate artifacts (Python, Pydantic, JSON Schema, etc.)
just gen-project
```

## Example Data

The repository includes example data to demonstrate validation:

### Valid Examples (`tests/data/valid/`)
- **PlantTissueSample-001.yaml** - Complete valid sample with all required fields

### Invalid Examples (`tests/data/invalid/`)
- **PlantTissueSample-missing-required.yaml** - Missing required fields (strain_variety_cultivar, ncbi_taxonomy_id, tissue)
- **PlantTissueSample-bad-range.yaml** - Invalid enum values and type mismatches
- **PlantTissueSample-pattern-violation.yaml** - Pattern constraint violations (plate location, sample size format)

Run validation to see error messages:
```bash
linkml-validate -s src/linkml_tutorial_2025/schema/linkml_tutorial_2025.yaml \
  -C PlantTissueSample tests/data/invalid/PlantTissueSample-missing-required.yaml
```

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

### Common Commands
- `just test` - Run all tests and generate artifacts
- `just gen-project` - Generate Python datamodels, JSON Schema, etc.
- `just docs-serve` - Serve documentation locally

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
