import matplotlib.pyplot as plt
import numpy  as np

n_trials      = 100
n_experiments = 10000
mu_min        = -0.01
mu_max        = 0.01
n_min         = 1
n_max         = n_experiments
n_step        = 500
mu_mins       = np.array([-.1,-.01,-.001])

def chebyshev(n_range: np.array, mu_min:float, mu_max: float) -> np.array:
    return 1 - ( 1 / (((mu_max - mu_min)/2)**2 * n_range))


def part_1(min: float, max: float, n_trials: int, n_experiments: int) -> float:
    '''
    For n=100, what fraction of the 10,000  
    Xs were in the range [−0.01,0.01]?
    '''
    X_bars = generate_sample_means(n_experiments, n_trials)

    return get_fraction_within_epsilon(X_bars, min, max)




def part_2(n_experiments: int, n_min: int, n_max, n_step, mu_min: float, mu_max: float) -> None:

    n_range   = np.arange(n_min, n_max, n_step)
    in_ranges = np.array([])

    for n_r in n_range:
 
        in_range  = part_1(mu_min, mu_max, n_r, n_experiments)
        in_ranges = np.append(in_ranges,in_range)

    
    

    plt.figure(figsize=(10, 6))
    plt.title(fr"$P({mu_min} \leq x \leq {mu_max})$ vs.  how many how many values, $n_r$ we draw from that same distribution ")
    plt.ylabel(fr"Fraction of values in range $\epsilon$:" + f"[{mu_min}, {mu_max}]")
    plt.xlabel(r"$n_r$: The numbers of values drawn from Standard Normal Distribution")
    plt.xscale("log")
    # chebyshev_data = chebyshev(n_range,mu_min, mu_max)
    # plt.plot(n_range, chebyshev_data, label = "chebyshev")
    plt.scatter(n_range, in_ranges, label = fr'$n_r$ vs $P({mu_min} \leq x \leq {mu_max})$')
    plt.legend()
    plt.savefig("HW3_2_2.png")
    plt.show()



def get_fraction_within_epsilon(data: np.array, mu_min: float, mu_max: float)-> np.array:
    return data[(data >= mu_min) & (data <= mu_max)].size / data.size

def get_dataset(n: int) -> np.array:
    '''
    f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

    For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
    It is a continuous probabilty density function
    
    r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]
    '''
    
    return np.random.standard_normal(n) 

def generate_sample_means(n_experiments: int, n_trials: int)-> np.array:
    X_bars = np.array([])

    for n_ex in range(n_experiments):

        data = get_dataset(n_trials)
        
        X_bars = np.append(X_bars, data.mean()) 

    return X_bars



def main():

    in_range = part_1(mu_min, mu_max, n_trials, n_experiments)

    print(f"For {n_experiments} experiments drawing {n_trials} values, the percentage in range [{mu_min}, {mu_max}] is {in_range:.3}%") 

    part_2(n_experiments, n_min, n_max, n_step, mu_min, mu_max)


if __name__ == "__main__":
    main()