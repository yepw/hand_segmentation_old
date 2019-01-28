import os
import numpy as np
from PIL import Image

root_dir= './'


img_name = './s1_cheese_0000000460.png'

def read_image(x):
    img_arr = np.array(Image.open(x).resize((625,468)))
    if len(img_arr.shape) == 2: # grayscale
	print('grayscale')
        img_arr = np.tile(img_arr, [3, 1, 1]).transpose(1, 2, 0) 
    return img_arr
        
image = read_image(img_name)
	
print(image)
