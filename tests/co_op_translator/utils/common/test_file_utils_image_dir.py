import shutil
import tempfile
from pathlib import Path
import pytest
from co_op_translator.utils.common.file_utils import (
    reset_translation_directories,
    delete_translated_images_by_language_code,
)

def create_dummy_image(lang_dir, fname):
    f = lang_dir / fname
    f.write_text("dummy image content")
    return f

def test_image_dir_language_subfolders():
    with tempfile.TemporaryDirectory() as tmpdir:
        translations_dir = Path(tmpdir) / "translations"
        image_dir = Path(tmpdir) / "translated_images"
        langs = ["fr", "de"]
        reset_translation_directories(translations_dir, image_dir, langs)
        for lang in langs:
            assert (translations_dir / lang).is_dir()
            assert (image_dir / lang).is_dir()

def test_delete_translated_images_by_language_code():
    with tempfile.TemporaryDirectory() as tmpdir:
        image_dir = Path(tmpdir) / "translated_images"
        langs = ["fr", "de"]
        # Setup dirs and dummy files
        reset_translation_directories(Path(tmpdir) / "translations", image_dir, langs)
        for lang in langs:
            lang_dir = image_dir / lang
            lang_dir.mkdir(parents=True, exist_ok=True)
            create_dummy_image(lang_dir, f"img1.{lang}.png")
            create_dummy_image(lang_dir, f"img2.{lang}.jpg")
            assert any(lang_dir.iterdir())
        # Delete 'fr' images
        delete_translated_images_by_language_code("fr", image_dir)
        assert not (image_dir / "fr").exists()
        assert (image_dir / "de").is_dir() and any((image_dir / "de").iterdir())
