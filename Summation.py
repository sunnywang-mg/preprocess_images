# By Sunny Wang in March 2023

import os
import cv2
import numpy as np
import math

# Set working directory
os.chdir(r"")

def final_loop():

    # Close prevoious windows
    cv2.destroyAllWindows()
    cv2.waitKey(100)

    # Ask for image type
    result_img_type = input('what type of images are you producing(e.g 1+3):')
    if result_img_type not in['1+3','2+4','1+4','2+3']:
        print('re-enter bandpass filter type!')
        final_loop()

    # Set two groups of images based on sigma value
    if result_img_type == '1+3':
        folder1_sig = 1.0
        folder2_sig = 3.0
    elif result_img_type == '2+4':
        folder1_sig = 2.0
        folder2_sig = 4.0
    elif result_img_type == '1+4':
        folder1_sig = 1.0
        folder2_sig = 4.0
    elif result_img_type == '2+3':
        folder1_sig = 2.0
        folder2_sig = 3.0

    # Read names of the less blurry images
    img1_path_list= []
    folder1 = '/base'+str(folder1_sig)
    for img1_path in os.listdir(folder1):
        if img1_path != '.DS_Store':
            img1_path_list.append(img1_path)
    img1_path_list.sort()
    print (img1_path_list)

    # Read in names of the more blurry images
    img2_path_list= []

    folder2 = '/base'+str(folder2_sig)
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
        img1 = cv2.imread(folder1+'/'+img1_name)/256

        if isinstance(img1,np.ndarray):
            print('img1 is type numpy ndarray --> Continue')
        else:
            raise ValueError('img1 has to be type numpy ndarray!')

        # Get name for result image
        result_img_name = img1_name.replace('_sigd2.0_'+'base'+str(folder1_sig)+'.png','')

        # Load img2
        img2_name = img2_path_list[index]
        img2 = cv2.imread(folder2+'/'+img2_name)/256
        if isinstance(img2,np.ndarray):
            print('img2 is type numpy ndarray --> Continue')
        else:
            raise ValueError('img2 has to be type numpy ndarray!')

        # Produce bandpass image
        result = img1+img2

        # Normalize image
        #result = cv2.normalize(result, None, 0.0, 0.5, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        result = cv2.convertScaleAbs(result, alpha=(255.0))
        result = result.astype('uint8')

        cv2.imshow('result_img_name',result)
        cv2.waitKey(300)

        # Save images to path
        os.chdir(r""+result_img_type)
        cv2.imwrite(result_img_name+result_img_type+'.png',result)

        # Calculate mean intensity
        mean_intensity = np.mean(result)

        # Calculate RMS
        variance = np.var(result)
        root_mean_square = math.sqrt(variance)

        # Write in intensity information

        os.chdir(r"/Users/sunnywang/Library/CloudStorage/OneDrive-McGillUniversity/Research/Farivar lab/stimuli/experiment_img")
        filename= 'img_intensity_info.csv'
        f = open(filename, "a")
        f.write (result_img_name+','+result_img_type+', '+str(round(mean_intensity,6))+', '+str(round(root_mean_square,6)))
        f.write ('\n')
        f.close()

        index+=1 

if __name__ == "__main__":
    final_loop()
