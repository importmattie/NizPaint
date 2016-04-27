import numpy as np

def colorBomb(img,x,y,radius,color):
    pixels = img.load()
    for dx in range(-radius,radius+1):
        for dy in range(-radius,radius+1):
            dist = distFromCent(x,y,dx,dy)
            if(insideImage(img,x+dx,y+dy) and dist < radius):
                colorA = np.array(color)
                pixelA = np.array(pixels[x+dx,y+dy])
                pixels[x+dx,y+dy] = tuple((colorA*(1-(1.*dist/radius))+pixelA*(1.*dist/radius)).astype(int))

def distFromCent(x,y,dx,dy):
    return (dx**2+dy**2)**0.5

def insideImage(image,xPix,yPix):
    size = image.size
    if(xPix < 0 or xPix >= size[0] or yPix < 0 or yPix >= size[1]):
        return False
    return True
