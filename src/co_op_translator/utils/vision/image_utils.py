"""
This module contains utility functions for handling images.
Functions include saving and loading bounding boxes, drawing text on images, and plotting images with bounding boxes.
"""

import os
import logging
import json
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageStat
import matplotlib.pyplot as plt
from co_op_translator.config.font_config import FontConfig
from co_op_translator.utils.common.file_utils import get_filename_and_extension
from co_op_translator.config.constants import (
    RGB_IMAGE_EXTENSIONS,
    RGBA_IMAGE_EXTENSIONS,
)

logger = logging.getLogger(__name__)


def save_bounding_boxes(image_path, bounding_boxes):
    """
    Save bounding boxes and confidence scores to a JSON file.

    Args:
        image_path (str): Path to the image file.
        bounding_boxes (list): List of bounding boxes and text data.
    """
    base_name = os.path.basename(image_path)
    name, _ = os.path.splitext(base_name)
    output_dir = "./bounding_boxes"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{name}.json")

    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(bounding_boxes, json_file, ensure_ascii=False, indent=4)


def load_bounding_boxes(json_path):
    """
    Load bounding boxes and confidence scores from a JSON file.

    Args:
        json_path (str): Path to the JSON file.

    Returns:
        list: List of bounding boxes and text data.
    """
    with open(json_path, "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def group_bounding_boxes(original_boxes):
    """
    Group bounding boxes into paragraphs based on x-coordinate proximity.

    Args:
        original_boxes (list): Flat list of bounding box dictionaries

    Returns:
        list: List of grouped bounding boxes (list of lists)
    """
    if not original_boxes:
        return []

    grouped = []
    current_group = [original_boxes[0]]

    for box in original_boxes[1:]:
        prev_x = current_group[-1]["bounding_box"][0]
        curr_x = box["bounding_box"][0]

        if abs(curr_x - prev_x) <= 5:
            current_group.append(box)
        else:
            grouped.append(current_group)
            current_group = [box]

    grouped.append(current_group)
    return grouped


def adjust_bg_color(bg_color, factor=0.05):
    avg = sum(bg_color) / 3
    if avg >= 128:
        # For bright colors, reduce each channel by a percentage.
        return tuple(max(int(c * (1 - factor)), 0) for c in bg_color)
    else:
        # For dark colors, increase each channel towards 255 by a percentage.
        return tuple(min(int(c + (255 - c) * factor), 255) for c in bg_color)


def pad_text_image_to_target_aspect(text_img, target_aspect, alignment):
    """
    Pad the text image to approach the target aspect ratio.

    If the text image is too wide (current_aspect > target_aspect), vertical
    padding is added. If it is too narrow, horizontal padding is added according
    to the effective alignment.
    """
    h, w = text_img.shape[:2]
    current_aspect = w / h if h > 0 else 1
    if abs(current_aspect - target_aspect) < 1e-2:
        return text_img

    if current_aspect > target_aspect:
        # Text is too wide: add vertical padding.
        desired_height = int(round(w / target_aspect))
        pad_total = desired_height - h
        pad_top = pad_total // 2
        pad_bottom = pad_total - pad_top
        padded = cv2.copyMakeBorder(
            text_img, pad_top, pad_bottom, 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0, 0]
        )
    else:
        # Text is too narrow: add horizontal padding.
        desired_width = int(round(h * target_aspect))
        pad_total = desired_width - w
        if alignment == "left":
            pad_left = 0
            pad_right = pad_total
        elif alignment == "right":
            pad_left = pad_total
            pad_right = 0
        else:  # center
            pad_left = pad_total // 2
            pad_right = pad_total - pad_left
        padded = cv2.copyMakeBorder(
            text_img, 0, 0, pad_left, pad_right, cv2.BORDER_CONSTANT, value=[0, 0, 0, 0]
        )
    return padded


