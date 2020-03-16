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






WD = r'C:/Users/nannavee/Desktop/Important/Crop_New/'
files = glob.glob(os.path.join(WD, '*.lstmf'))
with open('eng.train_files.txt', 'w') as in_files:
    in_files.writelines(fn + '\n' for fn in files)





#fie tuning
print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/lstmtraining.exe --model_output C:/Users/nannavee/AppData/Local/tesstutorial/necessary_files/tess4tutorial/eng_layer_eng/eng.lstm --traineddata C:/Users/nannavee/AppData/Local/tesstutorial/necessary_files/tess4tutorial/trainlayer/eng/eng.traineddata --tr
ain_listfiles C:/Users/nannavee/Desktop/Important/Crop_New/eng.train_files.txt --continue_from C:/Users/nannavee/AppData/Local/tesstutorial/necessary_files/tess4tutorial/eng_layer_eng/layer_checkpoint max_iteration 10'"))
              
              
