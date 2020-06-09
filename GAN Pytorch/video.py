import os
import numpy as np 
import cv2 as cv 

parent_dir = os.path.dirname(os.path.abspath(__file__))
sample_dir = os.path.join(parent_dir, 'samples')
video = os.path.join(parent_dir, 'GAN-Training.avi')

paths = []

for img in os.listdir(sample_dir):
    path = os.path.join(sample_dir, img)
    paths.append(path)

paths.sort()

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(video, fourcc, 10, (482, 242))

for path in paths:
	frame = cv.imread(path)
	out.write(frame)

out.release()
cv.destroyAllWindows()