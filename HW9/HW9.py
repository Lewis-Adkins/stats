import numpy as np
from scipy.stats import norm
import math
import matplotlib.pyplot as plt
data_size = (10,1)
probability_heads = .4
significance_level = .01
z = norm.ppf(1- significance_level/2)

def generate_binary_dataset(data_size: tuple[int], probability_heads:float)-> np.array:
    rng = np.random.default_rng()
    return rng.binomial(n=1, p = probability_heads, size = data_size)

def proportional_estimates(data: np.array)-> float:
    return data.sum(axis = 0) / data.shape[0]

def get_p_tilde(p_estimate:np.array, n_trials: int)-> np.array:
    num = p_estimate + (z**2 / (2 * n_trials))
    denom = 1 + (z**2 / n_trials)
    return num / denom

def sqrt_term_ci(p_estimate:np.array, n_trials)-> np.array:
    denom = (1 + z**2 /n_trials)
    q_estimate = (1- p_estimate)
    num = z *  np.sqrt((p_estimate * q_estimate / n_trials) + (z**2 / (4 * n_trials**2)))
    return num / denom

def score_confidence_interval_small(data: np.array)->np.array:
    n_trials = data.shape[0]
    n_experiments = data.shape[1]
    p_hat = proportional_estimates(data)
    p_tilde = get_p_tilde(p_hat, n_trials)
    u_bound = np.zeros(n_experiments) + p_tilde + sqrt_term_ci(p_hat,n_trials)
    l_bound = np.zeros(n_experiments) + p_tilde - sqrt_term_ci(p_hat, n_trials)

    return np.vstack((l_bound, u_bound))

def score_confidence_interval_large(data:np.array)-> np.array:
    n_trials = data.shape[0]
    n_experiments = data.shape[1]
    p_hat = proportional_estimates(data)
    q_hat = (1 - p_hat)
    u_bound = np.zeros(n_experiments) + p_hat + z * np.sqrt(p_hat * q_hat / n_trials)
    l_bound = np.zeros(n_experiments) + p_hat - z* np.sqrt(p_hat * q_hat / n_trials)

    return np.vstack((l_bound, u_bound))

def part_1()-> None:
    data      = generate_binary_dataset(data_size, probability_heads)
    sci_small = score_confidence_interval_small(data)
    sci_large = score_confidence_interval_large(data)
    # print(sci_large.mean(axis  = 1))
    # print(sci_small.mean(axis = 1))
# small_sci = [0.02399285 0.77000715]
# large_sci = [0.13702361 0.73914034]

def likelihood(theta: float,n_success: int, n_trials:int )->np.array:

    return math.comb(n_trials, n_success) * theta ** n_success * (1 - theta) ** (n_trials - n_success)



def part_2()->None:

    thetas  = np.linspace(0,1,100)
    likelihoods = likelihood(thetas, 4,10)
    evidence = np.trapezoid(likelihoods, thetas)
    posterior = likelihoods / evidence
    print('P(D|0): ', likelihoods)
    print('P(D):', evidence)
    print('p(0|D)', posterior)

    plt.xlabel(r'$\theta$'); plt.ylabel(r'$p(\theta|D)$')
    plt.plot(thetas, posterior)
    plt.savefig('HW9_2_1.png')
    plt.close()

    a_vals = np.arange(.02,.12,.02)
    areas = []
    for a in a_vals:
        thetas = np.linspace(0, a, 100)
        posterior = likelihood(thetas, 4, 10) / evidence
        areas.append(np.trapezoid(posterior, thetas))


    plt.plot(a_vals, areas)
    plt.xlabel('a')
    plt.savefig('HW9_2_2.png')





def main():
    part_1()
    part_2()

if __name__ == '__main__':
    main()