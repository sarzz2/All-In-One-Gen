import random


def hex():
    color = "%06x" % random.randint(0, 0xFFFFFF)
    return color


def rgb():
    x = hex()
    RGB = tuple(int(x[i:i + 2], 16) for i in (0, 2, 4))
    return RGB
