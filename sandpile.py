# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:41:24 2018
@author: mlund
"""

import numpy as np
import matplotlib.pyplot as plt

#generates a random 2D array
#low is minimum cell count
#max is maximum cell count
#dim is dimensions of array
def randomArray(low,high,dim):
    field = np.random.randint(low,high,(dim,dim))
    return field
#Starts with random assortment of cells
#low is integer for minimum cell count
#high is integer for maximum cell count minus 1
#dim is dimensions of grid
def rule1(low, high, maxHeight, dim):
    a = randomArray(low,high, dim)
    rows = a.shape[0]
    cols = a.shape[1]
    while np.max(a)>maxHeight:
        t=1
        for i in range(0,rows):
            for j in range(0,cols):
                while a[i][j] > maxHeight:
                    # check top left corner
                    if (j-1 < 0) and (i-1 < 0):
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i][j+1] = a[i][j+1] + 1
                            a[i+1][j] = a[i+1][j] + 1
                            a[0][cols-1] = a[0][cols-1] + 1 #closed periodic grid
                            a[rows-1][0] = a[rows-1][0] + 1 #closed periodic grid
                    # check top right corner
                    elif (j+1 >= cols) and (i-1 < 0):
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i][j-1] = a[i][j-1] + 1
                            a[i+1][j] = a[i+1][j] + 1
                            a[0][0] = a[0][0] + 1 #closed periodic grid
                            a[rows-1][cols-1] = a[rows-1][cols-1] + 1 #closed periodic grid
                    # check bottom left corner
                    elif (j-1 < 0) and (i+1 >= rows):
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i][j+1] = a[i][j+1] + 1
                            a[i-1][j] = a[i-1][j] + 1
                            a[0][0] = a[0][0] + 1 #closed periodic grid
                            a[rows-1,cols-1] = a[rows-1,cols-1] + 1 #closed periodic grid
                    # check bottom right corner
                    elif (j+1 >= cols) and (i+1 >= rows):
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i][j-1] = a[i][j-1] + 1
                            a[i-1][j] = a[i-1][j] + 1
                            a[rows-1,0] = a[rows-1,0] + 1 #closed periodic grid
                            a[0,cols-1] = a[0,cols-1] + 1 #closed periodic grid
                    # beginning of row
                    elif(j-1 < 0):
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i-1][j] = a[i-1][j] + 1
                            a[i+1][j] = a[i+1][j] + 1
                            a[i][j+1] = a[i][j+1] + 1
                            a[i][cols-1] = a[i][cols-1] + 1 #closed periodic grid
                    # end of row
                    elif(j+1 >= cols):
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i][j-1] = a[i][j-1] + 1
                            a[i-1][j] = a[i-1][j] + 1
                            a[i+1][j] = a[i+1][j] + 1
                            a[i][0] = a[i][0] + 1 #closed periodic grid
                    # beginning of column
                    elif(i-1 < 0):
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i][j-1] = a[i][j-1] + 1
                            a[i+1][j] = a[i+1][j] + 1
                            a[i][j+1] = a[i][j+1] + 1
                            a[rows-1][j] = a[rows-1][j] + 1 #closed periodic grid
                    # end of column
                    elif(i+1>=rows):
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i][j-1] = a[i][j-1] + 1
                            a[i-1][j] = a[i-1][j] + 1
                            a[i][j+1] = a[i][j+1] + 1
                            a[0][j] = a[0][j] + 1 #closed periodic grid
                    else:
                        if a[i][j] > maxHeight:
                            a[i][j] = a[i][j] - 4
                            a[i][j-1] = a[i][j-1] + 1
                            a[i-1][j] = a[i-1][j] + 1
                            a[i+1][j] = a[i+1][j] + 1
                            a[i][j+1] = a[i][j+1] + 1
        print(t)
        plt.imshow(a, cmap='seismic')
        plt.colorbar()
        plt.show()
        t=t+1
        
#Creates sandpile in center and corners
#Max height is the maximum height of a cell
#dim is dimension of grid
#pile is how much to pile in the corners and center
#neighbor is type of neighborhood 'Moore' or 'Von Neumann'
def rule2(maxHeight, dim, pile, neighbor):
    a = np.zeros((dim,dim))
    rows = a.shape[0]
    cols = a.shape[1]
    a[int(dim/2)][int(dim/2)] = pile #center pile
##    a[1][1] = pile #top left corner pile
##    a[rows-1][1] = pile #bottom left corner pile
##    a[1][cols-1] = pile #top right corner pile
##    a[rows-1][cols-1] = pile #bottom right corner pile
##    a[int(dim/2), 1] = pile #center far left column pile
##    a[int(dim/2), cols-1] = pile #center far right column pile
##    a[1, int(dim/2)] = pile #center top row pile
##    a[rows-1, int(dim/2)] = pile #center bottom row pile
#    a[1, int(dim/4)*3] = pile
#    a[1, int(dim/4)] = pile
#    a[rows-1, int(dim/4)*3] = pile
#    a[rows-1, int(dim/4)] = pile 
#    a[int(dim/4)*3, 1] = pile
#    a[int(dim/4), 1] = pile
#    a[int(dim/4)*3, cols-1] = pile
#    a[int(dim/4), cols-1] = pile
    if neighbor == 'Von Neumann':
        t = 1
        while np.max(a)> maxHeight:
                for i in range(0,rows):
                    for j in range(0,cols):
                        while a[i][j] > maxHeight:
                            # check top left corner
                            if (j-1 < 0) and (i-1 < 0):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[0][cols-1] = a[0][cols-1] + 1 #closed periodic grid
                                    a[rows-1][0] = a[rows-1][0] + 1 #closed periodic grid
                            # check top right corner
                            elif (j+1 >= cols) and (i-1 < 0):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[0][0] = a[0][0] + 1 #closed periodic grid
                                    a[rows-1][cols-1] = a[rows-1][cols-1] + 1 #closed periodic grid
                            # check bottom left corner
                            elif (j-1 < 0) and (i+1 >= rows):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[0][0] = a[0][0] + 1 #closed periodic grid
                                    a[rows-1,cols-1] = a[rows-1,cols-1] + 1 #closed periodic grid
                            # check bottom right corner
                            elif (j+1 >= cols) and (i+1 >= rows):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[rows-1,0] = a[rows-1,0] + 1 #closed periodic grid
                                    a[0,cols-1] = a[0,cols-1] + 1 #closed periodic grid
                            # beginning of row
                            elif(j-1 < 0):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i][cols-1] = a[i][cols-1] + 1 #closed periodic grid
                            # end of row
                            elif(j+1 >= cols):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i][0] = a[i][0] + 1 #closed periodic grid
                            # beginning of column
                            elif(i-1 < 0):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[rows-1][j] = a[rows-1][j] + 1 #closed periodic grid
                            # end of column
                            elif(i+1>=rows):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[0][j] = a[0][j] + 1 #closed periodic grid

                            else:
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 4
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i][j+1] = a[i][j+1] + 1
                print(t)
                plt.imshow(a, cmap='viridis')
                #plt.colorbar()
                plt.xticks([],[])
                plt.yticks([],[])
                plt.savefig(str(t)+'.png',dpi=300)
                plt.close()
                t = t+1
    elif neighbor == 'Moore':
        t = 1
        while np.max(a) > maxHeight:
                for i in range(0,rows):
                    for j in range(0,cols):
                        while a[i][j] > maxHeight:
                            # check top left corner
                            if (j-1 < 0) and (i-1 < 0):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i+1][j+1] = a[i+1][j+1] + 1
                                    a[0][cols-1] = a[0][cols-1] + 1 #closed periodic grid send to top right
                                    a[rows-1][0] = a[rows-1][0] + 1 #closed periodic grid send to bottom left
                                    a[rows-1][1] = a[rows-1][1] + 1 #closed periodic grid send to the right of bottom left
                                    a[rows-1][cols-1] = a[rows-1][cols-1] + 1 #closed periodic grid send to bottom right
                                    a[1][cols-1] = a[1][cols-1] + 1 #closed periodic grid send to second row, far right
                            # check top right corner
                            elif (j+1 >= cols) and (i-1 < 0):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i+1][j-1] = a[i+1][j-1] + 1
                                    a[0][0] = a[0][0] + 1 #closed periodic grid, send to top left
                                    a[rows-1][cols-1] = a[rows-1][cols-1] + 1 #closed periodic grid, send to bottom right
                                    a[1][0] = a[1][0] + 1 #closed periodic grid, send to first col, second row
                                    a[rows-1][0] = a[rows-1][0] + 1 #closed periodic grid, send to bottom left
                                    a[rows-1][cols-2] = a[rows-1][cols-2] + 1 #closed periodic grid, send to left of bottom right
                            # check bottom left corner
                            elif (j-1 < 0) and (i+1 >= rows):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i-1][j+1] = a[i-1][j+1] + 1
                                    a[0][0] = a[0][0] + 1 #closed periodic grid, send to top left
                                    a[rows-1][cols-1] = a[rows-1][cols-1] + 1 #closed periodic grid send to bottom right
                                    a[0][cols-1] = a[0][cols-1] + 1 #closed periodic grid send to top right
                                    a[rows-2][cols-1] = a[rows-2][cols-1] + 1 #closed periodic grid, send to one above bottom right
                                    a[0][1] = a[0][1] + 1 #closed periodic grid, send to right of top left
                            # check bottom right corner
                            elif (j+1 >= cols) and (i+1 >= rows):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i-1][j-1] = a[i-1][j-1] + 1
                                    a[0][cols-1] = a[0][cols-1] + 1 #closed periodic grid send to top right
                                    a[0][0] = a[0][0] + 1 #closed periodic grid, send to top left
                                    a[rows-1][0] = a[rows-1][0] + 1 #closed periodic grid, send to bottom left
                                    a[rows-2][0] = a[rows-1][0] + 1 #closed periodic grid, send to one above bottom left
                                    a[0][cols-2] = a[0][cols-2] + 1 #closed periodic grid, send to left of top right
                            # beginning of row
                            elif(j-1 < 0):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i-1][j+1] = a[i-1][j+1] + 1
                                    a[i+1][j+1] = a[i+1][j+1] + 1
                                    a[i][cols-1] = a[i][cols-1] + 1 #closed periodic grid, send to far right column
                                    a[i-1][cols-1] = a[i-1][cols-1] + 1 #closed periodic grid, send above far right column
                                    a[i+1][cols-1] = a[i+1][cols-1] + 1 #closed periodic gird, send below far right column
                            # end of row
                            elif(j+1 >= cols):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i-1][j-1] = a[i-1][j-1] + 1
                                    a[i+1][j-1] = a[i+1][j-1] + 1
                                    a[i][0] = a[i][0] + 1 #closed periodic grid, send to far left column
                                    a[i-1][0] = a[i-1][0] + 1 #closed periodic grid, send to one above far left column
                                    a[i+1][0] = a[i+1][0] + 1 #closed periodic grid, send to one below far left column
                            # beginning of column
                            elif(i-1 < 0):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i+1][j-1] = a[i+1][j-1] + 1
                                    a[i+1][j+1] = a[i+1][j+1] + 1
                                    a[rows-1][j] = a[rows-1][j] + 1 #closed periodic grid, send to bottom row
                                    a[rows-1][j-1] = a[rows-1][j-1] + 1 #closed periodic grid, send to left of bottom row
                                    a[rows-1][j+1] = a[rows-1][j+1] + 1 #closed periodic grid, send to right of bottom row
                            # end of column
                            elif(i+1>=rows):
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i-1][j+1] = a[i-1][j+1] + 1
                                    a[i-1][j-1] = a[i-1][j-1] + 1
                                    a[0][j] = a[0][j] + 1 #closed periodic grid, send to top row
                                    a[0][j-1] = a[0][j-1] + 1 #closed periodic grid, send to left of top row
                                    a[0][j+1] = a[0][j+1] + 1 #closed periodic grid, send to right of top row
                            #check top left diagonal
                            #check top right diagonal
                            #check bottom left diagonal
                            #check bottom right diagonal
                            else:
                                if a[i][j] > maxHeight:
                                    a[i][j] = a[i][j] - 8
                                    a[i][j-1] = a[i][j-1] + 1
                                    a[i-1][j] = a[i-1][j] + 1
                                    a[i+1][j] = a[i+1][j] + 1
                                    a[i][j+1] = a[i][j+1] + 1
                                    a[i-1][j-1] = a[i-1][j-1] + 1
                                    a[i-1][j+1] = a[i-1][j+1] + 1
                                    a[i+1][j-1] = a[i+1][j-1] + 1
                                    a[i+1][j+1] = a[i+1][j+1] + 1
                print(t)
                plt.imshow(a, cmap='viridis')
                #plt.colorbar()
                plt.xticks([],[])
                plt.yticks([],[])
                plt.savefig(str(t)+'.png',dpi=300)
                plt.close()
                t = t+1
        return a
