#libraries
import random
import math
import numpy


#variables
WIDTH = 100 #placeholder values
HEIGHT = 100
DETAIL = 50
SEED = 0

#functions
def normalise(value, scale):
    normValue = value/scale
    return(normalValue)

#GRADIENT VECTOR GENERATION
#determine max size of gradient vector grid - based on map size and highest octave
#generate a array of gradient vectors and calculate components


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

