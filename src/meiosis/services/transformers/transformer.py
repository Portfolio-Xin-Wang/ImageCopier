from abc import ABC, abstractmethod
from ...Domain import ImageStore


class Transformer(ABC):

    @abstractmethod
    def transform(self, image_store: ImageStore) -> ImageStore:
        pass