"""
Tests for DirectoryManager class
"""

import pytest
from pathlib import Path
from unittest.mock import patch

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
        excluded_dirs=excluded_dirs
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
        translations_dir = root_dir / "translations"
        language_codes = ["ko"]
        excluded_dirs = []
        
        # Create a translation without original file
        translations_dir.mkdir()
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir()
        (ko_dir / "orphaned.md").write_text("# Orphaned content")
        
        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs
        )
        manager.cleanup_orphaned_translations()
        
        # Orphaned file should be removed
        assert not (ko_dir / "orphaned.md").exists()

    @patch("co_op_translator.core.project.directory_manager.filter_files")
    def test_filter_files_usage(self, mock_filter_files, setup_test_dirs):
        """Test filter_files usage in DirectoryManager"""
        root_dir = setup_test_dirs
        language_codes = ["ko"]
        excluded_dirs = ["node_modules", ".git"]
        translations_dir = root_dir / "translations"
        
        # Create translations directory and files
        translations_dir.mkdir()
        ko_dir = translations_dir / "ko"
        ko_dir.mkdir()
        
        # Create both original and translated files
        (root_dir / "test.md").write_text("# Original Test")
        test_file = ko_dir / "test.md"
        test_file.write_text("# Test Translation")
        
        # Setup mock for filter_files to return our test file
        mock_filter_files.return_value = [test_file]
        
        manager = DirectoryManager(
            root_dir=root_dir,
            translations_dir=translations_dir,
            language_codes=language_codes,
            excluded_dirs=excluded_dirs
        )
        
        # Call cleanup_orphaned_translations with markdown=True to ensure markdown files are processed
        manager.cleanup_orphaned_translations(markdown=True, images=False)
        
        # Verify filter_files was called with correct arguments - only directory and excluded_dirs
        mock_filter_files.assert_called_once_with(ko_dir, excluded_dirs)
        
        # Verify files still exist since they have matching originals
        assert (root_dir / "test.md").exists()
        assert test_file.exists()
