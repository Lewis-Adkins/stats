import numpy as np

cnt = 0

ne = 100000
n = 7
mu = 0



x = np.random.normal(mu, 1, size = (n,ne))

xbar = np.mean(x, axis = 0)

print(xbar.shape)

ci = np.array([xbar-1.96/np.sqrt(n), xbar+1.96/np.sqrt(n)])



print(np.where((ci[0,:] > 0) | (ci[1,:] < 0))[0].shape[0]/ ne)



# cnt = cnt+1

# print(cnt/ne)