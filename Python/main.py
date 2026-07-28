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
#functions

#GRADIENT VECTOR GENERATOR
#generates a grid of gradient vectors for the map pixels to reference when calculating the dot product for each pixel
def generateGradientVectors():
    maxWidth = octaves * WIDTH
    maxHeight = octaves * HEIGHT
    gradVectGrid = []

    for y in range (maxHeight):
        gridRow = []
        for x in range (maxWidth):
            angleDeg = random.randint(0,360)
            angleRad = math.radians(angleDeg)
            i = math.sin(angleRad)
            j = math.cos(angleRad)
            coordValues = [i,j]
            gridRow.append(coordValues)

        gradVectGrid.append(gridRow)  
    return gradVectGrid

gradVectGrid = generateGradientVectors()
print(gradVectGrid)
print(len(gradVectGrid))
print(len(gradVectGrid[0]))

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

