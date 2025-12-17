from pytest import raises
from src.meiosis import LocalFileStorage, BreadMapper, Mapper

def test_if_entities_return_only_images():
    new_mapper = Mapper()
    repo = LocalFileStorage("tests/images/retrieval", new_mapper)
    image_frame = repo.get()
    assert image_frame.length == 2

def test_if_error_is_raised_on_invalid_datasource():
    with raises(Exception):
        LocalFileStorage("tests/images/non_existent")

# Test if import of image1 in cat1 one, assigns target directory cat1
def test_import_image_in_directory_cat1():
    # Arrange
    expected_result = "cat1"
    expected_location = "/cat1/kof1.jpg"
    directory = "tests/images/import_new"
    new_mapper = Mapper()
    repo = LocalFileStorage(directory, new_mapper)
    # Act
    images = repo.get()
    # Assert
    meta_data = images.images_collection[1].meta_data
    assert meta_data.name == "kof1.jpg"
    assert meta_data.location == expected_location
    assert meta_data.target_director == expected_result

# Test if import of image2 in cat1/cat3 has the exact location, but assigns target directory cat3
def test_import_image_in_directory_cat3():
    expected_result = "cat3"
    expected_location = "/cat1/cat3/crois.jpg"
    directory = "tests/images/import_new"
    new_mapper = Mapper()
    repo = LocalFileStorage(directory, new_mapper)
    # Act
    images = repo.get()
    # Assert
    meta_data = images.images_collection[0].meta_data
    assert meta_data.name == "crois.jpg"
    assert meta_data.location == expected_location
    assert meta_data.target_director == expected_result

# Test if import of image4 in root has assigns target directory _
def test_import_image_in_directory_root():
    expected_result = ""
    expected_location = "/crois2.jpg"
    directory = "tests/images/import_new"
    new_mapper = Mapper()
    repo = LocalFileStorage(directory, new_mapper)
    # Act
    images = repo.get()
    # Assert
    meta_data = images.images_collection[3].meta_data
    assert meta_data.name == "crois2.jpg"
    assert meta_data.location == expected_location
    assert meta_data.target_director == expected_result

def test_import_image_in_directory_returns_four_entities():
    expected_result = 4
    expected_directories = ["cat3", "cat1", "cat2", ""]
    directory = "tests/images/import_new"
    new_mapper = Mapper()
    repo = LocalFileStorage(directory, new_mapper)
    # Act
    images = repo.get()
    names = [n.meta_data.target_director for n in images.images_collection]
    assert len(names)
    assert names == expected_directories
    