from .transformer import Transformer
from ...Domain import PILImageEntity
import random

class RotatorTransformer(Transformer):
    base_value: int 

    def __init__(self, value = 1):
        self.base_value = value

    def transform(self, image_store):
        for image in image_store.images_collection:
            image: PILImageEntity
            angle = self._generate_random_angle()
            image.image.rotate(angle)
            image.meta_data.add_transformation("rot", angle)
        return image_store
    
    def _generate_random_angle(self):
        return random.randint(1, 360)