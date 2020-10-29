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
imagenrgb2gray = rgb2gray(imagen_i)
cv2.imwrite("Imagen_escala_de_grises.jpg",imagenrgb2gray)

imagen_2 = cv2.imread('paisaje.jpg')
imagen_2 = cv2.resize(imagen_2, (512, 256))
imagen2rgb2gray = rgb2gray(imagen_2)
cv2.imwrite('Imagen_paisaje_escala_de_grises.jpg', imagen2rgb2gray)

def blancoynegro(imagen):
    valorF = imagen.shape[0]
    valorC = imagen.shape[1]
    bw = np.zeros((valorF, valorC))
    valorIntermedio = 127
    for x in range (len(bw)):
        for y in range (valorC):
            if imagen[x][y] <= valorIntermedio:
                bw[x][y]  = 0
            else:
                bw[x][y] = 1
     return bw

byn = blancoynegro(imagenrgb2gray)
cv2.imwrite("blanco_negro.jpg", byn)
byn2 = blancoynegro(imagen2rgb2gray)
cv2.imwrite("blanco_negro_paisaje.jpg", byn2)
