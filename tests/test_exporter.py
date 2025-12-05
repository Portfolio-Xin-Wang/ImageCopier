import os
import shutil

import pytest

from src.meiosis import (Export, ImageHandler, LocalFileExporter,
                         LocalFileStorage, ImageTransformer)

IMPORT_LOCAL_FOLDER = "tests/images/retrieval"
EXPORT_TEST_FOLDER = "tests/images/new_exporter"
EXPORT_EXISTING_FOLDER = "tests/images/exporter"

@pytest.fixture
def clear():
    shutil.rmtree(EXPORT_TEST_FOLDER)

def test_if_localfile_exporter_exports_images_correctly():
    repository = LocalFileStorage(IMPORT_LOCAL_FOLDER)
    trans = ImageTransformer()
    handler = ImageHandler(image_repo=repository, transformers=trans)
    exporter = LocalFileExporter(handler, EXPORT_EXISTING_FOLDER)
    results = exporter.export()

    file_names = os.listdir(EXPORT_EXISTING_FOLDER)
    assert len(file_names) == 2
    assert results.length == 2


def test_if_localfile_exporter_exports_images_to_non_existent_directory(clear):
    export_api = Export()
    results = export_api.read_from_directory(original_dir=IMPORT_LOCAL_FOLDER, output_dir=EXPORT_TEST_FOLDER, copies=2, rotation_base=15)

    file_names = os.listdir(EXPORT_TEST_FOLDER)
    assert len(file_names) == 4
    assert results.length == 4


 

