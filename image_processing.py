import os
import logging
from PIL import Image
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def correct_image_orientation(image_path):
    try:
        img=Image.open(image_path)
        if img.height-img.width>250:
            img = img.rotate(90, expand=True)
            img.save(image_path)
            logging.info(f"Rotated image:{image_path}")
    except Exception as e:
        logging.error(f"Error processing image {image_path}:{e}")
    