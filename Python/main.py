#libraries
import random
import math



#variables
WIDTH = 100 #placeholder values
HEIGHT = 100
DETAIL = 50
SEED = 0
octaves = 3
Radian = 2*(math.pi)
#functions

#GRADIENT VECTOR GENERATION
#determine max size of gradient vector grid - based on map size and highest octave
#generate a array of gradient vectors and calculate components
maxWidth = octaves * WIDTH
maxHeight = octaves * HEIGHT
gradVectGrid = []
gridRow = []
for i in range (maxHeight):
    for j in range (maxWidth):
        angleDeg = random.randint(0,360)
        angleRad = (angleDeg/360)*Radian
        x = math.sin(angleRad)
        y = math.cos(angleRad)
        coordValues = [x,y]
        gridRow.append(coordValues)
    gradVectGrid.append(gridRow)
    gridRow = []

print (gradVectGrid)
#[ [ [x1,y1], [x2,y2] ]
#  [ [x3,y3], [x4,y4] ] ]

#create array for based on map size
#calculate the distance between each plotted pixdl and the next using the lacunarity value
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

