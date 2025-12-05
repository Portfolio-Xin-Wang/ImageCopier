from ...Domain import ImageFrame
from .transformer import Transformer


class ImageTransformer(Transformer):

    transformers: list[Transformer]
    starting_transformer: Transformer

    def __init__(self):
        self.transformers = []
        super().__init__()

    def transform(self, image_store):
        updated_image_store: ImageFrame = image_store
        for transformer in self.transformers:
            updated_image_store = transformer.transform(image_store=image_store)
        return updated_image_store
    
    def add_component(self, transformer: Transformer):
        self.transformers.append(transformer)

    def get_all(self):
        return self.transformers