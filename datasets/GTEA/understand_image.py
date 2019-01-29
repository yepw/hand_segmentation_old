import os
import numpy as np
from PIL import Image

root_dir= './'


img_name = './Masks/s1_cheese_0000000460.png'

img = Image.open(img_name)
	
image = np.array(img)

color = img.getcolors()
print color

print(image)
