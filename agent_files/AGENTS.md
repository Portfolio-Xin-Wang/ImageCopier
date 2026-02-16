# Meiosis Codebase - Agent Development Rules

## .MD file structure
This project contains the following relevant .MD files needed to perform actions.

**CODE.md** The rules for code generations, tests and implementation

Future .md,
- Documentation generation
- Quick commands.

## Project Overview
**Meiosis** is a Python package (v0.1.6, alpha state) for creating and transforming images for ML workflows. It provides image data generation, transformation, and synthetic data creation capabilities.

- **Language**: Python 3.12+
- **Key Dependencies**: Pillow, NumPy, Pytest, Coverage
- **Purpose**: Image generation, transformation, and copying for CV/ML applications
- **Status**: Alpha (methods and parameters subject to change)

---

## Architecture & Design Patterns

### Layered Architecture
The codebase follows a clean, layered architecture:

```
TODO: Replace this with Image.
API Layer (Export)
    ↓
Service Layer (ImageServiceFactory, Exporter, Transformer)
    ↓
Domain Layer (Entity, EntityInfo, ImageFrame)
```

### Key Design Patterns

1. **Factory Pattern**: `ImageServiceFactory` creates service instances
   - Used for instantiating image handlers, exporters, and transformers
   - Location: `src/meiosis/services/meiosis_factory.py`

2. **Abstract Base Class (ABC)**: Core interfaces for extensibility
   - `Entity` - encapsulates images and metadata
   - `Transformer` - base for transformation chains
   - Used throughout domain and service layers

3. **Strategy Pattern**: Transformers implement pluggable algorithms
   - `Transformer` and `MapTransformer` allow custom transformation pipelines
   - Builder pattern with `TransformerBuilder` for composing transformers

4. **Dependency Injection**: Services receive dependencies via constructor
   - Promotes testability and loose coupling
---

## Code Conventions

### Naming
- **Classes**: PascalCase (`Export`, `PILEntity`, `TransformerBuilder`)
- **Methods/Functions**: snake_case (`read_from_directory`, `return_image_name`)
- **Constants**: UPPER_SNAKE_CASE
- **Private/Protected**: prefix with `_` (Python convention)

### Type Hints
- Always use type hints for method parameters and return types
- Import from `typing` module for complex types
- Use domain types where applicable: `ImageFrame`, `EntityInfo`, `Transformer`

### Documentation
- Use docstrings for public methods
- Format: concise single-line or multi-line with description and type info
- Example from `Entity.return_image_name()`:
  ```python
  def return_image_name(self) -> str:
      """Returns an image name"""
      return self.meta_data.name
  ```

### Abstract Base Classes
- Use `ABC` and `@abstractmethod` for interfaces
- Example:
  ```python
  from abc import ABC, abstractmethod
  
  class Transformer(ABC):
      @abstractmethod
      def transform(self, image_store: ImageFrame) -> ImageFrame:
          pass
  ```
---

## Common Workflows & Patterns

### Adding a New Transformer
1. Create file in `/src/meiosis/services/transformers/`
2. Extend `Transformer` ABC
3. Implement `transform(self, image_store: ImageFrame) -> ImageFrame`
4. Register in `TransformerBuilder` if composable
5. Add tests in `/tests/test_transformer.py`

### Adding a New Image Entity Type
1. Create class extending `Entity` in `/src/meiosis/domain/entity.py`
2. Implement abstract methods: `return_image_name()`, `deep_copy()`, `image_to_numpy()`
3. Store metadata as `EntityInfo`
4. Update factory to support new type if needed

### Exporting Images
1. Use `Export` API from `src/meiosis/api/export.py`
2. Call `read_from_directory()` with parameters:
   - `original_dir`: source directory
   - `output_dir`: destination directory
   - `copies`: number of copies per image
   - `rotation_base`: rotation increment
   - `custom_mapper`: optional custom transformation
3. Returns `ImageFrame` with processed images

---

## Dependencies & Imports

### External Libraries
```python
from PIL import Image          # Image processing
from numpy import array, ...   # Numerical operations
import pytest                  # Testing framework
```

### Internal Imports
- Use relative imports within package: `from ..services import ...`
- Use absolute imports for external code
- Follow module hierarchy: `from .domain import Entity`

### Import Organization
```python
# 1. ABC/typing
from abc import ABC, abstractmethod
from typing import Optional, List

# 2. External libraries
from PIL import Image
import numpy as np

# 3. Internal imports
from ..domain import Entity, ImageFrame
from ..services import ImageServiceFactory
```

---

## Code Quality Guidelines

### Principles
- **Single Responsibility**: Each class has one reason to change
- **Open/Closed**: Open for extension (via ABC), closed for modification
- **Dependency Injection**: Pass dependencies, don't instantiate them
- **DRY**: Avoid repetition; extract to helper methods/classes

### Anti-Patterns to Avoid
- ❌ Hardcoded paths without parameterization
- ❌ Mixing concerns (e.g., image processing + file I/O in same method)
- ❌ Missing type hints
- ❌ Skipping tests for "simple" code
- ❌ Circular imports between layers

### Error Handling
- Use specific exception types when possible
- Document exceptions in docstrings
- Consider validation at layer boundaries (API/Domain)

---

## Future Extensibility

The codebase is designed for:
1. **New Transformers**: Add to `transformers/` following `Transformer` ABC
2. **New Entity Types**: Extend `Entity` in domain layer
3. **New Data Sources**: Implement in `ImageHandler` or new handler class
4. **Custom Mappers**: Pass `MapTransformer` implementations to `Export.read_from_directory()`
5. **New Storage Backends**: Implement in `image_storage.py`

---

## Version & Stability Notes

⚠️ **Alpha State**: This package (v0.1.6) is in active development
- Method signatures may change
- New features may be added
- Breaking changes possible in minor versions
- Pin specific versions in production: `meiosis==0.1.6`

---

## Quick Reference: File Locations

| Concern | Location |
|---------|----------|
| Public API | `src/meiosis/api/export.py` |
| Entities | `src/meiosis/domain/` |
| Services | `src/meiosis/services/` |
| Transformers | `src/meiosis/services/transformers/` |
| Tests | `tests/test_*.py` |
| Configuration | `pyproject.toml`, `requirements.txt` |
