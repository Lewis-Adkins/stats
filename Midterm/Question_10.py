import numpy as np

cnt = 0

ne = 10000

sigma = 1

for i in range(ne):

  x = np.random.normal(0, sigma, 7)

  xbar = np.mean(x)

  ci = [xbar-1.96*sigma/np.sqrt(7), xbar+1.96*sigma/np.sqrt(7)]

  if ci[0] < 0 and ci[1] > 0: # 0 now in ci and both cases must be true

    cnt = cnt+1

print(cnt/ne)