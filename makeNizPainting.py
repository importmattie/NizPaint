import nizpaint as nizp
from PIL import Image
import random

xPixels = 1600
yPixels = 900

def getRandom255():
    return (int(random.random()*255))

img = Image.new('RGB',(xPixels,yPixels),(getRandom255(),getRandom255(),getRandom255()))

for ii in range(0,1500):
    color = (getRandom255(),getRandom255(),getRandom255())
    radius = int(random.random()*50)
    x = int(random.random()*xPixels)
    y = int(random.random()*yPixels)
    nizp.colorBomb(img,x,y,radius,color)

img.save('output.png')
