import math
import statistics as stats
from scipy import stats

import matplotlib.pyplot as plt
import numpy as np


mu = 74

sigma = 0.5

sigma_gjennomsnitt = sigma/math.sqrt(11) 

øvre_grense = 74.3
nedre_grense = 73.7
Z_øvre = (øvre_grense - mu)/sigma_gjennomsnitt
Z_nedre = (nedre_grense - mu)/sigma_gjennomsnitt
mellomrom = stats.norm.cdf(Z_øvre) - stats.norm.cdf(Z_nedre)

print(mellomrom)