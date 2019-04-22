import cv2
import numpy as np

img = cv2.imread('images/input.jpg')
num_rows, num_cols = img.shape[:2]
print('dimensiones de la imagen renglones, columnas \n', num_rows,num_cols)
matriz_translacion = np.float32([ [1,0,int(0.5*num_cols)], [0,1,int(0.5*num_rows)] ])
print('matrix de traslacion\n',matriz_translacion)
rotation_matrix = cv2.getRotationMatrix2D((num_cols-2, num_rows-2), 45, .5)
#                                          centro(col,ren),angulo,escala
print('matrix de rotacion\n',rotation_matrix)
img_translation = cv2.warpAffine(img, matriz_translacion, (2*num_cols, 2*num_rows))
cv2.imshow('traslacion', img_translation)
img_rotation = cv2.warpAffine(img_translation, rotation_matrix,
                              (num_cols*2, num_rows*2))
cv2.imshow('Rotacion', img_rotation)
cv2.waitKey()
