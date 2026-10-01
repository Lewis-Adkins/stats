import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

n_trials = 10
n_experiments = 10000
chi2_df = n_trials - 1
confidence_level = .95
# See my code for how to put re-used functions in a subdir named "lib".

def get_dataset(n_trials: int, n_experiments: int, dist_type: str = "std_norm")-> np.array:

   match dist_type:
        case "std_norm":
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
        case "chi2":
            '''
            f(x) = (1/2)^(k/2) / \\Gamma(k/2) x^((k/2)-1)e^(-k/2)

            k = degrees of freedom
            X = number of successful outcomes

            the mode of chi2 is at the degrees of freedom -2 so we subtract chi2_df -2 
            '''
            return np.random.chisquare(chi2_df,size = (n_experiments, n_trials))
       
def generate_sample_means(datasets: np.array)-> np.array:
    '''
    Compute  \bar{X} .
    Gets the mean of the sample

    arg1: datasets = sample mean

    returns mean of sample mean
    '''


    X_bars = np.mean(datasets, axis = 0)

    return X_bars


def get_chi2_critical_values(alpha: float, data: np.array)-> tuple[float,float]:

    l_chi2_cv = stats.chi2.ppf(1 - alpha, df = data.shape[0] - 1)
    u_chi2_cv = stats.chi2.ppf(alpha, df = data.shape[0] - 1)
    return (l_chi2_cv, u_chi2_cv)

def get_alpha(confidence_level:float)-> float:
    return 1 - confidence_level

def get_chi2_confidence_interval(chi2_critcal_values: tuple[float,float], data: np.array)-> tuple[float,float]:
    l_bound = (data.shape[0] - 1) * data.var(axis = 0) / chi2_critcal_values[0]
    u_bound = (data.shape[0]- 1) * data.var(axis = 0) / chi2_critcal_values[1]
    return (l_bound, u_bound)


def part_1(hist_label:str, dist_type: str = "std_norm"):
    '''
    To determine if this is the case, sample n=10 values from a normal distribution with μ=0 and σ=1, computing Sb2, and repeating Ne=10,000 times.
    Plot the histogram of the 10,000 Sb2 values, and, in the title, display the average and variance of the 10,000 Sb2 values.
    
    On the plot title, show the average value of the 10,000 Sb2 values (it should be slightly less than σ2).

    Modify your code for HW 3.3.2 to numerically generate an approximation of the sampling distribution of (n−1)S 2/σ2 using n=10 and σ=1.
    '''
    datasets = get_dataset(n_experiments, n_trials, dist_type=dist_type)
    X_bars = generate_sample_means(datasets)

    Ss = ((datasets - X_bars)**2).sum(axis=0)

    plt.title(fr"$S^2$ for std normal, $\langle S^2 \rangle$ = {Ss.mean():.2f} " + r"$\text{Var}(S^2)$ = " +   fr"{Ss.var():.2f}")
    plt.ylabel("Count")
    plt.xlabel("$S^2$s")
    plt.hist(Ss, bins = 50, edgecolor = "black", label = hist_label, density= True)

def part_2():
    x = np.linspace(0,50,100)
    y = stats.chi2.pdf(x , df = chi2_df)
    plt.plot(x, y, label = fr"$\chi^2, df = {chi2_df}$ ")

def part_3():
    datasets = get_dataset(n_trials,n_experiments, dist_type="std_norm")

    X_bars = generate_sample_means(datasets)

    Ss = ((datasets - X_bars)**2).sum(axis=0)

    alpha = get_alpha(confidence_level)

    chi2_cv = get_chi2_critical_values(alpha, Ss)

    ci = get_chi2_confidence_interval(chi2_cv, Ss)
    print(f"alpha/2:{alpha/2}, 1-alpha/2: {1-alpha/2}")
    print(f"var: {Ss.var()}")
    print(f"cv: {chi2_cv}")
    # print(f"formula: ({datasets.size[0]-1} * {datasets.var()} / {crit_vals[0]}, {data.size-1} * {data.var()} / {crit_vals[1]})")
    print(f"ci: {np.sqrt(ci)}")
def main():

    part_1(fr"orig")
    part_2()
    part_3()


    plt.legend()
    plt.savefig("HW4/HW4_2/HW4_2_2.png")
    plt.show()
if __name__ == "__main__":
    ## __name__ == "__main__" is really only needed when a script is imported
    main()