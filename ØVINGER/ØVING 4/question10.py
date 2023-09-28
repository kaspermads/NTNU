from scipy import stats

p = 0.26


def P(Y):
    return p*(1-p)**(Y-1)

def E(p):
    return 1/p

#a 
print(E(p))

#b
print(1 - stats.geom.cdf(2,p))

#c
print(1 - (P(1) + P(2)))