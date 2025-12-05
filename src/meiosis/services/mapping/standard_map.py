from PIL import Image
from ...Domain import Entity, PILEntity, EntityInfo, map_name_to_id
from abc import ABC, abstractmethod

class ImageMapper(ABC):

    @abstractmethod
    def map(self, img: Image, img_name: str, source: str) -> Entity:
        pass

class StandardMapper(ImageMapper):
    def map(self, img, img_name, source):
        info = EntityInfo(name=img_name, location=source)
        return PILEntity(img, info)

class BreadMapper(ImageMapper):
    """
    A custom mapper for the Bread checkout software.
    Replace it with the standard mapper or custom mapper
    """

    def map(self, img, img_name, source):
        label_id = map_name_to_id(img_name)
        info = EntityInfo(label_id=label_id, name=img_name, location=source)
        return PILEntity(img, info)