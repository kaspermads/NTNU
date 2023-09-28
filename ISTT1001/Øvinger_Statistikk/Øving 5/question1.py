import math
from math import factorial as fact




def poisson(x, rate, tid):
    return ((((rate*tid)**x)*math.e**(-rate*tid))/(fact(x)))
    
print(poisson(3, 3.5, 1))