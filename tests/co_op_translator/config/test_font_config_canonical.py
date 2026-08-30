import pytest
from pathlib import Path
from unittest.mock import patch, mock_open

from co_op_translator.config.font_config import FontConfig

sample_yaml = """
zh-TW:
  name: Chinese (Traditional, Taiwan)
  font: "NotoSansCJK-Medium.ttc"
pt-PT:
  name: Portuguese (Portugal)
  font: "NotoSans-Medium.ttf"
pt-BR:
  name: Portuguese (Brazil)
  font: "NotoSans-Medium.ttf"
"""


def test_font_config_resolves_canonical_to_alias_keys():
    # Mock YAML with alias keys only
    with patch("co_op_translator.config.font_config.resources.files") as mock_files:
        mappings_resource = mock_files.return_value.joinpath.return_value
        mappings_resource.open = mock_open(read_data=sample_yaml)
        fc = FontConfig()

    # get_font_path should resolve alias input 'tw' to canonical 'zh-TW'
    with patch("co_op_translator.config.font_config.resources.files") as mock_files:
        mock_files.return_value.joinpath.return_value = Path(
            "fake_fonts/NotoSansCJK-Medium.ttc"
        )
        path = fc.get_font_path("tw")
        assert Path(path).name == "NotoSansCJK-Medium.ttc"
        mock_files.assert_called_once_with("co_op_translator.fonts")
        mock_files.return_value.joinpath.assert_called_once_with(
            "NotoSansCJK-Medium.ttc"
        )

    # get_language_name should resolve alias input 'br' to canonical 'pt-BR'
    name = fc.get_language_name("br")
    assert name == "Portuguese (Brazil)"

    # is_rtl defaults to False if not set
    assert fc.is_rtl("zh-TW") is False


def test_font_config_invalid_language_errors():
    with patch("co_op_translator.config.font_config.resources.files") as mock_files:
        mappings_resource = mock_files.return_value.joinpath.return_value
        mappings_resource.open = mock_open(read_data=sample_yaml)
        fc = FontConfig()

    with pytest.raises(ValueError) as excinfo:
        fc.get_language_name("xx")
    assert "Language code 'xx' is not supported." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo2:
        fc.is_rtl("xx")
    assert "Language code 'xx' is not supported." in str(excinfo2.value)
