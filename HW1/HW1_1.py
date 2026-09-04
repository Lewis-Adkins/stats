import random
import matplotlib.pyplot as plt
import numpy as np


def q1(n_ex: int = 1000, show = False) -> None:
    a = [0, 1]

    # Repeat the experiment n times

    results = {}

    for n in range(1,n_ex+1): # size of experiment is equal to the number of experiment
        # print('-'*5, f'Experiment {n}','-'*5)
        data = []
        field = {}

        for exp in range(1, n+1):
            
            result = random.choice(a)
            data.append(result)
        
        field["exp"] = data 
        field["rf1"] = sum(data) / exp
        field["rf0"] = 1 - field["rf1"]


        results[f'{n} exp'] = field

    rf1s = []
    rf0s = []

    for ex, val  in results.items():
        rf1s.append(val['rf1'])
        rf0s.append(val['rf0'])

    ns = np.arange(len(results))

    plt.title(r'Flipping Coin Outcomes')
    plt.plot(ns, rf1s, label = "rf1")
    plt.plot(ns, rf0s, label = "rf0")
    plt.xlabel("Number of Experiments")
    plt.ylabel(r"Relative Frequency $R_f$")
    plt.legend()
    plt.axhline(.5,  color = 'r', linestyle = '--')
    if show:
        plt.show()


# # ------------ QUESTION 2 ------------ #

# # There are 2 possible outcomes for 3 trials making the sample space size = 2^3 = 8

# # ------------ QUESTION 3 ------------ #

def q3(n_ex: int = 1000, show = False) -> None:
    print('=' * 10 ,' Question 3','=' * 10)

    a = [0, 1]
    # Experiment: Randomly select an element from the list a
    result = random.choice(a)

    # Repeat the experiment n times

    results = np.random.randint(2, size = n_ex, dtype = int)
    
    sizes = np.arange(1,n_ex+1)

    # From Class ==============
    rf1      = np.cumsum(results) /sizes
    rf0 = 1 - rf1

    # ==========================
    print(results) 

    
    print(rf1)
    plt.title(r'Cum-Sum No Loop')
    plt.xlabel("Number of Experiments")
    plt.ylabel(r"Relative Frequency $R_f$")
    plt.axhline(.5,  color = 'r', linestyle = '--')
    plt.plot(sizes, rf1 , label = "rf1")
    plt.plot(sizes, rf0 , label = "rf0")
    plt.legend()
    if show:
        plt.show()

q1()
q3()

### Thoughts: The plots for q1 vs q3 are very different from eachother. is this because q3 resamples an increarely large portion the same dataset while q1 generates a new dataset every single time?