import math
from math import factorial as fact

from scipy import stats # statistikk-modulen i scipy-pakken
import matplotlib.pyplot as plt # plotting


mu_A = 12 # forventningsverdi
mu_B = 20
x = 0     # det tallet vi vil regne på sannsynlighet for
stats.poisson.cdf(x,mu_A)  # P(X = x)

P_L_gitt_A = 1- math.e**(-mu_A*15)
print(P_L_gitt_A/(6/9))

