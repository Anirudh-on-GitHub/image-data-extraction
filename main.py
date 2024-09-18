import sys
import os
import logging
from image_processing import correct_image_orientation
from data_extraction import process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process_folder(folder_path):
    num=0
    for img_name in os.listdir(folder_path):
        if img_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            base_name = f"file{num}.png"
            new_img_path = os.path.join(folder_path, base_name)
            while os.path.exists(new_img_path):
                num += 1
                base_name = f"file{num}.png"
                new_img_path = os.path.join(folder_path, base_name)
            
            os.rename(os.path.join(folder_path, img_name), new_img_path)
            num += 1
    results_path=process(folder_path)
    return results_path


def main():
    if len(sys.argv) !=2:
        logging.error("Usage: python main.py <folder_path>")
        sys.exit(1)
    folder_path=sys.argv[1]
    results_path=process_folder(folder_path)
    print(f"Results saved in : {results_path}")

if __name__== "__main__":
    main()