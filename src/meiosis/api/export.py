from ..services.image_copy_factory import ImageServiceFactory

class Export:

    image_service_factory: ImageServiceFactory

    def __init__(self):
        self.image_service_factory = ImageServiceFactory()

    def read_from_directory(self, original_dir="test_images", output_dir="output", copies=3, rotation_base=5) -> list:
        exporter = self.image_service_factory.create_pil_image_copier(copies, rotation_base, original_dir, output_dir)
        return exporter.export()