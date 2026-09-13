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
    print(results)
    plt.plot(list(results.keys()), list(results.values()), label = 'experiment')

def p_discrete(x:int, n: int, p: float) -> float:
    '''
    For n trials, the probability of successess is given bth the Binomial distribution:
    P(x) = (n x) p^x (1-p)^(n-x)
    arg1 x = number of successful outcomes you want to count
    arg2 n = number of trials
    arg3 p = probabiltiy of success
    '''

    return (math.factorial(n) / (math.factorial(x) * math.factorial(n-x))) * p**x * (1-p) ** (n-x)


def p_continuous(x: int, n: int, p: float) -> float:
    '''
    For n trials, the probability of successess is given bth the Binomial distribution:
    P(x) = 1/sqrt(2* pi * n * p * q) * exp(-(x-np)^2 / (2 * n * p * q)
    arg1 x = number of successful outcomes you want to count
    arg2 n = number of trials
    arg3 p = probabiltiy of success
    '''
    return 1 / math.sqrt(2 * math.pi * n * p * (1-p)) * math.exp(-(x - n * p)**2 / (2 * n * p *(1-p)))

def plot_P(n: int, p: float) -> None:
    xs = np.arange(n).tolist()
    Px_dis = [p_discrete(x, n, p)  for x in xs]

    Px_cont = [p_continuous(x,n,p) for x in xs]
    plt.plot(xs, Px_dis, label = r'$P(x)_\text{dis}$')
    plt.plot(xs, Px_cont, label = r'$P(x)_\text{cont}$')


def main():

    run_simulation(data, n_values, n_experiments)
    plot_P(n_values, p)
    plt.title(f"{r"$n_{\text{ex}}=$"}{n_experiments} {r"$n_\text{v} = $"}{n_values}, {r"$p = $"}{p}")
    plt.xlim(0,n_values)
    plt.xlabel(r"$x$ : " + "Number of times " +r"$1$" + "was selected in dataset " + r"$n_v$" + " times"  )
    plt.ylabel(r"$P$ :" + "Probability of selecting " + r"$1$" + " " +  r"$x$" + " number of times")
    plt.legend()
    plt.show()

if __name__== "__main__":
    main()

