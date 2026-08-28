import random
import matplotlib.pyplot as plt
import numpy as np

a = [0, 1]


# Experiment: Randomly select an element from the list a

result = random.choice(a)


# Repeat the experiment n times
n_ex = 1000

results = {}


for n in range(1,n_ex+1): # size of experiment is equal to the number of experiment
    print('-'*5, f'Experiment {n}','-'*5)
    data = []
    field = {}

    for exp in range(1, n+1):
        
        result = random.choice(a)
        data.append(result)
    
    field["exp"] = data
    field["rf1"] = data.count(1) / n
    field["rf0"] = data.count(0) / n

    print(f'exp {n} : {field["exp"]}')
    print(f'rf1 : {field["rf1"]:.3f}')
    print(f'rf0 : {field["rf0"]:.3f}')
    results[f'{n} exp'] = field


rf1s = []
rf0s = []
for ex, val  in results.items():
    rf1s.append(val['rf1'])
    rf0s.append(val['rf0'])

ns = np.arange(len(results))
plt.title(r'Flipping Coin Outcomes')
plt.plot(ns, rf1s)
plt.plot(ns, rf0s)
plt.xlabel("Number of Experiments")
plt.ylabel(r"Relative Frequency $R_f$")
plt.axhline(.5,  color = 'r', linestyle = '--')
plt.show()


# ------------ QUESTION 2 ------------ #

# There are 2 possible outcomes for 3 trials making the sample space size = 2^3 = 8

# ------------ QUESTION 3 ------------ #

print('=' * 10 ,' Question 3','=' * 10)

a = [0, 1]
# Experiment: Randomly select an element from the list a
result = random.choice(a)

# Repeat the experiment n times
n = 2

results = np.random.randint(0,1, size = n, dtype = int).tolist()

print(f"n = {n} experiments:")
print(f"  Results: {results}")

# rf = relative frequency
print(f"  rf(0) = {results.count(0) / n}")
print(f"  rf(1) = {results.count(1) / n}")
