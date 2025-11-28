from src import ImageCopier, LocalFileStorage, LocalImageExporter

from src.Domain import ImageMetadata
# If images are found, return names

repo = LocalFileStorage(image_directory="test_images")
copier = ImageCopier(image_repo=repo)
exporter = LocalImageExporter(copier=copier, output_direction="output")

entities = exporter.export()


