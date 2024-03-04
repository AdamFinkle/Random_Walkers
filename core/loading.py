import json

class Config:
    """Configuration of the display and print-outs"""
    def __init__(self, path):
        with open(path) as f:
            config = json.load(f)
        self._increment = config["increment"]
        self._decimals = config["decimals"]
        self._ratio = config["ratio"]
        self._animate = config["animate"]

    @property
    def increment(self):
        return self._increment

    @property
    def decimals(self):
        """Number of decimals for calculation reporting."""
        return self._decimals

    @property
    def ratio(self):
        """
        How many frames of history to skip between each animation"""
        return self._ratio

    @property
    def animate(self):
        """Whether to animate the movement of walkers in the terminal"""
        return self._animate


class Data:
    """Data initializing the simulation"""
    def __init__(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        self._steps = data["steps"]
        self._numberOfWalkers = data["numberOfWalkers"]
        self._x0 = data["x0"]
        self._y0 = data["y0"]
        self._seed = data["seed"]

    @property
    def steps(self):
        """How many steps each walker should take during one simulation"""
        return self._steps

    @property
    def number_of_walkers(self):
        """How many walkers should be simulated"""
        return self._numberOfWalkers

    @property
    def x0(self):
        """The starting x coordinate of all the walkers"""
        return self._x0

    @property
    def y0(self):
        """The starting y coordinate of all the walkers"""
        return self._y0

    @property
    def seed(self):
        """Seed for random generation of walk directions"""
        return self._seed


def environment(path):
    """
    Returns the environment as a nested tuple grid of integers.

    Reads every line except the last, which is presumed to be a newline
    character, and converts each character into an integer, including
    non-digit characters.

    path - string path to the environment file
    """
    with open(path, 'r') as f:
        return tuple(tuple(int(i) for i in line[:-1]) for line in f.readlines())
