import os

os.remove('D:/Important/Tesseract-OCR/tessdata/eng.traineddata')

print(os.system('cmd /c "D:/Important/Tesseract-OCR/lstmtraining.exe --stop_training --continue_from D:/Important/_checkpoint --traineddata C:/Users/praarun1/Desktop/eng.traineddata --model_output D:/Important/Tesseract-OCR/tessdata/"'))

os.rename('lstmtrain','eng.traineddata')
