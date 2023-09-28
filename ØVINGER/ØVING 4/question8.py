from scipy import stats


def E(p):
    return 1/p

print(E(1/6))

print(1 - stats.geom.cdf(2,1/6))