from .transformer import Transformer
from ...Domain import ImageFrame

class ImageTransformer(Transformer):

    transformers: list[Transformer]
    starting_transformer: Transformer

    def transform(self, image_store):
        updated_image_store: ImageFrame = image_store
        for transformer in self.transformers:
            updated_image_store = transformer.transform(image_store=image_store)
        return updated_image_store
    
    def add_component(self, transformer: Transformer):
        self.transformers.append(transformer)

    def get_all(self):
        return self.transformers