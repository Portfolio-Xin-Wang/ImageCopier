from .image_exporter import LocalFileExporter
from .image_handler import ImageHandler
from .image_storage import LocalFileStorage
from .transformers import PILImageBuilder, MapTransformer


class ImageServiceFactory:
    transformer_builder: PILImageBuilder

    def __init__(self):
        self.transformer_builder = PILImageBuilder()

    def create_pil_image_copier(self, copies: int = 1, rotation_base: int = 1, original_dir: str="test_images", output_dir: str = "output", mapping: MapTransformer = None) -> LocalFileExporter:
        """
        This method creates an ImageCopier with 
        - LocalFileStorage as the image repository.
        - A ImageTransformation with RotatorTransformer and CopierTransformer as transformers.
        - LocalImageExporter as the image exporter.
        - Using a PILImageBuilder to build the ImageTransformer.
        """
        # Add repository
        local_file_storage = LocalFileStorage(image_directory=original_dir)
        # Add transformers
        transformers = self.transformer_builder.reset().add_mapping(mapping).add_copies(copies).add_rotation(rotation_base).build()
        copier = ImageHandler(local_file_storage, transformers)
        # Build exporter
        exporter = LocalFileExporter(copier=copier, output_direction=output_dir)
        return exporter