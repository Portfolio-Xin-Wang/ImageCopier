from abc import ABC, abstractmethod
from Domain import ImageStore, PILImageEntity


class Transformer(ABC):

    @abstractmethod
    def transform(self, image_store: ImageStore) -> ImageStore:
        pass