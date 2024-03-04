"""Unit tests"""
#project modules
from Random_Walkers.core import loading
from Random_Walkers.core import simulation
from Random_Walkers.core import analysis
from Random_Walkers.core import regression
from Random_Walkers.core import graphing
from Random_Walkers.core import tallying
from Random_Walkers.core import filming
from Random_Walkers.core import printing
#external modules
import matplotlib.pyplot as plt
import pytest


def test_Config():
    """
    Config loads its json, and each field has the right type.
    """
    config = loading.Config("config.json")
    assert isinstance(config.increment, int)
    assert isinstance(config.decimals, int)
    assert isinstance(config.ratio, int)
    assert isinstance(config.animate, bool)


def test_Data():
    """
    Config loads its json, and each field has the right type.
    """
    data = loading.Data("data.json")
    assert isinstance(data.steps, int)
    assert isinstance(data.number_of_walkers, int)
    assert isinstance(data.x0, int)
    assert isinstance(data.y0, int)
    assert isinstance(data.seed, int)


def test_environment():
    """
    environment() loads its text file and returns a nested tuple of
    zeros and ones.
    """
    environment = loading.environment("environment.txt")
    assert isinstance(environment, tuple)
    for row in environment:
        assert isinstance(row, tuple)
        for element in row:
            assert isinstance(element, int)
            assert element == 0 or element == 1


def test_walkers_initial():
    """
    A group of walkers initializes with the correct number, position,
    and path history.

    Should be [[(x0, y0), None, None, ... None], [...], ... ]
    """
    steps = 8
    number_of_walkers = 3
    x0 = 2
    y0 = 2
    walkers = simulation.walkers_initial(steps, number_of_walkers, x0, y0)
    assert walkers == [
        [(2,2), None, None, None, None, None, None, None],
        [(2,2), None, None, None, None, None, None, None],
        [(2,2), None, None, None, None, None, None, None]
    ]

@pytest.fixture
def small_environment():
    return ((1,1,1,1,1,1,1),
            (1,0,0,0,0,0,1),
            (1,0,0,0,0,0,1),
            (1,0,0,0,0,0,1),
            (1,0,0,0,0,0,1),
            (1,0,0,0,0,0,1),
            (1,1,1,1,1,1,1))


def test_walk(small_environment):
    """
    Walkers walk as expected.

    Tests a few walkers in a small box.
    """
    initial_walkers = [
        [(5,5), None, None, None, None, None, None, None],
        [(5,5), None, None, None, None, None, None, None],
        [(5,5), None, None, None, None, None, None, None]
    ]
    steps = 8
    seed = 0
    final_walkers = simulation.walk(small_environment, initial_walkers, seed)
    assert final_walkers == [
        [(5, 5), (5, 4), (4, 4), (3, 4), (3, 5), (3, 5), (3, 5), (4, 5)],
        [(5, 5), (5, 4), (5, 3), (5, 2), (5, 3), (5, 3), (4, 3), (3, 3)],
        [(5, 5), (5, 5), (5, 4), (4, 4), (3, 4), (2, 4), (3, 4), (3, 3)]
    ]


def test_tuplefied():
    """
    Nested list changes to nested tuple. 
    """
    walkers = [
        [(5, 5), (5, 4), (4, 4), (3, 4), (3, 5), (3, 5), (3, 5), (4, 5)],
        [(5, 5), (5, 4), (5, 3), (5, 2), (5, 3), (5, 3), (4, 3), (3, 3)],
        [(5, 5), (5, 5), (5, 4), (4, 4), (3, 4), (2, 4), (3, 4), (3, 3)]
    ]
    assert analysis.tuplefied(walkers) == (
        ((5, 5), (5, 4), (4, 4), (3, 4), (3, 5), (3, 5), (3, 5), (4, 5)),
        ((5, 5), (5, 4), (5, 3), (5, 2), (5, 3), (5, 3), (4, 3), (3, 3)),
        ((5, 5), (5, 5), (5, 4), (4, 4), (3, 4), (2, 4), (3, 4), (3, 3))
    )


@pytest.fixture
def stacked_walkers():
    """
    Walkers stacked from 1 to 10 in a small environment to demonstrate
    the tally tracking in the film frame.
    """
    return (((1,1),),
            ((1,2),),
            ((1,2),),
            ((1,3),),
            ((1,3),),
            ((1,3),),
            ((1,4),),
            ((1,4),),
            ((1,4),),
            ((1,4),),
            ((1,5),),
            ((1,5),),
            ((1,5),),
            ((1,5),),
            ((1,5),),
            ((2,1),),
            ((2,1),),
            ((2,1),),
            ((2,1),),
            ((2,1),),
            ((2,1),),
            ((2,2),),
            ((2,2),),
            ((2,2),),
            ((2,2),),
            ((2,2),),
            ((2,2),),
            ((2,2),),
            ((2,3),),
            ((2,3),),
            ((2,3),),
            ((2,3),),
            ((2,3),),
            ((2,3),),
            ((2,3),),
            ((2,3),),
            ((2,4),),
            ((2,4),),
            ((2,4),),
            ((2,4),),
            ((2,4),),
            ((2,4),),
            ((2,4),),
            ((2,4),),
            ((2,4),),
            ((2,5),),
            ((2,5),),
            ((2,5),),
            ((2,5),),
            ((2,5),),
            ((2,5),),
            ((2,5),),
            ((2,5),),
            ((2,5),),
            ((2,5),))


def test_frame(small_environment, stacked_walkers):
    """
    Stacked walkers in a small environment fill every digital
    representation in the film.
    """
    step = 0
    frame = filming.frame(small_environment, stacked_walkers, step)
    assert "".join(frame[0]) == "OOOOOOO"
    assert "".join(frame[1]) == "O5#   O"
    assert "".join(frame[2]) == "O49   O"
    assert "".join(frame[3]) == "O38   O"
    assert "".join(frame[4]) == "O27   O"
    assert "".join(frame[5]) == "O*6   O"
    assert "".join(frame[6]) == "OOOOOOO"


@pytest.fixture
def one_frame_history():
    """A history with one frame representing the stacked walkers."""
    return ((('O', 'O', 'O', 'O', 'O', 'O', 'O'),
             ('O', 1, 6, 0, 0, 0, 'O'),
             ('O', 2, 7, 0, 0, 0, 'O'),
             ('O', 3, 8, 0, 0, 0, 'O'),
             ('O', 4, 9, 0, 0, 0, 'O'),
             ('O', 5, 10, 0, 0, 0, 'O'),
             ('O', 'O', 'O', 'O', 'O', 'O', 'O')),)


def test_history(small_environment, stacked_walkers, one_frame_history):
    """
    Stacked walkers in a small environment are totalled accurately.
    """
    history = analysis.history(small_environment, stacked_walkers)
    assert history == one_frame_history


def test_tallies(one_frame_history):
    """The one frame history should have fifteen zeroes and ten ones."""
    assert (tallying.tallies(one_frame_history[0])
            == (15, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))
