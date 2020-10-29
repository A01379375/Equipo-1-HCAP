import numpy as np
import cv2

#A escala de grises
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

#Funcion que calcula la matriz resultante C despues de aplicar la operacion convolucion de A*B
def convolucion(A, B):
    C_filas = len(A) - len(B) + 1
    C_columnas = len(A[0]) - len(B[0]) + 1
    C = np.zeros((C_filas, C_columnas))
    for i in range(len(C)):
        for j in range(len(C[0])):
            suma = 0
            for n in range(len(B)):
                for m in range(len(B[0])):
                    suma += A[n + i][m + j] * B[n][m]
            C[i][j] = suma
    return C

#filtro = [[3, 4, 2], [1, 0, 1], [2, 3, 1]]
filtro = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
res_sinpadd = convolucion(imagenrgb2gray, filtro)
cv2.imwrite('imagen_convolucion_sin_padding.jpg', res_sinpadd)
