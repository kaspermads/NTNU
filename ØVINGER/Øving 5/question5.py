import math
from math import factorial as fact

from scipy import stats # statistikk-modulen i scipy-pakken
import matplotlib.pyplot as plt # plotting


mu = 2 # forventningsverdi
x = 0     # det tallet vi vil regne på sannsynlighet for
stats.poisson.pmf(x,mu)  # P(X = x)

#a 
# x = 0
print(stats.poisson.pmf(0, 2))

#b

P_2 = 1 - stats.poisson.cdf(2,2)

P_0 = 1 - stats.poisson.cdf(0,2)

print(P_2/P_0)

#c

print(math.sqrt(2))