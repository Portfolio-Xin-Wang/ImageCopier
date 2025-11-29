from .transformer import Transformer

class CopyTransformer(Transformer):

    copies: int

    def __init__(self, copy: int):
        self.copies = copy

    def transform(self, image_store):
        entities = []
        for index in range(1, self.copies + 1):
            for entity in image_store.images_collection:
                copy = entity.deep_copy()
                copy.meta_data.add_transformation("copy", index)
                entities.append(copy)
        image_store.update(entities)
        return image_store