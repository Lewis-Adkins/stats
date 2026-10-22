import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
n_trials = 20
n_experiemnts = 10000
beta_1 = 1
beta_0 = 1
sigma = .2
mu = 0
significance_level = .05

def part_1(n_trials: int, beta_1: float, beta_0: float, mu: float, sigma:float)-> tuple[np.array]:

    x = np.divide(np.arange(0, n_trials ),n_trials)
    epsilon = np.random.normal(mu, sigma, size = n_trials)
    y = beta_1 * x + beta_0 + epsilon

    plt.scatter(x,y)


    return x,y

def part_2(x:np.array, y:np.array)-> tuple[float]: # I didnt write down equation so i redervied from partial SSE b_1 and b_0, see HW5_1_2.png
    x_bar = x.mean(axis = 0)
    y_bar = y.mean(axis = 0)

    num = ((x - x_bar)*(y - y_bar)).sum(axis = 0)
    denom = ((x - x_bar)**2).sum(axis = 0)

    b_1 = np.divide(num, denom)
    b_0 = y_bar - b_1 * x_bar

    Y = b_1 * x + b_0
    plt.plot(x,Y, label = fr"My $\beta$ Values ")
    return b_1, b_0


def part_3(x: np.array,y: np.array)-> tuple[float]:

    return np.polyfit(x,y, deg = 1)

def part_4(x:np.array, y:np.array, significance_level:float)-> tuple[float]:
    x_bar = x.mean(axis = 0)
    y_bar = y.mean(axis = 0)
    Sxx = ((x-x_bar)**2).sum(axis = 0)
    b_1_est = ((x - x_bar) * y).sum(axis = 0) / Sxx
    b_0_est = y_bar - b_1_est * x_bar
    
    SSE = (y**2).sum(axis = 0) - b_0_est * y.sum(axis = 0) - b_1_est * (x * y).sum(axis = 0)
    s2 = SSE / (x.shape[0] - 2)
    b_1_est_std_err = np.sqrt(s2 / Sxx)
    t_crit = t.ppf((1-significance_level/2), x.shape[0]-2)
    lb =  b_1_est - t_crit  * b_1_est_std_err
    ub = b_1_est + t_crit  * b_1_est_std_err
    return lb,ub

def part_5(n_trials:int, n_experiments:int, beta_1: float, beta_0: float, mu:float, sigma:float, significance_level:float)-> None:
    x = np.repeat([np.divide(np.arange(0, n_trials ),n_trials)], n_experiments, axis = 0).T

    epsilon = np.random.normal(mu, sigma, size = (n_trials, n_experiments))
    y = beta_1 * x + beta_0 + epsilon

    b1,b0 = part_2(x,y)
    lb, ub = part_4(x,y, significance_level)

    frac_within = np.mean((lb < beta_1) & (beta_1 < ub))
    
    print(fr"frac within CI: {frac_within}")
    # Im for each sample im testing the number of points "trapped" within the confidence interval over the size of the sample
    return frac_within


def main():
    x,y = part_1(n_trials, beta_1, beta_0, mu, sigma)
    b_1,b_0        = part_2(x,y)
    np_b_1, np_b_0 = part_3(x,y)
    ci_b_1_lb, ci_b_1_ub=part_4(x,y, significance_level)
    box_properties = dict(
        boxstyle='round',       # Shape: 'round', 'square', etc.
        facecolor='wheat',      # Background color
        edgecolor='gray',       # Border color
        alpha=0.5,              # Transparency (0 to 1)
        pad=0.5                 # Padding inside the box
    )
    plt.text(
        x=0.03,                 # X coordinate (axes fraction)
        y=0.97,                 # Y coordinate (axes fraction)
        s=(fr"Mine:  $\beta_1$ = {b_1:.4f}, $\beta_0$ = {b_0:.4f}" "\n"
           fr"numpy: $\beta_1$ = {np_b_1:.4f}, $\beta_0$ = {np_b_0:.4f}" "\n"
           fr"CI $\beta_1$: ({ci_b_1_lb:.4f},{ci_b_1_ub:.4f})"),  # The text string
        fontsize=12,            # Size of the text
        bbox=box_properties,     # Appyling the bounding box
        verticalalignment='top', # Vertical alignment relative to coordinates
        transform=plt.gca().transAxes  # Place relative to axes, not data
    )

    ci_l_line = ci_b_1_lb * x  +b_0
    ci_u_line = ci_b_1_ub * x + b_0

    plt.plot(x,ci_l_line, linestyle = "--", color = 'k')    
    plt.plot(x,ci_u_line, linestyle = "--", color = 'k')    
    plt.legend()
    
    plt.savefig("HW5_1.png")
    part_5(n_trials, n_experiemnts, 1,1,0,.2,.05)
main()