from abc import ABC, abstractmethod
from PIL import Image
from Domain import PILImageEntity, ImageEntity, map_name_to_id, ImageMetadata
import os

from pathlib import Path


class ImageRepository(ABC):
    """
    Abstract base class for image repositories.
    - Local file storage
    - Cloud based solution
    """

    @abstractmethod
    def get(self) -> list:
        pass


class LocalFileStorage(ImageRepository):
    """
    An image repository that retrieves images from local file system.
    This returns the PILImageEntity type
    """
    image_directory: str
    IMAGE_FORMATS: dict = {".png": True, ".jpg": True, ".jpeg": True, ".svg": True}

    def __init__(self, image_directory: str):
        """
        Should return an error if no directory is found
        :param image_directory:

        Throws error if directory does not exist
        """
        self.image_directory = image_directory
        os.listdir(self.image_directory)

    def get(self) -> list[ImageEntity]:
        """
        Retrieves images from local file system.
        The assumption is that all images are located at the same directory.
        :return: List of ImageEntities. In the type of PILImageEntity
        """
        file_names = os.listdir(self.image_directory)
        image_names = self._filter_non_images(file_names)
        return self._format_images(image_names, self.image_directory)

    def _format_images(self, images: list[str], source: str) -> list[ImageEntity]:
        """
        Locates images in local file system.
        Formats it in a image entity
        :param images:
        :return:
        """
        _pil_image = []
        location = "{data_dir}/{name}"
        for image_location in images:
            image = Image.open(location.format(data_dir=source, name=image_location))
            label_id = map_name_to_id(image_location)
            meta_data = ImageMetadata(label_id, image_location, source)
            entity = PILImageEntity(image, meta_data)
            _pil_image.append(entity)
        return _pil_image

    def _filter_non_images(self, images: list[str]) -> list:
        _images = []
        for image in images:
            # Future check if file with a extension is a directory or folder and a directory
            file = Path(image)
            is_image = self.IMAGE_FORMATS.get(file.suffix)
            if is_image:
                # Returns in format file_name.jpg for example
                _images.append(file.name)
        return _images
