import numpy as np
import statistics as st
array = np.array([0.86,0.1,0.59,0.84,0.28,0.3])
sample_variance = np.var(array, ddof=1)
print(st.variance(array))
print(sample_variance)