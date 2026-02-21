# Meiosis 0.1.6
Meiosis is a Python package for creating new Images, usable for generating extra image data for ML-workflows.

*Warning: This package is currently in alpha state, methods and its input parameters might be subject to change.*

## Use cases:
- Transformation of Image data
- Generation of small to mid-size image sets suitable for CV.
- Generation of Synthetic data.

## Software design and architecture:
This tool utilizes a n-tier architecture:
- Entities as the domain layer.
- Service layer, handling business logic.
- API, usable for the users of this  package.

## Installation

Pip:
```sh
pip install meiosis
```

For a specific version:
```sh
pip install meiosis==0.1.5
```

Poetry:
```sh
poetry add meiosis
```

## Quick start
The current package provides one way to copy images locally, from a local data source. In this case a file directory.

```py
from src import Export

export_api = Export()

images = export_api.read_from_directory()

print("Exported images:")
for image in images:
    print(f"- {image}") 
```

## Future features:
- External data source extraction
- Copy functionality
- Customizability of export files