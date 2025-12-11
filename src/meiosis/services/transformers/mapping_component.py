from ...Domain import ImageFrame, Entity, PILEntity, EntityInfo, map_name_to_id
from .transformer import Transformer

class MapTransformer(Transformer):
    """
    This transformer is related to assigning labels to image metadata.
    """

    def transform(self, image_store):
        """
        This method assigns labels to an image entity based on image name
        """
        for entity in image_store.images_collection:
            label_code = map_name_to_id(entity.meta_data.name)
            entity.meta_data.add_transformation("label", label_code)
        return image_store
