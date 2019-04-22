import cv2 # Se carga la libreria cv2
img = cv2.imread('./images/inteligenciaArtificial.jpg') #  se lee la imagen
cv2.imshow('Imagen', img) # se despliega la imagen
cv2.waitKey(1)
