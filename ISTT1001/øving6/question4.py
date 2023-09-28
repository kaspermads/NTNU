import math
import statistics as stats
from scipy import stats

import matplotlib.pyplot as plt
import numpy as np

mu = (35*0.2)

sigma = math.sqrt(35*0.2*0.8)

Z = stats.norm.cdf(10,mu,sigma)
print(Z)

P = stats.binom.cdf(10,35,0.2)
print(P)

Z_2 = stats.norm.cdf(10.5,mu,sigma)
print(Z_2)