import os

import numpy as np
import random
from PIL import Image


def random_images():
    a = [512, 1024, 2048]
    x = random.choice(a)
    dX, dY = x, x
    xArray = np.linspace(0.0, 2.0, dX).reshape((1, dX, 1))
    yArray = np.linspace(0.0, 2.0, dY).reshape((dY, 1, 1))

    def randColor():
        return np.array([random.random(), random.random(), random.random()]).reshape((1, 1, 3))

    def getX():
        return xArray

    def getY():
        return yArray

    def safeDivide(a, b):
        return np.divide(a, np.maximum(b, 0.001))

    functions = [(0, randColor),
                 (0, getX),
                 (0, getY),
                 (1, np.sin),
                 (1, np.cos),
                 (2, np.add),
                 (2, np.subtract),
                 (2, np.multiply),
                 (2, safeDivide)]
    depthMin = random.choice((2, 3, 4))
    depthMax = random.choice((10, 15, 20))

    def buildImg(depth=0):
        funcs = [f for f in functions if
                 (f[0] > 0 and depth < depthMax) or
                 (f[0] == 0 and depth >= depthMin)]
        nArgs, func = random.choice(funcs)
        args = [buildImg(depth + 1) for n in range(nArgs)]
        return func(*args)

    img = buildImg()
    # Ensure it has the right dimensions, dX by dY by 3
    img = np.tile(img, (dX // img.shape[0], dY // img.shape[1], 3 // img.shape[2]))

    # Convert to 8-bit, send to PIL and save
    img8Bit = np.uint8(np.rint(img.clip(0.0, 2.0) * 255.0))
    path = os.path.split(os.getcwd())[0]
    path += "/timathon/AIG/static/assets/img/"
    Image.fromarray(img8Bit).save(f"{path}temp.jpg")

