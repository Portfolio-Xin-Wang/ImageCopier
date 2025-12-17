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
    expected_result = "cat1"
    expected_location = "/cat1"
    assert False

# Test if import of image2 in cat1/cat3 has the exact location, but assigns target directory cat3
def test_import_image_in_directory_cat3():
    expected_result = "cat3"
    expected_location = "/cat1/cat3"
    assert False

# Test if import of image4 in root has assigns target directory _
def test_import_image_in_directory_root():
    expected_result = ""
    expected_location = ""
    assert False

def test_import_image_in_directory_returns_four_entities():
    expected_result = 4
    expected_directories = ["cat1", "cat3", "cat2", ""]
    assert False