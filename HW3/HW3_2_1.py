import math
import matplotlib.pyplot as plt
import numpy  as np


n_trials = 100
n_experiments = 10000

def get_dataset(n: int) -> np.array:
    '''
    f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

    For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
    It is a continuous probabilty density function
    
    r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]
    '''
    return np.random.standard_normal(n) 

def get_sample_mean(data: np.array)-> float:
    return data.mean()

def generate_sample_means(n_experiments: int, n_trials: int)-> np.array:
    X_bars = np.array([])

    for n_ex in range(n_experiments):

        data = get_dataset(n_trials)
        X_bars = np.append(X_bars, data.mean()) 

    return X_bars


def main():
    
    X_bars = generate_sample_means(n_experiments, n_trials)

    np.savetxt("X_bars.txt", X_bars)
    plt.hist(X_bars, bins = int(n_experiments / n_trials), density = True, edgecolor = "black", align = "left")
    plt.title(r"Average of $\bar{X}$")
    plt.savefig("HW3_2_1.png")
    plt.show()


if __name__ == "__main__":
    main()