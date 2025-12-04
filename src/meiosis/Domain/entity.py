from abc import ABC, abstractmethod

from numpy import array, ndarray
from PIL import Image

from .entity_info import EntityInfo


class Entity(ABC):
    """
    Abstract base class for ImageEntity
    It may be used to encapsulate images in different ways.
    """
    meta_data: EntityInfo

    def __init__(self, meta_data: EntityInfo):
        self.meta_data = meta_data

    @abstractmethod
    def return_image_name(self) -> str:
        """
        Returns an image name
        """
        return self.meta_data.name

    @abstractmethod
    def deep_copy(self) -> Entity:
        pass

    @abstractmethod
    def image_to_numpy(self) -> ndarray:
        pass

    def metadata_to_numpy(self) -> ndarray:
        return array(self.meta_data.__dict__())


class PILEntity(Entity):

    image: Image

    def __init__(self, image: Image, meta_data: EntityInfo):
        super().__init__(meta_data)
        self.image = image

    def return_image_name(self) -> str:
        return self.meta_data.return_name()

    def deep_copy(self) -> PILEntity:
        new_meta = EntityInfo(
            self.meta_data.label_id, self.meta_data.name, self.meta_data.location
        )
        return PILEntity(self.image, new_meta)
    
    def image_to_numpy(self):
        return array(self.image)
