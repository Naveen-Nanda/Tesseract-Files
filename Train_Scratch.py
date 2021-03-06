import os
import cv2
import numpy as np
from PIL import Image
import glob

path = 'C:/Users/nannavee/Desktop/Important/Crop_New/'
def file_size(fname):
        statinfo = os.stat(fname)
        return statinfo.st_size

size = len(os.listdir(path))
for i in range(1,size+1):
    path = 'C:/Users/nannavee/Desktop/Important/Crop_New/' +str(i) + '.jpg'
    im = Image.open(path)
    im.save('C:/Users/nannavee/Desktop/Important/Crop_New/' +str(i)+ '.tif')
    os.remove('C:/Users/nannavee/Desktop/Important/Crop_New/'+str(i)+'.jpg)

   
for j in range(1,size+1):
        new_path = 'C:/Users/nannavee/Desktop/Important/Crop_New/'+str(j)+'.tif'
        gray = cv2.imread(new_path)
        ret, thresh1 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        cv2.imwrite('C:/Users/nannavee/Desktop/Important/Crop_New/'+str(j)+'.tif',gray)
        print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/tesseract.exe C:/Users/nannavee/Desktop/Important/Crop_New/%d.tif %d --psm 6 -l lstmbox"'%(j,j)))
        print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/tesseract.exe C:/Users/nannavee/Desktop/Important/Crop_New/%d.tif %d --psm 6 lstm.train"'%(j,j)))




#At iteration 16636/92000/92000, Mean rms=0.219%, delta=0.388%, char train=1.12%, word train=2.275%, skip ratio=0%,  New worst char error = 1.12 wrote checkpoint.


files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.lstmf' in file:
            files.append(os.path.join(r, file))
with open('eng.traineddata.txt','w') as f:
    for z in files:
        f.write(z + '\n')
    



# train from scratch
print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR>lstmtraining.exe --traineddata C:/Users/nannavee/AppData/Local/tesstutorial/necessary_files/tess4tutorial/trainlayer/eng/eng.traineddata --train_listfile C:/Users/nannavee/Desktop/eng.traineddata.txt --net_spec "[1,36,0,1 Ct3,3,16 Mp3,3 Lfys48 Lfx96 Lrx9
6 Lfx256 O1c111]" --model_output C:/Users/nannavee/AppData/Local/tesstutorial/engout --eval_listfile C:/Users/nannavee/AppData/Local/tesstutorial/necessary_files/tess4tutorial/evallayer/eng.evaltext.txt max_iterations 5000"'))

#fine tuning
print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/lstmtraining.exe --model_output C:/Users/nannavee/AppData/Local/tesstutorial/necessary_files/tess4tutorial/eng_layer_eng/eng.lstm --traineddata C:/Users/nannavee/AppData/Local/tesstutorial/necessary_files/tess4tutorial/trainlayer/eng/eng.traineddata --tr
ain_listfiles C:/Users/nannavee/Desktop/Important/Crop_New/eng.train_files.txt --continue_from C:/Users/nannavee/AppData/Local/tesstutorial/necessary_files/tess4tutorial/eng_layer_eng/layer_checkpoint max_iteration 10'"))
              
              
