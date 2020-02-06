#!/usr/bin/env python3
from PIL import Image 

im = Image.open('last.png').convert('RGB')

newimgdata = []

for i in im.getdata():
    if i == (0, 0, 0): newimgdata.append((255, 255, 255))
    else: newimgdata.append((0, 0, 0))

newim = Image.new(im.mode, im.size)
newim.putdata(newimgdata)

newim.save('out.png')

# https://imgur.com/download/Xrv86y2
