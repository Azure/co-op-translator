import os
from pathlib import Path
import subprocess
import sys

import pytest
from unittest.mock import patch, MagicMock
from PIL import Image
from co_op_translator.utils.vision.image_utils import (
    _create_image_comparison,
    display_image,
    get_average_color,
    get_text_color,
    draw_text_on_image,
    create_filled_polygon_mask,
    get_image_mode,
)

REPOSITORY_ROOT = Path(__file__).resolve().parents[4]


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
    assert text_color == (255, 255, 255), "Expected white text for dark background"

    # Test light background
    bg_color = (200, 200, 255)  # Light blue
    text_color = get_text_color(bg_color)
    assert text_color == (0, 0, 0), "Expected black text for light background"


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

    mock_image_new.assert_called_once()
    args, kwargs = mock_image_new.call_args
    assert args[0] == "RGBA"
    width, height = args[1]
    assert width >= 100
    assert height > 0
    assert args[2] == (255, 255, 255, 0)

    assert text_image == text_image_mock

    draw_mock.text.assert_called_once()
    (position, text_arg), text_kwargs = draw_mock.text.call_args
    assert position[0] >= 0 and position[1] >= 0
    assert text_arg == "Test Text"
    assert text_kwargs["font"] == font_mock
    assert text_kwargs["fill"] == (0, 0, 0)


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


@patch("PIL.ImageShow.show")
def test_display_image_uses_the_pillow_viewer(mock_show, tmp_path):
    original_path = tmp_path / "original.png"
    annotated_path = tmp_path / "annotated.png"
    Image.new("RGB", (20, 10), "blue").save(original_path)
    Image.new("RGB", (10, 20), "red").save(annotated_path)

    display_image(original_path, annotated_path)

    mock_show.assert_called_once()
    comparison = mock_show.call_args.args[0]
    assert comparison.width > 30
    assert comparison.height == 52
    assert mock_show.call_args.args[1] == "Image comparison"


@pytest.mark.parametrize("mode", ["RGBA", "P"])
def test_image_comparison_flattens_transparency_onto_white(mode):
    if mode == "RGBA":
        transparent = Image.new("RGBA", (200, 1), (255, 0, 0, 0))
    else:
        transparent = Image.new("P", (200, 1), 0)
        transparent.putpalette([255, 0, 0] + [0, 0, 0] * 255)
        transparent.info["transparency"] = 0

    comparison = _create_image_comparison(
        transparent,
        Image.new("RGB", (200, 1), "black"),
        "Transparent",
        "Opaque",
    )

    assert comparison.getpixel((0, 32)) == (255, 255, 255)


def test_image_comparison_reserves_space_for_both_titles():
    comparison = _create_image_comparison(
        Image.new("RGB", (1, 1), "red"),
        Image.new("RGB", (1, 1), "blue"),
        "Annotated Image with Translated Text",
        "Original Image",
    )

    assert comparison.width > 200


def test_image_utils_does_not_require_matplotlib():
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(REPOSITORY_ROOT / "src")
    probe = """
import builtins

original_import = builtins.__import__

def reject_matplotlib(name, *args, **kwargs):
    if name == "matplotlib" or name.startswith("matplotlib."):
        raise ModuleNotFoundError("matplotlib is intentionally unavailable")
    return original_import(name, *args, **kwargs)

builtins.__import__ = reject_matplotlib
import co_op_translator.utils.vision.image_utils
"""

    result = subprocess.run(
        [sys.executable, "-c", probe],
        cwd=REPOSITORY_ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
