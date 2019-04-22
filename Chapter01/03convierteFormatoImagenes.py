import cv2

img = cv2.imread('images/inteligenciaArtificial.jpg')

cv2.imwrite('images/inteligenciaArtificial.png', img, [cv2.IMWRITE_PNG_COMPRESSION])
