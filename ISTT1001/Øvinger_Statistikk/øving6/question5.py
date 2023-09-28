import math
import statistics as stats
from scipy import stats

import matplotlib.pyplot as plt
import numpy as np

mu = 100
sigma = 0.7


#a
Z_99 =stats.norm.cdf(99,mu,sigma)

Z_101 =1 -stats.norm.cdf(101,mu,sigma)

print(Z_101+Z_99)   

#b

print(25*mu + 50)

#c

variance = 25*sigma**2

print(variance)

#d

mu_2 = 2550
X = 2545
sigma_2 = variance
Z_score = ((X-mu_2)/math.sqrt(sigma_2))
probability = stats.norm.cdf(Z_score)   
print(probability)
print(sigma_2)
