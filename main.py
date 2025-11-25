from src import ImageCopier, LocalFileStorage
# If images are found, return names
repo = LocalFileStorage(image_directory="test_images")
copier = ImageCopier(image_repo=repo)

collection = copier.basic_perform("output", 4)
mapi = {"entity.py": 1}
test = "./image/entity.py"

print(mapi.get(test, 0))

print(len(collection))
print(collection)

