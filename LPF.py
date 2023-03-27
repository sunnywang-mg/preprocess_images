from scipy import ndimage
import os
import cv2
import math
import numpy as np


folder = '/Users/sunnywang/Library/CloudStorage/OneDrive-McGillUniversity/Research/Farivar lab/stimuli/original_img'

for img_path in os.listdir(folder):
    if img_path != '.DS_Store':
        img = cv2.imread(folder+'/'+img_path)
        sigma = 6.0

        gaussian_LP = (ndimage.gaussian_filter(img, sigma=(sigma, sigma, 0)))
        #gaussian_LP = cv2.convertScaleAbs(gaussian_LP, alpha=(255.0))
        gaussian_LP = gaussian_LP.astype('uint8')

        # Show and save output image
        name = img_path.replace('.jpg','')

        os.chdir(r'/Users/sunnywang/Library/CloudStorage/OneDrive-McGillUniversity/Research/Farivar lab/stimuli/LPF_sig='+str(round(sigma,2)))
        cv2.imwrite(name+'_sig='+str(round(sigma,2))+'.png',gaussian_LP)
        cv2.imshow("", gaussian_LP)
        cv2.waitKey(200)