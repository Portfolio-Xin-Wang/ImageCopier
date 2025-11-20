from abc import ABC, abstractmethod
from PIL import Image


class ImageEntity(ABC):
    """
    Abstract base class for ImageEntity
    It may be used to encapsulate images in different ways.
    """
    image_name: str
    source_location: str
    label_id: int = 0

    def __init__(self, image_name: str, source: str, label_id: int):
        self.image_name = image_name
        self.source_location = source
        self.label_id = label_id

    @abstractmethod
    def return_image_name(self) -> str:
        """
        Returns an image name
        """
        return self.image_name

    @abstractmethod
    def deep_copy(self):
        return ImageEntity(self.image_name, self.label_id)


class PILImageEntity(ImageEntity):

    image: Image

    def __init__(self, image: Image, image_name: str, source: str, label_id: int):
        super().__init__(image_name, source, label_id)
        self.image = image

    def return_image_name(self) -> str:
        return self.image_name

    def deep_copy(self):
        return PILImageEntity(self.image, self.image_name, self.label_id)
