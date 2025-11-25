from .image_entity import ImageEntity

class ImageStore:
    """
    An in memory data struture for storing images.
    """
    images: list[ImageEntity] = []

    def __init__(self):
        self.images = []

    def add(self, image: ImageEntity) -> None:
        self.images.append(image)
    
    def get_all(self) -> list[ImageEntity]:
        return self.images
    
    def clear(self) -> None:
        self.images = []
