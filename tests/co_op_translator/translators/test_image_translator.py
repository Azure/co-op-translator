import pytest
from unittest.mock import patch, MagicMock
from co_op_translator.translators.image_translator import ImageTranslator
from pathlib import Path
from PIL import Image

TEST_IMAGE_PATH = Path("test_image.png").resolve()
ROOT_DIR = Path(".").resolve()

@pytest.fixture
def image_translator():
    """
    Fixture to provide an instance of ImageTranslator for each test.
    """
    return ImageTranslator(default_output_dir="./test_translated_images", root_dir=ROOT_DIR)

@pytest.fixture
def mock_line_bounding_boxes():
    """
    Fixture that returns mock bounding box data for testing.
    """
    return [
        {
            "text": "LIFE IS LIKE",
            "bounding_box": [41, 111, 963, 77, 966, 147, 41, 185],
            "confidence": 0.988
        },
        {
            "text": "RIDING A BICYCLE",
            "bounding_box": [210, 231, 1035, 204, 1037, 254, 212, 281],
            "confidence": 0.993
        },
        {
            "text": "TO",
            "bounding_box": [120, 377, 219, 373, 220, 422, 121, 426],
            "confidence": 0.954
        },
        {
            "text": "KEEP YOUR BALANCE",
            "bounding_box": [244, 365, 1136, 318, 1139, 373, 247, 423],
            "confidence": 0.989
        },
        {
            "text": "YOU MUST KEEP MOVING",
            "bounding_box": [171, 473, 1211, 516, 1208, 573, 168, 531],
            "confidence": 0.998
        }
    ]

# Test the extract_line_bounding_boxes method
@patch('builtins.open', new_callable=MagicMock)
@patch('PIL.Image.open', return_value=MagicMock(spec=Image.Image))
@patch('PIL.Image.Image.save')
@patch('co_op_translator.translators.image_translator.ImageTranslator.get_image_analysis_client')
def test_extract_line_bounding_boxes(mock_get_image_analysis_client, mock_image_save, mock_image_open, mock_file_open, image_translator):
    """
    Test extract_line_bounding_boxes method to ensure it extracts text and bounding boxes correctly.
    """
    # Mock Azure Image Analysis Client response
    mock_client = MagicMock()
    mock_result = MagicMock()
    mock_block = MagicMock()
    mock_line = MagicMock()

    mock_line.text = "LIFE IS LIKE"
    mock_line.bounding_polygon = [
        MagicMock(x=41, y=111),
        MagicMock(x=963, y=77),
        MagicMock(x=966, y=147),
        MagicMock(x=41, y=185)
    ]
    mock_line.words = [MagicMock(confidence=0.988)]
    mock_block.lines = [mock_line]
    mock_result.read.blocks = [mock_block]
    mock_client.analyze.return_value = mock_result
    mock_get_image_analysis_client.return_value = mock_client

    bounding_boxes = image_translator.extract_line_bounding_boxes(TEST_IMAGE_PATH)

    assert len(bounding_boxes) == 1
    assert bounding_boxes[0]['text'] == "LIFE IS LIKE"
    assert bounding_boxes[0]['bounding_box'] == [41, 111, 963, 77, 966, 147, 41, 185]

# Test the translate_image method
@patch('co_op_translator.translators.image_translator.ImageTranslator.plot_annotated_image')
@patch('co_op_translator.translators.image_translator.TextTranslator.translate_image_text')
@patch('co_op_translator.translators.image_translator.ImageTranslator.extract_line_bounding_boxes')
def test_translate_image(mock_extract_boxes, mock_translate_text, mock_plot_annotated_image, image_translator, mock_line_bounding_boxes):
    """
    Test translate_image method to ensure the image is correctly translated and annotated.
    """
    # Mock bounding box extraction and translation process
    mock_extract_boxes.return_value = mock_line_bounding_boxes
    mock_translate_text.return_value = [
        'LA VIDA ES COMO',
        'ANDAR EN BICICLETA',
        'PARA',
        'MANTENER EL EQUILIBRIO',
        'DEBES SEGUIR MOVIÉNDOTE'
    ]
    mock_plot_annotated_image.return_value = "./test_translated_images/translated_image.png"

    target_language = "es"

    result_path = image_translator.translate_image(TEST_IMAGE_PATH, target_language)

    assert result_path == "./test_translated_images/translated_image.png"
    mock_extract_boxes.assert_called_once_with(TEST_IMAGE_PATH)
    mock_translate_text.assert_called_once_with(
        ['LIFE IS LIKE', 'RIDING A BICYCLE', 'TO', 'KEEP YOUR BALANCE', 'YOU MUST KEEP MOVING'], 
        'Spanish'
    )
    mock_plot_annotated_image.assert_called_once()
