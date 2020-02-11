from PIL import Image

def readPic(path):
    image = Image.open(path)

    a, b = image.size
    print 'a: ', a
    print 'b: ', b


    for i in range(a):
        for j in range(b):
            pixel = image.getpixel((i,j))
            #if pixel == (49, 173, 140, 255):
            print i, j, pixel

readPic('0.png')
