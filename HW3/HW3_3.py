
import numpy as np
import matplotlib.pyplot as plt

n = 10
n_experiments = 10000

n_min = 1
n_max = n_experiments
n_step = 50

dist_types =["std_norm", "uni"]
box = ""

def get_dataset(n: int,n_experiments: int,  type: str) -> np.array:

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
            return np.random.uniform(-1, 1, size = (n,n_experiments))

def generate_sample_means(n_experiments: int, n_trials: int, dist_type: str = "std_norm")-> np.array:

    data = get_dataset(n_trials, n_experiments, dist_type)
        
    X_bars = np.mean(data, axis = 0)

    return X_bars

def part_2(data: np.array, n: int)-> np.array:

    return data[(data >= 1/np.sqrt(n))].size / data.size


def part_1(n_trials: int, n_experiments: int, dist_type: str) -> float:
    
    X_bars = generate_sample_means(n_experiments, n_trials, dist_type)

    plt.hist(X_bars, label = f"{dist_type}", density=True, bins = 50, edgecolor = "black")

    global box
    box +=f"{dist_type} {part_2(X_bars, n)*100:.3}% above" + r'$\frac{1}{\sqrt{n}}$' + '\n'

def part_3(n_min: int, n_max: int, n_step: float):
    n_range = np.arange(n_min, n_max, n_step)
    above_inv_sqrt_n = np.array([])
    for n_r in n_range:
        X_bar = generate_sample_means(n_experiments, n_r)
        plt.title(fr"$n_r$: {n_r}, above: {part_2(X_bar, n_r)}")
        plt.hist(X_bar, density=True, bins = 50, edgecolor = "black")
        plt.show()
        above_inv_sqrt_n = np.append(above_inv_sqrt_n, part_2(X_bar, n_r))

    plt.plot(n_range, above_inv_sqrt_n)
    # plt.xscale("log")
    # plt.show()
def main():


    # for dt in dist_types:
    #     part_1(n, n_experiments, dt)
    # plt.legend()

    # plt.text(
    #     0.3, .2, box,
    #     transform=plt.gca().transAxes,
    #     ha='right', va='bottom',
    #     bbox=dict(boxstyle='round', facecolor='white')
    # )
    # plt.show()
    part_3(n_min, n_max, n_step)
if __name__ == "__main__":
    main()