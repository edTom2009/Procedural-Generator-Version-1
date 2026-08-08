#libraries
import random
import math



#variables
WIDTH = 100 #placeholder values
HEIGHT = 100
DETAIL = 50
SEED = 0
octaves = 3
RADIAN = 2*(math.pi)
CELLSIZE = 20
#functions

#GRADIENT VECTOR GENERATOR
#generates a grid of gradient vectors for the map pixels to reference when calculating the dot product for each pixel
def generateGradientVectors():
    maxWidth = (octaves+1) * WIDTH // CELLSIZE
    maxHeight = (octaves+1) * HEIGHT // CELLSIZE
    gradVectGrid = []

    for height in range (maxHeight):
        gridRow = []
        for width in range (maxWidth):
            angleDeg = random.randint(0,360)
            angleRad = math.radians(angleDeg)
            i = math.sin(angleRad)
            j = math.cos(angleRad)
            coordValues = [i,j]
            gridRow.append(coordValues)

        gradVectGrid.append(gridRow)  
    return gradVectGrid

def generateOctaves(lacunarity, step, gradVectGrid):
    maxWidth = lacunarity * WIDTH
    maxHeight = lacunarity * HEIGHT
    distVectGrid = []
    y=0
    for j in range (maxHeight):
        gridRow = []
        x=0
        for i in range (maxWidth):
            gridX = x // CELLSIZE
            gridY = y // CELLSIZE

            v00 = gradVectGrid[gridY][gridX]         # top left
            v10 = gradVectGrid[gridY][gridX + 1]     # top right
            v01 = gradVectGrid[gridY + 1][gridX]     # bottom left
            v11 = gradVectGrid[gridY + 1][gridX + 1] # bottom right

            local_x = (x % CELLSIZE) / CELLSIZE
            local_y = (y % CELLSIZE) / CELLSIZE

            d00 = [local_x, local_y]
            d10 = [local_x - 1, local_y]
            d01 = [local_x, local_y - 1]
            d11 = [local_x - 1, local_y - 1]

            dot00 = v00[0] * d00[0] + v00[1] * d00[1]
            dot10 = v10[0] * d10[0] + v10[1] * d10[1]
            dot01 = v01[0] * d01[0] + v01[1] * d01[1]
            dot11 = v11[0] * d11[0] + v11[1] * d11[1]

            x=x+step

        distVectGrid.append(gridRow)
    
    return distVectGrid
    

gradVectGrid = generateGradientVectors()
octave1 = generateOctaves(1, 3, gradVectGrid)
#print(octave1)
print(len(octave1))
print(len(octave1[0]))
#print(len(octave1[0]))

#create array for based on map size
#calculate the distance between each plotted pixel and the next using the lacunarity value
#add random offset for first pixel on grid
#plot first pixel and calulate respecive distance vectors to each corner
#take dot products of each distance and gradient vectors
#interpolate between values first horizontally then vertically
#store result as a single value in the array
#normalise values to between 0 and 1
#repeat for each pixel in map grid
#repeat for each octave using respective lacunarity value
#store each ocatve as its own array

#divide each octave value by its persistance value to determine its eefect on the map
#add octaves together for each pixel

#render map
#colour based on height value
#water = 0 - 0.2
#beach = 0.2 - 0.3
#grass = 0.3 - 0.7
#mountain = 0.7 - 0.9
#snow = 0.9 - 1

