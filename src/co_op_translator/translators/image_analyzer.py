import os
import logging
from co_op_translator.translators.image_translator import ImageTranslator
from co_op_translator.utils.image_utils import (
    save_bounding_boxes,
    plot_bounding_boxes,
)

logger = logging.getLogger(__name__)

class ImageAnalyzer:
    def __init__(self, output_dir="./bounding_boxes"):
        """
        Initialize the ImageAnalyzer with an output directory.

        Args:
            output_dir (str): The directory where bounding boxes will be saved.
        """
        self.image_translator = ImageTranslator()
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def analyze_image(self, image_paths):
        """
        Process a list of image paths, extract bounding boxes, and plot them.

        Args:
            image_paths (list): List of paths to image files.
        """
        for image_path in image_paths:
            if image_path.endswith((".png", ".jpg", ".jpeg")):
                print(f"Processing {image_path}")
                line_bounding_boxes = self.image_translator.extract_line_bounding_boxes(image_path)
                if line_bounding_boxes:
                    save_bounding_boxes(image_path, line_bounding_boxes)
                    plot_bounding_boxes(image_path, line_bounding_boxes,language_code="en", display=True)
