from .image_exporter import LocalFileExporter
from .image_handler import ImageHandler
from .image_storage import LocalFileStorage
from .mapping import ImageMapper, StandardMapper
from .transformers import PILImageBuilder


class ImageServiceFactory:
    transformer_builder: PILImageBuilder

    def __init__(self, custom_mapper:ImageMapper = StandardMapper()):
        self.transformer_builder = PILImageBuilder()
        self.custom_mapper = custom_mapper

    def create_pil_image_copier(self, copies: int = 1, rotation_base: int = 1, original_dir: str="test_images", output_dir: str = "output") -> LocalFileExporter:
        """
        This method creates an ImageCopier with 
        - LocalFileStorage as the image repository.
        - A ImageTransformation with RotatorTransformer and CopierTransformer as transformers.
        - LocalImageExporter as the image exporter.
        - Using a PILImageBuilder to build the ImageTransformer.
        """
        # Add repository
        local_file_storage = LocalFileStorage(image_directory=original_dir, mapper=self.custom_mapper)
        # Add transformers
        transformers = self.transformer_builder.reset().add_copies(copies).add_rotation(rotation_base).build()
        copier = ImageHandler(local_file_storage, transformers)
        # Build exporter
        exporter = LocalFileExporter(copier=copier, output_direction=output_dir)
        return exporter