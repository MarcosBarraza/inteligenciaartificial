import cv2
#  convierte la imagen a gris
imagenGris = cv2.imread('images/inteligenciaArtificial.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale', imagenGris)
cv2.imwrite('images/output.jpg', imagenGris) # la graba en gris

cv2.waitKey()
