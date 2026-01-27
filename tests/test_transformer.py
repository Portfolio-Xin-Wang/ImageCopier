from PIL import Image

from src.meiosis.domain import EntityInfo, ImageFrame, PILEntity
from src.meiosis.services.transformers import (CopyTransformer,
                                               ImageTransformer,
                                               PILImageBuilder,
                                               RotatorTransformer, Transformer)


def test():
    assert (2 + 2) == (6 - 2)

def test_empty_composite_transofrmer():
    builder = PILImageBuilder()
    
    composite: ImageTransformer = builder.reset().build()

    assert composite is not None
    assert len(composite.transformers) == 0

def test_two_transformers_in_composite():
    builder = PILImageBuilder()
    
    composite: ImageTransformer = builder.reset().add_rotation(45).add_copies(3).build()

    assert composite is not None
    assert len(composite.transformers) == 2
    assert isinstance(composite.transformers[0], RotatorTransformer)
    assert isinstance(composite.transformers[1], Transformer)

def test_copy_transformer_creates_4_copies_with_unique_names():
    # Arrange
    test_image = Image.open("tests/images/transform/test_copy_image1.jpg")
    composite: CopyTransformer = CopyTransformer(4)
    image_entity = PILEntity(test_image, EntityInfo(name="test_copy_image1.jpg", location="test_images/", target_director=""))
    existing_image_store = ImageFrame(images=[image_entity])
    # Act
    end_result: ImageFrame = composite.transform(existing_image_store)
    
    # Assert
    assert 4 == len(end_result.images_collection)
    assert 1 == end_result.images_collection[0].meta_data._applied_transformation["copy"]
    assert 2 == end_result.images_collection[1].meta_data._applied_transformation["copy"]
    assert 3 == end_result.images_collection[2].meta_data._applied_transformation["copy"]
    assert 4 == end_result.images_collection[3].meta_data._applied_transformation["copy"]

def test_rotator_transformer_rotates_image():
    # Arrange
    test_image = Image.open("tests/images/transform/test_rotator_image1.jpg")
    composite: ImageTransformer = PILImageBuilder().reset().add_copies(2).add_rotation(2).build()
    image_entity = PILEntity(test_image, EntityInfo(name="test_rotation_image1.jpg", location="test_images/", target_director=""))
    existing_image_store = ImageFrame(images=[image_entity])
    # Act
    end_result: ImageFrame = composite.transform(existing_image_store)
    
    # Assert
    assert 2 == len(end_result.images_collection)
    assert end_result.images_collection[0].meta_data._applied_transformation["rot"] is not None
    assert end_result.images_collection[1].meta_data._applied_transformation["rot"] is not None

def test_return_name_post_transformations_format():
    # Arrange
    test_image = Image.open("tests/images/transform/test_rotator_image1.jpg")
    composite: ImageTransformer = PILImageBuilder().reset().add_copies(2).add_rotation(2).build()
    image_entity = PILEntity(test_image, EntityInfo(name="test_rotation_image1.jpg", location="test_images/", target_director=""))
    existing_image_store = ImageFrame(images=[image_entity])
    # Act
    end_result: ImageFrame = composite.transform(existing_image_store)
    
    # Assert
    splitted1 = end_result.images_collection[0].return_image_name().split("&")
    splitted2 = end_result.images_collection[1].return_image_name().split("&")

    assert '1' == splitted1[0].split(";")[0]
    assert '2' == splitted2[0].split(";")[0]
    assert "copy" == splitted1[0].split(";")[1]
    assert "copy" == splitted2[0].split(";")[1]
    assert "rot" == splitted1[1].split(";")[1]
    assert "rot" == splitted2[1].split(";")[1]