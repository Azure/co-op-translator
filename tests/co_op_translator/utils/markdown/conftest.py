import pytest


@pytest.fixture
def sample_markdown():
    """Sample markdown content for testing."""
    return """# Test Document
This is a test document with [a link](test.md) and ![an image](test.png).
Here's another [link](docs/example.md) and ![image](images/test.jpg).
"""


@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory structure for testing."""
    # Create directories
    (tmp_path / "translations").mkdir()
    (tmp_path / "translations/ko").mkdir()
    (tmp_path / "images").mkdir()
    (tmp_path / "translated_images").mkdir()

    # Create test files
    (tmp_path / "test.md").touch()
    (tmp_path / "test.png").touch()
    (tmp_path / "images/test.jpg").touch()

    return tmp_path
