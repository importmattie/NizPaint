import nizpaint as nizp
from PIL import Image
import random

xPixels = 1024
yPixels = 1024

img = Image.new('RGB',(xPixels,yPixels),'black')

for ii in range(0,1500):
    color = (int(random.random()*255),int(random.random()*255),int(random.random()*255))
    radius = int(random.random()*50)
    x = int(random.random()*xPixels)
    y = int(random.random()*yPixels)
    nizp.colorBomb(img,x,y,radius,color)

img.save('output.png')
