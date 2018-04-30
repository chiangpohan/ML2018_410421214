import numpy as np
import cv2
from PIL import Image
import random

img_key1 = Image.open('key1.png')
img_key2 =Image.open('key2.png')
img_target = Image.open('target.png')
img_E = Image.open('E.png')
img_Eprime = Image.open('Eprime.png')


output = Image.new("L",(400,300), 0)
rate = 1e-8
epoch = 69

def mse():
    N_Epoch =1
    w = [random.random(), random.random(), random.random(), ]
    while N_Epoch == 1 or N_Epoch<epoch:
        for i in range(0,400):
            for j in range(0, 300):
                a = w[0] * img_key1.getpixel((i,j)) + \
                    w[1] * img_key2.getpixel((i, j)) + \
                    w[2] * img_target.getpixel((i, j))
                error = (img_E.getpixel((i,j))-a)
                w[0] += rate * error * img_key1.getpixel((i,j))
                w[1] += rate * error * img_key2.getpixel((i, j))
                w[2] += rate * error * img_E.getpixel((i, j))
        print ("epoch->",N_Epoch,"error=>",error,"\tW=>",w)
        N_Epoch +=1
    return w

wFound = mse()

for i in range(0,400):
     for j in range(0,300):
         output.putpixel((i,j),int(round((img_Eprime.getpixel((i, j))-wFound[0]*img_key1.getpixel((i, j))-wFound[1]*img_key2.getpixel((i, j)))/wFound[2])))

output.save("Final.png")