import matplotlib.pyplot as plt
import numpy  as np


n_trials      = 100
n_experiments = 10000
mu_min        = -0.01
mu_max        = 0.01
n_min         = 1
n_max         = n_experiments
n_step        = 500

def part_1(min: float, max: float, n_trials: int, n_experiments: int) -> float:
    '''
    For n=100, what fraction of the 10,000  
    Xs were in the range [−0.01,0.01]?
    '''
    X_bars = generate_sample_means(n_experiments, n_trials)
    in_range = (X_bars[(X_bars >= min) & (X_bars <= max)].size / X_bars.size) 
    
    return in_range

def part_2(n_experiments: int, n_min: int, n_max, n_step, mu_min: float, mu_max: float) -> None:

    n_range   = np.arange(n_min, n_max, n_step)
    in_ranges = np.array([])

    for n_r in n_range:
        in_range  = part_1(mu_min, mu_max, n_r, n_experiments)
        in_ranges = np.append(in_ranges,in_range)


    x_new = np.arange(0,10000,1)
    b_log, a_log = np.polyfit(np.log(n_range), in_ranges, 1)    
    log_fit = a_log + b_log * np.log(x_new)

    
    quad_z = np.polyfit(n_range, in_ranges, 2)
    
    model = np.poly1d(quad_z)


    b_exp, a_exp = np.polyfit(n_range, np.log(in_ranges),1)
    exp_fit = np.exp(a_exp) * np.exp(b_exp * x_new)

    # 1. Fit a 2nd-degree polynomial (quadratic: y = a*x^2 + b*x + c)
    a2_log, b2_log, c2_log = np.polyfit(np.log(n_range), in_ranges, 2)

    # 2. Calculate the fitted values using the quadratic equation
    log2_fit = a2_log * (np.log(x_new)**2) + b2_log * np.log(x_new)  + c2_log

    
    plt.figure(figsize=(10, 6))
    plt.title(r"The portion of our distribution, $\beta$, in certain range $\epsilon$ vs.  how many how many values, $n_r$ we draw from that same distribution ")
    plt.ylabel(r"Fraction of values in range $\epsilon$:" + f"[{mu_min}, {mu_max}]")
    plt.xlabel(r"$n_r$: The numbers of values drawn from Standard Normal Distribution")
    plt.xscale("log")

    # plt.plot(x_new, model(x_new), label = fr"qaud: {quad_z[2]:.2}$x^2$ + {quad_z[1]:.2}$x$ + {quad_z[0]:.2}" , linestyle = '--')
    # plt.plot(x_new, exp_fit, label = fr"$\exp({a_exp:.2})\exp({b_exp:.2} n_r)$)", linestyle = '--')
    # plt.plot(x_new, log_fit, label = fr"{a_log:.2} + {b_log:.2}$\log n_r$", linestyle = '--')
    # plt.plot(x_new, log2_fit, label = fr"${a2_log:.2}(\log n_r)^2) + {b2_log:.2}\log n_r + {c2_log:.2}$", linestyle = '--')
    plt.plot(n_range, in_ranges, label = r'$n_r$ vs $\beta$')
    plt.legend()
    plt.savefig("HW3_2_2.png")
    plt.show()

    


def get_dataset(n: int) -> np.array:
    '''
    f(x) = 1 / sqrt(2 * pi * sigma) * exp[-(x - mu)^2 / (2 * sigma ^2)]

    For the case of mu = 0 , sigma = 1, this is the Standard Normal which is a specific case of the Gaussian Distribution.
    It is a continuous probabilty density function
    
    r(x) = 1 / sqrt(2 * pi) * exp [ -x^2 / 2]
    '''
    return np.random.standard_normal(n) 

def get_mean(data: np.array)-> float:
    return data.mean()

def generate_sample_means(n_experiments: int, n_trials: int)-> np.array:
    X_bars = np.array([])

    for n_ex in range(n_experiments):

        data = get_dataset(n_trials)
        X_bars = np.append(X_bars, data.mean()) 

    return X_bars



def main():
    
    in_range = part_1(mu_min, mu_max, n_trials, n_experiments)

    print(f"For {n_experiments} experiments drawing {n_trials} values, the percentage in range [{mu_min}, {mu_max}] is {in_range * 100:.3}%") 

    part_2(n_experiments, n_min, n_max, n_step, mu_min, mu_max)


if __name__ == "__main__":
    main()