RANDOM WALKERS
-Adam Finkle

REQUIREMENTS:
    -Python Interpreter
    -virtualenv
    

HOW TO RUN:
    -Open your terminal
    -Change directory to the Source folder
    -Enter the shell command "source bin/activate" to open a virtual environment
    -Enter the shell command “python main.py"


RESULT:
        Within seconds, the program will simulate the steps of random walkers
    across an enclosed, obstacle-filled environment.  It counts the walkers at
    each coordinate and records these results in tuples of 2D frames called
    history and film. The program tallies how many cells have how many walkers
    in each frame of history, starting at 0 for empty cells, and returns an
    animated scatter plot of the tally throughout history.  The program also
    prints the last frame of the film, each frame of which is a pretty
    representation of history, with "O" representing an impassable cell, "*"
    representing one walker, and "#" representing ten or more.  Below the film
    frame, the program prints the tally for the last history frame, the sigma of
    the Maxwell-Boltzmann distribution best fitting it, and its error.  The
    tally and distribution are represented in scatter plots that appear after
    the user closes the tally animation.


CONFIGURATION:
    Random Walkers is fully-configurable.
    -config.txt
        >increment of the plots and curve-fitting
        >decimal places of the sigma and error
        >number of history frames to skip in the tally animation
        >1 to print film animation or 0 to print last film frame
    -data.txt
        >number of steps for each random walker to take
        >number of random walkers
        >starting y-coordinate of all the walkers
        >starting x-coordinate of all the walkers
    -environment.txt
        >a one-to-one specification of the environment the walkers traverse.
        1s specify impassable cells, and 0s specify passable ones.  The
        environment must be rectangular and enclosed by 1s, but the user may
        choose any cell within these bounds to be 0 or 1.
