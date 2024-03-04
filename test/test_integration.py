"""Integration tests"""
#project modules
from Random_Walkers.core import loading
from Random_Walkers.core import simulation
from Random_Walkers.core import analysis
from Random_Walkers.core import tallying
from Random_Walkers.core import regression
from Random_Walkers.core import graphing
from Random_Walkers.core import filming
from Random_Walkers.core import printing
#external modules
import matplotlib.pyplot as plt

def test_integration():
    """
    Walks random walkers through an environment and displays how the
    tallies of how many cells of that environment contain how many
    walkers approach a Maxwell-Boltzmann distribution over time.
    """
    #load
    config = loading.Config("config.json")
    data = loading.Data("data.json")
    environment = loading.environment("environment.txt")
    #simulate
    walkers = simulation.walkers_initial(data.steps,
                                         data.number_of_walkers,
                                         data.x0, data.y0)
    walkers = simulation.walk(environment, walkers, data.seed)
    #analyze
    walkers = analysis.tuplefied(walkers)
    history = analysis.history(environment, walkers)
    #tally
    tallies = tallying.tallies(history[-1])
    tallies_history = tallying.tallies_history(history)
    normalized_tallies = tallying.normalized_tallies(tallies)
    #regress
    sigma, model, error = regression.Maxwell_Boltzmann_fit(normalized_tallies,
                                                           config.increment,
                                                           config.decimals)
    #print
    printing.print_analysis(tallies, sigma, error, config.decimals)
    #film
    film = filming.film(environment, walkers)
    if config.animate: filming.display_film(film)
    else: filming.display_frame(film, -1)
    #graph
    fig = graphing.data_versus_model(normalized_tallies, model)
    #animate
    anim = graphing.scatter_animation(tallies_history[::config.ratio])
    plt.show()
