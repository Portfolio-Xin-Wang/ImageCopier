from PIL import Image
from .Image_repository import ImageRepository
from ..Domain import PILImageEntity

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

    def basic_perform(self, copies: int = 2) -> list[PILImageEntity]:
        """
        This is the basic class that looks up images and makes a copy of them like image_1|rot-5.jpg
        """
        # Currently extracting a concrete type. Later this responsibility will be moved to a transformer class
        images: list[PILImageEntity] = self.image_repository.get()
        # Export function: format metadata
        transformed_images: list[PILImageEntity] = []

        for entity in images:
            # This implemenation should be redundant if transformer class is implemented
            for i in range(copies):
                new_entity = entity.deep_copy()
                new_angle = self._apply_rotation(copies)
                # Transformation function: Should be reformatted into own transformer class
                new_entity.meta_data.add_transformation("copy", i)
                new_entity.meta_data.add_transformation("rot", new_angle)
                processed_image: Image = entity.image.rotate(new_angle)
                # Transformation function: format metadata
                new_entity.image = processed_image
                transformed_images.append(new_entity)
        return transformed_images

    def _apply_rotation(self, number: int) -> int:
        angle = 360 / (number + 1)
        self._angle += angle
        if self._angle > 360:
            self._reset()
        return self._angle

    def _reset(self):
        self._angle = 0
