from numpy import ndarray, stack, reshape

from .entity import Entity


class ImageFrame:
    """
    An in memory data struture for storing images.
    """
    images_collection: list[Entity] = []
    length: int = 0

    def __init__(self, images: list[Entity]):
        self.images_collection = images
        self.length = len(images)

    def add(self, image: Entity) -> None:
        self.images_collection.append(image)

    def update(self, new_images: list[Entity]):
        self.images_collection = new_images
        self.length = len(self.images_collection)
    
    def get_all(self) -> list[Entity]:
        return self.images_collection
    
    def clear(self) -> None:
        self.images_collection = []

    def image_to_numpy(self) -> ndarray:
        n = [entity.image_to_numpy() for entity in self.get_all()]
        # Temporarely solution for inconsistent images
        standard = n[0].shape
        r = [input.reshape(standard) for input in n]
        return stack(r)
    
    def metadata_to_numpy(self) -> ndarray:
        return stack([entity.metadata_to_numpy() for entity in self.get_all()])
