import os
import json
import pandas as pd
from PIL import Image
import logging
from config import *
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def process(folder_path):
    output_dir=os.path.join(folder_path,'Results')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
        logging.info(f"Created Directory: {output_dir}")
        
    for file_name in os.listdir(folder_path):
        try:
            file_path=os.path.join(folder_path,file_name)
            img_id=os.path.splitext(os.path.basename(file_name))[0]
            logging.info(f"Extracting: {file_name}")
            img=Image.open(file_path)
            response = model.generate_content([prompt, img],safety_settings=safe)
            result=json.loads(response.text.strip('`json\\n'))

            df=pd.DataFrame(result)
            df.insert(0,'file_name',file_name)        
            df.to_csv(os.path.join(output_dir,f"{img_id}.csv"),index=False)
            logging.info(f"Results saved for image : {file_name}")
        except Exception as e:
            logging.error(f"Error processing image {file_name}: {e}")
    return output_dir