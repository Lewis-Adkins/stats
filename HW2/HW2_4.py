import numpy as np
import random
import matplotlib.pyplot as plt
import math



data =  [1,1,1,1,0,0,0,0,0,0]
n_experiments =  10000
n_values = 100
p =  data.count(1) / len(data)



def execute_experiment(data:list[int], n: int) -> list[int]:
    '''
    the experiment is selecting 100 values from the list [0, 1]
    with the probability of selecting a 1 being p. 
    '''
    results = []
    for i in range(n):
        results.append(random.choice(data))
    return results


def run_simulation(data: list, n_values: int, n_experiments: int) -> None:
    
    results = {i : 0 for i in range(n_values)}

    for n_ex in range(n_experiments):
        n_1s = execute_experiment(data, n_values).count(1)
        results[n_1s] += 1/n_experiments

    plt.plot(list(results.keys()), list(results.values()), label = 'experiment')

def P(x:int, n: int, p: float) -> float:
    '''
    For n trials, the probability of successess is given bth the Binomial distribution:
    P(x) = (n x) p^x (1-p)^(n-x)
    arg1 x = number of successful outcomes you wnat to count
    arg2 n = number of trials
    arg3 p = probabiltiy of success
    '''

    return (math.factorial(n) / (math.factorial(x) * math.factorial(n-x))) * p**x * (1-p) ** (n-x)


def plot_P(n: int, p: float) -> None:
    xs = np.arange(n).tolist()
    Px = [P(x, n, p)  for x in xs]
    plt.plot(xs, Px, label = r'$P(x)$')



def main():

    run_simulation(data, n_values, n_experiments)
    plot_P(n_values, p)
    plt.xlim(0,n_values)
    plt.legend()
    plt.show()

if __name__== "__main__":
    main()

