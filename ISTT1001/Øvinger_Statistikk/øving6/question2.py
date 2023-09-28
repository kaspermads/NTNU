import math
import statistics as stats
from scipy import stats

import matplotlib.pyplot as plt

mu = 4.0

standard_avvik = 3

#a

z = (3-4)/standard_avvik

probability = 1 - stats.norm.cdf(z)

print (probability)

#b

print((1.8-4)/3)
svaret = 0.3707 - 0.2327

print(svaret)