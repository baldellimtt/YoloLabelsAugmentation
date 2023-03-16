# YoloLabelsAugmentation
Scripts and samples to augment yolo annotations: txt annotations and images to be augmented must be located inside "dataset" folder, as described in the example.
Augmented will be saved in "output". 
In my project I needed rotations, change in contrast and blurring.


# Basic Example
Suppose you have to develop a Glenn Danzig detector, and you have to augment annotations like this:

![alt text](https://user-images.githubusercontent.com/62099945/225581976-0c582baf-586a-45d3-b928-6c419b3ca947.jpg)

after running the script you will find in output directory images and annotations like this:

90 degree rotation:

![alt text](https://user-images.githubusercontent.com/62099945/225583347-bcb0157e-e427-4873-a2f7-b2a882fabe44.jpg)

180 degree rotation:

![alt text](https://user-images.githubusercontent.com/62099945/225583462-98b4bafe-c646-484f-b3f3-f6d6dec70059.jpg)

270 degree rotation:

![alt text](https://user-images.githubusercontent.com/62099945/225583572-98e97bc5-ba4d-4680-994b-ed09edc85d54.jpg)

All images are slightly blurred and have randomly changed contrast, but you can simply implement your own augmentations.
If images inside dataset directory have no txt annotations will be considered background and augmented without annotations.
