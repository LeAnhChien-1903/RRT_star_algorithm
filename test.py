import numpy as np
a = np.array([100, 1, 2, 3, 4,5])
index = [idx for idx, val in enumerate(a) if val == a.min()] 
print(index)