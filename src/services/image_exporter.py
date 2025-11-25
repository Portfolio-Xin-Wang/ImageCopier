from abc import ABC, abstractmethod
from ..Domain import ImageEntity

class ImageExporter(ABC):

    @abstractmethod
    def export(self, images: list[ImageEntity]) -> None:
        pass