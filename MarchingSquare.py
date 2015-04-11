'''
Created on Jan 11, 2014
author: sushant
This was a tutorial created by sushant to demostrate the marching squares algorithm.


Modified on March 10, 2015
Author: Andrew Huy Nguyen
The following algorithm was modified to compute the number of full and partial squares.  Full and partial squares are counted if the value is below 0.  The function/curve (circle) has a postive value in all case execpt for the interface(0) and interior (<0).

Changed how the zeros are handled within the codes. Plus skip the interpolation for these with 2 zeros or 1z_3- or 1z_3+.

'''

import numpy as np
import math
    
class MarchingSquareHandler:
    
    #default Values
    gridSize = 0
    winHeight = 0
    winWidth = 0
    _nSquare = 0
    radius=0
    isovalue=0
    linelist=[]
    _scVal = []
    
    def setWindow(self,w,h):
        self.winHeight = h
        self.winWidth = w
    
    def setGridSize(self,grid):
        self.gridSize = grid
        
    def setRadius(self,r):
        self.radius = r
        
    def getGridSize(self):
        return self.gridSize
    
    def getLineList(self):
        return self.linelist
        
    #define Scalar Function (Circle)
    def scalarFunc(self,x,y,r): # a circle
        return x**2+y**2-r**2
        #return x+y-r
        #return (2*x)+y-r
 
    def scalarFunc3(self,x,r): # a circle
        return (r**2-x**2)**(1.0/2.0)
	#return r-(2*x)
	#return r-(x)

    #define function 1-cos(r)
    #here return isovalue for each point in marching squares

