#!/usr/bin/python3
#Ella Adam

import numpy
import math

hypotenuse = 4
adjacent = 5
opposite = 3

trig = ("sine", "cosine", "tangent")
sine = math.sin(opposite/hypotenuse)
cosine = math.cos(opposite/hypotenuse)
tangent = math.tan(opposite/adjacent)

print(sine)
print(cosine)
print(tangent)

print(cosine, sine, tangent)