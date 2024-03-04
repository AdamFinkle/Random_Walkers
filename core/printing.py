def print_analysis(tallies, sigma, error: float, decimals: int):
    """
    Prints the tallies, sigma, and standard error of a Maxwell-Boltzmann
    fit.
    """
    print("Tallies:", tallies,
          "\nSigma:", round(sigma, decimals),
          "\nStandard Error:", round(error*sum(tallies), decimals))
