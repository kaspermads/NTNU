import numpy as np

tall = np.array([0.1109,0.0951,0.0862,0.1015,0.1579,0.0981,0.0925,0.0987])
nye_tall = np.array([0.1109,0.0951,0.0862,0.1015,0.0981,0.0925,0.0987])

sortert = np.sort(tall)
print(sortert)
print(np.mean([sortert[4],sortert[3]]))
print(np.mean(nye_tall))
print(np.median(nye_tall))
print(np.mean(tall))