'''
Created on Jan 11, 2014
Author: sushant
This was a tutorial created by sushant to demostrate the marching squares algorithm.

Modified: March 10, 2015
Author: Andrew Huy Nguyen
This script was modified to 
'''

import sys
from MarchingSquare import *
import time
import math

#Globals
winHeight = 1
winWidth = 1
msHandler = -1
ESCAPE = '\033'
window = 0
showGrid = True


def init():    
    global msHandler
    msHandler = MarchingSquareHandler()
    
    msHandler.setWindow(winWidth,winHeight)
#    msHandler.setGridSize(10)
#    gsize=raw_input("Give the grid size:(use integer with minimum equal to 1)")
#    gsize=int(gsize)
    gsize=raw_input("Give the grid size:")
    gsize=float(gsize)
    msHandler.setGridSize(gsize)
#    msHandler.setGridSize(1)
    rad=raw_input("Radius:")
    rad=float(rad)
    msHandler.setRadius(rad)
#print statement to check inputs and outputs are corrected    
    print "Grid size:"
    print gsize
    print "Total number of squares:"
    print int((winHeight/gsize)*(winWidth/gsize))
    print "Radius:"
    print rad
#    print "Area:"
#    print rad*rad*math.pi
    
    
    start=time.clock()

    fullsq, partsq, Tpartarea = msHandler.compute()

    end=time.clock()
    print "Compute Time:"
    print end - start

    print "Number of Full Squares:"
    print fullsq
    print "Number of Partial Squares:"
    print partsq
    print "Total area computed by marching squares:"
    print fullsq*gsize*gsize + Tpartarea
#    ITarea, numtrap = msHandlder.compute2()
	
	
#integration         
#def Integration()

def main():
	
    init()
    print "Finished"


main()
