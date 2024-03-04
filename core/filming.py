import os

def frame(environment, walkers, step: int):
    """
    Returns a frame counting the walkers at each coordinate at a step.

      for no walkers
    * for single walkers
    2-9 for 2 through 9 walkers
    # for ten or more
    O for impassable cells
    """
    frame = list(list(row) for row in environment)
    for l, line in enumerate(frame):
        for n, number in enumerate(line):
            if number == 1: frame[l][n] = "O"
    for walker in walkers:
        x, y = walker[step]
        frame[y][x] += 1
    for l, line in enumerate(frame):
        for n, number in enumerate(line):
            if number == 0: frame[l][n] = " "
            elif number == 1: frame[l][n] = "*"
            elif isinstance(number, int) and number > 9: frame[l][n] = "#"
            else: frame[l][n] = str(number)
    return tuple("".join(line) for line in reversed(frame))


def film(environment, walkers):
    """
    Returns a tuple of frames counting the walkers at each coordinate,
    representing single walkers with *, ten or more with #, and
    impassable cells with O.
    """
    return tuple(frame(environment, walkers, step) for step
                 in range(len(walkers[0])))


def display_frame(film, index: int):
    """Pretty prints the selected frame of a film."""
    for line in film[index]: print(line)


def display_film(film):
    """
    Pretty prints the film, frame by frame, as a movie in the terminal.
    """
    clear = 'cls' if os.name == 'nt' else 'clear'
    for frame in film:
        system(clear)
        for line in frame: print(line)
