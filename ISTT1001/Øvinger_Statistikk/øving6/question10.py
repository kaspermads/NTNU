import math
from scipy import stats

import matplotlib.pyplot as plt

mu = 200
sigma = 9
x_threshold = 185.0  # Grense for akseptable sylindere
x = 191.75  # Ønsket trykkfasthet


#a
Z = ((mu-185)/sigma)

print( 1- stats.norm.cdf(Z))

#b
Z_2= ((191.75-mu)/sigma)

probability = stats.norm.cdf(Z_2) 

z_x = (x - mu) / sigma
z_threshold = (x_threshold - mu) / sigma
probability = (stats.norm.cdf(z_x) - stats.norm.cdf(z_threshold)) / (1 - stats.norm.cdf(z_threshold))

print(probability)

#c
n = 14
p = probability
probability_1 = sum(stats.binom.pmf(k, n, p) for k in range(3))
print(probability_1)

