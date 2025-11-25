from abc import ABC, abstractmethod
from ..Domain import ImageEntity

from .image_copier import ImageCopier

class ImageExporter(ABC):

    @abstractmethod
    def export(self, images: list[ImageEntity]) -> None:
        pass

class LocalImageExporter(ImageExporter):
    """
    Exports images to local file system.
    """
    OUTPUT_DIRECTORY: str

    def __init__(self, output_directory: str = "./exported/"):
        self.OUTPUT_DIRECTORY = output_directory


    def export(self, images: list[ImageEntity]) -> None:
        # Implementation for exporting images locally
        for image in images:
            print(f"Exporting image {image.meta_data.name} to local storage.")
        # Actual export logic would go here

class ActiveImageExporter(ImageExporter):
    """
    Exports images to an active service. 
    Alternative solution to local export.
    """
    SERVICE_ENDPOINT: str
    image_copier: ImageCopier

    def __init__(self, service_endpoint: str, copier: ImageCopier):
        self.SERVICE_ENDPOINT = service_endpoint
        self.image_copier = copier

    def export(self, images: list[ImageEntity]) -> None:
        # Implementation for exporting images to an active service
        for image in images:
            print(f"Exporting image {image.meta_data.name} to service at {self.SERVICE_ENDPOINT}.")
        # Actual export logic would go here