from scipy import stats

p = 0.2
n = 14
x = 6
 
print(1 - stats.binom.cdf(x,n,p))