import cv2 as cv
import numpy as np

imagenOriginal=cv.imread('floppa.jpg')
imagenEngris=cv.imread('floppa.jpg',0)

filtro_gaussiano = np.array([[2,4,5,4,2],
                            [4,9,12,9,4],
                            [5,12,15,12,5],
                            [4,9,12,9,4],
                            [2,4,5,4,2]])
cv.imshow('imagenen gris',imagenEngris)
cv.waitKey()
cv.imshow('imagen original',imagenOriginal)
cv.waitKey()

print(np.shape(imagenOriginal))
print(np.shape(imagenEngris))
filas,columnas,canales=np.shape(imagenOriginal)

filas,columnas=np.shape(imagenEngris)


imagenEngrisParafiltro5x5=imagenEngris.copy()


for fila in range(2,filas-2):
    for columna in range(2,columnas-2):
        suma=0
        for filaK in range(fila-2,fila+3):
            for colK in range(columna-2,columna+3):
                suma=suma+imagenEngris[filaK][colK]

        imagenEngrisParafiltro5x5[fila][columna]=suma/25
    
cv.imshow('filtro de medias 5x5',imagenEngrisParafiltro5x5)
cv.waitKey()
