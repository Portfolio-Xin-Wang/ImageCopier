import os
from abc import ABC, abstractmethod

from ..Domain import Entity, PILEntity, ImageFrame
from .image_handler import ImageHandler


class Exporter(ABC):

    @abstractmethod
    def export(self) -> ImageFrame:
        pass

class LocalFileExporter(Exporter):
    """
    Exports images to an active service. 
    Alternative solution to local export.
    """
    image_copier: ImageHandler
    transformed_name: str
    OUTPUT_DIRECTORY: str

    def __init__(self, copier: ImageHandler, output_direction: str):
        self.image_copier = copier
        self.transformed_name = "{label_id}&{rotation};{file}.{extension}"
        self.OUTPUT_DIRECTORY = output_direction
        self._create_directory_if_not_exists(self.OUTPUT_DIRECTORY)

    def export(self) -> ImageFrame:
        images = self.image_copier.handle()
        for image in images.images_collection:
            self._export_to_local(image)
        return images

    def _format_output_file(self, entity: Entity) -> str:
        return f"./{self.OUTPUT_DIRECTORY}/{entity.meta_data.return_name()}"

    def _create_directory_if_not_exists(self, directory: str) -> str:
        if not os.path.exists(directory):
            os.makedirs(f"{directory}")
        return directory
    
    # Export function
    def _export_to_local(self, entity: PILEntity) -> None:
        output_name = self._format_output_file(entity)
        entity.image.save(output_name)