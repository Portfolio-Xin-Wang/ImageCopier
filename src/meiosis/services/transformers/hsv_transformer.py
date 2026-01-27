from ...domain import PILEntity
from .transformer import Transformer


class HSVTransformer(Transformer):
    def __init__(self):
        super().__init__()

    def transform(self, image_store):
        for image in image_store.images_collection:
            image: PILEntity
            hsv = image.image.convert("HSV")
            img_rgb = hsv.convert("RGB")
            image.image = img_rgb
            image.meta_data.add_transformation("hsv", "hsv_converted")
        return image_store