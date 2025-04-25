"""
Tests for DirectoryManager class
"""

import pytest
import os

from co_op_translator.core.project.directory_manager import DirectoryManager


@pytest.fixture
def setup_test_dirs(tmp_path):
    """Set up test directory structure"""
    # Create test directories
    root_dir = tmp_path / "test_project"
    translations_dir = root_dir / "translations"
    root_dir.mkdir()

    # Create some test files
    (root_dir / "test.md").write_text("# Test content")
    (root_dir / "img").mkdir()
    (root_dir / "img/test.png").write_bytes(b"fake png content")

    return root_dir


@pytest.fixture
def setup_manager(setup_test_dirs):
    """Create a DirectoryManager instance with test configuration"""
    root_dir = setup_test_dirs
    translations_dir = root_dir / "translations"
    language_codes = ["ko", "ja"]
    excluded_dirs = ["node_modules", ".git"]

    return DirectoryManager(
        root_dir=root_dir,
        translations_dir=translations_dir,
        language_codes=language_codes,
        excluded_dirs=excluded_dirs,
    )


class TestDirectoryManager:
    def test_init_directories(self, setup_manager, setup_test_dirs):
        """Test directory initialization"""
        manager = setup_manager
        translations_dir = setup_test_dirs / "translations"

        manager.sync_directory_structure()

        # Check if translations directory is created
        assert translations_dir.exists()

        # Check if language-specific directories are created
        for lang in ["ko", "ja"]:
            assert (translations_dir / lang).exists()

    def test_cleanup_orphaned_translations(self, setup_test_dirs):
        """Test cleanup of orphaned translations"""
        root_dir = setup_test_dirs
        language_codes = ["ko"]
        excluded_dirs = ["node_modules", ".git"]
        translations_dir = root_dir / "translations"

        # Create translations directory and files
        translations_dir.mkdir()
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir()

        # Create test files
        test_file = ko_dir / "test.md"
        test_file.write_text(
            """<!--
{
    "source_file": "test.md"
}
-->
# Test Translation"""
        )

        orphaned_file = ko_dir / "orphaned.md"
        orphaned_file.write_text(
            """<!--
{
    "source_file": "nonexistent.md"
}
-->
# Orphaned Translation"""
        )

        # Create original file only for test.md
        (root_dir / "test.md").write_text("# Original Test")

        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs,
        )

        # Run cleanup
        manager.cleanup_orphaned_translations(markdown=True, images=False)

        # Verify test.md translation still exists (has matching original)
        assert test_file.exists()
        # Verify orphaned.md was removed (no matching original)
        assert not orphaned_file.exists()

    def test_cleanup_orphaned_image_translations(self, setup_test_dirs):
        """Test cleanup of orphaned image translations"""
        root_dir = setup_test_dirs
        translations_dir = root_dir / "translations"
        language_codes = ["ko"]
        excluded_dirs = []

        # Create original image
        img_dir = root_dir / "img"
        img_dir.mkdir(exist_ok=True)
        original_img = img_dir / "test.png"
        original_img.write_bytes(b"test image content")

        # Create translated image with hash
        translations_dir.mkdir(exist_ok=True)
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir(exist_ok=True)
        ko_img_dir = ko_dir / "img"
        ko_img_dir.mkdir(exist_ok=True)

        # Valid translated image (with correct hash)
        from co_op_translator.utils.common.file_utils import get_unique_id

        original_name, ext = os.path.splitext(original_img.name)
        path_hash = get_unique_id(original_img, root_dir)
        valid_trans_name = f"{original_name}.{path_hash}.ko{ext}"
        valid_trans_img = ko_img_dir / valid_trans_name
        valid_trans_img.write_bytes(b"translated content")

        # Orphaned translated image (with incorrect hash)
        orphaned_trans_img = ko_img_dir / "test.invalid_hash.ko.png"
        orphaned_trans_img.write_bytes(b"orphaned content")

        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs,
        )

        # Run cleanup
        removed = manager.cleanup_orphaned_translations(markdown=False, images=True)

        # Should have removed one file
        assert removed == 1
        # Valid translation should still exist
        assert valid_trans_img.exists()
        # Orphaned translation should be removed
        assert not orphaned_trans_img.exists()

    def test_cross_platform_path_handling(self, setup_test_dirs):
        """Test handling of cross-platform path separators in metadata."""
        import json
        from pathlib import PurePosixPath

        root_dir = setup_test_dirs
        translations_dir = root_dir / "translations"
        language_codes = ["ko"]
        excluded_dirs = []

        # Create translations directory and files
        translations_dir.mkdir(exist_ok=True)
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir(exist_ok=True)

        # Create a nested directory structure to test path handling
        nested_dir = root_dir / "nested" / "path" / "to"
        nested_dir.mkdir(parents=True)
        original_file = nested_dir / "test.md"
        original_file.write_text("# Original Content")

        # 1. Test with Windows-style backslash paths
        windows_style_path = str(original_file.relative_to(root_dir)).replace("/", "\\")
        windows_trans_file = ko_dir / "windows_style.md"

        # Create a translation file with Windows-style path in metadata
        windows_metadata = {
            "source_file": windows_style_path,
            "original_hash": "test_hash",
            "translation_date": "2025-01-26T14:30:00+00:00",
            "language_code": "ko",
        }

        windows_content = f"""<!--
{json.dumps(windows_metadata, indent=2)}
-->
# Windows Style Path Test"""

        windows_trans_file.write_text(windows_content)

        # 2. Test with POSIX-style forward slash paths
        posix_style_path = str(PurePosixPath(original_file.relative_to(root_dir)))
        posix_trans_file = ko_dir / "posix_style.md"

        # Create a translation file with POSIX-style path in metadata
        posix_metadata = {
            "source_file": posix_style_path,
            "original_hash": "test_hash",
            "translation_date": "2025-01-26T14:30:00+00:00",
            "language_code": "ko",
        }

        posix_content = f"""<!--
{json.dumps(posix_metadata, indent=2)}
-->
# POSIX Style Path Test"""

        posix_trans_file.write_text(posix_content)

        # 3. Test with a nonexistent file path
        nonexistent_trans_file = ko_dir / "nonexistent.md"
        nonexistent_metadata = {
            "source_file": "nonexistent/file.md",
            "original_hash": "test_hash",
            "translation_date": "2025-01-26T14:30:00+00:00",
            "language_code": "ko",
        }

        nonexistent_content = f"""<!--
{json.dumps(nonexistent_metadata, indent=2)}
-->
# Nonexistent File Test"""

        nonexistent_trans_file.write_text(nonexistent_content)

        # Run the directory manager's cleanup function
        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs,
        )

        removed = manager.cleanup_orphaned_translations(markdown=True, images=False)

        # Verify results:
        # 1. Both Windows and POSIX style paths should be resolved correctly
        assert (
            windows_trans_file.exists()
        ), "Windows-style path translation was incorrectly removed"
        assert (
            posix_trans_file.exists()
        ), "POSIX-style path translation was incorrectly removed"

        # 2. Nonexistent file should be removed
        assert (
            not nonexistent_trans_file.exists()
        ), "Nonexistent file translation was not removed"

        # 3. Only the nonexistent file should be removed
        assert removed == 1, f"Expected 1 file to be removed, but got {removed}"
