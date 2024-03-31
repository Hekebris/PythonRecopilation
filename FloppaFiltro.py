import numpy as np
import cv2 as cv

floppa = cv.imread('floppa.jpg', 0)
confiltro = floppa.copy()
filtrog = np.array([[1,5,10,5,1],
                            [5,15,20,15,5],
                            [10,20,40,20,10],
                            [5,15,20,15,5],
                            [1,5,10,5,1]])

filas, columnas = np.shape(floppa)

for fila in range(2,filas-2):
    for columna in range(2,columnas-2):
        suma = 0
        i = 0
        for fk in range(fila-2, fila+3):
            j = 0
            for ck in range(columna-2, columna+3):
                suma = suma + floppa[fk][ck] * filtrog[i][j]
            
                j += 1
            i += 1
        confiltro[fila][columna] = suma/290
  
cv.imshow('floppa sin instagram', floppa)
cv.imshow('floppa con instagram', confiltro)
cv.waitKey()