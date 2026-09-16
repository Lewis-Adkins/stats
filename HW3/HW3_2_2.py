import matplotlib.pyplot as plt
import numpy  as np
n_trials =    100

mu_min        = -0.01
mu_max        = 0.01

n_experiments = 10000
n_min         = 1
n_max         = n_experiments
n_step        = 50

epsilons_min  = -3 # 10^-n, specifying n
epsilons_max  = -1 # 10^-n, specifying n

fraction_in_range = .99
box = ""

dist_types = ["std_norm", "uni", "bin", "poi", "chi2", "geo"]

def chebyshev(n_range: np.array, mu_min:float, mu_max: float) -> np.array:
    return 1 - ( 1 / (((mu_max - mu_min)/2)**2 * n_range**2))


def part_1(min: float, max: float, n_trials: int, n_experiments: int, dist_type: str) -> float:
    '''
    For n=100, what fraction of the 10,000  
    Xs were in the range [−0.01,0.01]?
    '''
    X_bars = generate_sample_means(n_experiments, n_trials, dist_type)

    return get_fraction_within_epsilon(X_bars, min, max)




def part_2(n_experiments: int, n_min: int, n_max, n_step, mu_min: float, mu_max: float, dist_type: float) -> None:

    n_range   = np.arange(n_min, n_max, n_step)
    in_ranges = np.array([])

    for n_r in n_range:
 
        in_range  = part_1(mu_min, mu_max, n_r, n_experiments, dist_type)
        in_ranges = np.append(in_ranges,in_range)

    
    box = part_3(n_range, in_ranges, fraction_in_range, mu_min, mu_max)
    # chebyshev_data = chebyshev(n_range,mu_min, mu_max)   

    plt.text(
        1,.5,
        box,
        bbox = dict(boxstyle = 'round', facecolor = 'white')
    )

    # plt.ylim(0,in_ranges.max())
    plt.scatter(n_range, in_ranges, label = fr'$P({mu_min} \leq x \leq {mu_max})$')
    # plt.plot(n_range, chebyshev_data, label = "chebyshev")

    # plt.legend()


def part_3(n_range: np.array, in_ranges: np.array, fraction_in_range: float, mu_min: float, mu_max: float)-> str:
    global box
    fraction_finder = n_range[np.argmax(in_ranges > fraction_in_range)]

    if fraction_finder == 1:
        box += fr"[{float(mu_min)},{mu_max}] $n_r$ = N/A {"\n"}"      
    else:
        box += fr"[{float(mu_min)},{mu_max}] $n_r$ ={fraction_finder}{"\n"}"
    return box


def part_4(n_experiments: int, n_min: int, n_max: int, n_step: int, epsilons_min: float, epsilons_max: float, dist_type: str) -> None:

    epsilons = np.logspace(epsilons_min, epsilons_max, abs(epsilons_min))
    global box

    box +=fr"{fraction_in_range*100:.3}% within $[-\epsilon, \epsilon]$ {"\n"}"

    plt.figure(figsize=(10, 6))
    plt.title(fr"{dist_type} distribution $P(\epsilon \leq x \leq \epsilon)$ vs. $n_r$")
    plt.ylabel(fr"Fraction of values in range $\epsilon$, when $P(\epsilon \leq x \leq \epsilon)$")
    plt.xlabel(fr"$n_r$: The numbers of values drawn from Standard Normal Distribution")
    plt.xscale("log")
    

    


    for ep in epsilons:
        print(fr"Plotting {n_experiments} experiments drawing up to {n_max} values with mean tolerance {ep}")

        part_2(n_experiments, n_min, n_max, n_step, -ep, ep, dist_type)

    plt.savefig(f"HW3_2_2_{dist_type}.png")
    plt.legend()


def part_5(n_experiments: int, n_min: int, n_max:int, n_step:int, epsilons_min: float, epsilons_max:float)-> None:

    for dt in dist_types:
        print("="*5, dt, "="*5)
        part_4(n_experiments, n_min, n_max, n_step, epsilons_min, epsilons_max, dt)
        global box
        box = ""
    
    


def get_fraction_within_epsilon(data: np.array, mu_min: float, mu_max: float)-> np.array:
    return data[(data >= mu_min) & (data <= mu_max)].size / data.size

def get_dataset(n: int, type: str) -> np.array:

    match type:
        case "std_norm":
            '''
            f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

            For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
            It is a continuous probabilty density function
            
            r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]
            '''
            return np.random.standard_normal(n) 
        case "bin":
            return np.random.binomial(n,.5,n)
        case "uni":
            return np.random.uniform(size = n)
        case "poi":
            return np.random.poisson(size = n)
        case "chi2":
            return np.random.chisquare(1, n)
        case "geo":
            return np.random.geometric(.5, n)

    
        



def generate_sample_means(n_experiments: int, n_trials: int, dist_type: str)-> np.array:
    X_bars = np.array([])

    for n_ex in range(n_experiments):

        data = get_dataset(n_trials, dist_type)
        
        X_bars = np.append(X_bars, data.mean()) 

    return X_bars



def main():

    in_range = part_1(mu_min, mu_max, n_trials, n_experiments, "std_norm")
    
    # part_4(n_experiments, n_min, n_max, n_step, epsilons_min, epsilons_max, "std_norm")
    part_5(n_experiments, n_min, n_max, n_step, epsilons_min, epsilons_max)

if __name__ == "__main__":
    main()