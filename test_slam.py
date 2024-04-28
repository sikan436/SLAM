#!/usr/bin/env python3
import time
import cv2
from display import Display

W = 1920
H = 1080

disp = Display(W, H)

def process_frame(img):
  img = cv2.resize(img, (W,H))
  disp.paint(img)

if __name__ == "__main__":
  cap = cv2.VideoCapture("test.mp4")

  while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
      process_frame(frame)
    else:
      break







# import cv2 
# import numpy as np
# import pygame
# from display import Display

# W=1920//2
# H=1080//2

# # screen = pygame.display.set_mode((W,H ))
# disp=Display(W,H)
# def process_frame(img):
#     img=cv2.resize(img,(W,H))
#     disp.paint(img)
#     cv2.imshow('Img', img)
  
#     # pygame.display.flip()
#     print(img.shape)

     
# if __name__=="__main__":

#     cap = cv2.VideoCapture('test_countryroad.mp4')

#     if (cap.isOpened()== False):
#         print("Error opening video file") 
#     while(cap.isOpened()): 
        
#         ret, frame = cap.read() 
#         if ret == True: 
#             process_frame(frame)


#         else: 
#             break
 
