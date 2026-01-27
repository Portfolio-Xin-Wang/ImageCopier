from ..domain import ImageFrame
from .image_storage import IStorage
from .transformers import ImageTransformer


class ImageHandler:
    """
    Main entry point for image copier.
    """
    output_direction: str
    image_repository: IStorage
    transformers: ImageTransformer

    def __init__(self, image_repo: IStorage, transformers: ImageTransformer) -> None:
        self.transformers = transformers
        self.image_repository = image_repo

    def handle(self) -> ImageFrame:
        """
        This is the basic class that looks up images and makes a copy of them like image_1|rot-5.jpg
        """
        # Currently extracting a concrete type. Later this responsibility will be moved to a transformer class
        images: ImageFrame = self.image_repository.get()
        # Export function: format metadata
        result = self.transformers.transform(images)
        return result
