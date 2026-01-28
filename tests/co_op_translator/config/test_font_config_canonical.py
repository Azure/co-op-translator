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
    with (
        patch("importlib.resources.path") as mock_path_yaml,
        patch("builtins.open", mock_open(read_data=sample_yaml)),
    ):
        mock_path_yaml.return_value = Path("fake/fonts/font_language_mappings.yml")
        fc = FontConfig()

    # get_font_path should resolve alias input 'tw' to canonical 'zh-TW'
    with patch(
        "importlib.resources.path",
        return_value=Path("fake_fonts/NotoSansCJK-Medium.ttc"),
    ) as mock_path_font:
        path = fc.get_font_path("tw")
        assert Path(path).name == "NotoSansCJK-Medium.ttc"
        mock_path_font.assert_called_once_with(
            "co_op_translator.fonts", "NotoSansCJK-Medium.ttc"
        )

    # get_language_name should resolve alias input 'br' to canonical 'pt-BR'
    name = fc.get_language_name("br")
    assert name == "Portuguese (Brazil)"

    # is_rtl defaults to False if not set
    assert fc.is_rtl("zh-TW") is False


def test_font_config_invalid_language_errors():
    with (
        patch("importlib.resources.path") as mock_path_yaml,
        patch("builtins.open", mock_open(read_data=sample_yaml)),
    ):
        mock_path_yaml.return_value = Path("fake/fonts/font_language_mappings.yml")
        fc = FontConfig()

    with pytest.raises(ValueError) as excinfo:
        fc.get_language_name("xx")
    assert "Language code 'xx' is not supported." in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo2:
        fc.is_rtl("xx")
    assert "Language code 'xx' is not supported." in str(excinfo2.value)
