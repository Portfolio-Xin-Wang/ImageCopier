from ..services.meiosis_factory import ImageServiceFactory
from ..services.transformers import MapTransformer
from ..Domain import ImageFrame

class Export:

    image_service_factory: ImageServiceFactory

    def __init__(self):
        self.image_service_factory = ImageServiceFactory()

    def read_from_directory(self, original_dir="test_images", output_dir="output", copies=3, rotation_base=5, custom_mapper: MapTransformer=None) -> ImageFrame:
        exporter = self.image_service_factory.create_pil_image_copier(copies, rotation_base, original_dir, output_dir, custom_mapper)
        return exporter.export()
    
    