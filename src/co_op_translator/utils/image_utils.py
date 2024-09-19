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
from co_op_translator.utils.file_utils import get_filename_and_extension

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
    pts = [(bounding_box[i], bounding_box[i+1]) for i in range(0, len(bounding_box), 2)]
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

def warp_image_to_bounding_box(image, bounding_box, image_width, image_height):
    """
    Apply perspective warp to a text image to fit the bounding box.
    
    Args:
        image (numpy.ndarray): The text image array.
        bounding_box (list): The bounding box coordinates.
        image_width (int): The width of the output image.
        image_height (int): The height of the output image.
        
    Returns:
        numpy.ndarray: The warped image array.
    """
    h, w = image.shape[:2]
    src_pts = np.float32([[0, 0], [w, 0], [w, h], [0, h]])
    dst_pts = np.float32([(bounding_box[i], bounding_box[i+1]) for i in range(0, len(bounding_box), 2)])
    matrix = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(image, matrix, (image_width, image_height))
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
    size = font.getbbox(text)[2:]  # width and height of the text
    text_image = Image.new('RGBA', size, (255, 255, 255, 0))
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
    mask_image = Image.new('RGBA', image_size, (255, 255, 255, 0))
    mask_draw = ImageDraw.Draw(mask_image)
    pts = [(bounding_box[i], bounding_box[i+1]) for i in range(0, len(bounding_box), 2)]
    mask_draw.polygon(pts, fill=fill_color)
    return mask_image

# Function to Plot Bounding Boxes on Image. Set display=True to display the image in a notebook.
# Saves images to ./analyzed_images
def plot_bounding_boxes(image_path, line_bounding_boxes, language_code="en", display=True):
    # Create output directory if it doesn't exist
    os.makedirs('./analyzed_images', exist_ok=True)
    
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    font_size = 20
    # Load the font using FontConfig
    font_config = FontConfig()
    font_path = font_config.get_font_path(language_code)
    font = ImageFont.truetype(font_path, font_size)
    
    for line_info in line_bounding_boxes:
        print(line_info)
        bounding_box = line_info['bounding_box']
        confidence = line_info['confidence']
        pts = [(bounding_box[i], bounding_box[i+1]) for i in range(0, len(bounding_box), 2)]
        
        # Draw thicker polygon for bounding box with width parameter
        draw.line(pts + [pts[0]], fill="yellow", width=4)
        
        # Coordinates for the text
        x, y = bounding_box[0], bounding_box[1] - font_size

        # Draw white text outline
        outline_range = 2
        for dx in range(-outline_range, outline_range + 1):
            for dy in range(-outline_range, outline_range + 1):
                if dx != 0 or dy != 0:
                    draw.text((x + dx, y + dy), f"{line_info['text']} ({confidence:.2f})", font=font, fill="white")

        # Draw black text
        draw.text((x, y), f"{line_info['text']} ({confidence:.2f})", font=font, fill="black")
    
    # Save the annotated image
    output_path = os.path.join('./analyzed_images', os.path.basename(image_path))
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
    if extension in ['.png']:
        return 'RGBA'
    elif extension in ['.jpg', '.jpeg']:
        return 'RGB'
    else:
        raise ValueError(f"Unsupported image format: {extension}")
