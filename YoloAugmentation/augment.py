import os
import numpy as np
import cv2
from src.yolo import yoloRotatebbox,cvFormattoYolo

# Definisci la directory in cui si trovano le immagini e le label
dir_path = "dataset"
output = "output/"

# Definisci l'angolo di rotazione desiderato
angles = [90, 180, 270]

# Loop attraverso tutti i file nella directory
for filename in os.listdir(dir_path):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
        # Leggi l'immagine
        image_ext = os.path.splitext(filename)[1]
        image_name = os.path.splitext(filename)[0]


        # Se esiste un file di label corrispondente, ruota anche quello
        label_path = os.path.join(dir_path, os.path.splitext(filename)[0] + ".txt")
        if os.path.exists(label_path):
            for angle in angles:
                im = yoloRotatebbox(dir_path + '/' + image_name, image_ext, angle)

                bbox = im.rotateYolobbox()
                image = im.rotate_image()

                contrast = np.random.uniform(0.7, 1.3)
                image = np.clip(image * contrast, 0, 255).astype(np.uint8)

                blur_radius = 1
                image = cv2.GaussianBlur(image, (blur_radius, blur_radius), 0)
                # to write rotateed image to disk
                cv2.imwrite(output + 'rotated_'+image_name+'_' + str(angle) + image_ext, image)

                file_name = output + 'rotated_'+image_name+'_' + str(angle) + '.txt'
                if os.path.exists(file_name):
                    os.remove(file_name)

                # to write the new rotated bboxes to file
                for i in bbox:
                    with open(file_name, 'a') as fout:
                        fout.writelines(
                            ' '.join(map(str, cvFormattoYolo(i, im.rotate_image().shape[0], im.rotate_image().shape[1]))) + '\n')
