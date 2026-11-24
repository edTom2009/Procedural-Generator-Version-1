#import libraries
import math
import random

#import cv2
#import matplotlib.pyplot as plt
import numpy as np

# variables
RADIAN = 2 * (math.pi)


#===================GRADIENT VECTOR GENERATOR=========================
# generates a grid of gradient vectors for the map pixels to reference when calculating the dot product for each pixel

def generateGradientVectors(NumOctaves, width, height, cellSize):
    maxWidth = (NumOctaves + 1) * width // cellSize + 1
    maxHeight = (NumOctaves + 1) * height // cellSize + 1
    gradVectGrid = np.empty((maxHeight, maxWidth, 2), dtype=float)

    for y in range(maxHeight):
        for x in range(maxWidth):
            angleDeg = random.randint(0, 360)
            angleRad = math.radians(angleDeg)
            gradVectGrid[y, x] = [math.sin(angleRad), math.cos(angleRad)]

    return gradVectGrid

#===================PERLIN NOISE FUNCTIONS=========================
#fade function for smooth interpolation
def fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3

#linear interpolation function
def lerp(a, b, t):
    return a + t * (b - a)

#===================OCTAVE GENERATOR=========================
#generates the perlin noise map for each octave based on the gradient vector grid and the specified lacunarity and step size
def generateOctaves(lacunarity, step, gradVectGrid, width, height, CELLSIZE):
    maxWidth = max(1, int(lacunarity * width))
    maxHeight = max(1, int(lacunarity * height))
    octaveGrid = np.empty((maxHeight, maxWidth), dtype=float)

    y = 0
    for j in range(maxHeight):
        x = 0
        for i in range(maxWidth):
            #finds the grid cell coordinates for the current pixel
            gridX = min(x // CELLSIZE, gradVectGrid.shape[1] - 1)
            gridY = min(y // CELLSIZE, gradVectGrid.shape[0] - 1)

            #fetches the gradient vectors for the four corners of the grid cell
            v00 = gradVectGrid[gridY, gridX]
            v10 = gradVectGrid[gridY, min(gridX + 1, gradVectGrid.shape[1] - 1)]
            v01 = gradVectGrid[min(gridY + 1, gradVectGrid.shape[0] - 1), gridX]
            v11 = gradVectGrid[min(gridY + 1, gradVectGrid.shape[0] - 1), min(gridX + 1, gradVectGrid.shape[1] - 1)]

            #calculates the local coordinates of the pixel within the grid cell
            local_x = (x % CELLSIZE) / CELLSIZE
            local_y = (y % CELLSIZE) / CELLSIZE

            #calculates the distance vectors from the pixel to the four corners of the grid cell
            d00 = np.array([local_x, local_y], dtype=float)
            d10 = np.array([local_x - 1, local_y], dtype=float)
            d01 = np.array([local_x, local_y - 1], dtype=float)
            d11 = np.array([local_x - 1, local_y - 1], dtype=float)

            #takes the dot product of the distance vectors and the gradient vectors for each corner of the grid cell
            dot00 = v00[0] * d00[0] + v00[1] * d00[1]
            dot10 = v10[0] * d10[0] + v10[1] * d10[1]
            dot01 = v01[0] * d01[0] + v01[1] * d01[1]
            dot11 = v11[0] * d11[0] + v11[1] * d11[1]

            #fades the local coordinates
            u = fade(local_x)
            v = fade(local_y)

            #interpolates horizontally
            top = lerp(dot00, dot10, u)
            bottom = lerp(dot01, dot11, u)

            #interpolates vertically
            value = lerp(top, bottom, v)

            #stores the final value in the octave grid
            octaveGrid[j, i] = value

            x += step
        y += step

    return octaveGrid


def generate_terrain(width, height, seed, detail):
    # Set the random seed for reproducibility
    if seed == 0:
        seed = random.randint(0, 1000000)
    random.seed(seed)

    #use the detail value to determine the number of octaves and cell size
    NumOctaves = int(detail / 10) + 1
    cellSize = max(1, int(100 / detail))  # Adjust cell size based on detail level

    # Generates the terrain using Perlin noise or any other algorithm
    terrain = np.zeros((height, width), dtype=float)#defines the terrain array with the specified width and height
    vectorGrid = generateGradientVectors(NumOctaves, width, height, cellSize)#generates the gradient vector grid for the terrain generation

    # Generate multiple octaves of noise and combine them
    for octave in range(NumOctaves):
        frequency = 2 ** octave
        amplitude = 1 / frequency
        step = int(cellSize / frequency)
        octave_noise = generateOctaves(frequency, step, vectorGrid, width, height, cellSize)
        terrain += amplitude * octave_noise[:height, :width]

    # Normalises the terrain values to the range [0, 1]
    terrain -= terrain.min()
    terrain /= terrain.max()

    # Saves the terrain as an image
    plt.imshow(terrain, cmap='terrain')
    plt.axis('off')
    plt.savefig('terrain.png', bbox_inches='tight', pad_inches=0)
    plt.close()

    print("Terrain generated successfully!")



