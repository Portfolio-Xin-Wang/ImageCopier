from abc import ABC, abstractmethod

from ...Domain import ImageFrame


class Transformer(ABC):

    @abstractmethod
    def transform(self, image_store: ImageFrame) -> ImageFrame:
        pass