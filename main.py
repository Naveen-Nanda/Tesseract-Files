def file_size(fname):
        import os
        
        statinfo = os.stat(fname)
        return statinfo.st_size


import os
import cv2
import numpy as np
kernel = np.ones((2,2),np.uint8)
for i in range(1,453):
        path = 'C:/Users/nannavee/Desktop/Important/Crop_New-Copy/'+str(i)+'.tif'
        gray = cv2.imread(path)
        ret, thresh1 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
        print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/tesseract.exe C:/Users/nannavee/Desktop/Important/crop_2/%d.tif %d --psm 6 -l eng lstmbox"'%(i,i)))

#for j in range(2152,2172):
#    path = 'C:/Users/nannavee/Desktop/crop/' +str(j)+ '.box'
#    if file_size(path)==0:
#        img = cv2.imread('C:/Users/nannavee/Desktop/crop/' +str(j)+ '.jpg')
#        resize = cv2.resize(img,(169,25),interpolation = cv2.INTER_AREA)
#        opening = cv2.morphologyEx(resize, cv2.MORPH_OPEN, kernel)
#        denoise = cv2.fastNlMeansDenoisingColored(opening,None,20,10,7,21)
#        ret, threshold = cv2.threshold(denoise, 120, 255, cv2.THRESH_BINARY_INV)
#        cv2.imwrite(str(j)+'.tif',threshold)
#        print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/tesseract.exe C:/Users/nannavee/Desktop/crop/%d.tif %d -l eng wordstrbox"'%(j,j)))
   
 #   else:
 #       print("All good %d"%(j))


# Function to rename multiple files
#def main():
 #  i = 274
 #  path="C:/Users/nannavee/Desktop/Important/crop_3/"
  # for filename in os.listdir(path):
   #   my_dest =str(i) + ".jpg"
    #  my_source =path + filename
     # my_dest =path + my_dest
      # rename() function will
      # rename all the files
    #  os.rename(my_source, my_dest)
    #  i += 1
# Driver Code
#if __name__ == '__main__':
   # Calling main() function
#   main()







#dilation = cv2.dilate(resized,kernel,iterations = 1)
    #print(os.system('cmd /c "C:/Users/nannavee/AppData/Local/Tesseract-OCR/tesseract.exe C:/Users/nannavee/Desktop/Snipped_Images/%d.box %d --psm 6 lstm.train "'%(i,i)))



    