#    def scalarFunc2(self,r,y):
    	#tmp = math.exp(r) # e^r
	#tmp = 1.0-math.cos(r) # 1-cos(r)
	#tmp = r #r^2; could have used r**2 but either should give the same answer one less character to type
	#print "tmp"
	#print tmp
	#print "Y"
	#print y
	#print "rad"
	#print r
	#if y < tmp:
	#    value = -1.0
	#elif y == tmp:
	#    value = 0.0
	#else:
	#   value = 1.0
	#return value
	#return (1-math.cos(r))
   
    #check if scalar function intersects
    def checkifIntersects(self,_val):
        if _val[0] > 0 and _val[1] > 0 and _val[2] > 0 and _val[3] > 0:
            return False
        if _val[0] < 0 and _val[1] < 0 and _val[2] < 0 and _val[3] < 0:
            return False
        return True

    #get the full squares captured by marching square
    def countfull(self,_val):	
        if _val[0] <= 0 and _val[1] <= 0 and _val[2] <= 0 and _val[3] <= 0:
            return 1
	else:
	    return 0

    #get the partial squares that intersects with curve or function.
    def countpartial(self,_val):
        if _val[0] > 0 and _val[1] > 0 and _val[2] > 0 and _val[3] > 0:
            return 0
        elif _val[0] == 0 and _val[1] == 0 and _val[2] == 0 and _val[3] == 0 :
            return 0
        elif _val[0] < 0 or _val[1] < 0 or _val[2] < 0 or _val[3] < 0 :
            return 1
        else:
            return 0


    #Get the intersected indexs
    def getIntersects(self,_val):
        index=[]
        if _val[0] * _val[1] < 0:
        #if ( _val[0] == 0 or _val[1] == 0 ) and _val[0] * _val[1] <= 0:
            index.append([0,1])
        if _val[1] * _val[2] < 0:
        #if ( _val[1] == 0 or _val[2] == 0 ) and _val[1] * _val[2] <= 0:
            index.append([1,2])
        if _val[2] * _val[3] < 0:
        #if ( _val[2] == 0 or _val[3] == 0 ) and _val[2] * _val[3] <= 0:
            index.append([2,3])
        if _val[3] * _val[0] < 0:
        #if ( _val[3] == 0 or _val[0] == 0 ) and _val[3] * _val[0] <= 0:
            index.append([3,0])
        return index
        
    #Compute Scalar Values
    def compSval(self):
	textfile=open('isovalue.dat',"w")
        textfile.write('#x    y \n')
        #textfile.write('x    y isovalue \n')
	#posline = '{0} {1} {2}\n'.format(L,L,L)
        #textfile.write(posline)
        lenY = len(np.arange(0,self.winHeight,self.gridSize))
	lenY = lenY + 1
        lenX = len(np.arange(0,self.winWidth,self.gridSize))
	lenX = lenX + 1
        #lenX = len(np.arange(0,self.radius,self.gridSize))
	#print ("lenX lenY")
	#print(lenX, lenY)
        for y in range(lenY):
            for x in range(lenX):		
                self._scVal[x][y] = self.scalarFunc(self.gridSize*x,self.gridSize*y,self.radius)
                #self._scVal[x][y] = self.scalarFunc2(self.gridSize*x,self.gridSize*y)
        	##compute the isovalues
  		#print(self.gridSize*x,self.gridSize*y,self._scVal[x][y])
		if self._scVal[x][y] == 0.000000:
 		    posline = '{0} {1}\n'.format(self.gridSize*x,self.gridSize*y)
        	    textfile.write(posline)
 		    #posline = '{0} {1} {2}\n'.format(self.gridSize*x,self.gridSize*y,self._scVal[x][y])
        	    #textfile.write(posline)
		#print(self.gridSize*x, self.gridSize*y)


    #Compute Scalar Values
    def compSval2(self):
	areaTR=float(0)
        lenY = len(np.arange(0,self.winHeight,self.gridSize))
	lenY = lenY + 1
        lenX = len(np.arange(0,self.winWidth,self.gridSize))
	lenX = lenX + 1
	print("number of Trap")
	print(lenX-1)
	tmp = np.zeros(((self.winWidth/self.gridSize)+1))
        for x in range(lenX):
            tmp[x] = self.scalarFunc3(self.gridSize*x,self.radius)
    	    print("x tmp[x]")
	    print(x, tmp[x])
	Trap=lenX-1
	for ta in range(Trap):
	    if tmp[ta] > 0.0:
	    	areaTR = areaTR +((tmp[ta]+tmp[ta+1])/2.0)*self.gridSize
	print("Area of Trap Rule")
	print(areaTR)



    #Find the intersection Point
    def intersectionPoint(self,p1,p2,isoValue,v1,v2):
        _p=[0,0]
        _p[0] = p1[0] + (isoValue - v1)*(p2[0] - p1[0] ) / (v2-v1)
        _p[1] = p1[1] + (isoValue - v2)*(p2[1] - p1[1] ) / (v2-v1)
	#print (_p[0],_p[1]) 
        return _p
        
    #Get all the Data about square
    def getSquareData(self,n): #returns squares sv and vertices
        #r=n/((self.winHeight/self.gridSize)-2)
        #c=n%((self.winHeight/self.gridSize)-2)
        r=n/((self.winHeight/self.gridSize)-1)
        c=n%((self.winHeight/self.gridSize)-1)
	#print("squares and vertices")
	#print(r, c)
        sv=[self._scVal[r][c],self._scVal[r][c+1],self._scVal[r+1][c+1],self._scVal[r+1][c]]
        vertices =[[self.gridSize*r,self.gridSize*c],[self.gridSize*r,self.gridSize*(c+1)],[self.gridSize*(r+1),self.gridSize*(c+1)],[self.gridSize*(r+1),self.gridSize*c]]    
        return [sv,vertices]
	
	        
    #Check if Zero
    def checkSingularity(self,sv):
        found=False
        index=[]
        for i in np.arange(0,len(sv)):
            if sv[i] == 0:
                found = True
                index.append(i)
        return [found,index]
    

    #Computes the line list
    def compute(self):
        self._scVal = np.zeros(((self.winWidth/self.gridSize)+1,(self.winHeight/self.gridSize)+1))
        _nSquare = ((self.winHeight/self.gridSize)-1)*((self.winWidth/self.gridSize)-1)
        #self._scVal = np.zeros(((self.winWidth/self.gridSize),(self.winHeight/self.gridSize)))
        #_nSquare = ((self.winHeight/self.gridSize)-2)*((self.winWidth/self.gridSize)-2)	
	textfile2=open('intersectionpoint.dat',"w")
        textfile2.write('#x  y \n')
        self.compSval2()
        self.compSval()
	area2 = float(0.0)
	area1o3 = float(0.0)
	cfull=0
	cpart=0
	cpart1=0
	cpart2=0
	cpart3=0
        for i in np.arange(0,_nSquare):
            [_sv,_vert] = self.getSquareData(i)
	    #compute number of full squares and partial squares
	    nfull=self.countfull(_sv)
	    cfull=cfull + nfull
	    npart=self.countpartial(_sv)
	    cpart = cpart + npart	    
	 
            #check the intersect of function/curve with marching squares
            if self.checkifIntersects(_sv):
                isSig=self.checkSingularity(_sv)
                if isSig[0]:
                    if len(isSig[1]) > 1: #two point Singularity
                        p1 = _vert[isSig[1][0]]
                        p2 = _vert[isSig[1][1]]
			print "two point singularity"
			print p1
			print p2	
		    	area2 = area2 + float((1.0/2.0) * self.gridSize * self.gridSize)
		    	#aa = float((1.0/2.0) * self.gridSize * self.gridSize)
			#print aa
                    else: #one point Singularity
                        #check if other intersection exists
                        intPoint = self.getIntersects(_sv)
                        if len(intPoint) == 0:
                            p1 = _vert[isSig[1][0]]
                            p2 = _vert[isSig[1][0]]
                        else:
                            [_i1] = self.getIntersects(_sv)
                            p1 =self.intersectionPoint(_vert[_i1[0]],_vert[_i1[1]],self.isovalue,_sv[_i1[0]],_sv[_i1[1]])
                            p2 = _vert[isSig[1][0]]
			#print "one point singularity"	
                    	area1o3 = area1o3 + float((1.0/2.0)*(self.gridSize/2.0)*(self.gridSize/2.0))
                    	#aa = float((1.0/2.0)*(self.gridSize/2.0)*((2*(self.gridSize)**2)**0.5))
                    	#print aa
			#area1o3 = area1o3 + float((1.0/2.0)*(p1)*(p2))
                else:
                    [_i1,_i2]=self.getIntersects(_sv)
                    p1 =self.intersectionPoint(_vert[_i1[0]],_vert[_i1[1]],self.isovalue,_sv[_i1[0]],_sv[_i1[1]])
                    p2=self.intersectionPoint(_vert[_i2[0]],_vert[_i2[1]],self.isovalue,_sv[_i2[0]],_sv[_i2[1]])
                    area1o3 = area1o3 + float((self.gridSize**2)-((1.0/2.0)*(self.gridSize/2.0)*((2*(self.gridSize)**2)**0.5)))
                    #aa = float((self.gridSize**2)-((1.0/2.0)*(self.gridSize/2.0)*((2*(self.gridSize)**2)**0.5)))
		    #print aa
                    #print "else"
		    #area1o3 = area1o3 + float((self.gridSize**2)-((1.0/2.0)*(p1)*(p2)))
                self.linelist.append([p1,p2])
		#print("point of intersections")
		#print(p1, p2)
		posline2 = '{0} {1} \n'.format(p1[0],p1[1])
		posline3 = '{0} {1} \n'.format(p2[0],p2[1])
                textfile2.write(posline2)
		textfile2.write(posline3)
        #output to screen area and number of squares 
	print "Number of full squares:"
	print cfull
	print "Number of partial squares:"
	print cpart
 	print "Area of partial squares:"
	TParea = area2 + area1o3 
	TParea = float(TParea)
 	print TParea
        return cfull, cpart, TParea


    #Computes the line list
    #def compute2(self):
        #self._scVal = np.zeros(((self.winWidth/self.gridSize)+1,(self.winHeight/self.gridSize)+1))
        #_nSquare = ((self.winHeight/self.gridSize)-1)*((self.winWidth/self.gridSize)-1)
        #self.compSval()
        #for i in np.arange(0,_nSquare):
        #    [_sv,_vert] = self.getSquareData(i)
        #return traparea, trapnum 
