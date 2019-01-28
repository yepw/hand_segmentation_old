import os
import random

root = "/home/intuitivecomputing/light-weight-refinenet/datasets/GTEA/Images"

f1 = open('train.gtea', 'w')
f2 = open('val.gtea', 'w')

for path, subdirs, files in os.walk(root):
    for name in files:
        print name
	if random.random()<0.8:
	    mask_name = name[0:len(name)-3]+'png'
            f1.write('Images/'+name+'\t'+'Masks/'+mask_name+'\n')
	else:
  	    mask_name = name[0:len(name)-3]+'png'
            f2.write('Images/'+name+'\t'+'Masks/'+mask_name+'\n')
f1.close()
f2.close()
	    
