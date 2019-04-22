import cv2
img = cv2.imread('./images/inteligenciaArtificial.jpg', cv2.IMREAD_COLOR)
#  g,b,r = cv2.split(img)
r,g,b = cv2.split(img)
gbr_img = cv2.merge((g,b,r))
rgr_img = cv2.merge((r,g,r))
brb_img = cv2.merge((b,r,b))
gbg_img = cv2.merge((g,b,g))
rbr_img = cv2.merge((r,g,r))
cv2.imshow('Original', img)
cv2.imshow('GRB', gbg_img)
cv2.imshow('RGR', rgr_img)
cv2.imshow('BRB', brb_img)
cv2.imshow('GBG', gbr_img)
cv2.imshow('RBR', rbr_img)

cv2.waitKey()