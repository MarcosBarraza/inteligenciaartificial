import cv2 
import numpy as np 
 
img = cv2.imread('images/input.jpg') 
rows, cols = img.shape[:2] 
print('Renglones columnas\n',rows,cols)
#  generando una mascara viñeta (encuadre) usando un kernel gausiano
#  El filtro de viñeta básicamente enfoca el brillo en una parte
#  particular de la imagen y las otras partes se ven difuminadas
kernel_x = cv2.getGaussianKernel(cols,200) #  tamaño,desv std radio de la parte brillante
kernel_y = cv2.getGaussianKernel(rows,200) #  tamaño,desv std radio de la parte brillante
kernel = kernel_y * kernel_x.T 
mask = 255 * kernel / np.linalg.norm(kernel)#  normalizamos la imagen 
#  mask = mask[int(0.5*rows):, int(0.5*cols):]
#  se usa para mover el foco de la imagen
output = np.copy(img) 
# aplicando la mascara a cada canal en la imagen de entrada 
for i in range(3): 
    output[:,:,i] = output[:,:,i] * mask 
cv2.imshow('Original', img) 
cv2.imshow('Vignette', output) 
cv2.waitKey(0)
