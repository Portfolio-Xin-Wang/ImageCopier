import os
from abc import ABC, abstractmethod
from pathlib import Path

from PIL import Image

from ..Domain import Entity, ImageFrame
from .mapping import ImageMapper, Mapper


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
        # Perhaps a recursive loop.
        for name in file_names:
            exact_location = f"{parent_directory}/{name}"
            file_entity = Path(exact_location)
            # If name is a directory, enter and start loop.
            extra_root = f"{root}/{name}"
            if(file_entity.is_dir()):
                # Append results into array
                entities += self._enter_file(extra_root, exact_location)
            # If name is an image, retrieve image and map data to entity, with the location, and target directory.
            elif(self.IMAGE_FORMATS.get(file_entity.suffix)):
                # name = file_entity.stem # Will need to be used in the future to seperate the name without its suffix
                image_ent = Image.open(exact_location)
                format_image = self._format(image=image_ent, 
                                            name=name, 
                                            exact_location=extra_root, 
                                            target_dir=file_entity.parent.name, 
                                            root=root)
                entities.append(format_image)
            else:
                print("Not an image")
                continue
        return entities

    def set_mapper(self, mapper):
        return super().set_mapper(mapper)

    def _format(self, image, name: str, exact_location: str, target_dir: str, root: str):
        # This means the current pointer is at the root folder level.
        if root != "":
            return self.mapper.map(img=image, img_name=name, source=exact_location, target=target_dir)
        # If root is empty. 
        return self.mapper.map(img=image, img_name=name, source=exact_location, target=root)