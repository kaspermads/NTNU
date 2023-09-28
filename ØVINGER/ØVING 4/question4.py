from scipy import stats
import matplotlib.pyplot as plt

n = 23
p = 0.4
x = 13

punkt = stats.binom.pmf(x,n,p)

stats.binom.pmf(range(0,16),n,p)

x_max = n + 3

plt.bar(range(0,x_max), stats.binom.pmf(range(0,x_max), n,p))

plt.grid(); plt.ylabel("P(X = x)"); plt.xlabel("x")

plt.show()
