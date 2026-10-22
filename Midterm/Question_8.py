import numpy as np

n = 5
ne = 1000000

x = np.random.normal(0,1,(n,ne))
xbar = np.mean(x,axis = 0)

sb2 = (1/(n-1)) * np.sum((x - xbar)**2, axis = 0)
print(np.mean(sb2), (n-1)/(n))