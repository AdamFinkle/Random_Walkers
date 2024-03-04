def tallies(grid: tuple[tuple[int]]) -> tuple[int]:
    """
    Returns how many cells hold how many walkers in a history grid.

    Each index of the returned tuple is the number of walkers, and
    the value at each index is the number of cells holding the
    corresponding number of walkrs.

    For example (3, 4, 5) would mean that 3 cells held one walker, 4 
    cells held two walkers, and 5 cells held three walkers.

    grid - a nested tuple counting the walkers at each (x,y) coordinate
           of the environment
    """
    numbers = []
    for row in grid:
        for i in row:
            try:
                if not i == "O": numbers[i] += 1
            except:
                numbers.extend([0 for j in range(i-len(numbers))] + [1])
    return tuple(numbers)


def normalized_tallies(tallies: tuple[int]) -> tuple[float]:
    """
    Returns each talley divided by the total tallies.

    Each index of the returned tuple is the number of walkers, and
    the value at each index is the number of cells holding the
    corresponding number of walkrs.

    For example (0.3, 0.5, 0.2) would mean that 30% of the cells held
    one walker, 50% of the cells held two walkers, and 20% of the cells 
    held three walkers.

    tallies - a tuple of integers counting how many cells held
              how many walkers
    """
    n = sum(tallies)
    return tuple(tally/n for tally in tallies)


def tallies_history(history) -> tuple[tuple[int]]:
    """
    Returns a history of the raw tallies at each step of the walk.
    """
    return tuple(tallies(grid) for grid in history)
