import logging
import math
import time
from abc import ABC, abstractmethod
from math import hypot
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm


import arabic_reshaper
from bidi.algorithm import get_display


from co_op_translator.config.font_config import FontConfig
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

logger = logging.getLogger(__name__)


class ImageTranslator(ABC):
    def __init__(self, default_output_dir="./translated_images", root_dir="."):
        """Initialize translator dependencies.

        Sets up the text translation service and font configuration. The
        default output directory is kept for compatibility, but directories are
        created only by project-level persistence code.

        Args:
            default_output_dir: Default directory used by project orchestration
            root_dir: Root directory of the project for path calculations
        """
        self.text_translator = TextTranslator.create()
        self.font_config = FontConfig()
        self.root_dir = Path(root_dir)
        self.default_output_dir = default_output_dir

    @abstractmethod
    def get_image_analysis_client(self):
        """
        Initialize and return an Image Analysis Client.

        Returns:
            Configured client instance for image analysis
        """
        pass

    def extract_line_bounding_boxes(self, image_path):
        """
        Extract line bounding boxes from an image using Azure Analysis Client.

        Args:
            image_path: Path to the image file to analyze

        Returns:
            List of dictionaries containing text content, bounding box coordinates,
            and confidence scores for each detected text line

        Raises:
            Exception: If text recognition fails or no text is found
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
            raise Exception(
                f"No text detected in image '{Path(image_path).name}': "
                f"The image may not contain clear, high-contrast text, or the text quality is too poor for recognition. "
                f"Please ensure the image contains readable text."
            )

    def render_translated_image(
        self,
        image_path,
        line_bounding_boxes,
        translated_text_list,
        target_language_code,
        verbose=False,
        fast_mode=False,
    ) -> Image.Image:
        """Render translated text onto an image and return the processed image.

        Uses either a fast or high-quality ("neat") rendering approach based on the
        fast_mode parameter. Handles text orientation, RTL languages, and maintains
        visual context.

        Args:
            image_path: Path to the image file
            line_bounding_boxes: List of detected text regions with coordinates
            translated_text_list: List of translated texts corresponding to each region
            target_language_code: Language code determining font and text direction
            verbose: Whether to display processing progress
            fast_mode: Whether to use faster rendering (3x faster but less precise)

        Returns:
            PIL image with translated text rendered in place
        """
        style = "fast" if fast_mode else "neat"
        logger.info("=" * 50)
        logger.info(f"Starting annotation ({style} mode) for image: {image_path} ")
        rtl = self.font_config.is_rtl(target_language_code)

        # Apply RTL language-specific text processing for Arabic, Hebrew, etc.
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
                logger.error(
                    f"Font file not found for language '{target_language_code}' at '{font_path}' in image '{Path(image_path).name}': "
                    f"Using default font. Install the required font or check font configuration."
                )
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
                            f"Invalid text detection data in image '{Path(image_path).name}': "
                            f"Expected 8 coordinates but got {len(bounding_box_flat)}. "
                            f"The text detection may be corrupted."
                        )
                        continue

                    bounding_box_tuples = list(
                        zip(bounding_box_flat[::2], bounding_box_flat[1::2])
                    )
                    if len(bounding_box_tuples) < 4:
                        logger.error(
                            f"Insufficient bounding box points in image '{Path(image_path).name}': "
                            f"Text detection data is incomplete. Try re-processing the image."
                        )
                        continue

                    try:
                        p0, p1, p2, p3 = bounding_box_tuples[:4]
                        box_width = hypot(p1[0] - p0[0], p1[1] - p0[1])
                        box_height = hypot(p2[0] - p1[0], p2[1] - p1[1])
                        angle = math.degrees(math.atan2(p1[1] - p0[1], p1[0] - p0[0]))
                        angle = -angle  # Invert angle for proper rotation.
                    except ValueError:
                        logger.error(
                            f"Invalid bounding box coordinates in image '{Path(image_path).name}': "
                            f"Text detection geometry is malformed. The image may have distorted text regions."
                        )
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
                                f"Font file not found for language '{target_language_code}' at '{font_path}' in image '{Path(image_path).name}': "
                                f"Using default font. Install the required font or check font configuration."
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

                    rendered_text_img = draw_text_on_image(
                        translated_text,
                        font,
                        text_color,
                        font_path=font_path,
                    )
                    text_img.paste(
                        rendered_text_img, (offset_x, offset_y), rendered_text_img
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
            # Regular (neat) method with dynamic font sizing.
            mode = get_image_mode(image_path)
            image = Image.open(image_path).convert(mode)

            font_path = self.font_config.get_font_path(target_language_code)
            # Supersampling factor for high-quality rendering
            SUPERSAMPLE = 2

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

                    # Calculate bounding box dimensions
                    pts = np.array(bounding_box, dtype=np.float32).reshape(4, 2)
                    widthA = np.linalg.norm(pts[0] - pts[1])
                    widthB = np.linalg.norm(pts[2] - pts[3])
                    maxWidth = max(widthA, widthB)
                    heightA = np.linalg.norm(pts[0] - pts[3])
                    heightB = np.linalg.norm(pts[1] - pts[2])
                    maxHeight = max(heightA, heightB)
                    target_aspect = maxWidth / maxHeight if maxHeight != 0 else 1

                    # Dynamic font size based on bounding box height (with supersampling)
                    base_font_size = int(maxHeight * 0.85 * SUPERSAMPLE)
                    base_font_size = max(base_font_size, 12)  # Minimum font size

                    try:
                        font = ImageFont.truetype(font_path, base_font_size)
                    except IOError:
                        logger.error(
                            f"Font file not found for language '{target_language_code}' at '{font_path}': "
                            f"Using default font."
                        )
                        font = ImageFont.load_default()

                    # Measure text width and adjust font size if text is too wide
                    dummy_img = Image.new("RGBA", (1, 1))
                    dummy_draw = ImageDraw.Draw(dummy_img)
                    bbox = dummy_draw.textbbox((0, 0), translated_text, font=font)
                    text_width = bbox[2] - bbox[0]
                    target_width = maxWidth * SUPERSAMPLE * 0.95  # 95% of box width

                    if text_width > target_width and text_width > 0:
                        # Scale down font to fit width
                        scale_factor = target_width / text_width
                        adjusted_font_size = max(int(base_font_size * scale_factor), 10)
                        try:
                            font = ImageFont.truetype(font_path, adjusted_font_size)
                        except IOError:
                            pass  # Keep previous font

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
                        translated_text,
                        font,
                        get_text_color(final_bg_color),
                        font_path=font_path,
                    )
                    text_image_array = np.array(text_image)

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

        return image

    def translate_image(
        self, image_path, target_language_code, fast_mode=False, verbose=False
    ) -> Image.Image:
        """Translate text in an image and return the rendered image.

        This method performs text extraction, text translation, and in-memory image
        rendering. It performs no output path calculation, no image saving, and no
        metadata writes; project-level callers decide where and how to persist the
        returned image.

        Args:
            image_path: Path to the image file
            target_language_code: Language code to translate text into
            fast_mode: Whether to use faster rendering with slightly lower quality
            verbose: Whether to display rendering progress

        Returns:
            PIL image with translated text rendered in place
        """
        image_path = Path(image_path)

        line_bounding_boxes = self.extract_line_bounding_boxes(image_path)
        if not line_bounding_boxes:
            logger.info(
                f"No text detected in image '{image_path.name}': "
                f"The image may not contain readable text or text may be too small/blurry to detect."
            )
            with Image.open(image_path) as original_image:
                return original_image.copy()

        text_data = [line["text"] for line in line_bounding_boxes]
        translated_text_list = self.text_translator.translate_image_text(
            text_data, target_language_code
        )
        return self.render_translated_image(
            image_path,
            line_bounding_boxes,
            translated_text_list,
            target_language_code,
            verbose=verbose,
            fast_mode=fast_mode,
        )

    @classmethod
    def create(
        cls, default_output_dir="./translated_images", root_dir="."
    ) -> "ImageTranslator":
        """Create appropriate ImageTranslator instance based on configuration.

        Factory method that determines and instantiates the correct provider-specific
        implementation (currently only Azure AI Service is supported).

        Args:
            default_output_dir: Default directory used by project orchestration
            root_dir: Root directory of the project for path calculations

        Returns:
            Configured ImageTranslator instance ready for use

        Raises:
            ValueError: If Azure AI Service is not properly configured
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
            logger.warning(f"Azure AI Service is not properly configured: {e}")
            raise ValueError(
                "Image translation is not configured: Missing required environment variables "
                "(AZURE_AI_SERVICE_API_KEY, AZURE_AI_SERVICE_ENDPOINT). "
                "Please check your .env file and ensure your Azure AI service credentials are set correctly."
            )
