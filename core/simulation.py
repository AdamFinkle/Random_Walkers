import json
import random
from os import system


def _tuplefied(paths: list[list]) -> tuple[tuple]:
    return tuple(tuple(path) for path in paths)


def paths_initial(steps: int, 
                  number_of_walkers: int, 
                  x0: int, 
                  y0: int) -> list[list]:
    """
    Returns a nested list to contain every step of every walker.

    The nested list has one list for each walker, and each of those
    lists has one tuple of its original coordinates followed by one
    None for every future step.

    Sets the initial position of each walker to the same x and y
    coordinate.

    steps - number of steps for each walker to take
    number_of_walkers - how many walkers to return
    x0 - integer coordinate of lateral position
    y0 - integer coordinate of vertical position

    Usage example:
    >>> walkers_initial(8, 1, 2, 2)
    [[(2, 2), None, None, None, None, None, None, None]]
    """
    
    paths = [[None for _ in range(steps)] for _ in range(number_of_walkers)]
    for path in paths: path[0] = (x0, y0)
    return paths


def walk(environment: tuple[tuple], 
         paths: list[list], 
         seed: int) -> tuple[tuple[int]]:
    """
    Walks the walkers a number of steps through the environment and
    returns a list of their coordinates at each step.

    Each walker randomly chooses to step up, down, left, or right,
    takes a step unless a wall is in the way, and then records its 
    current grid coordinates as an (x,y) tuple of integers in the
    list of its steps.

    environment - grid of 0s and 1s through which the walkers step
    paths - paths the walkers take through the grid, containing one 
            'slot' for an (x,y) coordinate pair per step per walker
    seed - seed for the random number generator for consistent results
    """
    directions = ((1,0), (0,1), (-1,0), (0,-1))
    random.seed(seed)
    def coordinates(x, y):
        choice = random.randint(0,3)
        change = directions[choice]
        return (x+change[0], y+change[1])
    
    for step in range(1, len(paths[0])):
        for path in paths: 
            place = coordinates(*path[step-1])
            if environment[place[1]][place[0]] == 0: path[step] = place
            else: path[step] = path[step-1]
    return _tuplefied(paths)
