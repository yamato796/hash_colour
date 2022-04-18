from time import time
from io   import BytesIO
import os
from tqdm import tqdm
import cv2
import math
import numpy as np
import base64
import logging
import random

s = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
s_1 = s+s+s
print(s_1)
size = 64
x = 0
y = 0
index = 0
img = np.ones((size,size,3),np.uint8)
for i in tqdm(range(0,size)):
    for j in range(0,size):
        r = s_1[index] + s_1[index+1]
        g = s_1[index+2] + s_1[index+3]
        b = s_1[index+4] + s_1[index+5]
        img[i][j] = (int(r, 16), int(g, 16), int(b,16))
    index = index +2
    print(r,g,b,img[i][j],index)

cv2.imwrite("./img_test.png",img)
