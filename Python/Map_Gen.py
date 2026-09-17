import math
import random

import cv2
import matplotlib.pyplot as plt
import numpy as np

# variables
WIDTH = 100
HEIGHT = 100
DETAIL = 50
SEED = 0
NumOctaves = 5
CELLSIZE = 50
RADIAN = 2 * (math.pi)


# functions
# GRADIENT VECTOR GENERATOR
# generates a grid of gradient vectors for the map pixels to reference when calculating the dot product for each pixel

def generateGradientVectors():
    maxWidth = (NumOctaves + 1) * WIDTH // CELLSIZE + 1
    maxHeight = (NumOctaves + 1) * HEIGHT // CELLSIZE + 1
    gradVectGrid = np.empty((maxHeight, maxWidth, 2), dtype=float)

    for y in range(maxHeight):
        for x in range(maxWidth):
            angleDeg = random.randint(0, 360)
            angleRad = math.radians(angleDeg)
            gradVectGrid[y, x] = [math.sin(angleRad), math.cos(angleRad)]

    return gradVectGrid


def fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3


def lerp(a, b, t):
    return a + t * (b - a)


def generateOctaves(lacunarity, step, gradVectGrid):
    maxWidth = max(1, int(lacunarity * WIDTH))
    maxHeight = max(1, int(lacunarity * HEIGHT))
    octaveGrid = np.empty((maxHeight, maxWidth), dtype=float)

    y = 0
    for j in range(maxHeight):
        x = 0
        for i in range(maxWidth):
            gridX = min(x // CELLSIZE, gradVectGrid.shape[1] - 1)
            gridY = min(y // CELLSIZE, gradVectGrid.shape[0] - 1)

            v00 = gradVectGrid[gridY, gridX]
            v10 = gradVectGrid[gridY, min(gridX + 1, gradVectGrid.shape[1] - 1)]
            v01 = gradVectGrid[min(gridY + 1, gradVectGrid.shape[0] - 1), gridX]
            v11 = gradVectGrid[min(gridY + 1, gradVectGrid.shape[0] - 1), min(gridX + 1, gradVectGrid.shape[1] - 1)]

            local_x = (x % CELLSIZE) / CELLSIZE
            local_y = (y % CELLSIZE) / CELLSIZE

            d00 = np.array([local_x, local_y], dtype=float)
            d10 = np.array([local_x - 1, local_y], dtype=float)
            d01 = np.array([local_x, local_y - 1], dtype=float)
            d11 = np.array([local_x - 1, local_y - 1], dtype=float)

            dot00 = v00[0] * d00[0] + v00[1] * d00[1]
            dot10 = v10[0] * d10[0] + v10[1] * d10[1]
            dot01 = v01[0] * d01[0] + v01[1] * d01[1]
            dot11 = v11[0] * d11[0] + v11[1] * d11[1]

            u = fade(local_x)
            v = fade(local_y)

            top = lerp(dot00, dot10, u)
            bottom = lerp(dot01, dot11, u)

            value = lerp(top, bottom, v)
            octaveGrid[j, i] = value

            x += step
        y += step

    return octaveGrid

vectorGrid = generateGradientVectors()
Octave1 = generateOctaves(1, 1, vectorGrid)





