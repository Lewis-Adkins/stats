
import numpy as np
import matplotlib.pyplot as plt

n = 100
n_experiments = 10000

n_min = 1
n_max = n_experiments
n_step = 500

dist_types =["std_norm", "uni"]
box = ""

def get_dataset(n: int,n_experiments: int,  type: str) -> np.array:
    '''
    Grabs dataset of type "type" and returns simulated data drawing from type of distribution

    arg1: n_trials = number of trials
    arg2: n_experiments = number of experiments
    arg3: type = distribution type from possible list =  ["std_norm", "uni"]
    '''
    match type:
        case "std_norm":
            '''
            f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

            For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
            It is a continuous probabilty density function
            
            r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]
            '''
            return np.random.standard_normal(size=(n, n_experiments)) 
        case "uni":
            '''
            f(x) = 1/(b-a) for a<= x <=b else 0

            uni_min = a
            uni_max = b
            '''
            return np.random.uniform(-1, 1, size = (n,n_experiments))

def generate_sample_means(n_experiments: int, n_trials: int, dist_type: str = "std_norm")-> np.array:

    '''
    To simulate n_experiments each with n_trials we return a (n_trials, n_experiments) np array populated with values from a dist_type

    arg1: n_experiments   = number of experiments
    arg2: n_trials        = number of trials
    arg3: dist_type       = distribution type from possible list =  ["std_norm", "uni"]

    return np array of sample means
    '''

    data = get_dataset(n_trials, n_experiments, dist_type)
        
    X_bars = np.mean(data, axis = 0)

    return X_bars

def part_1(n_trials: int, n_experiments: int, dist_type: str) -> None:
    '''
    Draw n=10 values from a normal distribution with μ=0 and σ2=1 and compute  X.
    Repeat this 10,000 times and plot the probability density function of X.
    On the plot title, show the average value of the 10,000  X values.

    arg1: n_trials      = number of trials
    arg2: n_experiemnts = number of experiments
    arg3: dist_type     = distribution type from possible list =  ["std_norm", "uni"]
    '''
    X_bars = generate_sample_means(n_experiments, n_trials, dist_type)

    plt.hist(X_bars, label = f"{dist_type}", density=True, bins = 50, edgecolor = "black")


    global box
    box +=f"{dist_type} {part_2(X_bars, n)*100:.3}% above" + r'$\frac{1}{\sqrt{n}}$' + '\n'


def part_2(data: np.array, n_trials: int)-> np.array:
    '''
    Of the 10,000 X values, what fraction was above 1/n? Add this fraction to the title of your previous plot.

    arg1: data = sample means
    arg2: n_trials = number of trials

    returns fraction of values above 1/sqrt(n)
    '''
    return data[(data >= 1/np.sqrt(n_trials))].size / data.size

def part_3(n_min: int, n_max: int, n_step: float)-> None:
    '''
    (590 only) Think of a numerical experiment that you can perform to determine how the fraction computed in part 2.
    depends on n. Create a plot that demonstrates the result of your experiment.

    arg1: n_min = lower bound of n_range
    arg2: n_max = upper bound of n_range
    arg3: n_step = linear steps between ranges
    '''
    n_range = np.arange(n_min, n_max, n_step)
    above_inv_sqrt_n = np.array([])

    for n_r in n_range:
        X_bar = generate_sample_means(n_experiments, n_r)
        plt.title(fr"$n_r$: {n_r}, above: {part_2(X_bar, n_r)}")
        above_inv_sqrt_n = np.append(above_inv_sqrt_n, part_2(X_bar, n_r))
 

    plt.plot(n_range, above_inv_sqrt_n)
    plt.xscale("log")
    plt.savefig("HW3_3/HW3_3_1_3.png")

    plt.close()

def part_4(n_trials: int, n_experiments: int, dist_types:list[str]) -> None:
    '''
    (590 only) Repeat parts 1. and 2. using a uniform distribution in the range [0,1] (use the np.random.uniform() function).

    arg1: n_trials = number of trials
    arg2: n_experiments   = number of experiments
    arg3: dist_type     = distribution type from possible list =  ["std_norm", "uni"]
    '''
    for dt in dist_types:
        part_1(n_trials, n_experiments, dt)

    plt.legend()

    plt.text(
        0.3, .2, box,
        transform=plt.gca().transAxes,
        ha='right', va='bottom',
        bbox=dict(boxstyle='round', facecolor='white')
    )
    plt.ylabel(fr"Count")
    plt.xlabel(r"$\bar{X}$")
    plt.savefig("HW3_3/HW3_3_1_1")
    plt.show()
    plt.close()

def main():

    part_4(n, n_experiments, dist_types)


    part_3(n_min, n_max, n_step)
if __name__ == "__main__":
    main()