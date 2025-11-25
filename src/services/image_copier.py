import os
import traceback

from PIL import Image
from .Image_repository import ImageRepository
from ..Domain import ImageMetadata, ImageEntity, PILImageEntity

class ImageCopier:
    """
    Main entry point for image copier.
    """
    output_direction: str
    transformed_name: str
    image_repository: ImageRepository
    _angle: int

    def __init__(self, image_repo: ImageRepository, output_direction: str = "./output/") -> None:
        self.output_direction = output_direction
        self.transformed_name = "{label_id}&{rotation};{file}.{extension}"
        self._angle = 0
        self.image_repository = image_repo

    def basic_perform(self, directory, copies: int):
        """
        This is the basic class that looks up images and makes a copy of them like image_1|rot-5.jpg
        """
        # Currently extracting a concrete type. Later this responsibility will be moved to a transformer class
        images: list[PILImageEntity] = self.image_repository.get()
        # Export function: format metadata
        transformed_images: list[PILImageEntity] = []

        for entity in images:
            for i in range(copies):
                new_angle = self._apply_rotation(copies)
                format_out = self._format_output_file(entity, new_angle)
                processed_image: Image = entity.image.rotate(new_angle)
                # Export function
                output_file_name = f"{directory}/{format_out}"
                self._copy_image(processed_image, output_file_name)
                # Export function: format metadata
                new_entity = entity.deep_copy()
                new_entity.meta_data = ImageMetadata(entity.meta_data.label_id, format_out, directory)
                transformed_images.append(new_entity)
        return transformed_images

    # Export function
    @staticmethod
    def _copy_image(image: Image, output_name: str) -> None:
        try:
            # output
            image.save(output_name)
            return True
        except:
            traceback.print_exc()
            return False

    def _format_output_file(self, entity: ImageEntity, angle: int) -> str:
        return self.transformed_name.format(label_id=entity.meta_data.label_id, file=entity.return_image_name(), rotation=angle,
                                            extension="jpg")

    def _apply_rotation(self, number: int) -> int:
        angle = 360 / (number + 1)
        self._angle += angle
        if self._angle > 360:
            self._reset()
        return self._angle

    def _create_directory_if_not_exists(self, directory: str) -> str:
        if not os.path.exists(directory):
            print(f"Created directory: {directory}")
            os.makedirs(f"{self.output_direction}{directory}")
            return directory
        return directory

    def _reset(self):
        self._angle = 0
