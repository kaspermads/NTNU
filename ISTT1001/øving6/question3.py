import math
import statistics as stats
from scipy import stats

import matplotlib.pyplot as plt
import numpy as np

mu = 12   # forventningsverdien til X
sigma = 1.3  # standardavviket til X

xval = np.linspace(mu - 4*sigma, mu + 4*sigma, 100)  # x-verdier
fx = stats.norm.pdf(xval, mu, sigma)                 # f(x)
plt.plot(xval, fx)
plt.grid(); plt.ylabel("f(x)"); plt.xlabel("x")
#plt.show()


p_11= 1 - stats.norm.cdf(11, mu, sigma)
print(p_11)
#B

p_13 = 1 - stats.norm.cdf(13, mu, sigma)

print(p_13/p_11)




