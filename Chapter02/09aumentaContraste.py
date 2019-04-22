import cv2 
import numpy as np 
 
img = cv2.imread('images/imageOscura.jpg', 0) 
 
# ecualiza el histograma de la imagen de entrada 
histeq = cv2.equalizeHist(img) 
 
cv2.imshow('imagenOriginal', img) 
cv2.imshow('HistogramaEqualizado', histeq) 
cv2.waitKey(0) 
