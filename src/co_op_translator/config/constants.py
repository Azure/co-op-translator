# Different approaches are used for RGB and RGBA images
RGBA_IMAGE_EXTENSIONS = {".png"}
RGB_IMAGE_EXTENSIONS = {".jpg", ".jpeg"}
# WebP is used for translated images (supports both lossy and lossless compression)
WEBP_EXTENSION = ".webp"
SUPPORTED_IMAGE_EXTENSIONS = RGBA_IMAGE_EXTENSIONS.union(RGB_IMAGE_EXTENSIONS)

# All input image formats that can be translated (includes WebP for re-processing)
SUPPORTED_IMAGE_EXTENSIONS = SUPPORTED_IMAGE_EXTENSIONS.union({WEBP_EXTENSION})

# Supported notebook file extensions
SUPPORTED_NOTEBOOK_EXTENSIONS = {".ipynb"}

# Supported markdown file extensions
SUPPORTED_MARKDOWN_EXTENSIONS = {".md", ".mdx", ".markdown"}

EXCLUDED_DIRS = {
    "translations",
    "translated_images",
    "translated_images_fast",
    ".git",
    ".github",
    ".vscode",
    "__pycache__",
    "node_modules",
    "build",
    "dist",
    "venv",
    "env",
    "site-packages",
    ".venv",
    ".idea",
    ".devcontainer",
    ".pytest_cache",
}

# Maximum allowed difference in line breaks between original and translated text
# A margin is needed to account for added disclaimer and metadata
LINE_BREAK_MARGIN = 15
