from abc import ABC, abstractmethod

from ...domain import ImageFrame


class Transformer(ABC):

    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def transform(self, image_store: ImageFrame) -> ImageFrame:
        pass