def get_dominant_color(image, bounding_box, palette_size=16):
    """
    Get the dominant (colour occurring with the highest pixel frequency) of a bounding box area in the image.

    Args:
        image (PIL.Image.Image): The image object.
        bounding_box (list): The bounding box coordinates.
        palette_size (int): The size of the color palette to reduce the image to.

    Returns:
        tuple: The dominant color (R, G, B).
    """
    cropped_image = image.crop(
        (
            min(bounding_box[::2]),
            min(bounding_box[1::2]),
            max(bounding_box[::2]),
            max(bounding_box[1::2]),
        )
    )

    # Crop, resize and use the palette to identify the dominant colour
    cropped_image.thumbnail((400, 400))
    paletted = cropped_image.convert("P", palette=Image.ADAPTIVE, colors=palette_size)
    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[0][1]
    dominant_color = palette[palette_index * 3 : palette_index * 3 + 3]

    return tuple(dominant_color), cropped_image


def get_average_color(image, bounding_box):
    """
    Get the average color of a bounding box area in the image.

    Args:
        image (PIL.Image.Image): The image object.
        bounding_box (list): The bounding box coordinates.

    Returns:
        tuple: The average color (R, G, B).
    """
    mask = Image.new("L", image.size, 0)
    draw = ImageDraw.Draw(mask)
    pts = [
        (bounding_box[i], bounding_box[i + 1]) for i in range(0, len(bounding_box), 2)
    ]
    draw.polygon(pts, fill=255)
    stat = ImageStat.Stat(image, mask)
    avg_color = tuple(int(x) for x in stat.mean[:3])
    return avg_color


def get_text_color(bg_color):
    """
    Determine the grayscale color for text based on background color.

    Args:
        bg_color (tuple): Background color (R, G, B).

    Returns:
        tuple: Text color (R, G, B).
    """
    luminance = (0.299 * bg_color[0] + 0.587 * bg_color[1] + 0.114 * bg_color[2]) / 255
    return (0, 0, 0) if luminance > 0.5 else (255, 255, 255)


def warp_image_to_bounding_box(text_img_array, bounding_box, image_width, image_height):
    """
    Apply a perspective warp to a text image so it fits a (possibly rotated)
    bounding box. The text image is first resized to the rectangle defined by
    the bounding box geometry, then warped.
    """
    pts = np.array(bounding_box, dtype=np.float32).reshape(4, 2)
    # Compute destination width and height.
    widthA = np.linalg.norm(pts[0] - pts[1])
    widthB = np.linalg.norm(pts[2] - pts[3])
    maxWidth = max(int(widthA), int(widthB))
    heightA = np.linalg.norm(pts[0] - pts[3])
    heightB = np.linalg.norm(pts[1] - pts[2])
    maxHeight = max(int(heightA), int(heightB))
    src_pts = np.float32([[0, 0], [maxWidth, 0], [maxWidth, maxHeight], [0, maxHeight]])
    # Resize the padded text image to the computed rectangle.
    resized_text = cv2.resize(text_img_array, (maxWidth, maxHeight))
    matrix = cv2.getPerspectiveTransform(src_pts, pts)
    warped = cv2.warpPerspective(
        resized_text, matrix, (image_width, image_height), flags=cv2.INTER_LINEAR
    )
    return warped


def draw_text_on_image(text, font, text_color):
    """
    Draw text onto an image with a transparent background.

    Args:
        text (str): The text to draw.
        font (PIL.ImageFont.ImageFont): The font object.
        text_color (tuple): The text color (R, G, B).

    Returns:
        PIL.Image.Image: The image with text.
    """
    size = tuple(font.getbbox(text)[2:])  # width and height of the text
    text_image = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_image)
    draw.text((0, 0), text, font=font, fill=text_color)
    return text_image


def create_filled_polygon_mask(bounding_box, image_size, fill_color):
    """
    Create a filled polygon mask for the bounding box area.

    Args:
        bounding_box (list): The bounding box coordinates.
        image_size (tuple): The size of the image (width, height).
        fill_color (tuple): The fill color (R, G, B, A).

    Returns:
        PIL.Image.Image: The mask image.
    """
    mask_image = Image.new("RGBA", image_size, (255, 255, 255, 0))
    mask_draw = ImageDraw.Draw(mask_image)
    pts = [
        (bounding_box[i], bounding_box[i + 1]) for i in range(0, len(bounding_box), 2)
    ]
    mask_draw.polygon(pts, fill=fill_color)
    return mask_image


