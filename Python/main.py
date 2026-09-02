#libraries
import random
import math

import numpy as np

import matplotlib.pyplot as plt
import cv2



#variables
WIDTH = 100 #placeholder values
HEIGHT = 100
DETAIL = 50
SEED = 0
NumOctaves = 5
CELLSIZE = 50

RADIAN = 2*(math.pi)

#functions
#GRADIENT VECTOR GENERATOR
#generates a grid of gradient vectors for the map pixels to reference when calculating the dot product for each pixel
def generateGradientVectors():
    maxWidth = (NumOctaves + 1) * WIDTH // CELLSIZE
    maxHeight = (NumOctaves + 1) * HEIGHT // CELLSIZE
    gradVectGrid = np.empty((maxHeight, maxWidth, 2), dtype=float)

    for y in range(maxHeight):
        for x in range(maxWidth):
            angleDeg = random.randint(0, 360)
            angleRad = math.radians(angleDeg)
            gradVectGrid[y, x] = [math.sin(angleRad), math.cos(angleRad)]

    return gradVectGrid

def fade(t): #Fade function for interpolation, smooths the transition between values, from 
    return 6*t**5 - 15*t**4 + 10*t**3

def lerp(a, b, t):
    return a + t * (b - a)

def generateOctaves(lacunarity, step, gradVectGrid):
    maxWidth = lacunarity * WIDTH
    maxHeight = lacunarity * HEIGHT
    octaveGrid = np.empty((maxHeight, maxWidth), dtype=float)

    y = 0
    for j in range(maxHeight):
        x = 0
        for i in range(maxWidth):
            gridX = x // CELLSIZE
            gridY = y // CELLSIZE

            v00 = gradVectGrid[gridY, gridX]         # top left
            v10 = gradVectGrid[gridY, gridX + 1]     # top right
            v01 = gradVectGrid[gridY + 1, gridX]     # bottom left
            v11 = gradVectGrid[gridY + 1, gridX + 1] # bottom right

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
    

gradVectGrid = generateGradientVectors()
octave1 = generateOctaves(1, 3, gradVectGrid)
#print(octave1)
print(len(octave1))
print(len(octave1[0]))

fig, ax = plt.subplots()
ax.imshow(octave1, cmap='gray')
plt.show()
#print(len(octave1[0]))


#repeat for each octave using respective lacunarity value
#store each ocatve as its own array

#divide each octave value by its persistance value to determine its effect on the map
#add octaves together for each pixel

#render map
#colour based on height value
#water = 0 - 0.2
#beach = 0.2 - 0.3
#grass = 0.3 - 0.7
#mountain = 0.7 - 0.9
#snow = 0.9 - 1

