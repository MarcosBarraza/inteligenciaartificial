import cv2 
import numpy as np 
 
img_emboss_input = cv2.imread('images/geometric.jpg') 
 
# generating the kernels 
kernel_emboss_1 = np.array([[0,-1,-1], 
                            [1,0,-1], 
                            [1,1,0]]) 
kernel_emboss_2 = np.array([[-1,-1,0], 
                            [-1,0,1], 
                            [0,1,1]]) 
kernel_emboss_3 = np.array([[1,0,0], 
                            [0,0,0], 
                            [0,0,-1]]) 
 
# converting the image to grayscale 
gray_img = cv2.cvtColor(img_emboss_input,cv2.COLOR_BGR2GRAY) 
 
# applying the kernels to the grayscale image and adding the offset to produce the shadow
output_1 = cv2.filter2D(gray_img, -1, kernel_emboss_1) + 128 
output_2 = cv2.filter2D(gray_img, -1, kernel_emboss_2) + 128 
output_3 = cv2.filter2D(gray_img, -1, kernel_emboss_3) + 128 
 
cv2.imshow('Input', img_emboss_input) 
cv2.imshow('Relieve - sur oeste', output_1) 
cv2.imshow('Relieve - sur este', output_2) 
cv2.imshow('Relieve - noroeste', output_3) 
cv2.waitKey(0)
