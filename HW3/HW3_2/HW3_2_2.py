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

fit_chebyshev = False
fit_log_log    = True

dist_types =  ["std_norm", "uni", "bin", "poi", "chi2", "gauss", "geo"]

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

# geo #
geo_p = .5

def part_1(epsilon_min: float, epsilon_max: float, n_trials: int, n_experiments: int, dist_type: str) -> float:
    '''
    For n=100, what fraction of the 10,000  
    Xs were in the range [−0.01,0.01]?

    part_1 will perform two actions: 1. generate sample means from n_experiments number of experiments and n_trials, number of trials
    from the "dist_type" distribution 2. calculate the proportion of values within the sample means that are within [epsilon_min, epsilon_max]

    arg1: epsilon_min   = lower bound of sample mean search
    arg2: epsilon_max   = upper bound of sample mean search
    arg3: n_trials      = number of trials
    arg4: n_experiments = number of experiments
    arg5: dist_type     = distribution type from possible list =  ["std_norm", "uni", "bin", "poi", "chi2", "gauss", "geo"]

    returns: fraction of sample means from distribtuion type within [epsilon_min, epsilon_max]
    '''


    X_bars = generate_sample_means(n_experiments, n_trials, dist_type)

    return get_fraction_within_epsilon(X_bars, epsilon_min, epsilon_max)

def fitting_log_log(n_range: np.array, in_ranges: np.array, fit_log_log: bool)-> None:
    '''
    The graph produced showing the fraction of values within a certain range will be on a log-log plot.
    We fit a line as we observe a linear relationship at this scale of the number of trials vs the fraction within a range.

    arg1: n_range     = an array of number of trials for each experiemnt
    arg2: in_ranges   = an array of fraction of sample means that are within a range
    arg3: fit_log_log =  plot or not plot log log fit
    '''
    

    if fit_log_log:
        log_n_range = np.log(n_range)
        log_in_ranges = np.where(in_ranges>0, np.log(in_ranges), 0)   

        z = np.polyfit(log_n_range, log_in_ranges, 1)

        log_fit = np.poly1d(z)

        plt.plot(n_range, np.exp(log_fit(np.log(n_range))), linestyle = "--", label = fr"log-log fit , $m$ = {z[0]:.2f}, $y$ = {z[1]:.2f}")

def part_2(n_experiments: int, n_min: int, n_max, n_step, epsilon_min: float, epsilon_max: float, dist_type: str) -> np.array:
    '''
    How does the fraction depend on n?

    For a given range E = [epsilon_min, epsilon_max], we ant to describe the relationship between the fraction of sample means within E and how it
    evolves over the number of trials n_r defined with n_min, n_max, n_step. we repeat the process in part_1 over all of N for all distirbution types.
    We plot results for each dist_type. see part_4 for saving and configuring graphs

    arg1: n_experiments = number of experiments
    arg2: n_min         = the lower bound of number of trials n_r
    arg3: n_max         = upper bound of number of trials n_r
    arg4: n_step        = linear steps between each n_r
    arg5: epsilon_min   = lower bound of sample mean search
    arg6: epsilon_max   = upper bound of sample mean search
    arg7: dist_type     = distribution type from possible list =  ["std_norm", "uni", "bin", "poi", "chi2", "gauss", "geo"]

    return in_ranges    = an array of fraction of sample means that are within a range E
    '''

    n_range   = np.arange(n_min, n_max, n_step)
    in_ranges = np.array([])

    for n_r in n_range:
 
        in_range  = part_1(epsilon_min, epsilon_max, n_r, n_experiments, dist_type)
        in_ranges = np.append(in_ranges,in_range)

    plt.scatter(n_range, in_ranges, label = fr'$P({epsilon_min} \leq x \leq {epsilon_max})$')

    fitting_log_log(n_range, in_ranges, fit_log_log)

    plt.legend()

    return in_ranges

