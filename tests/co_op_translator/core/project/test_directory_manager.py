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

    def test_migrate_markdown_image_links(self, setup_test_dirs):
        """Test that markdown image basenames are updated using the rename map."""

        root_dir = setup_test_dirs
        translations_dir = root_dir / "translations"
        language_codes = ["ko"]
        excluded_dirs = []

        translations_dir.mkdir(exist_ok=True)
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir(parents=True)

        md_file = ko_dir / "readme.md"
        old_image_name = "logo.0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef.ko.png"
        new_image_name = "logo.0123456789abcdef.ko.png"
        original_content = f"# Test\n![Logo]({old_image_name})\n"
        md_file.write_text(original_content, encoding="utf-8")

        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs,
        )

        updated_files = manager.migrate_markdown_image_links({old_image_name: new_image_name})

        # One file should be updated
        assert updated_files == 1

        # Content should now reference the new image basename
        migrated_content = md_file.read_text(encoding="utf-8")
        assert old_image_name not in migrated_content
        assert new_image_name in migrated_content

    def test_migrate_notebook_image_links(self, setup_test_dirs):
        """Test that notebook markdown cells are updated using the rename map."""

        import json

        root_dir = setup_test_dirs
        translations_dir = root_dir / "translations"
        language_codes = ["ko"]
        excluded_dirs = []

        translations_dir.mkdir(exist_ok=True)
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir(parents=True)

        nb_file = ko_dir / "test.ipynb"
        old_image_name = "logo.0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef.ko.png"
        new_image_name = "logo.0123456789abcdef.ko.png"

        notebook_content = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "source": [f"# Test\n![Logo]({old_image_name})\n"],
                },
                {
                    "cell_type": "code",
                    "source": ["print('hello')\n"],
                },
            ],
            "metadata": {},
        }

        nb_file.write_text(json.dumps(notebook_content), encoding="utf-8")

        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs,
        )

        updated_files = manager.migrate_notebook_image_links({old_image_name: new_image_name})

        assert updated_files == 1

        loaded = json.loads(nb_file.read_text(encoding="utf-8"))
        cell_source = "".join(loaded["cells"][0]["source"])
        assert old_image_name not in cell_source
        assert new_image_name in cell_source

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

    def test_escaped_backslash_path_handling(self, setup_test_dirs):
        """Test handling of escaped backslash paths in metadata (like those from JSON serialization)."""
        import json

        root_dir = setup_test_dirs
        translations_dir = root_dir / "translations"
        language_codes = ["ko"]
        excluded_dirs = []

        # Create translations directory and files
        translations_dir.mkdir(exist_ok=True)
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir(exist_ok=True)

        # Create a nested directory structure with deep nesting to test escaped path handling
        deep_dir = root_dir / "deep" / "nested" / "path" / "structure"
        deep_dir.mkdir(parents=True)
        original_file = deep_dir / "test_file.md"
        original_file.write_text("# Original Content for Escaped Path Test")

        # Create a translation file with double-escaped backslash path in metadata
        # This simulates how paths might appear in JSON after multiple serialization/deserialization
        escaped_path = "deep\\\\nested\\\\path\\\\structure\\\\test_file.md"
        escaped_trans_file = ko_dir / "escaped_backslash.md"

        escaped_metadata = {
            "source_file": escaped_path,
            "original_hash": "test_hash",
            "translation_date": "2025-01-26T14:30:00+00:00",
            "language_code": "ko",
        }

        escaped_content = f"""<!--
{json.dumps(escaped_metadata, indent=2)}
-->
# Escaped Backslash Path Test"""

        escaped_trans_file.write_text(escaped_content)

        # Test with a real-world example from the issue
        real_example_path = "md\\\\02.Application\\\\01.TextAndChat\\\\Phi3\\\\E2E_Phi-3-Evaluation_AIFoundry.md"
        real_example_dir = (
            root_dir / "md" / "02.Application" / "01.TextAndChat" / "Phi3"
        )
        real_example_dir.mkdir(parents=True)
        real_example_file = real_example_dir / "E2E_Phi-3-Evaluation_AIFoundry.md"
        real_example_file.write_text("# Real Example Content")

        real_example_trans_file = ko_dir / "real_example.md"
        real_example_metadata = {
            "source_file": real_example_path,
            "original_hash": "test_hash",
            "translation_date": "2025-01-26T14:30:00+00:00",
            "language_code": "ko",
        }

        real_example_content = f"""<!--
{json.dumps(real_example_metadata, indent=2)}
-->
# Real Example Path Test"""

        real_example_trans_file.write_text(real_example_content)

        # Run the directory manager's cleanup function
        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs,
        )

        removed = manager.cleanup_orphaned_translations(markdown=True, images=False)

        # Verify results:
        # Both escaped backslash paths should be resolved correctly and not be removed
        assert (
            escaped_trans_file.exists()
        ), "Translation with escaped backslashes was incorrectly removed"
        assert (
            real_example_trans_file.exists()
        ), "Translation with real-world escaped path was incorrectly removed"
        assert removed == 0, f"Expected 0 files to be removed, but got {removed}"

    def test_nested_directory_recursive_removal(self, setup_test_dirs):
        """Test handling of nested directory removal and preventing access to already deleted directories."""
        import json

        root_dir = setup_test_dirs
        translations_dir = root_dir / "translations"
        language_codes = ["ko"]
        excluded_dirs = []

        # Create translations directory and files
        translations_dir.mkdir(exist_ok=True)
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir(exist_ok=True)

        # Create a deep nested directory structure
        deep_dir = ko_dir / "deep" / "nested" / "directory" / "structure"
        deep_dir.mkdir(parents=True)

        # Create multiple markdown files that will be orphaned (no original source)
        orphaned_files = []
        for i in range(5):
            orphaned_file = deep_dir / f"orphaned_{i}.md"
            orphaned_metadata = {
                "source_file": f"nonexistent/path/file_{i}.md",
                "original_hash": "test_hash",
                "translation_date": "2025-01-26T14:30:00+00:00",
                "language_code": "ko",
            }

            orphaned_content = f"""<!--
{json.dumps(orphaned_metadata, indent=2)}
-->
# Orphaned File {i}"""

            orphaned_file.write_text(orphaned_content)
            orphaned_files.append(orphaned_file)

        # Run the directory manager's cleanup function which should delete all orphaned files
        # and then try to recursively remove empty directories
        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs,
        )

        removed = manager.cleanup_orphaned_translations(markdown=True, images=False)

        # Verify results:
        # 1. All orphaned files should be removed
        assert removed == 5, f"Expected 5 files to be removed, but got {removed}"

        # 2. The entire directory structure should be removed since it's now empty
        assert not (
            ko_dir / "deep"
        ).exists(), "Deep directory wasn't removed recursively"

        # 3. Make sure no errors occurred when trying to access already deleted directories
        # This is implicitly verified by the test passing without exceptions
