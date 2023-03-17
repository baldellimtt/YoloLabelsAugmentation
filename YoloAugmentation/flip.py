import os
import cv2
import numpy as np
import sys

# The first argument is the name of the script itself, so we skip it
args = sys.argv[1:]

# Check if there are any arguments
if not args:
    print("No arguments provided")

input_dir = args[0] # directory containing all files to read (ex: *.png and *.txt)
flip = args[1] # [0 if flip v, 1 if flip h, -1 both vertical and horizontal] (ex: [0] or [1] or [-1])
flip = int(flip)
output_dir = 'output'

exist = os.path.exists(output_dir)
if not exist:
   # Create a new directory because it does not exist
   os.makedirs(output_dir)

if(flip == 0):
    CONST = '/flipped_v_'
elif(flip == 1):
    CONST = '/flipped_h_'
elif(flip == -1):
    CONST = '/flipped_h_v_'


# Loop attraverso tutti i file nella directory
for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # read image and label
        image_ext = os.path.splitext(filename)[1]
        image_name = os.path.splitext(filename)[0]

        # if i find a correspondent txt I start augmentation
        label_path = os.path.join(input_dir, os.path.splitext(filename)[0] + ".txt")
        if os.path.exists(label_path):
            # Read image using cv2

            image_file = input_dir + '/' + filename
            image = cv2.imread(image_file, 1)

            # flip the image by:
            # flip = 0 -> vertically
            # flip = 1 -> horizontally
            # flip = -1 -> both vertically and horizontally
            img_flipped = cv2.flip(image, flip)

            # read bounding box from txt file
            bb_image_file = input_dir + '/' + image_name + ".txt"
            with open(bb_image_file, "r") as file_r:
                data = file_r.readlines()

            # bbox = [class_index, x_center, y_center, width, height]
            # we update x_center if flip = 1 (horizontal)
            # we update y_center if flip = 0 (vertical) 
            # we update both x_center and y_center if flip = -1  
            output_file_bb = output_dir + CONST + image_name + '.txt'

            if flip == 0: # vertical flip
                indexToUpdate = 2
            elif flip == 1: # horizontal flip
                indexToUpdate = 1
            elif flip == -1: # both horizontal and vertical
                indexToUpdate = 1
                secondIndexToUpdate = 2

            with open(output_file_bb, "w") as file_w:
                for bboxes in data:
                    bbox = bboxes.strip().split()
                    bbox[indexToUpdate] = round(1.0 - float(bbox[indexToUpdate]), 4)
                    if(flip == -1):
                        bbox[secondIndexToUpdate] = round(1.0 - float(bbox[secondIndexToUpdate]), 4)

                    file_w.write(f"{bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]} {bbox[4]}\n")

            # to write rotateed image to disk
            output_img = output_dir + CONST + filename
            cv2.imwrite(output_img, img_flipped)





