from .transformer import Transformer
from ...Domain import PILEntity
class CopyTransformer(Transformer):

    copies: int

    def __init__(self, copy: int):
        self.copies = copy

    def transform(self, image_store):
        # TODO: Open for improvement like memory performance
        entities = []
        for entity in image_store.images_collection:
            entities += self._copy(entity)
        image_store.update(entities)
        return image_store
    
    def _copy(self, entity: PILEntity) -> PILEntity:
        entities = []
        for index in range(1, self.copies + 1):
            copy = entity.deep_copy()
            copy.meta_data.add_transformation("copy", index)
            entities.append(copy)
        return entities