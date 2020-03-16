import os
import glob

path = 'C:/Users/nannavee/Desktop/Important/Crop_New/'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.lstmf' in file:
            files.append(os.path.join(r, file))
with open('data.txt','w') as f:
    for z in files:
        f.write(z + '\n')
    
  
