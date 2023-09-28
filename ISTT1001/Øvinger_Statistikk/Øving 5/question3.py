import math
from math import factorial as fact

from scipy import stats # statistikk-modulen i scipy-pakken
import matplotlib.pyplot as plt # plotting




def poisson(x, rate, tid):
    return ((((rate*tid)**x)*math.e**(-rate*tid))/(fact(x)))

def forventningsverdi_E(rate,tid):
    return rate*tid
    

mu = 5.4 # forventningsverdi
x = 3     # det tallet vi vil regne på sannsynlighet for
stats.poisson.pmf(x,mu)  # P(X = x)

plt.bar(range(0,20), stats.poisson.pmf(range(0, 20), mu))
plt.grid(); plt.ylabel("P(X = x)"); plt.xlabel("x")
plt.show()

#a

print(stats.poisson.pmf(10,5.47))

#b
print(stats.poisson.cdf(4,5.47))

#c

print(stats.poisson.cdf(6,5.47) - stats.poisson.cdf(2,5.47))