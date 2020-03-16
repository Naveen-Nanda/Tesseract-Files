#import os

#for i in range(600,621):
#    print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/tesseract.exe C:/Users/nannavee/Desktop/crop/%d.jpg %d --psm 6 lstm.train"'%(i,i)))

#print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/tesseract.exe C:/Users/nannavee/Desktop/crop/600.jpg 600 --psm 6 lstm.train"'))



import os
def file_size(fname):
        
        statinfo = os.stat(fname)
        return statinfo.st_size

#print("File size in bytes of a plain file: ",file_size("test.txt"))

from PIL import Image
for i in range(179,453):
    path = 'C:/Users/nannavee/Desktop/Important/crop_2/' +str(i) + '.jpg'
    #if print(os.path.exists(path)) == 1:
    im = Image.open(path)
    im.save('C:/Users/nannavee/Desktop/Important/crop_2/' +str(i)+ '.tif')
    #else:
     #       print("no file")

#for i in range(3000,4599):
 #       path = 'C:/crop/' +str(i) +'.jpg'
  #      if file_size(path) == 0:
   #             os.remove(path)
    #    else:
     #           print("All ok")

