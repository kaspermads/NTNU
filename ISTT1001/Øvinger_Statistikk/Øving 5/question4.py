import math
from math import factorial as fact

from scipy import stats # statistikk-modulen i scipy-pakken
import matplotlib.pyplot as plt # plotting


mu = (0.45*24) # forventningsverdi
x = 3     # det tallet vi vil regne på sannsynlighet for
stats.poisson.pmf(x,mu)  # P(X = x)

plt.bar(range(0,23), stats.poisson.pmf(range(0, 23), mu))
plt.grid(); plt.ylabel("P(X = x)"); plt.xlabel("x")
plt.show()
