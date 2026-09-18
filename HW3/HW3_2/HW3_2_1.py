import math
import matplotlib.pyplot as plt
import numpy  as np


n_trials = 100
n_experiments = 10000

def get_dataset(n: int) -> np.array:
    '''

    Draw n=100 values from a population of Gaussian-distributed numbers with mean μ=0 and standard deviation σ=1.

    f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

    For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
    It is a continuous probabilty density function
    
    r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]
    '''
    return np.random.standard_normal(n) 

def get_sample_mean(data: np.array)-> float:
    '''
    Compute  \bar{X} .
    Gets the mean of the sample

    arg1: data = sample mean

    returns mean of sample mean
    '''

    return data.mean()

def generate_sample_means(n_experiments: int, n_trials: int)-> np.array:

    '''
    Repeat 1. and 2. 10,000 times and plot a probability density function of \bar{X}.

    To simulate n_experiments each with n_trials we return a (n_trials, n_experiments) np array populated with values from standard normal

    arg1: n_experiments   = number of experiments
    arg2: n_trials        = number of trials

    return np array of sample means
    '''

    X_bars = np.array([])

    for n_ex in range(n_experiments):

        data = get_dataset(n_trials)
        X_bars = np.append(X_bars, data.mean()) 

    return X_bars


def main():
    
    X_bars = generate_sample_means(n_experiments, n_trials)
    plt.hist(X_bars, bins = int(n_experiments / n_trials), density = True, edgecolor = "black", align = "left")
    plt.title(r"Average of $\bar{X}$")
    plt.xlabel(r"$\bar{X}$")
    plt.ylabel("Counts")
    plt.savefig(f"HW3_2/HW3_2_1.png")
    plt.show()


if __name__ == "__main__":
    main()