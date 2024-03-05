import numpy as np 

x = np.arange(0, 20, 1)
X = x**2
X = X.reshape(-1, 4)
print(X)