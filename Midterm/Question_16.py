import numpy as np

reject = 0

ne = 100000

mu = 0
std = 1
n = 7

x = np.random.normal(mu,std, size = (n,ne) )

x_bar = np.mean(x, axis = 0)

nrr_size = 1.96 * std / np.sqrt(n) #non rejectino region

a = mu - nrr_size

b = mu + nrr_size



print("rejects: ",100 * np.where((x_bar < a) | (x_bar > b))[0].shape[0]/ne,"%")
