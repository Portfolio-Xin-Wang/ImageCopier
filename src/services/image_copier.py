from PIL import Image
from .Image_repository import ImageRepository
from ..Domain import PILImageEntity, ImageStore
from src.services.transformers import ImageTransformer

class ImageCopier:
    """
    Main entry point for image copier.
    """
    output_direction: str
    transformed_name: str
    image_repository: ImageRepository
    transformers: ImageTransformer
    _angle: int

    def __init__(self, image_repo: ImageRepository, transformers: ImageTransformer) -> None:
        self.transformed_name = "{label_id}&{rotation};{file}.{extension}"
        self._angle = 0
        self.transformers = transformers
        self.image_repository = image_repo

    def basic_perform(self) -> list[PILImageEntity]:
        """
        This is the basic class that looks up images and makes a copy of them like image_1|rot-5.jpg
        """
        # Currently extracting a concrete type. Later this responsibility will be moved to a transformer class
        images: list[PILImageEntity] = self.image_repository.get()
        # Export function: format metadata
        result = self.transformers.transform(ImageStore(images=images))
        return result.images_collection 
