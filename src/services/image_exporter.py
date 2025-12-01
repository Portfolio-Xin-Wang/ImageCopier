import os
import traceback

from abc import ABC, abstractmethod
from ..Domain import ImageEntity, PILImageEntity

from .image_copier import ImageCopier

class ImageExporter(ABC):

    @abstractmethod
    def export(self) -> None:
        pass

class LocalImageExporter(ImageExporter):
    """
    Exports images to an active service. 
    Alternative solution to local export.
    """
    image_copier: ImageCopier
    transformed_name: str
    OUTPUT_DIRECTORY: str

    def __init__(self, copier: ImageCopier, output_direction: str):
        self.image_copier = copier
        self.transformed_name = "{label_id}&{rotation};{file}.{extension}"
        self.OUTPUT_DIRECTORY = output_direction

    def export(self) -> list[ImageEntity]:
        # Implementation for exporting images to an active service

        images = self.image_copier.basic_perform(9)
        print(f"Files to be copied {len(images)}")
        for image in images:
            self._copy_image(image)
        # Actual export logic would go here
        return images

    def _format_output_file(self, entity: ImageEntity) -> str:
        return f"./{self.OUTPUT_DIRECTORY}/{entity.meta_data.return_name()}"

    def _create_directory_if_not_exists(self, directory: str) -> str:
        if not os.path.exists(directory):
            print(f"Created directory: {directory}")
            os.makedirs(f"{self.OUTPUT_DIRECTORY}{directory}")
            return directory
        return directory
    
    # Export function
    def _copy_image(self, entity: PILImageEntity) -> None:
        try:
            output_name = self._format_output_file(entity)
            # output
            entity.image.save(output_name)
        except:
            traceback.print_exc()
            raise