#
import cv2
import numpy as np

def blancoynegro(imagen):
    valorF = len(imagen)
    valorC = len(imagen[0])
    bw = np.zeros((valorF, valorC))
    valorIntermedio = 128
    for x in range (len(bw)):
        for y in range (len(valorC)):
            if imagen[x][y] <= valorIntemedio:
                bw[x][y]  = 0
            else:
                bw[x][y] = 1
        return bw
    
imagen_i = cv2.imread("imagen_escala_de_grises.jpg")
byn = blancoynegro(imagen_i)
cv2.imwrite("blanco_negro.jpg", byn)

