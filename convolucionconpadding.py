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
            if suma > 255:
                C[i][j] = 255
            else:
                C[i][j] = suma
    return C

def convolucion_padding(A, B):
    C = np.zeros((len(A) + 2, len(A[0]) + 2))
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            C[i + 1][j + 1] = A[i][j]
    return convolucion(C, B)

#filtro = [[3, 4, 2], [1, 0, 1], [2, 3, 1]]
filtro = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
res = convolucion_padding(imagenrgb2gray, filtro)
cv2.imwrite('imagen_convolucion_con_padding.jpg', res)
res = convolucion_padding(imagen2rgb2gray, filtro)
cv2.imwrite('imagen_paisaje_convolucion_con_padding.jpg', res)
