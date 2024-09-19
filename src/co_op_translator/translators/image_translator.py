import os
import logging
import numpy as np
from PIL import Image, ImageFont
from pathlib import Path
from co_op_translator.config.font_config import FontConfig
from co_op_translator.utils.image_utils import (
    get_average_color,
    get_text_color,
    create_filled_polygon_mask,
    draw_text_on_image,
    warp_image_to_bounding_box,
    get_image_mode
)
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from co_op_translator.config.base_config import Config
from co_op_translator.translators.text_translator import TextTranslator
from co_op_translator.utils.file_utils import generate_translated_filename

logger = logging.getLogger(__name__)

class ImageTranslator:
    def __init__(self, default_output_dir='./translated_images', root_dir='.'):
        """
        Initialize the ImageTranslator with a default output directory.

        Args:
            default_output_dir (str): The default directory where translated images will be saved.
        """
        self.text_translator = TextTranslator()
        self.font_config = FontConfig()
        self.root_dir = Path(root_dir)
        self.default_output_dir = default_output_dir
        os.makedirs(self.default_output_dir, exist_ok=True)

    def get_image_analysis_client(self):
        """
        Initialize and return an Image Analysis Client.

        Returns:
            ImageAnalysisClient: The initialized client.
        """
        endpoint = Config.AZURE_AI_SERVICE_ENDPOINT
        subscription_key = Config.AZURE_SUBSCRIPTION_KEY
        return ImageAnalysisClient(endpoint, AzureKeyCredential(subscription_key))

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
                line_bounding_boxes.append({
                    "text": line.text,
                    "bounding_box": bounding_box,
                    "confidence": line.words[0].confidence if line.words else None
                })
            return line_bounding_boxes
        else:
            raise Exception("No text was recognized in the image.")

    def plot_annotated_image(self, image_path, line_bounding_boxes, translated_text_list, target_language_code, destination_path=None):
        """
        Plot annotated image with translated text.

        Args:
            image_path (str): Path to the image file.
            line_bounding_boxes (list): List of bounding boxes and text data.
            translated_text_list (list): List of translated texts.
            destination_path (str, optional): The path to save the translated image. 
                                            If None, save in default location (./translated_images/).

        Returns:
            str: The path to the annotated image.
        """
        # Load the image with the appropriate mode
        mode = get_image_mode(image_path)
        image = Image.open(image_path).convert(mode)
        
        font_size = 40
        font_path = self.font_config.get_font_path(target_language_code)
        font = ImageFont.truetype(font_path, font_size)

        # Annotate the image with translated text
        for line_info, translated_text in zip(line_bounding_boxes, translated_text_list):
            bounding_box = line_info['bounding_box']

            # Get the average color of the bounding box area
            bg_color = get_average_color(image, bounding_box)
            text_color = get_text_color(bg_color)

            # Create a mask to fill the bounding box area with the background color
            mask_image = create_filled_polygon_mask(bounding_box, image.size, bg_color)

            if mode == 'RGBA':
                # Composite the mask onto the image to fill the bounding box (for PNG images)
                image = Image.alpha_composite(image, mask_image)
            else:
                # Convert image to RGBA (if it's not already in RGBA mode)
                image = image.convert('RGBA')
                mask_image = mask_image.convert('RGBA')

                # Use alpha_composite to overlay mask_image onto the original image
                image = Image.alpha_composite(image, mask_image)

            # Draw the translated text onto a temporary image
            text_image = draw_text_on_image(translated_text, font, text_color)

            # Convert the text image to an array and warp it to fit the bounding box
            text_image_array = np.array(text_image)
            warped_text_image = warp_image_to_bounding_box(text_image_array, bounding_box, image.width, image.height)

            # Convert the warped text image back to PIL format and paste it onto the original image
            warped_text_image_pil = Image.fromarray(warped_text_image)
            image = Image.alpha_composite(image, warped_text_image_pil)
        
        actual_image_path = Path(image_path).resolve()

        # Generate the new filename based on the original file name, hash, and language code
        new_filename = generate_translated_filename(actual_image_path, target_language_code, self.root_dir)

        logger.info(f"Resolved image path in plot_annotated_image: {actual_image_path}")

        # Determine the output path using pathlib
        if destination_path is None:
            output_path = Path(self.default_output_dir) / new_filename
        else:
            output_path = Path(destination_path) / new_filename

        # Save the annotated image to the determined output path
        if mode == 'RGBA':
            image.save(output_path)
        else:
            image = image.convert("RGB")  # Ensure JPG compatibility
            image.save(output_path, format="JPEG")

        # Return the path to the annotated image
        return str(output_path)

    def translate_image(self, image_path, target_language_code, destination_path=None):
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
            new_filename = generate_translated_filename(actual_image_path, target_language_code, self.root_dir)

            # Determine the output path using pathlib
            if destination_path is None:
                output_path = Path(self.default_output_dir) / new_filename
            else:
                output_path = Path(destination_path) / new_filename

            # Check if any text was recognized
            if not line_bounding_boxes:
                logger.info(f"No text was recognized in the image: {image_path}. Saving the original image as the translated image.")
                
                # Load the original image and save it with the new name
                original_image = Image.open(image_path)
                original_image.save(output_path)
                
                return str(output_path)  # Return the new image path with original content

            # Extract the text data from the bounding boxes
            text_data = [line['text'] for line in line_bounding_boxes]

            # Retrieve the name of the target language based on the language code
            target_language_name = self.font_config.get_language_name(target_language_code)
            
            # Translate the text data into the target language
            translated_text_list = self.text_translator.translate_image_text(text_data, target_language_name)
            
            # Annotate the image with the translated text and save the result
            return self.plot_annotated_image(image_path, line_bounding_boxes, translated_text_list, target_language_code, destination_path)

        except Exception as e:
            logger.error(f"Failed to translate image {image_path} due to an error: {e}. Saving the original image instead.")

            # Load the original image and save it with the new name
            actual_image_path = Path(image_path).resolve()
            new_filename = generate_translated_filename(actual_image_path, target_language_code, self.root_dir)
            output_path = Path(self.default_output_dir) / new_filename

            original_image = Image.open(image_path)
            original_image.save(output_path)
            
            return str(output_path)  # Return the path to the original image with the new name
