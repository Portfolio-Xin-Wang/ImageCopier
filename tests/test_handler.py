from pytest import raises

from src.meiosis import ImageHandler, LocalFileStorage, ImageTransformer

def test_failed_retrieval_raises_exception():
    with raises(Exception):
        local_storage = LocalFileStorage("tests/images/non_existent")
        handler = ImageHandler(local_storage, transformers=ImageTransformer())
        handler.handle()

def test_handler_retrieves_data_correctly():
    local_storage = LocalFileStorage("tests/images/retrieval")
    handler = ImageHandler(image_repo=local_storage, transformers=ImageTransformer())
    result = handler.handle()
    assert result.length == 2