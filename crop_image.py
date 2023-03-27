import os
import cv2

# Change working directory
os.chdir(r"/Users/sunnywang/Library/CloudStorage/OneDrive-McGillUniversity/Research/Farivar lab/stimuli/raw_img")

# Load image
img_name = 'mgh'
uncropped_img = cv2.imread(img_name+'.jpg')

# Crop image to 512:512
img = uncropped_img[200:200+512, 300:300+512]

# Check size & channel number -->  supposed to be (512,512,3)
print('img:',img.shape) 

name = img_name+'.jpg'

os.chdir(r"/Users/sunnywang/Library/CloudStorage/OneDrive-McGillUniversity/Research/Farivar lab/stimuli/original_img")
cv2.imwrite(name, img)
cv2.imshow(name,img)
cv2.waitKey(2000)