import os
import random
from PIL import Image

root = "/home/intuitivecomputing/light-weight-refinenet/datasets/GTEA/Images"

f1 = open('train.gtea', 'w')
f2 = open('val.gtea', 'w')

for path, subdirs, files in os.walk(root):
    for name in files:
        print name
	im = Image.open('Images/'+name).resize((625,468))
	name = name[0:len(name)-3]+'png'
	im.save('Images/'+name)
	if random.random()<0.8:
            f1.write('Images/'+name+'\t'+'Masks/'+name+'\n')
	else:
            f2.write('Images/'+name+'\t'+'Masks/'+name+'\n')
	
f1.close()
f2.close()
	    
