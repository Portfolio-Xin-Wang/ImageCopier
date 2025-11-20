from src import ImageCopier, LocalFileStorage

# If images are found, return names
repo = LocalFileStorage(image_directory="test_images")
copier = ImageCopier(image_repo=repo)

copier.basic_perform("output", 1)
mapi = {"entity.py": 1}
test = "./image/entity.py"

print(mapi.get(test, 0))

