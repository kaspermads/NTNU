import math
from scipy import stats

import matplotlib.pyplot as plt

mu = 90
sigma = 5


kritisk_verdi_Z = 0.842


kritisk_verdi_X = kritisk_verdi_Z*sigma + mu

print(kritisk_verdi_X)

