# Different approaches are used for RGB and RGBA images
RGBA_IMAGE_EXTENSIONS = {".png"}
RGB_IMAGE_EXTENSIONS = {".jpg", ".jpeg"}
SUPPORTED_IMAGE_EXTENSIONS = RGBA_IMAGE_EXTENSIONS.union(RGB_IMAGE_EXTENSIONS)

EXCLUDED_DIRS = {
    "translations",
    "translated_images",
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
