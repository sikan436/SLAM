#!/usr/bin/env python3
import time
import cv2
from display import Display
from matplotlib import pyplot as plt
import numpy as np
W = 1920//2
H = 1080//2

disp = Display(W, H)



class FeatureExtractor(object):
    def extract(self,img):
          feats=cv2.goodFeaturesToTrack(np.mean(img,axis=2).astype(np.uint8),3000,qualityLevel=.01,minDistance=3)
          # print(feats)

          return feats

fe=FeatureExtractor()

def process_frame(img):
  img = cv2.resize(img, (W,H))
  kp=fe.extract(img)
  
  for p in kp:
    u,v=map(lambda x:int(round(x)),p[0])
    cv2.circle(img,(u,v),color=(0,255,0),radius=3)
  disp.paint(img)

if __name__ == "__main__":
  cap = cv2.VideoCapture("test.mp4")

  while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
      process_frame(frame)
    else:
      break
