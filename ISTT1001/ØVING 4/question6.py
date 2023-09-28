from scipy import stats

p = 0.5
n = 20
x = 9

p_mer_enn_10_gitt_12 = (stats.binom.pmf(11,n,p) + stats.binom.pmf(12,n,p))/stats.binom.cdf(12,n,p)
print(p_mer_enn_10_gitt_12)