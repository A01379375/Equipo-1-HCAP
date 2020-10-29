import numpy as np
import cv2

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

img = cv2.imread('imagen.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filtro = [[3, 4, 2], [1, 0, 1], [2, 3, 1]]
res = convolucion(img, filtro)
cv2.imwrite('imagenconvolucionsinpadding.jpg', res)