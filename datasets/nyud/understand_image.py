import os
import numpy as np
from PIL import Image

root_dir= './'


img_name = './train_labels/000003.png'

img = Image.open(img_name)

image = np.array(img)

color = img.getcolors()
print color	
print(img.palette)
print(img.mode)
print(img)
print(image.shape)
