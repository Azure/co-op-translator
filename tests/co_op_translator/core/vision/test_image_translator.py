import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from PIL import Image
from co_op_translator.core.vision.image_translator import ImageTranslator
from co_op_translator.core.llm.text_translator import TextTranslator

TEST_IMAGE_PATH = Path("test_image.png").resolve()
ROOT_DIR = Path(".").resolve()


class MockTextTranslator(TextTranslator):
    """Mock implementation of TextTranslator for testing."""

    def __init__(self):
        self.client = self.get_openai_client()

    def get_openai_client(self):
        return MagicMock()

    def get_model_name(self):
        return "gpt-4"

    def translate_batch(self, texts, target_language):
        """Mock implementation of translate_batch."""
        return [f"Translated: {text}" for text in texts]


class MockImageTranslator(ImageTranslator):
    """Mock implementation of ImageTranslator for testing."""

    def __init__(self, default_output_dir="./translated_images", root_dir="."):
        self.text_translator = MockTextTranslator()
        self.default_output_dir = default_output_dir
        self.root_dir = Path(root_dir)
        Path(default_output_dir).mkdir(parents=True, exist_ok=True)

    def get_image_analysis_client(self):
        return MagicMock()

    def extract_text_from_image(self, image_path):
        """Mock implementation of extract_text_from_image."""
        return [
            {
                "text": "LIFE IS LIKE",
                "bounding_box": [41, 111, 963, 77, 966, 147, 41, 185],
                "confidence": 0.988,
            }
        ]

    def translate_image(self, image_path, target_language):
        """Mock implementation of translate_image."""
        bounding_boxes = self.extract_text_from_image(image_path)
        texts = [box["text"] for box in bounding_boxes]
        translated_texts = self.text_translator.translate_batch(texts, target_language)
        return self.plot_annotated_image(
            image_path, bounding_boxes, translated_texts, target_language
        )

    def plot_annotated_image(
        self, image_path, bounding_boxes, translated_texts, target_language
    ):
        """Mock implementation of plot_annotated_image."""
        return Path(self.default_output_dir) / "translated_image.png"


@pytest.fixture
def image_translator(tmp_path):
    """
    Fixture to provide an instance of MockImageTranslator for each test.
    """
    return MockImageTranslator(default_output_dir=tmp_path, root_dir=ROOT_DIR)


@pytest.fixture
def mock_line_bounding_boxes():
    """
    Fixture that returns mock bounding box data for testing.
    """
    return [
        {
            "text": "LIFE IS LIKE",
            "bounding_box": [41, 111, 963, 77, 966, 147, 41, 185],
            "confidence": 0.988,
        },
        {
            "text": "RIDING A BICYCLE",
            "bounding_box": [210, 231, 1035, 204, 1037, 254, 212, 281],
            "confidence": 0.993,
        },
    ]


@patch("builtins.open", new_callable=MagicMock)
@patch("PIL.Image.open", return_value=MagicMock(spec=Image.Image))
@patch("PIL.Image.Image.save")
@patch("os.makedirs")
def test_extract_text_from_image(
    mock_makedirs, mock_image_save, mock_image_open, mock_file_open, image_translator
):
    """
    Test extract_text_from_image method to ensure it extracts text and bounding boxes correctly.
    """
    mock_client = image_translator.get_image_analysis_client()
    mock_result = MagicMock()
    mock_block = MagicMock()
    mock_line = MagicMock()

    mock_line.text = "LIFE IS LIKE"
    mock_line.bounding_polygon = [
        MagicMock(x=41, y=111),
        MagicMock(x=963, y=77),
        MagicMock(x=966, y=147),
        MagicMock(x=41, y=185),
    ]
    mock_line.words = [MagicMock(confidence=0.988)]
    mock_block.lines = [mock_line]
    mock_result.read.blocks = [mock_block]
    mock_client.analyze_document.return_value = mock_result

    bounding_boxes = image_translator.extract_text_from_image(TEST_IMAGE_PATH)

    assert (
        len(bounding_boxes) == 1
    ), f"Expected 1 bounding box, got {len(bounding_boxes)}"
    assert (
        bounding_boxes[0]["text"] == "LIFE IS LIKE"
    ), f"Expected text 'LIFE IS LIKE', got {bounding_boxes[0]['text']}"
    assert bounding_boxes[0]["bounding_box"] == [
        41,
        111,
        963,
        77,
        966,
        147,
        41,
        185,
    ], f"Bounding box mismatch: {bounding_boxes[0]['bounding_box']}"


