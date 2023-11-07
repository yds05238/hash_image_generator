import os 
import time 
from PIL import Image

import blurhash 

# PATHS
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
INPUTS_DIR = os.path.join(CURR_DIR, 'inputs')
OUTPUTS_DIR = os.path.join(CURR_DIR, 'outputs')

def main():
    # Generate blurhashes for all images in the inputs directory
    for image_name in os.listdir(INPUTS_DIR):
        time.sleep(0.5)
        
        image_path = os.path.join(INPUTS_DIR, image_name)
        with Image.open(image_path) as f:
            hash_string = blurhash.encode(f, x_components=3, y_components=5)
            
            
        hash_image = blurhash.decode(hash_string, f.size[0], f.size[1])
        out_image_path = os.path.join(OUTPUTS_DIR, image_name)
        hash_image.save(out_image_path)
        
        print(f'Image {image_name} has been processed')
        
    

if __name__ == '__main__':
    main()
