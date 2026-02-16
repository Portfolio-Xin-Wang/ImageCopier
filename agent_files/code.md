# Code.MD
This .md file contains the instructions for the Agent for the creation new classes based on the instruction set in this file.

## Folder Structure & Responsibilities

### `/src/meiosis/api/`
**Entry point for external consumers**
- `export.py`: Main public API (`Export` class with `read_from_directory()` method)
- No business logic here; delegates to service layer
- Methods should be thin wrappers around factory/service calls

### `/src/meiosis/domain/`
**Business entities and value objects**
- `entity.py`: Abstract `Entity` and concrete `PILEntity` classes
- `entity_info.py`: Metadata wrapper for images
- `image_frame.py`: Container for image collections
- `map_names.py`: Mapping utilities for image names
- **Rules**: 
  - Pure data structures; minimal logic
  - Use ABC for extensibility (PILEntity extends Entity)
  - Include metadata alongside image data

### `/src/meiosis/services/transformers/`
**Image transformation pipeline**
- `transformer.py`: Abstract base for transformations
- `transformer_builder.py`: Builder pattern for chaining transformers
- `copy_component.py`: Copy transformation
- `hsv_transformer.py`: HSV color space transformations
- `image_transformer.py`: Concrete PIL-based transformer
- `mapping_component.py`: Name mapping transformations
- `rotator_component.py`: Rotation transformations
- **Rules**:
  - All transformers extend `Transformer` ABC
  - Transformers accept and return `ImageFrame`
  - Builder pattern for composition
  - Each transformer handles one concern (SRP)


## Testing Rules

### Test Structure
- Use `pytest` framework
- Place tests in `/tests/` mirroring `/src/` structure
- Naming: `test_<functionality>.py`

### `/tests/`
**Unit and integration tests**
- Mirror source structure
- Use `pytest` framework
- Test files: `test_*.py`
- Image test artifacts in `/tests/images/`
- **Rules**:
  - Test file naming: `test_<module>.py`
  - Use fixtures for common test data
  - 100% coverage target (coverage package configured)

### Coverage
- Use `coverage` package for measurement
- Aim for high coverage on:
  - Domain entities
  - Service orchestration
  - Transformer implementations
- Lower priority on:
  - PIL/NumPy wrapper code
  - Test utilities
  
### Test Data
- Store test images in `/tests/images/`
- Use subdirectories by test type:
  - `/tests/images/import_new/`: new image imports
  - `/tests/images/transform/`: transformation test artifacts
  - `/tests/images/exporter/`: export test artifacts
  - `/tests/images/retrieval/`: retrieval test data

---