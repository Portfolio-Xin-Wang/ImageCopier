from .image_entity import ImageEntity

class ImageFrame:
    """
    An in memory data struture for storing images.
    """
    images_collection: list[ImageEntity] = []

    def __init__(self, images: list[ImageEntity] = None):
        self.images_collection = images

    def add(self, image: ImageEntity) -> None:
        self.images_collection.append(image)

    def update(self, new_images: list[ImageEntity]):
        self.images_collection = new_images
    
    def get_all(self) -> list[ImageEntity]:
        return self.images_collection
    
    def clear(self) -> None:
        self.images_collection = []
