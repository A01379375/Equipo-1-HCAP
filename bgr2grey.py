import numpy as np
import cv2

def rgb2gray(A):
    filas = len(A)
    columnas = len(A[0])
    B = np.zeros((filas,columnas))
    for i in range(filas):
        for j in range(columnas):
            B[i][j] = (A[i][j][0]*0.07 + A[i][j][1]*0.72 + A[i][j][2]*0.21)
    return B


imagen_i = cv2.imread("imagen.jpg")
print(imagen_i.shape)
imagenrgb2gray = rgb2gray(imagen_i)
cv2.imwrite("Imagen_escala_de_grises.jpg",imagenrgb2gray)
