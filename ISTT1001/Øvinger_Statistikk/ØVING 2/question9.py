from math import factorial as fact
import statistics
import numpy as np

ulike_kombinasjoner = 7*8*4
print(ulike_kombinasjoner)

dessert = (fact(4)/(fact(2)*fact(4-2)))
forrett= (fact(7)/(fact(2)*fact(7-2)))
hovedrett = (fact(8)/(fact(2)*fact(8-2)))

p = dessert*forrett*hovedrett

print(p)