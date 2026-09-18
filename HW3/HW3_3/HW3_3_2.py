import numpy as np
import matplotlib.pyplot as plt

n_trials = 10
n_experiments = 10000

def get_dataset(n_trials: int, n_experiments: int)-> np.array:
    '''

    Draw n=100 values from a population of Gaussian-distributed numbers with mean μ=0 and standard deviation σ=1.

    f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

    For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
    It is a continuous probabilty density function
    
    r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]

    arg1: n_experiments = number of experiments
    arg2: n_trials = number of trials
    '''

    return np.random.standard_normal(size = (n_experiments, n_trials))

def generate_sample_means(datasets: np.array)-> np.array:
    '''
    Compute  \bar{X} .
    Gets the mean of the sample

    arg1: datasets = sample mean

    returns mean of sample mean
    '''


    X_bars = np.mean(datasets, axis = 0)

    return X_bars



def part_1():
    '''
    To determine if this is the case, sample n=10 values from a normal distribution with μ=0 and σ=1, computing Sb2, and repeating Ne=10,000 times.
    Plot the histogram of the 10,000 Sb2 values, and, in the title, display the average and variance of the 10,000 Sb2 values.
    
    On the plot title, show the average value of the 10,000 Sb2 values (it should be slightly less than σ2).
    '''
    datasets = get_dataset(n_experiments, n_trials)
    X_bars = generate_sample_means(datasets)

    Sbs = np.array([])

    for n_ex in range(n_experiments):
        sum = 0
        for n_t in range(n_trials):
            sum +=(datasets[n_t, n_ex] - X_bars[n_ex])**2/n_trials
        Sbs = np.append(Sbs, sum)
    var = 'Var'
    plt.title(fr"$S_b^2$ for std normal, $\langle S_b^2 \rangle$ = {Sbs.mean():.2f} " + r"$\text{Var}(S_b^2)$ = " +   fr"{Sbs.var():.2f}")
    plt.ylabel(fr"Count")   
    plt.xlabel("$S_b^2$s")
    plt.hist(Sbs, bins = 50, edgecolor = "black")
    plt.savefig("HW3_3/HW3_3_2.png")
    plt.show()


def main():
    part_1()
    
if __name__ == "__main__":
    main()