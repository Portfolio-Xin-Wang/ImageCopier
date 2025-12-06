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