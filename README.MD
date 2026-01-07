# Meiosis 0.1.4
Meiosis is a Python package for creating new Images, usable for generating extra image data for ML-workflows.
Thank you for using the Meiosis package.

*Warning: This package is currently in alpha state, methods and its input parameters might be subject to change.*

## Use cases:
- Transformation of Image data
- Expanding current image datasets.

## Installation

Pip:
```sh
pip install meiosis
```

For a specific version:
```sh
pip install meiosis==0.1.4
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
- More custom copy-pipeline functions
- Integration of OpenCV
- Customizability of export files
- A general data structure for images like DataFrames