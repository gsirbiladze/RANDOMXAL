
from PIL import Image,ImageDraw
from random import randint

def r(x, y):
    i = Image.new('RGBA', (x,y), (randint(0, 255),randint(0, 255),randint(0, 255)))
    d = ImageDraw.Draw(i)
    for _ in range(10000):
        d.point((randint(0, x),randint(0, y)),fill=(randint(0, 255),randint(0, 255),randint(0, 255),255))
    i.show()

if __name__ == '__main__':
    r(400,400)
