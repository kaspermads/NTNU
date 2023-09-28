import math
from scipy import stats

import matplotlib.pyplot as plt

mu_bolt = 15.8

sigma_bolt = 0.07

mu_mutter = 16

sigma_mutter = 0.06

Z_bolt = (15.8-mu_bolt)/sigma_bolt
Z_mutter = (16-mu_mutter)/sigma_mutter


Z = (mu_bolt - mu_mutter)/math.sqrt(sigma_bolt**2 + sigma_mutter**2)

print(1 - stats.norm.cdf(Z))