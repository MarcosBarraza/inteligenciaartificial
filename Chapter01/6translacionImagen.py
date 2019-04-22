import cv2
import numpy as np
# se sobrepone la imagen a un marco
img = cv2.imread('images/inteligenciaArtificial.jpg')
num_rows, num_cols = img.shape[:2]
print('dimensiones de la imagen \n','renglones ', num_rows,'\n','columnas',num_cols,'\n')
translation_matrix = np.float32([ [1,0,100], [0,1,110] ]) #  la imagen se traslada 100,110
#  aa=input()
print('matriz de traslacion\n',translation_matrix)
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols + 100, num_rows + 110))
cv2.imshow('contenedor de la imagen',img_translation)
translation_matrix = np.float32([ [1,0,-30], [0,1,-30] ]) # la imagen se traslada -30 -30
print('matriz de translacion\n',translation_matrix,'\n')
img_translation = cv2.warpAffine(img_translation, translation_matrix, (num_cols + 100 + 30
                                                                       , num_rows + 110 + 50))
cv2.imshow('original', img)
cv2.imshow('Translation', img_translation)
renglones,columnas =img_translation.shape[:2]
print('dimensiones de la imagen trasladada\n',renglones,columnas)
cv2.waitKey()
