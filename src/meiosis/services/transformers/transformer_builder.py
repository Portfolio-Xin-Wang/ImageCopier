from abc import ABC, abstractmethod

from .copy_component import CopyTransformer
from .image_transformer import ImageTransformer
from .rotator_component import RotatorTransformer


class TransformerBuilder(ABC):
    # Possible implementations:
    # PIL-Images
    # OpenCV images
    
    @abstractmethod
    def reset(self) -> TransformerBuilder:
        pass

    @abstractmethod
    def add_rotation(self, base_value: int = 20) -> TransformerBuilder:
        pass 

    @abstractmethod
    def add_copies(self, copies: int = 1) -> TransformerBuilder:
        pass

    @abstractmethod
    def build(self) -> ImageTransformer:
        pass

    # Add further transformations
    # - Color changes
    # - Augmentation to image
    # - Standardizing images to fixed size

class PILImageBuilder(TransformerBuilder):

    image_composite: ImageTransformer

    def __init__(self):
        self.image_composite = ImageTransformer()

    def reset(self):
        self.image_composite = ImageTransformer()
        self.image_composite.transformers = []
        return self
    
    def add_rotation(self, base_value = 2):
        self.image_composite.add_component(RotatorTransformer(base_value))
        return self
    
    def add_copies(self, copies = 1):
        self.image_composite.add_component(CopyTransformer(copy=copies))
        return self
    
    def build(self):
        return self.image_composite