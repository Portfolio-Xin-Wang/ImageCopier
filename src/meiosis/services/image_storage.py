import os
from abc import ABC, abstractmethod
from pathlib import Path

from PIL import Image

from ..Domain import Entity, ImageFrame
from .mapping import Mapper, ImageMapper


class IStorage(ABC):
    """
    Abstract base class for image repositories.
    - Local file storage
    - Cloud based solution
    """
    mapper: ImageMapper

    @abstractmethod
    def get(self) -> list:
        pass

    @abstractmethod
    def set_mapper(self, mapper: ImageMapper):
        self.mapper = mapper


class LocalFileStorage(IStorage):
    """
    An image repository that retrieves images from local file system.
    This returns the PILImageEntity type
    """
    image_directory: str
    IMAGE_FORMATS: dict = {".png": True, ".jpg": True, ".jpeg": True, ".svg": True}

    def __init__(self, image_directory: str, mapper=Mapper()):
        """
        Should return an error if no directory is found
        :param image_directory:

        Throws error if directory does not exist
        """
        self.image_directory = image_directory
        self.mapper = mapper
        os.listdir(self.image_directory)

    def get(self) -> ImageFrame:
        """
        Retrieves images from local file system.
        The assumption is that all images are located at the same directory.
        :return: List of ImageEntities. In the type of PILImageEntity
        """
        # Start loop
        transformed_images = self._enter_file("", self.image_directory)
        return ImageFrame(transformed_images)
    
    def _enter_file(self, root: str, parent_directory: str) -> list:
        entities = []
        file_names = os.listdir(parent_directory)
        for name in file_names:
            exact_location = f"{parent_directory}/{name}"
            file_entity = Path(exact_location)
            # If name is a directory, enter and start loop.
            extra_root = f"{root}/{name}"
            if(file_entity.is_dir()):
                # Append results into array
                entities += self._enter_file(extra_root,exact_location)
            # If name is an image, retrieve image and map data to entity, with the location, and target directory.
            elif(self.IMAGE_FORMATS.get(file_entity.suffix)):
                target = file_entity.parent
                print(target == parent_directory)
                image_ent = Image.open(exact_location)
                format_image = self.mapper.map(img=image_ent, img_name=name, source=extra_root)
                entities.append(format_image)
            else:
                print("Not an image")
                continue
        return entities

    def set_mapper(self, mapper):
        return super().set_mapper(mapper)

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
            entity = self.mapper.map(img=image, img_name=img_name, source=source)
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
