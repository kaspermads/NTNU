from scipy import stats

p = 0.71

def E(p):
    return 1/p

print(E(p))

def P(Y):
    return p*(1-p)**(Y-1)

print(P(3))

print(stats.geom.cdf(3,p))