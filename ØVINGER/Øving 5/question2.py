import math
from math import factorial as fact




def poisson(x, rate, tid):
    return ((((rate*tid)**x)*math.e**(-rate*tid))/(fact(x)))

def forventningsverdi_E(rate,tid):
    return rate*tid
    


#a
# print(poisson(3, 1, 3))

#b

def forventningsverdi_E(rate,tid):
    return rate*tid
print(forventningsverdi_E(1,3))
#c

print(1 - poisson(3,1,3))