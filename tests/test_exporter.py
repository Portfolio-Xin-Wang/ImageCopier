import os

from src.meiosis import ImageHandler, LocalFileExporter, LocalFileStorage
    

def test_if_localfile_exporter_exports_images_correctly():
    repository = LocalFileStorage("tests/test_images/retrieval")
    handler = ImageHandler(image_repo=repository)
    exporter = LocalFileExporter(handler, "tests/test_images/exporter")
    results = exporter.export()

    file_names = os.listdir("tests/test_images/exporter")
    assert len(file_names) == 2
    assert results.length == 2


def test_if_localfile_exporter_exports_images_to_non_existent_directory():
    repository = LocalFileStorage("tests/test_images/retrieval")
    handler = ImageHandler(image_repo=repository)
    exporter = LocalFileExporter(handler, "tests/test_images/new_exporter")
    results = exporter.export()

    file_names = os.listdir("tests/test_images/new_exporter")
    assert len(file_names) == 2
    assert results.length == 2

