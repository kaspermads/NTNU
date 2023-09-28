from scipy import stats

p = 0.21

def P(Y):
    return p*(1-p)**(Y-1)

print(P(3))


