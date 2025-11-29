from abc import ABC, abstractmethod
from PIL import Image
from .image_metadata import ImageMetadata

class ImageEntity(ABC):
    """
    Abstract base class for ImageEntity
    It may be used to encapsulate images in different ways.
    """
    meta_data: ImageMetadata

    def __init__(self, meta_data: ImageMetadata):
        self.meta_data = meta_data

    @abstractmethod
    def return_image_name(self) -> str:
        """
        Returns an image name
        """
        return self.meta_data.name

    @abstractmethod
    def deep_copy(self):
        pass


class PILImageEntity(ImageEntity):

    image: Image

    def __init__(self, image: Image, meta_data: ImageMetadata):
        super().__init__(meta_data)
        self.image = image

    def return_image_name(self) -> str:
        return self.meta_data.name

    def deep_copy(self):
        return PILImageEntity(self.image, self.meta_data)
