from scipy import stats

svar = 1 - stats.binom.cdf(5,9,0.81)
print(svar)

e = 9*0.81
print(e)
var = e*(1-0.81)
print(var)