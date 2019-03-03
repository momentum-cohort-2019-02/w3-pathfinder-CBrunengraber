        ### step 1 how to sort data into two lists x axis and y axis - DONE - elevations
        ### step 2 find min, max elevations, and other calculations on the data
        ### step 3 Draw the map
        ### step 4 Draw a lowest elevation change route starting from some row
        ### step 5 find and draw the lowest elevation change route in the map
        ### you will need to import from PIL
        ### Resources: use python for beginners, realpython.com, importpython.com, pycoder.com,
from PIL import Image, ImageColor, ImageDraw  
import sys
x = 0
y = 0


class Map:
    """
    Reads text file of map, and puts into multistring form. Shows elevation by color in image file.
    """
    def __init__(self):
        # self.elevations = elevations
        
        with open('elevation_small.txt') as file:
            elevations = [line.split() for line in file]
            elevations = [[int(elevation) for elevation in row] for row in elevations]
            # print(elevations)
# elevations = [0]
# max(max(x) for x in elevations)

# Python 3 code to find max element  
# in a matrix 
  
# Function to find max element 
# mat[][] : 2D array to find max element 
def findMax(elements): 
      
    # Initializing max element as INT_MIN 
    maxElement = -sys.maxsize - 1
  
    # checking each element of matrix 
    # if it is greater than maxElement, 
    # update maxElement 
    for i in range(x): 
        for j in range(y): 
            if (elevations[i][j] > maxElement): 
                maxElement = elevations[i][j] 
          
    # finally return maxElement 
    return maxElement 
  
# Driver code 
if __name__ == '__main__': 
      
    # matrix 
    elevations = [0] 
    print(findMax(elevations)) 




# class MapImage:
#     """
#     Generates the lists and methods used to create a map.
#     """



# class Pathfinder:
#     """
#     Shows the path starting from 0 0 to the easternside of the map. Create a method for a "greedy" algorithm that takes a "step" to any of the three adjacent cells in the next column over. Must choose closest to current elevation, in case of a tie go forwards if possible, and in a case of smallest change is a tie, pick randomly.
#     """

# if __name__ == "__main__":

