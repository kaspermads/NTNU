import statistics as st
import numpy as np
from math import factorial as fact


#oppgave a,b
def minst_to(n):
    p_no_one = (fact(365)/(fact((365-n))*365**n))
    
    p_atleast_two = 1 - p_no_one
    return p_atleast_two

print(minst_to(23))
   
#oppgave c,d

"""
#SIMULERING 1
np.random.choice(5,3) # for å trekke tilfeldige tall, 5 betyr at vi trekker fra tallene (0,1,2,3,4), og 3 at vi trekker tre tall
np.unique([1,2,4,5,2,4,2]) # returnerer kun de unike tallene i denne arrayen

n_sim = 100000 # Antall simuleringer du vil gjøre
n = 23 # Antall personer som skal velges ut
dager = 365

x =  np.zeros(n_sim) # initialiserer x-vektor med bare 0-eller

for i in range(n_sim):
    bursdager = np.random.choice(dager, n) # trekker tilfeldige datoer
    if len(np.unique(bursdager)) < n:  # Dersom det ikke er like mange unike bursdager som det er personer
        x[i] = 1
        
estimat = sum(x)/n_sim
print(estimat)
"""
#SIMULERING 2
antall_fødsler = np.array([4959, 4495, 4958, 5009, 5018, 4955, 4919, 4852, 4742, 4555, 4153, 4081])
andel_fødsler = antall_fødsler/sum(antall_fødsler)

mnd_dager = [31,28,31,30,31,30,31,31,30,31,30,31]

daglig_prob = [andel_fødsler[0]/mnd_dager[0]]*mnd_dager[0] # initialisere

for i in range(1,12):
    daglig_prob = daglig_prob + [andel_fødsler[i]/mnd_dager[i]]*mnd_dager[i]
    
# set(daglig_prob) # se på daglige sannsynligheter i hver mnd
# 1/365            # sammenligne med antagelsen i simulering 1

print(np.unique(daglig_prob)) # har fått 12 unike sannsynligheter, en for dagene i hver måned - men husk at daglig_prob har 365 elementer - og det er 12 unike verdier

n_sim = 100000 # Antall simuleringer du vil gjøre
n = 22 # Antall personer som skal velges ut
dager = 365

y = np.zeros(n_sim) # initialiserer y-vektor med bare 0-eller

for i in range(n_sim):
    bursdager = np.random.choice(dager, n, daglig_prob) # trekker tilfeldige datoer
    if len(np.unique(bursdager)) < n:  # Dersom det ikke er like mange unike bursdager som det er personer
        y[i] = 1
        
estimat = sum(y)/n_sim
print(estimat)