# Function to Plot Bounding Boxes on Image. Set display=True to display the image in a notebook.
# Saves images to ./analyzed_images
def plot_bounding_boxes(
    image_path, line_bounding_boxes, language_code="en", display=True
):
    # Create output directory if it doesn't exist
    os.makedirs("./analyzed_images", exist_ok=True)

    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    font_size = 20
    # Load the font using FontConfig
    font_config = FontConfig()
    font_path = font_config.get_font_path(language_code)
    font = ImageFont.truetype(font_path, font_size)

    for line_info in line_bounding_boxes:
        print(line_info)
        bounding_box = line_info["bounding_box"]
        confidence = line_info["confidence"]
        pts = [
            (bounding_box[i], bounding_box[i + 1])
            for i in range(0, len(bounding_box), 2)
        ]

        # Draw thicker polygon for bounding box with width parameter
        draw.line(pts + [pts[0]], fill="yellow", width=4)

        # Coordinates for the text
        x, y = bounding_box[0], bounding_box[1] - font_size

        # Draw white text outline
        outline_range = 2
        for dx in range(-outline_range, outline_range + 1):
            for dy in range(-outline_range, outline_range + 1):
                if dx != 0 or dy != 0:
                    draw.text(
                        (x + dx, y + dy),
                        f"{line_info['text']} ({confidence:.2f})",
                        font=font,
                        fill="white",
                    )

        # Draw black text
        draw.text(
            (x, y), f"{line_info['text']} ({confidence:.2f})", font=font, fill="black"
        )

    # Save the annotated image
    output_path = os.path.join("./analyzed_images", os.path.basename(image_path))
    image.save(output_path)

    if display:
        # Display the image
        plt.figure(figsize=(20, 10))
        plt.subplot(1, 2, 1)
        plt.imshow(np.array(image))
        plt.title("Image with Bounding Boxes")
        plt.axis("off")

        original_image = Image.open(image_path)
        plt.subplot(1, 2, 2)
        plt.imshow(np.array(original_image))
        plt.title("Original Image")
        plt.axis("off")

        plt.show()


def display_image(image_path, annotated_image_path):
    """
    Display the original image and the annotated image side by side.

    Args:
        image_path (str): Path to the original image file.
        annotated_image (PIL.Image.Image): The image annotated with translated text.
    """
    plt.figure(figsize=(20, 10))

    # Display the annotated image
    annotated_image = Image.open(annotated_image_path)
    plt.subplot(1, 2, 1)
    plt.imshow(annotated_image)
    plt.title("Annotated Image with Translated Text")
    plt.axis("off")

    # Display the original image
    original_image = Image.open(image_path)
    plt.subplot(1, 2, 2)
    plt.imshow(original_image)
    plt.title("Original Image")
    plt.axis("off")

    plt.show()


def retrieve_bounding_boxes_by_image_path(image_path):
    image_name = os.path.basename(image_path).split(".")[0]
    json_path = f"./bounding_boxes/{image_name}.json"
    if os.path.exists(json_path):
        bounding_boxes = load_bounding_boxes(json_path)
        if os.path.exists(image_path):
            return bounding_boxes
        else:
            print(f"Image file {image_path} does not exist.")
    else:
        print(f"Bounding box data {json_path} does not exist.")


def get_image_mode(image_path):
    """
    Determine the appropriate image mode (RGBA or RGB) based on the file extension.

    Args:
        image_path (str or Path): The path to the image file.

    Returns:
        str: 'RGBA' for PNG files, 'RGB' for JPG/JPEG files.
    """
    extension = get_filename_and_extension(image_path)[1]
    if extension in RGBA_IMAGE_EXTENSIONS:
        return "RGBA"
    elif extension in RGB_IMAGE_EXTENSIONS:
        return "RGB"
    else:
        raise ValueError(f"Unsupported image format: {extension}")
