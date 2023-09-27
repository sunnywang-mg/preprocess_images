# By Sunny Wang in March 2023
# Difference of Gaussian (DOG) Bandpass image filter

import os
import cv2
import numpy as np
import math


def BPF_loop():

    # Close prevoious windows
    cv2.destroyAllWindows()
    cv2.waitKey(100)

    # Ask for image type
    result_img_type = input('what type of images are you producing(e.g base1.0):')
    if result_img_type not in['base1.0','base2.0','base3.0','base4.0']:
        print('re-enter bandpass filter type!')
        BPF_loop()

    # Set two groups of images based on sigma value
    if result_img_type == 'base1.0':
        folder1_sig = 1.0
        folder2_sig = 3.0
    elif result_img_type == 'base2.0':
        folder1_sig = 2.0
        folder2_sig = 4.0
    elif result_img_type == 'base3.0':
        folder1_sig = 3.0
        folder2_sig = 5.0
    elif result_img_type == 'base4.0':
        folder1_sig = 4.0
        folder2_sig = 6.0

    # Read names of the less blurry images
    img1_path_list= []
    folder1 = ''+str(folder1_sig)
    for img1_path in os.listdir(folder1):
        if img1_path != '.DS_Store':
            img1_path_list.append(img1_path)
    img1_path_list.sort()
    print (img1_path_list)

    # Read in names of the more blurry images
    img2_path_list= []

    folder2 = ''+str(folder2_sig)
    for img2_path in os.listdir(folder2):
        if img2_path != '.DS_Store':
            img2_path_list.append(img2_path)
    img2_path_list.sort()
    print (img2_path_list)

    # Check if there is equal number of img1 and img2
    if len(img1_path_list)!= len(img2_path_list):
        raise ValueError('There is an unequal number of images in two folders!')
    else:
        print('There is an equal number of images in two folders --> Continue')

    # Acess image by index in path_list
    index = 0
    while index < len(img1_path_list):

        # Load img1
        img1_name = img1_path_list[index]
        img1 = cv2.imread(folder1+'/'+img1_name,0)/256

        if isinstance(img1,np.ndarray):
            print('img1 is type numpy ndarray --> Continue')
        else:
            raise ValueError('img1 has to be type numpy ndarray!')

        # Get name for result image
        result_img_name = img1_name.replace('_sig='+str(folder1_sig)+'.png','')

        # Load img2
        img2_name = img2_path_list[index]
        img2 = cv2.imread(folder2+'/'+img2_name,0)/256
        if isinstance(img2,np.ndarray):
            print('img2 is type numpy ndarray --> Continue')
        else:
            raise ValueError('img2 has to be type numpy ndarray!')

        # Produce bandpass image
        result = img1-img2

        # Normalize image
        result = cv2.normalize(result, None, 0.0, 0.5, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        result = cv2.convertScaleAbs(result, alpha=(255.0))
        result = result.astype('uint8')

        cv2.imshow('result_img_name',result)
        cv2.waitKey(500)

        # Save images to path
        os.chdir(r""+result_img_type)
        cv2.imwrite(result_img_name+'_'+'sigd2.0_'+result_img_type+'.png',result)


        index+=1 


if __name__ == "__main__":
    BPF_loop()
