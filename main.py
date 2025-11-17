import os

from src import ImageCopier
# Lookup for image names

# If images are found, return names
names = os.listdir("./test_images")

copier = ImageCopier("./output/")

copier.basic_perform("./test_images", names, 20)

