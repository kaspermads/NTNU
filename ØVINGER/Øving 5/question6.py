import math
from math import factorial as fact

from scipy import stats # statistikk-modulen i scipy-pakken
import matplotlib.pyplot as plt # plotting


mu = 2 # forventningsverdi
x = 0     # det tallet vi vil regne på sannsynlighet for
stats.poisson.pmf(x,mu)  # P(X = x)

rate = 0.26

print(math.e**(-10*rate))