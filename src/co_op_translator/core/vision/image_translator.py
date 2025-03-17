import os
import logging
import numpy as np
from PIL import Image, ImageFont
from pathlib import Path

import cv2
import math
from math import hypot
from tqdm import tqdm
import time
from PIL import Image, ImageFont, ImageDraw
import numpy as np
from pathlib import Path

import arabic_reshaper
from bidi.algorithm import get_display


from co_op_translator.config.font_config import FontConfig
from co_op_translator.config.constants import RGB_IMAGE_EXTENSIONS
from co_op_translator.config.vision_config.config import VisionConfig
from co_op_translator.config.vision_config.provider import VisionProvider
from co_op_translator.utils.vision.image_utils import (
    get_dominant_color,
    get_text_color,
    create_filled_polygon_mask,
    draw_text_on_image,
    warp_image_to_bounding_box,
    get_image_mode,
    group_bounding_boxes,
    pad_text_image_to_target_aspect,
    adjust_bg_color,
)
from azure.ai.vision.imageanalysis.models import VisualFeatures
from co_op_translator.core.llm.text_translator import TextTranslator
from co_op_translator.utils.common.file_utils import generate_translated_filename
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class ImageTranslator(ABC):
    def __init__(self, default_output_dir="./translated_images", root_dir="."):
        """
        Initialize the ImageTranslator with a default output directory.

        Args:
            default_output_dir (str): The default directory where translated images will be saved.
        """
        self.text_translator = TextTranslator.create()
        self.font_config = FontConfig()
        self.root_dir = Path(root_dir)
        self.default_output_dir = default_output_dir
        os.makedirs(self.default_output_dir, exist_ok=True)

    @abstractmethod
    def get_image_analysis_client(self):
        """
        Initialize and return an Image Analysis Client.

        Returns:
            ImageAnalysisClient: The initialized client.
        """
        pass

    def extract_line_bounding_boxes(self, image_path):
        """
        Extract line bounding boxes from an image using Azure Analysis Client.

        Args:
            image_path (str): Path to the image file.

        Returns:
            list: List of dictionaries containing text, bounding box coordinates, and confidence scores.

        Raises:
            Exception: If the OCR operation did not succeed.
        """
        image_analysis_client = self.get_image_analysis_client()
        with open(image_path, "rb") as image_stream:
            image_data = image_stream.read()
            result = image_analysis_client.analyze(
                image_data=image_data,
                visual_features=[VisualFeatures.READ],
            )

        if result.read is not None and result.read.blocks:
            line_bounding_boxes = []
            for line in result.read.blocks[0].lines:
                bounding_box = []
                for point in line.bounding_polygon:
                    bounding_box.append(point.x)
                    bounding_box.append(point.y)
                line_bounding_boxes.append(
                    {
                        "text": line.text,
                        "bounding_box": bounding_box,
                        "confidence": line.words[0].confidence if line.words else None,
                    }
                )
            logger.info(
                f"Extracted {len(line_bounding_boxes)} bounding boxes from {image_path}"
            )
            return line_bounding_boxes
        else:
            raise Exception("No text was recognized in the image.")

    def plot_annotated_image(
        self,
        image_path,
        line_bounding_boxes,
        translated_text_list,
        target_language_code,
        destination_path=None,
        verbose=False,
        fast_mode=False,
    ):
        """
        Plot an annotated image with translated text using a perspective warp.
        When fast_mode is True, a faster (though less neat) variant is used.

        Args:
            image_path (str): Path to the image file.
            line_bounding_boxes (list): Flat list of bounding box dictionaries.
            translated_text_list (list): List of translated texts corresponding to each bounding box.
            target_language_code (str): Target language code.
            destination_path (str, optional): Directory to save the output image.
            verbose (bool, optional): If True, display processing progress.
            fast_mode (bool, optional): Translations are up to 3x faster, at a slight cost to quality and alignment precision. If True, the fast method is used.

        Returns:
            str: The path to the annotated image.
        """
        style = "fast" if fast_mode else "neat"
        logger.info("=" * 50)
        logger.info(f"Starting annotation ({style} mode) for image: {image_path} ")
        rtl = self.font_config.is_rtl(target_language_code)

        # Process text for specific languages that need special handling
        processed_text_list = []
        try:
            # Import these libraries only when needed
            if target_language_code in ["ar", "fa", "ur", "he"]:
                for text in translated_text_list:
                    # Reshape Arabic text
                    reshaped_text = arabic_reshaper.reshape(text)
                    # Handle bidirectional text
                    bidi_text = get_display(reshaped_text)
                    processed_text_list.append(bidi_text)

                logger.info(
                    f"Applied Arabic reshaping and bidirectional processing for {target_language_code}"
                )
            else:
                processed_text_list = translated_text_list
        except ImportError:
            logger.warning(
                "Arabic reshaper or python-bidi not installed. Using original text."
            )
            processed_text_list = translated_text_list

        logger.debug(f"Translated text: {processed_text_list}")

        # Group bounding boxes into paragraphs.
        grouped_boxes = group_bounding_boxes(line_bounding_boxes)
        # Group translations to match the paragraph groups.
        grouped_translations = []
        text_index = 0
        for group in grouped_boxes:
            group_size = len(group)
            grouped_translations.append(
                processed_text_list[text_index : text_index + group_size]
            )
            text_index += group_size

        # Generate output path
        actual_image_path = Path(image_path).resolve()
        new_filename = generate_translated_filename(
            actual_image_path, target_language_code, self.root_dir
        )
        base_dir = "./translated_images_fast/" if fast_mode else "./translated_images/"
        dest = Path(destination_path) if destination_path else Path(base_dir)
        dest.mkdir(parents=True, exist_ok=True)
        output_path = dest / new_filename

        # ------------------------------------- Fast Mode -------------------------------------#
        if fast_mode:
            # Fast method variant.
            image = Image.open(image_path).convert("RGBA")

            font_size = 40
            # Use instance variable for font config
            font_path = self.font_config.get_font_path(target_language_code)
            try:
                base_font = ImageFont.truetype(font_path, font_size)
            except IOError:
                logger.error(f"Font file not found at {font_path}. Using default font.")
                base_font = ImageFont.load_default()

            iterator = zip(grouped_boxes, grouped_translations)
            if verbose:
                iterator = tqdm(
                    iterator, total=len(grouped_boxes), desc="Processing groups (fast)"
                )

            start_time = time.time()
            for group_info, group_translated in iterator:
                group_length = len(group_info)
                # Determine alignment for the group.
                if group_length == 1:
                    alignment = "center"
                elif rtl:
                    alignment = "right"
                else:
                    alignment = "left"

                for line_info, translated_text in zip(group_info, group_translated):
                    bounding_box_flat = line_info.get("bounding_box", [])
                    if len(bounding_box_flat) != 8:
                        logger.error(
                            f"Invalid bounding_box length: {bounding_box_flat}"
                        )
                        continue

                    bounding_box_tuples = list(
                        zip(bounding_box_flat[::2], bounding_box_flat[1::2])
                    )
                    if len(bounding_box_tuples) < 4:
                        logger.error("Bounding box does not have enough points.")
                        continue

                    try:
                        p0, p1, p2, p3 = bounding_box_tuples[:4]
                        box_width = hypot(p1[0] - p0[0], p1[1] - p0[1])
                        box_height = hypot(p2[0] - p1[0], p2[1] - p1[1])
                        angle = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0]))
                        angle = -angle  # Invert angle for proper rotation.
                    except ValueError:
                        logger.error("Invalid bounding_box points for quadrilateral.")
                        continue

                    bg_color, _ = get_dominant_color(image, bounding_box_flat)
                    final_bg_color = adjust_bg_color(bg_color)
                    draw = ImageDraw.Draw(image)
                    draw.polygon(bounding_box_tuples, fill=final_bg_color)

                    text_color = get_text_color(final_bg_color)

                    max_allowed_width = box_width * 0.90
                    max_allowed_height = box_height * 0.95

                    initial_font = base_font
                    # Measure text dimensions
                    dummy_draw = ImageDraw.Draw(image)
                    bbox = dummy_draw.textbbox(
                        (0, 0),
                        translated_text,
                        font=initial_font,
                    )
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    if text_width <= 0 or text_height <= 0:
                        font = initial_font
                    else:
                        width_ratio = max_allowed_width / text_width
                        height_ratio = max_allowed_height / text_height
                        scaling_factor = min(width_ratio, height_ratio)
                        optimal_font_size = max(
                            int(initial_font.size * scaling_factor), 1
                        )
                        try:
                            font = ImageFont.truetype(font_path, optimal_font_size)
                        except IOError:
                            logger.error(
                                f"Font file not found at {font_path}. Using default font."
                            )
                            font = ImageFont.load_default()

                    # Recalculate text dimensions with new font
                    bbox = dummy_draw.textbbox(
                        (0, 0),
                        translated_text,
                        font=font,
                    )
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    xs, ys = zip(*bounding_box_tuples)
                    box_width = max(xs) - min(xs)
                    box_height_val = max(ys) - min(ys)

                    # Create a temporary square image for the text with a transparent background.
                    square_side = max(box_width, box_height_val)
                    text_img = Image.new(
                        "RGBA", (square_side, square_side), (255, 255, 255, 0)
                    )
                    offset_y = (square_side - text_height) // 2
                    if alignment == "center":
                        offset_x = (square_side - text_width) // 2
                    elif alignment == "right":
                        offset_x = square_side - text_width - 10
                    else:
                        offset_x = 10

                    temp_draw = ImageDraw.Draw(text_img)
                    temp_draw.text(
                        (offset_x, offset_y),
                        translated_text,
                        font=font,
                        fill=text_color,
                        anchor="la",
                    )

                    rotated_text_img = text_img.rotate(angle, expand=True)
                    center_x = min(xs) + box_width / 2
                    center_y = min(ys) + box_height_val / 2
                    paste_x = int(center_x - rotated_text_img.width / 2)
                    paste_y = int(center_y - rotated_text_img.height / 2)

                    # Paste rotated text using its own alpha channel as mask.
                    image.paste(rotated_text_img, (paste_x, paste_y), rotated_text_img)

            elapsed_time = time.time() - start_time
            logger.info(
                f"Total time taken to plot annotated image (Fast Mode): {elapsed_time:.4f} seconds for {image_path}"
            )

        # ------------------------------------- Neat Mode -------------------------------------#
        else:
            # Regular (neat) method.
            mode = get_image_mode(image_path)
            image = Image.open(image_path).convert(mode)

            font_size = 40
            font_path = self.font_config.get_font_path(target_language_code)
            try:
                font = ImageFont.truetype(font_path, font_size)
            except IOError:
                logger.error(f"Font file not found at {font_path}. Using default font.")
                font = ImageFont.load_default()

            iterator = zip(grouped_boxes, grouped_translations)
            if verbose:
                iterator = tqdm(
                    iterator, total=len(grouped_boxes), desc="Processing paragraphs"
                )

            start_time = time.time()
            for group_info, group_translated in iterator:
                if len(group_info) == 1:
                    effective_alignment_group = "center"
                else:
                    effective_alignment_group = "right" if rtl else "left"

                for line_info, translated_text in zip(group_info, group_translated):
                    bounding_box = line_info["bounding_box"]

                    bg_color, _ = get_dominant_color(image, bounding_box)
                    final_bg_color = adjust_bg_color(bg_color)
                    mask_image = create_filled_polygon_mask(
                        bounding_box, image.size, final_bg_color
                    )
                    if mode == "RGBA":
                        image = Image.alpha_composite(image, mask_image)
                    else:
                        image = image.convert("RGBA")
                        mask_image = mask_image.convert("RGBA")
                        image = Image.alpha_composite(image, mask_image)

                    text_image = draw_text_on_image(
                        translated_text, font, get_text_color(final_bg_color)
                    )
                    text_image_array = np.array(text_image)

                    pts = np.array(bounding_box, dtype=np.float32).reshape(4, 2)
                    widthA = np.linalg.norm(pts[0] - pts[1])
                    widthB = np.linalg.norm(pts[2] - pts[3])
                    maxWidth = max(widthA, widthB)
                    heightA = np.linalg.norm(pts[0] - pts[3])
                    heightB = np.linalg.norm(pts[1] - pts[2])
                    maxHeight = max(heightA, heightB)
                    target_aspect = maxWidth / maxHeight if maxHeight != 0 else 1

                    padded_text_image = pad_text_image_to_target_aspect(
                        text_image_array, target_aspect, effective_alignment_group
                    )
                    warped_text_image = warp_image_to_bounding_box(
                        padded_text_image, bounding_box, image.width, image.height
                    )
                    warped_text_image_pil = Image.fromarray(warped_text_image)
                    image = Image.alpha_composite(image, warped_text_image_pil)

            elapsed_time = time.time() - start_time
            logger.info(
                f"Total time taken to plot annotated image (Neat Mode): {elapsed_time:.4f} seconds for {image_path}"
            )

        # Handle RGB conversion to RGBA if needed before saving - common for both methods
        if output_path.suffix.lower() in RGB_IMAGE_EXTENSIONS:
            image = image.convert("RGB")

        # Save the image
        image.save(output_path)

        logger.info(f"Annotated image saved to {output_path}")
        return str(output_path)

    def translate_image(
        self, image_path, target_language_code, destination_path=None, fast_mode=False
    ):
        """
        Translate text in an image and return the image annotated with the translated text.

        Args:
            image_path (str): Path to the image file.
            target_language_code (str): The language to translate the text into.
            destination_path (str, optional): The path to save the translated image.
                                            If None, save in default location (./translated_images/).

        Returns:
            str: The path to the annotated image, or the original image saved as a new file in case of errors.
        """
        image_path = Path(image_path)

        try:
            # Extract text and bounding boxes from the image
            line_bounding_boxes = self.extract_line_bounding_boxes(image_path)

            # Generate the new filename based on the original file name, hash, and language code
            actual_image_path = Path(image_path).resolve()
            new_filename = generate_translated_filename(
                actual_image_path, target_language_code, self.root_dir
            )

            # Determine the output path using pathlib
            if destination_path is None:
                output_path = Path(self.default_output_dir) / new_filename
            else:
                output_path = Path(destination_path) / new_filename

            # Check if any text was recognized
            if not line_bounding_boxes:
                logger.info(
                    f"No text was recognized in the image: {image_path}. Saving the original image as the translated image."
                )

                # Load the original image and save it with the new name
                original_image = Image.open(image_path)
                original_image.save(output_path)

                return str(
                    output_path
                )  # Return the new image path with original content

            # Extract the text data from the bounding boxes
            text_data = [line["text"] for line in line_bounding_boxes]

            # Retrieve the name of the target language based on the language code
            target_language_name = self.font_config.get_language_name(
                target_language_code
            )

            # Translate the text data into the target language
            translated_text_list = self.text_translator.translate_image_text(
                text_data, target_language_name
            )

            # Annotate the image with the translated text and save the result
            return self.plot_annotated_image(
                image_path,
                line_bounding_boxes,
                translated_text_list,
                target_language_code,
                destination_path,
                fast_mode=fast_mode,  # Add this parameter
            )

        except Exception as e:
            logger.error(
                f"Failed to translate image {image_path} due to an error: {e}. Saving the original image instead."
            )

            # Load the original image and save it with the new name
            actual_image_path = Path(image_path).resolve()
            new_filename = generate_translated_filename(
                actual_image_path, target_language_code, self.root_dir
            )
            output_path = Path(self.default_output_dir) / new_filename

            original_image = Image.open(image_path)
            original_image.save(output_path)

            return str(
                output_path
            )  # Return the path to the original image with the new name

    @classmethod
    def create(
        cls, default_output_dir="./translated_images", root_dir="."
    ) -> "ImageTranslator":
        """
        Factory method to create appropriate ImageTranslator instance.
        Currently only supports Azure Computer Vision.

        Args:
            default_output_dir (str): The default directory where translated images will be saved.
            root_dir (str): The root directory of the project.

        Returns:
            ImageTranslator: An instance of the appropriate image translator.
        """
        try:
            from co_op_translator.config.vision_config.config import VisionConfig

            provider = VisionConfig.get_available_provider()

            if provider == VisionProvider.AZURE_COMPUTER_VISION:
                from co_op_translator.core.vision.providers.azure.image_translator import (
                    AzureImageTranslator,
                )

                return AzureImageTranslator(default_output_dir, root_dir)

        except (ImportError, ValueError) as e:
            logger.warning(f"Computer Vision is not properly configured: {e}")
            raise ValueError(
                "Computer Vision environment variables are not properly configured"
            )
