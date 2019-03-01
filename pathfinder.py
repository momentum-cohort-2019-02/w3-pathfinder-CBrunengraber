        ### step 1 how to sort data into two lists x axis and y axis - should these be defined?
class Map:
    """
    Reads text file of map, and puts into multistring form. Shows elevation by color in image file.
    """
    def __init__(self):
        


        with open('elevation_small.txt') as file:
            elevations = [line.split() for line in file]
            elevations = [[int(elevation) for elevation in row] for row in elevations]
            print(elevations)

class MapImage:
    """
    Generates the lists and methods used to create a map.
    """

class Pathfinder:
    """
    Shows the path starting from 0 0 to the easternside of the map. Create a method for a "greedy" algorithm that takes a "step" to any of the three adjacent cells in the next column over. Must choose closest to current elevation, in case of a tie go forwards if possible, and in a case of smallest change is a tie, pick randomly.
    """


