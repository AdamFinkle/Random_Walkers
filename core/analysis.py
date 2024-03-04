def history(environment: tuple[tuple[int]], 
            paths: tuple[tuple]) -> tuple[tuple[tuple[int]]]:
    """
    Returns a tuple of tuple grids counting the walkers at each 
    coordinate, noting impassable cells.

    Each grid represents the distribution of walkers at each
    simulation step, counting the walkers at each coordinate pair on
    the grid.
    """
    steps = len(paths[0])
    history = [None for step in range(steps)]
    environment = list(list(row) for row in environment)
    for r, row in enumerate(environment):
        for n, number in enumerate(row):
            if number: environment[r][n] = "O"
    environment = tuple(tuple(row) for row in environment)
    for step in range(steps):
        grid = list(list(row) for row in environment)
        for path in paths:
            x, y = path[step]
            grid[y][x] += 1
        history[step] = tuple(tuple(row) for row in grid)
    return tuple(tuple(grid) for grid in history)
