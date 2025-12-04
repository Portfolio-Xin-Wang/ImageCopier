from pytest import raises
from src.meiosis import LocalFileStorage

def test_if_entities_return_only_images():
    repo = LocalFileStorage("tests/test_images/retrieval")
    image_frame = repo.get()
    assert image_frame.length == 2

def test_if_error_is_raised_on_invalid_datasource():
    with raises(Exception):
        LocalFileStorage("tests/test_images/non_existent")