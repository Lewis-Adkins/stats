import numpy as np
n = 10
ne = 10000
mu = 0
delta = 1.96 / np.sqrt(n)
exps = np.random.normal(0,1, size = (n,ne))
xbars = np.mean(exps, axis = 0)
frac= xbars[(xbars - delta < mu) & (xbars + delta > mu)].size / xbars.size
print(frac)