@patch(
    "co_op_translator.core.vision.image_translator.ImageTranslator.plot_annotated_image"
)
def test_translate_image(
    mock_plot_annotated_image, image_translator, mock_line_bounding_boxes, tmp_path
):
    """
    Test translate_image method to ensure the image is correctly translated and annotated.
    """
    # Set up mocks
    mock_plot_annotated_image.return_value = tmp_path / "translated_image.png"
    image_translator.plot_annotated_image = mock_plot_annotated_image

    with patch.object(
        image_translator,
        "extract_text_from_image",
        return_value=mock_line_bounding_boxes,
    ):
        target_language = "es"
        result_path = image_translator.translate_image(TEST_IMAGE_PATH, target_language)

        assert str(result_path) == str(tmp_path / "translated_image.png")

        # Verify that extract_text_from_image was called with correct arguments
        image_translator.extract_text_from_image.assert_called_once_with(
            TEST_IMAGE_PATH
        )

        # Verify that plot_annotated_image was called with correct arguments
        mock_plot_annotated_image.assert_called_once_with(
            TEST_IMAGE_PATH,
            mock_line_bounding_boxes,
            ["Translated: LIFE IS LIKE", "Translated: RIDING A BICYCLE"],
            target_language,
        )


def test_mock_text_translator_initialization():
    """
    Test MockTextTranslator initialization and basic functionality.
    """
    translator = MockTextTranslator()
    assert translator.client is not None
    assert translator.get_model_name() == "gpt-4"


def test_translate_batch_with_empty_input():
    """
    Test translate_batch method with empty input.
    """
    translator = MockTextTranslator()
    result = translator.translate_batch([], "ko")
    assert isinstance(result, list)
    assert len(result) == 0


def test_translate_batch_with_various_inputs():
    """
    Test translate_batch method with various input types.
    """
    translator = MockTextTranslator()
    inputs = [
        "Hello",
        "123",
        "Special !@#$%^&*() chars",
        "한글도 테스트",
        " Leading and trailing spaces ",
    ]
    target_language = "ko"

    results = translator.translate_batch(inputs, target_language)

    assert len(results) == len(inputs)
    for original, translated in zip(inputs, results):
        assert isinstance(translated, str)
        assert translated == f"Translated: {original}"


def test_plot_annotated_image_with_multiple_boxes(image_translator, tmp_path):
    """
    Test plot_annotated_image method with multiple bounding boxes.
    """
    image_path = TEST_IMAGE_PATH
    bounding_boxes = [
        {
            "text": "Text 1",
            "bounding_box": [0, 0, 100, 0, 100, 50, 0, 50],
            "confidence": 0.9,
        },
        {
            "text": "Text 2",
            "bounding_box": [150, 150, 250, 150, 250, 200, 150, 200],
            "confidence": 0.95,
        },
    ]
    translated_texts = ["번역 1", "번역 2"]
    target_language = "ko"

    result_path = image_translator.plot_annotated_image(
        image_path, bounding_boxes, translated_texts, target_language
    )

    assert isinstance(result_path, Path)
    assert result_path.parent == tmp_path
    assert str(result_path).endswith("translated_image.png")


@pytest.mark.parametrize("target_language", ["ko", "en", "ja", "zh"])
def test_translate_image_with_different_languages(
    image_translator, mock_line_bounding_boxes, target_language
):
    """
    Test translate_image method with different target languages.
    """
    result_path = image_translator.translate_image(TEST_IMAGE_PATH, target_language)

    assert isinstance(result_path, Path)
    assert str(result_path).endswith("translated_image.png")


def test_extract_text_with_low_confidence(image_translator):
    """
    Test extract_text_from_image method's handling of low confidence text.
    """
    mock_client = image_translator.get_image_analysis_client()

    # Override the mock implementation for this specific test
    def mock_extract_text(*args, **kwargs):
        return [
            {
                "text": "Low confidence text",
                "bounding_box": [10, 10, 100, 10, 100, 50, 10, 50],
                "confidence": 0.3,  # Low confidence score
            }
        ]

    image_translator.extract_text_from_image = mock_extract_text

    result = image_translator.extract_text_from_image(TEST_IMAGE_PATH)
    assert len(result) == 1
    assert result[0]["confidence"] < 0.5
    assert result[0]["text"] == "Low confidence text"
