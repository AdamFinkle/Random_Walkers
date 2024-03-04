import math, random

def _Maxwell_Boltzmann_PDF(o: float, x: float) -> float:
    """
    Returns the value of a Maxwell-Boltzmann probability density function,
    of sigma o, at x
    """
    return math.sqrt(2/math.pi) * x**2/o**3 * math.e**(-(x**2)/(2*(o**2)))


def _values(f: object, arguments: list, iterations: int, step: float) -> list:
    """
    Returns an iterations-long list of the values of a function of a single
    variable with constant arguments, incrementing by step per iteration.
    """
    return [f(*arguments, i*step) for i in range(iterations)]


def _residual_sum_of_squares(values: list, data: list) -> float:
    return sum((datum - value)**2 for value, datum in zip(values, data))


def _Maxwell_Boltzmann_PDF_sigma(data, step, decimals: int) -> float:
    """
    Returns the sigma of the Maxwell-Boltzmann distribution best 
    fitting the data, rounded to the specified decimals.  Step 
    specifies the increment of x between values of the distribution.
    """
    iterations = len(data)
    sigma = 0.75 #Don't set this too low, or else you'll get a delta function
    guess = _values(_Maxwell_Boltzmann_PDF, [sigma], iterations, step)
    old = _residual_sum_of_squares(guess, data)
    increment = 10**(-decimals)
    limit = increment / 10 #Allows one last back-pass to reach nominal tolerance
  
    while(abs(increment) > limit):
        sigma += increment
        guess = _values(_Maxwell_Boltzmann_PDF, [sigma], iterations, step)
        new = _residual_sum_of_squares(guess, data)
        if new < old: old = new
        else: increment *= -0.1
    
    return round(sigma, decimals)

  
def _standard_error_of_regression(data, values):
    return sum(datum-value for datum, value in zip(data, values))/len(data)


def _display(values, scale = 1):
    for v in values: print("*"*int(v*scale))


def Maxwell_Boltzmann_fit(data, step, decimals):
    """
    Returns the sigma and values of the Maxwell-Boltzmann distribution
    best fitting the data, alongside the standard error of this 
    regression.  Sigma and error are rounded to the given number of 
    decimals.
    """
    sigma = _Maxwell_Boltzmann_PDF_sigma(data, step, decimals)
    model = _values(_Maxwell_Boltzmann_PDF, [sigma], len(data), step)
    error = _standard_error_of_regression(data, model)
    return sigma, model, error


def main():
    """Demonstration of the above methods."""
    iterations = 30
    step = 0.30
    decimals = 3
    arguments = [2]
  
    data = values(Maxwell_Boltzmann, arguments, iterations, step)
    data = [datum + random.gauss(0, 0.1) for datum in data]
    sigma, model, error = Maxwell_Boltzmann_fit(data, step, decimals)
  
    scale = 50
    _display(data, scale)
    print(sigma)
    _display(model, scale)
    print(error)
if __name__ == "__main__": main()
