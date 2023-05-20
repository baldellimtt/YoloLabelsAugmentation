************* FLIP = python flip.py "path/to/input" flip *************    
(esempio: python flip.py "src/dataset" 1)

flip = 0 -> vertical flip,
flip = 1 -> horizontal flip,
flip = -1 -> horizontal + vertical flip

************* ROTATE = python rotate.py "path/to/input" "[90, 120, ...]" *************  
(esempio: python rotate.py "src/dataset" "[90, 12]")


NB: specificare solo il path contenente le immagini da flippare/ruotare, in automatico verrà creata una cartella "output"
La cartella deve contenere sia le immagini sia il file con i boundingbox corrispondente:
es: la cartella src/dataset contiene: 
											img1.png  --> immagine
											img1.txt  --> bounding box
											img2.png
											img2.txt
											img3.png
											img3.txt
											...