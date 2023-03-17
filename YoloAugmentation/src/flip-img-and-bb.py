import os
import cv2
import numpy as np
    

class yoloFlipbbox:

    def __init__(self, input_path, output_path, image_ext):
        assert os.path.isfile(input_path + image_ext)
        assert os.path.isfile(input_path + '.txt')

        self.input_path = input_path
        self.output_path = output_path
        self.image_ext = image_ext

        # Read image using cv2
        self.image = cv2.imread(self.input_path + self.image_ext, 1)
    
    def horizontal_flip_yolo(self):

        # flip the image by horizontally
        img_v = cv2.flip(self.image, 1)

        # read bounding box from txt file
        with open(self.input_path, "r") as file_r:
            data = file_r.readlines()

        flipped_data = []
        with open(self.output_path, "w") as file_w:
            for bboxes in data:
                bbox = bboxes.strip().split() 
                bbox[1] = round(1.0 - float(bbox[1]), 4)
                flipped_data.append(bbox)

                file_w.write(f"{bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]} {bbox[4]}\n")
        return img_v

    def vertical_flip_yolo(self):

        # flip the image by vertically
        img_v = cv2.flip(self.image, 0)

        # read bounding box from txt file
        with open(self.input_path, "r") as file_r:
            data = file_r.readlines()

        flipped_data = []
        with open(self.output_path, "w") as file_w:
            for bboxes in data:
                bbox = bboxes.strip().split()
                bbox[2] = round(1.0 - float(bbox[2]), 4)
                flipped_data.append(bbox)

                file_w.write(f"{bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]} {bbox[4]}\n")
        return img_v
