import os
import pytest
from unittest.mock import patch, MagicMock
from PIL import Image
from co_op_translator.utils.vision.image_utils import (
    save_bounding_boxes,
    load_bounding_boxes,
    get_average_color,
    get_text_color,
    draw_text_on_image,
    create_filled_polygon_mask,
    get_image_mode,
)


@pytest.fixture
def setup_test_environment(tmp_path):
    """
    Fixture to set up the testing environment with temporary directory.
    """
    bounding_boxes_dir = tmp_path / "bounding_boxes"
    analyzed_images_dir = tmp_path / "analyzed_images"
    bounding_boxes_dir.mkdir()
    analyzed_images_dir.mkdir()
    return tmp_path


def test_get_average_color():
    """
    Test calculating the average color of an image's bounding box area.
    """
    img = Image.new("RGB", (200, 200), color=(0, 0, 255))  # Blue image
    bounding_box = [50, 50, 150, 50, 150, 150, 50, 150]
    avg_color = get_average_color(img, bounding_box)
    assert avg_color == (0, 0, 255), f"Expected (0, 0, 255), got {avg_color}"


def test_get_text_color():
    """
    Test calculating text color based on background luminance.
    """
    # Test dark background
    bg_color = (0, 0, 50)  # Dark blue
    text_color = get_text_color(bg_color)
    assert text_color == (255, 255, 255), f"Expected white text for dark background"

    # Test light background
    bg_color = (200, 200, 255)  # Light blue
    text_color = get_text_color(bg_color)
    assert text_color == (0, 0, 0), f"Expected black text for light background"


@patch("PIL.ImageFont.truetype")
@patch("PIL.ImageDraw.Draw")
@patch("PIL.Image.new")
def test_draw_text_on_image(mock_image_new, mock_image_draw, mock_truetype):
    """
    Test drawing text onto an image with a transparent background.
    """
    font_mock = MagicMock()
    mock_truetype.return_value = font_mock
    font_mock.getbbox.return_value = [0, 0, 100, 30]

    text_image_mock = MagicMock()
    mock_image_new.return_value = text_image_mock
    draw_mock = MagicMock()
    mock_image_draw.return_value = draw_mock

    text_image = draw_text_on_image("Test Text", font_mock, (0, 0, 0))

    mock_image_new.assert_called_once_with("RGBA", (100, 30), (255, 255, 255, 0))
    assert text_image == text_image_mock
    draw_mock.text.assert_called_once_with(
        (0, 0), "Test Text", font=font_mock, fill=(0, 0, 0)
    )


@patch("PIL.Image.new")
@patch("PIL.ImageDraw.Draw")
def test_create_filled_polygon_mask(mock_image_draw, mock_image_new):
    """
    Test creating a filled polygon mask for a bounding box area.
    """
    bounding_box = [50, 50, 150, 50, 150, 150, 50, 150]
    mask_image_mock = MagicMock()
    mock_image_new.return_value = mask_image_mock
    draw_mock = MagicMock()
    mock_image_draw.return_value = draw_mock

    mask_image = create_filled_polygon_mask(bounding_box, (200, 200), (255, 0, 0, 255))

    mock_image_new.assert_called_once_with("RGBA", (200, 200), (255, 255, 255, 0))
    assert mask_image == mask_image_mock
    expected_points = [(50, 50), (150, 50), (150, 150), (50, 150)]
    draw_mock.polygon.assert_called_once_with(expected_points, fill=(255, 0, 0, 255))


def test_get_image_mode():
    """
    Test determining the appropriate image mode based on the file extension.
    """
    assert get_image_mode("test.jpg") == "RGB"
    assert get_image_mode("test.jpeg") == "RGB"
    assert get_image_mode("test.png") == "RGBA"

    with pytest.raises(ValueError):
        get_image_mode("test.bmp")
