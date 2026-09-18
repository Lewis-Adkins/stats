import matplotlib.pyplot as plt
import numpy  as np
n_trials =    100

mu_min        = -0.01
mu_max        = 0.01

n_experiments = 1000
n_min         = 1
n_max         = n_experiments*10
n_step        = 50

epsilons_min  = -3 # 10^-n, specifying n
epsilons_max  = -1 # 10^-n, specifying n

fraction_in_range = .99

plot_chebyshev = False

dist_types =  ["std_norm", "uni", "bin", "poi", "chi2", "gauss"]

# Dist parameters:

# poisson #
poi_lambda = 1

# chi2 #
chi2_df = 1

# bin #
bin_p = .5

# uni #
uni_min = -1
uni_max = 1

# gauss #
gauss_std = 2

def chebyshev(n_range: np.array, mu_min:float, mu_max: float) -> np.array:
    return 1 - ( 1 / (((mu_max - mu_min)/2)**2 * n_range**2))


def part_1(min: float, max: float, n_trials: int, n_experiments: int, dist_type: str) -> float:
    '''
    For n=100, what fraction of the 10,000  
    Xs were in the range [−0.01,0.01]?
    '''
    X_bars = generate_sample_means(n_experiments, n_trials, dist_type)

    return get_fraction_within_epsilon(X_bars, min, max)




def part_2(n_experiments: int, n_min: int, n_max, n_step, epsilon_min: float, epsilon_max: float, dist_type: float) -> np.array:

    n_range   = np.arange(n_min, n_max, n_step)
    in_ranges = np.array([])

    for n_r in n_range:
 
        in_range  = part_1(epsilon_min, epsilon_max, n_r, n_experiments, dist_type)
        in_ranges = np.append(in_ranges,in_range)

    chebyshev_data = chebyshev(n_range,epsilon_min, epsilon_max)
    chebyshev_data = chebyshev_data[(chebyshev_data >=0)]

    c_n_range = n_range[(n_range.size - chebyshev_data.size):]

    plt.scatter(n_range, in_ranges, label = fr'$P({epsilon_min} \leq x \leq {epsilon_max})$')

    if plot_chebyshev:
        plt.plot(c_n_range, chebyshev_data, label = "chebyshev")

    # plt.ylim(0,in_ranges.max())
    plt.legend()
    return in_ranges

def part_3(n_experiments: int, n: int,  epsilons_min: float, epsilons_max: float, fraction_within: float, dist_types: str)-> str:

    epsilons = np.linspace(epsilons_min, epsilons_max, 500)

    for dt in dist_types:
        final_ep = 0
        final_in_range = 0

        for ep in epsilons:
            in_range = part_1(-ep, ep, n ,n_experiments, dt)

            if in_range > fraction_within:
                final_ep += ep
                final_in_range +=  in_range
                break 
        print(fr"$\epsilon$ = {final_ep:.2f}, in_range = {final_in_range} for {dt}")

    
        
def part_4(n_experiments: int, n_min: int, n_max: int, n_step: int, epsilons_min: float, epsilons_max: float, dist_type: str) -> None:

    epsilons = np.logspace(epsilons_min, epsilons_max, abs(epsilons_min))

    plt.figure(figsize=(10, 6))
    plt.title(fr"{dist_type} distribution $P(\epsilon \leq x \leq \epsilon)$ vs. $n_r$")
    plt.ylabel(fr"Fraction of values in range $\epsilon$, when $P(\epsilon \leq x \leq \epsilon)$")
    plt.xlabel(fr"$n_r$: The numbers of values drawn from Standard Normal Distribution")
    plt.xscale("log")
    plt.yscale("log")
    
    for ep in epsilons:
        print(fr"Plotting {n_experiments} experiments drawing up to {n_max} values with mean tolerance {ep}")

        in_ranges = part_2(n_experiments, n_min, n_max, n_step, -ep, ep, dist_type)

    plt.savefig(f"HW3_2_2_dists/HW3_2_2_{dist_type}.png")
    
def part_5(n_experiments: int, n_min: int, n_max:int, n_step:int, epsilons_min: float, epsilons_max:float)-> None:

    for dt in dist_types:

        print("="*5, dt, "="*5)
        part_4(n_experiments, n_min, n_max, n_step, epsilons_min, epsilons_max, dt)    


def get_fraction_within_epsilon(data: np.array, epsilon_min: float, epsilon_max: float)-> np.array:
    return data[(data >= epsilon_min) & (data <= epsilon_max)].size / data.size

def get_dataset(n: int, n_experiments: int, type: str) -> np.array:

    match type:
        case "std_norm":
            '''
            f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

            For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
            It is a continuous probabilty density function
            
            r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]
            '''
            return np.random.standard_normal(size = (n,n_experiments)) 
        case "bin":
            bin_dist = np.random.binomial(n,bin_p,size = (n,n_experiments)) 
            
            return 4 *( (bin_dist -   bin_dist.min() ) / (bin_dist.max() -  bin_dist.min()) - (n * bin_p  / 1000))
        case "uni":
            return np.random.uniform(uni_min, uni_max, size = (n,n_experiments))
        case "poi":
            return np.random.poisson(size = (n,n_experiments)) - 1
        case "chi2":
            return np.random.chisquare(chi2_df,size = (n,n_experiments)) + chi2_df - 2
        case "gauss":
            return np.random.normal(loc = 0, scale = gauss_std, size = (n,n_experiments))

def generate_sample_means(n_experiments: int, n_trials: int, dist_type: str = "std_norm")-> np.array:


    data = get_dataset(n_trials, n_experiments, dist_type)

    X_bars = np.mean(data, axis = 0)

    return X_bars

def view_dists():

    n_columns = 2
    n_rows = int(np.ceil(len(dist_types) / n_columns))
    fig, axes = plt.subplots(nrows = n_rows, ncols = n_columns, figsize= (10,12))
    axes_flat = axes.flatten()

    for i, dt in enumerate(dist_types):
        ax = axes_flat[i]
        ax.set_title(dt)
        ax.hist(get_dataset(1000,1, dt), bins = 50)
    plt.savefig("HW3_2_2_dists/view_dists.png")


def main():

    view_dists()

    print("-"*10, "PART 1", "-" * 10, "\n")
    in_range = part_1(mu_min, mu_max, n_trials, n_experiments, "std_norm")
    print(fr"For $n_r = 100$ the fraction of {n_experiments} between [{mu_min:.1},{mu_max:.1}] is {in_range}")
    print("\n")

    print("-"*10, "PART 3", "-" * 10, "\n")
    part_3(n_experiments, n_trials, .001,10, .99, dist_types)
    print("\n")

    print("-"*10, "PART 5", "-" * 10, "\n")
    part_5(n_experiments, n_min, n_max, n_step, epsilons_min, epsilons_max)

if __name__ == "__main__":
    main()