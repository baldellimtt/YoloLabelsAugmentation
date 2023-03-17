import os
import numpy as np
import cv2
import sys
import ast
from utils import rotationUtils

# The first argument is the name of the script itself, so we skip it
args = sys.argv[1:]

# Check if there are any arguments
if not args:
    print("No arguments provided")

input_dir = args[0] # directory containing all files to read (ex: *.png and *.txt)
angles = args[1].strip('[]').split(',') # rotation degree angles Ex: angles = [90, 180, 270]
output_dir = 'output'

# Loop attraverso tutti i file nella directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # read image and label
        image_ext = os.path.splitext(filename)[1]
        image_name = os.path.splitext(filename)[0]

        # if i find a correspondent txt I start augmentation
        label_path = os.path.join(input_dir, os.path.splitext(filename)[0] + ".txt")
        if os.path.exists(label_path):
            for angle in angles:
                angle = float(angle)
                im = rotationUtils.YoloRotationUtils(input_dir + '/' + image_name, image_ext, angle)
                bbox = im.rotateYolobbox()
                image = im.rotate_image()

                #change randomly contrast of image
                contrast = np.random.uniform(0.7, 1.3)
                image = np.clip(image * contrast, 0, 255).astype(np.uint8)

                #slighly blur image
                blur_radius = 1
                image = cv2.GaussianBlur(image, (blur_radius, blur_radius), 0)
                # to write rotateed image to disk
                cv2.imwrite(output_dir + '/rotated_'+image_name+'_' + str(angle) + image_ext, image)

                # to write rotateed label to disk
                file_name = output_dir + '/rotated_'+image_name+'_' + str(angle) + '.txt'
                if os.path.exists(file_name):
                    os.remove(file_name)

                # to write the new rotated bboxes to file
                for i in bbox:
                    with open(file_name, 'a') as fout:
                        fout.writelines(
                            ' '.join(map(str, im.cvFormattoYolo(i, im.rotate_image().shape[0], im.rotate_image().shape[1]))) + '\n')



