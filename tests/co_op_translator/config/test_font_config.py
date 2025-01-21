import pytest
from unittest.mock import patch, mock_open
from pathlib import Path
from co_op_translator.config.font_config import FontConfig

# Sample YAML data for mocking font_language_mappings.yml
sample_yaml = """
en:
  name: English
  font: "Arial.ttf"
  rtl: False
ar:
  name: Arabic
  font: "Arial_Arabic.ttf"
  rtl: True
"""


@pytest.fixture
def mock_font_mappings():
    """
    Fixture that provides an instance of FontConfig with mocked font mappings.
    Mocks the loading of 'font_language_mappings.yml'.
    """
    with (
        patch("importlib.resources.path") as mock_path,
        patch("builtins.open", mock_open(read_data=sample_yaml)),
    ):
        mock_path.return_value = Path("fake_path/font_language_mappings.yml")
        return FontConfig()


def test_get_font_path(mock_font_mappings):
    """
    Test retrieving the font path for a valid language code.
    Ensures the correct path is returned for a valid language code.
    """
    with patch(
        "importlib.resources.path", return_value=Path("fake_font_path/Arial.ttf")
    ) as mock_path:
        font_path = mock_font_mappings.get_font_path("en")

        assert Path(font_path) == Path(
            "fake_font_path/Arial.ttf"
        ), "Font path for 'en' should return the correct path"
        mock_path.assert_called_once_with("co_op_translator.fonts", "Arial.ttf")


def test_get_font_path_invalid(mock_font_mappings):
    """
    Test that an invalid language code raises a ValueError.
    Ensures that requesting a font for an unsupported language code raises the appropriate error.
    """
    with pytest.raises(ValueError) as excinfo:
        mock_font_mappings.get_font_path("xx")
    assert "Font for language code 'xx' is not supported or not found." in str(
        excinfo.value
    )


def test_get_language_name(mock_font_mappings):
    """
    Test retrieving the language name for a valid language code.
    Ensures the correct language name is returned for a valid language code.
    """
    language_name = mock_font_mappings.get_language_name("en")
    assert language_name == "English", "Language name for 'en' should be 'English'"


def test_get_language_name_invalid(mock_font_mappings):
    """
    Test that an invalid language code raises a ValueError when retrieving the language name.
    Ensures that requesting a language name for an unsupported language code raises an error.
    """
    with pytest.raises(ValueError) as excinfo:
        mock_font_mappings.get_language_name("xx")
    assert "Language code 'xx' is not supported." in str(excinfo.value)


def test_is_rtl(mock_font_mappings):
    """
    Test if the language is RTL (Right-to-Left) for a valid language code.
    Ensures that the RTL value is correctly returned for RTL languages like Arabic.
    """
    is_rtl = mock_font_mappings.is_rtl("ar")
    assert is_rtl is True, "The 'ar' language code should return True for RTL"


def test_is_rtl_false(mock_font_mappings):
    """
    Test if the language is not RTL (Left-to-Right) for a valid language code.
    Ensures that the RTL value is correctly returned as False for non-RTL languages like English.
    """
    is_rtl = mock_font_mappings.is_rtl("en")
    assert is_rtl is False, "The 'en' language code should return False for RTL"


def test_is_rtl_invalid(mock_font_mappings):
    """
    Test that an invalid language code raises a ValueError when checking RTL.
    Ensures that requesting RTL info for an unsupported language code raises an error.
    """
    with pytest.raises(ValueError) as excinfo:
        mock_font_mappings.is_rtl("xx")
    assert "Language code 'xx' is not supported." in str(excinfo.value)