def part_3(n_experiments: int, n_trials: int,  epsilons_min: float, epsilons_max: float, fraction_within: float, dist_types: str)-> str:

    '''
    For n=100, what is the range [−ϵ,ϵ] for which 99% of the 10,000  \bar{Xs} fall in?

    Similar to part_2, we are able to repeat part_1 with the only difference of keeping n_r constant = 100, and trialing each epsilon to produce a range E.
    part_1 gives us the fraction of sample means that are within E, in_range. We slowly grow the bounds of E until in_range > fraction within. once true,
    we stop calculating and record our answer into "HW3_2/HW3_2_2_3.txt"

    arg1: n_experiments   = number of experiments
    arg2: n_trials        = number of trials
    arg3: epsilon_min     = lower bound of sample mean search
    arg4: epsilon_max     = upper bound of sample mean search
    arg5: fraction_within = limit of sample means within E before stopping calculations
    arg6: dist_type     = distribution type from possible list =  ["std_norm", "uni", "bin", "poi", "chi2", "gauss", "geo"]
    '''
    
    epsilons = np.linspace(epsilons_min, epsilons_max, 500)

    with open("HW3_2/HW3_2_2_3.txt", "w") as f:
        f.write(fr"| $\epsilon$| fraction_in_range | distribution |{'\n'}")
        f.write(fr"|-------|-----|-------|{'\n'}")

        for dt in dist_types:
            final_ep = 0
            final_in_range = 0

            for ep in epsilons:
                in_range = part_1(-ep, ep, n_trials ,n_experiments, dt)


                if in_range > fraction_within:
                    final_ep += ep
                    final_in_range +=  in_range
                    f.write(f"| {ep:.4f} | {in_range} | {dt} |{'\n'}")
                    break 
        

            print(fr"$\epsilon$ = {final_ep:.2f}, in_range = {final_in_range} for {dt}")
        
def part_4(n_experiments: int, n_min: int, n_max: int, n_step: int, epsilons_min: float, epsilons_max: float, dist_type: str) -> None:
    '''
    How does ϵ depend on n (for the 99% case of part 3.)? 

    part_4 repeats part_2 for all chosen ranges E. part_2 give us the relationship of the number of trials n_r to the fraction
    within E for only one range of E. on the same graph we show how the change in E, transforms our data. For all distributions we save
    our graphs in the HW3_2_2_dists folder and each will distirbtion will have the suffiz dist_type.
    arg1: n_experiments   = number of experiments
    arg2: n_min           = the lower bound of number of trials n_r
    arg3: n_max           = upper bound of number of trials n_r
    arg4: n_step          = linear steps between each n_r
    arg5: epsilon_min     = lower bound of sample mean search
    arg6: epsilon_max     = upper bound of sample mean search
    arg7: dist_type       = distribution type from possible list =  ["std_norm", "uni", "bin", "poi", "chi2", "gauss", "geo"]
    '''  
    epsilons = np.logspace(epsilons_min, epsilons_max, abs(epsilons_min))

    plt.figure(figsize=(10, 6))
    plt.title(fr"{dist_type} distribution $P(\epsilon \leq x \leq \epsilon)$ vs. $n_r$")
    plt.ylabel(fr"Fraction of values in range $\epsilon$, when $P(\epsilon \leq x \leq \epsilon)$")
    plt.xlabel(fr"$n_r$: The numbers of values drawn")
    plt.xscale("log")
    plt.yscale("log")
    
    for ep in epsilons:
        print(fr"Plotting {n_experiments} experiments drawing up to {n_max} values with mean tolerance {ep}")

        in_ranges = part_2(n_experiments, n_min, n_max, n_step, -ep, ep, dist_type)

    plt.savefig(f"HW3_2/HW3_2_2_dists/HW3_2_2_{dist_type}.png")
    
def part_5(n_experiments: int, n_min: int, n_max:int, n_step:int, epsilons_min: float, epsilons_max:float)-> None:
    '''
    How does your answer change if the distribution changes (that is, if you draw values from a distribution other than Gaussian)?
    
    The final layer of repeatability. starting from the bottom:
    part_1 - generates sample means and returns the fraction within a range E for a singular n_r, number of trials
    part_2 - iterates through part_1 for all n_r
    part_4 - iterates through part 2 for all given ranges E
    part_5 - iterates through part 4 for all distribution types.

    We are able to collect all information requested from part_1,2,4 for section 3.2.2 on the homework for all distributions.

    arg1: n_experiments   = number of experiments
    arg2: n_min           = the lower bound of number of trials n_r
    arg3: n_max           = upper bound of number of trials n_r
    arg4: n_step          = linear steps between each n_r
    arg5: epsilon_min     = lower bound of sample mean search
    arg6: epsilon_max     = upper bound of sample mean search

    '''
    for dt in dist_types:

        print("="*5, dt, "="*5)
        part_4(n_experiments, n_min, n_max, n_step, epsilons_min, epsilons_max, dt)    


def get_fraction_within_epsilon(data: np.array, epsilon_min: float, epsilon_max: float)-> np.array:
    '''
    Within a dataset, returns the proportion of values that are within a given range E

    arg1: data            = sample mean generated 
    arg2: epsilon_min     = lower bound of sample mean search
    arg3: epsilon_max     = upper bound of sample mean search
    '''

    return data[(data >= epsilon_min) & (data <= epsilon_max)].size / data.size

