from src.services.transformers import PILImageBuilder

from .image_copier import ImageCopier
from .Image_repository import LocalFileStorage
from .image_exporter import LocalImageExporter

class ImageServiceFactory:
    transformer_builder: PILImageBuilder

    def __init__(self):
        self.transformer_builder = PILImageBuilder()

    def create_pil_image_copier(self, copies: int = 1, rotation_base: int = 1, original_dir: str="test_images", output_dir: str = "output") -> LocalImageExporter:
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
        transformers = self.transformer_builder.reset().add_copies(copies).add_rotation(rotation_base).build()
        copier = ImageCopier(local_file_storage, transformers)
        # Build exporter
        exporter = LocalImageExporter(copier=copier, output_direction=output_dir)
        return exporter