import os
from abc import ABC, abstractmethod
from pathlib import Path

from PIL import Image

from ..Domain import Entity, EntityInfo, ImageFrame, PILEntity, map_name_to_id


class IStorage(ABC):
    """
    Abstract base class for image repositories.
    - Local file storage
    - Cloud based solution
    """

    @abstractmethod
    def get(self) -> list:
        pass


class LocalFileStorage(IStorage):
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

    def get(self) -> ImageFrame:
        """
        Retrieves images from local file system.
        The assumption is that all images are located at the same directory.
        :return: List of ImageEntities. In the type of PILImageEntity
        """
        file_names = os.listdir(self.image_directory)
        image_names = self._filter_non_images(file_names)
        transformed_images = self._format_images(image_names, self.image_directory)
        return ImageFrame(transformed_images)

    def _format_images(self, names: list[str], source: str) -> list[Entity]:
        """
        Locates images in local file system.
        Formats it in a image entity
        :param images:
        :return:
        """
        _pil_image = []
        location = "{data_dir}/{name}"
        for img_name in names:
            image = Image.open(location.format(data_dir=source, name=img_name))
            label_id = map_name_to_id(img_name)
            meta_data = EntityInfo(label_id, img_name, source)
            entity = PILEntity(image, meta_data)
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