def get_dataset(n_trials: int, n_experiments: int, type: str) -> np.array:
    '''
    Grabs dataset of type "type" and returns simulated data drawing from type of distribution

    arg1: n_trials = number of trials
    arg2: n_experiments = number of experiments
    arg3: type = distribution type from possible list =  ["std_norm", "uni", "bin", "poi", "chi2", "gauss", "geo"]
    '''
    match type:
        case "std_norm":
            '''
            f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

            For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
            It is a continuous probabilty density function
            
            r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]
            '''
            return np.random.standard_normal(size = (n_trials,n_experiments)) 
        
        case "bin":
            '''
            f(x) = (n x) p^x (1-p)^(n-x)

            a binomial distirbution by default has its mean value mu > 0. we recenter the pdf to x = 0 and sqaush the sides accordingly.

            n     = number of trials
            x     = numbner of successful outcomes 
            bin_p = probability of success
            1-p   = probability of failure
            '''
            bin_dist = np.random.binomial(n_trials, bin_p, size=(n_trials, n_experiments))
            centered = bin_dist - n_trials * bin_p                    
            squashed = centered / max(bin_p, 1 - bin_p) / (n_trials/10)     

            return squashed
        case "uni":
            '''
            f(x) = 1/(b-a) for a<= x <=b else 0

            uni_min = a
            uni_max = b
            '''
            return np.random.uniform(uni_min, uni_max, size = (n_trials,n_experiments))
        case "poi":
            '''
            f(x) = (\mu^x e^\mu )/x!
            
            \mu = mean
            x   = number of successful outcomes

            mean of poisson is at poi_lambda so we shift it back at 0 by subtracting by poi_lambda
            '''
            return np.random.poisson(lam = poi_lambda, size = (n_trials,n_experiments)) - poi_lambda
        case "chi2":
            '''
            f(x) = (1/2)^(k/2) / \Gamma(k/2) x^((k/2)-1)e^(-k/2)

            k = degrees of freedom
            X = number of successful outcomes

            the mode of chi2 is at the degrees of freedom -2 so we subtract chi2_df -2 
            '''
            return np.random.chisquare(chi2_df,size = (n_trials,n_experiments)) + chi2_df - 2
        case "gauss":
            '''
            or normal distirbution:
            f(x) = 1 / (2\pi \sigma) e^((x - \mu)^2/2\sigma^2)
            \sigma = variance
            \mu    = mean
            x      = number of successful outcomes

            because we want to keep the center of the gauss to be at 0 we set \mu = 0 but we use a non zero \sigma (gauss_std) to differentiate
            between standard normal distribution
            '''
            return np.random.normal(loc = 0, scale = gauss_std, size = (n_trials,n_experiments))
        case "geo":
            '''
            f(x) = (1-p)^(x-1) p

            x      = number of successful outcomes
            p      = probabiltiy of success

            the mean of a geometric pdf is at 1/p so we recenter by subtracting by 1/geo_p
            '''
            return np.random.geometric(geo_p, size = (n_trials, n_experiments)) - 1 / geo_p

def generate_sample_means(n_experiments: int, n_trials: int, dist_type: str = "std_norm")-> np.array:
    '''
    To simulate n_experiments each with n_trials we return a (n_trials, n_experiments) np array populated with values from a dist_type

    arg1: n_experiments   = number of experiments
    arg2: n_trials        = number of trials
    arg3: dist_type       = distribution type from possible list =  ["std_norm", "uni", "bin", "poi", "chi2", "gauss", "geo"]

    return np array of sample means
    '''

    data = get_dataset(n_trials, n_experiments, dist_type)

    X_bars = np.mean(data, axis = 0)

    return X_bars

def view_dists():
    '''
    View all distributions by creating image and saving to HW3_2/HW3_2_2_dists/view_dists.png
    '''
    n_columns = 2
    n_rows = int(np.ceil(len(dist_types) / n_columns))
    fig, axes = plt.subplots(nrows = n_rows, ncols = n_columns, figsize= (10,12))
    axes_flat = axes.flatten()

    for i, dt in enumerate(dist_types):
        ax = axes_flat[i]
        ax.set_title(dt)
        ax.hist(get_dataset(1000,1, dt), bins = 200)
    plt.savefig("HW3_2/HW3_2_2_dists/view_dists.png")


def main():

    view_dists()

    print("-"*10, "PART 1", "-" * 10, "\n")
    in_range = part_1(mu_min, mu_max, n_trials, n_experiments, "bin")
    print(fr"For $n_r = 100$ the fraction of {n_experiments} between [{mu_min:.1},{mu_max:.1}] is {in_range}")
    print("\n")

    print("-"*10, "PART 3", "-" * 10, "\n")
    part_3(n_experiments, n_trials, .001,10, .99, dist_types)
    print("\n")

    print("-"*10, "PART 5", "-" * 10, "\n")
    part_5(n_experiments, n_min, n_max, n_step, epsilons_min, epsilons_max)

if __name__ == "__main__":
    main()