import os
import pytest
from unittest.mock import patch, MagicMock
from PIL import Image
from co_op_translator.utils.image_utils import (
    save_bounding_boxes,
    load_bounding_boxes,
    get_average_color,
    get_text_color,
    draw_text_on_image,
    create_filled_polygon_mask,
    get_image_mode,
)

# Mock data for testing
image_path = "tests/sample_image.jpg"
bounding_boxes = [
    {
        "bounding_box": [50, 50, 150, 50, 150, 150, 50, 150],
        "text": "Sample Text",
        "confidence": 0.98
    }
]

json_file_path = os.path.join("bounding_boxes", "sample_image.json")


@pytest.fixture
def setup_test_environment():
    """
    Fixture to set up the testing environment.
    Deletes created files after each test.
    """
    os.makedirs("./bounding_boxes", exist_ok=True)
    os.makedirs("./analyzed_images", exist_ok=True)
    yield
    # Cleanup
    if os.path.exists(json_file_path):
        os.remove(json_file_path)
    if os.path.exists("./bounding_boxes"):
        os.rmdir("./bounding_boxes")
    if os.path.exists("./analyzed_images"):
        os.rmdir("./analyzed_images")


@patch("builtins.open", new_callable=MagicMock)
@patch("os.path.exists", return_value=True)
@patch("json.dump")
def test_save_and_load_bounding_boxes(mock_json_dump, mock_exists, mock_open, setup_test_environment):
    """
    Test saving and loading bounding box data to/from a JSON file using mock.
    """
    save_bounding_boxes(image_path, bounding_boxes)

    # Normalize paths to make them platform-independent and consistent
    expected_path = os.path.normpath(os.path.join(".", json_file_path))
    # Get the actual path used in the open call
    actual_path = mock_open.call_args[0][0]
    actual_path = os.path.normpath(actual_path)

    # Assert that the open function was called with the expected path
    assert actual_path == expected_path, f"Expected open to be called with {expected_path}, got {actual_path}"

    # Ensure json.dump was called with correct arguments
    mock_json_dump.assert_called_once()
    args, kwargs = mock_json_dump.call_args
    assert args[0] == bounding_boxes, "json.dump called with incorrect data."

    # Test loading bounding boxes
    mock_open.reset_mock()
    mock_exists.reset_mock()
    with patch("json.load", return_value=bounding_boxes):
        loaded_data = load_bounding_boxes(json_file_path)
        assert loaded_data == bounding_boxes, "Loaded bounding box data does not match original data."


def test_get_average_color():
    """
    Test calculating the average color of an image's bounding box area.
    """
    # Create a simple image for testing
    img = Image.new("RGB", (200, 200), color=(0, 0, 255))  # Blue image
    bounding_box = [50, 50, 150, 50, 150, 150, 50, 150]

    avg_color = get_average_color(img, bounding_box)

    # Check that the average color is blue
    assert avg_color == (0, 0, 255), f"Expected (0, 0, 255), got {avg_color}"


def test_get_text_color():
    """
    Test calculating text color based on background luminance.
    """
    # Test with dark background color (should return white text)
    bg_color = (0, 0, 50)  # Dark blue
    text_color = get_text_color(bg_color)
    assert text_color == (255, 255, 255), f"Expected (255, 255, 255), got {text_color}"

    # Test with light background color (should return black text)
    bg_color = (200, 200, 255)  # Light blue
    text_color = get_text_color(bg_color)
    assert text_color == (0, 0, 0), f"Expected (0, 0, 0), got {text_color}"

@patch("PIL.ImageFont.truetype")
@patch("PIL.ImageDraw.Draw")
@patch("PIL.Image.new")
def test_draw_text_on_image(mock_image_new, mock_image_draw, mock_truetype):
    """
    Test drawing text onto an image with a transparent background using mock.
    """
    font_mock = MagicMock()
    mock_truetype.return_value = font_mock
    font_mock.getbbox.return_value = [0, 0, 100, 30]

    text_image_mock = MagicMock()
    mock_image_new.return_value = text_image_mock

    draw_mock = MagicMock()
    mock_image_draw.return_value = draw_mock

    text_image = draw_text_on_image("Test Text", font_mock, (0, 0, 0))

    # Assert that the image mode is RGBA
    mock_image_new.assert_called_once_with('RGBA', (100, 30), (255, 255, 255, 0))
    assert text_image == text_image_mock, "Returned image does not match expected image."

    # Assert that text was drawn on the image
    draw_mock.text.assert_called_once_with((0, 0), "Test Text", font=font_mock, fill=(0, 0, 0))


@patch("PIL.Image.new")
@patch("PIL.ImageDraw.Draw")
def test_create_filled_polygon_mask(mock_image_draw, mock_image_new):
    """
    Test creating a filled polygon mask for a bounding box area using mock.
    """
    bounding_box = [50, 50, 150, 50, 150, 150, 50, 150]
    mask_image_mock = MagicMock()
    mock_image_new.return_value = mask_image_mock

    draw_mock = MagicMock()
    mock_image_draw.return_value = draw_mock

    mask_image = create_filled_polygon_mask(bounding_box, (200, 200), (255, 0, 0, 255))

    # Assert the size and mode of the image
    mock_image_new.assert_called_once_with('RGBA', (200, 200), (255, 255, 255, 0))
    assert mask_image == mask_image_mock, "Returned mask image does not match expected image."

    # Assert that the polygon function was called with the bounding box
    expected_points = [(50, 50), (150, 50), (150, 150), (50, 150)]
    draw_mock.polygon.assert_called_once_with(expected_points, fill=(255, 0, 0, 255))


def test_get_image_mode():
    """
    Test determining the appropriate image mode based on the file extension.
    """
    jpg_image_path = "sample.jpg"
    png_image_path = "sample.png"

    assert get_image_mode(jpg_image_path) == 'RGB', "Expected 'RGB' for JPG images."
    assert get_image_mode(png_image_path) == 'RGBA', "Expected 'RGBA' for PNG images."

    with pytest.raises(ValueError):
        get_image_mode("sample.bmp")
